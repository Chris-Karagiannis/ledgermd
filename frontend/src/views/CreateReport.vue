<script setup>
import { ref, nextTick } from 'vue'
import { marked } from 'marked'
import { useRouter } from 'vue-router';
import { formatReport } from '@/utils/formatReport';

const router = useRouter()
const markdownText = ref(`# New Report Title`)
const renderedHtml = ref(null)

// TODO: Need to figure out how to have a title for report, could use frontmatter or just have a text box.
async function saveReport() {
  try {
    const body = {"markdown": markdownText.value}
        const response = await fetch("/api/save-report", {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json"
            }
        });

        const result = await response.json();
        router.push(`/view-report?id=${result.report_id}`)

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`)
        }

  } catch (error) {
    console.error(error)
  }
}

async function previewReport() {
    try {
        const body = {"markdown": markdownText.value}
        const response = await fetch("/api/preview-markdown", {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json"
            }
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`)
        }
        
        renderedHtml.value = marked.parse(result.markdown)
        await nextTick();
        formatReport();

    } catch (error) {
        console.error(error)
    }

}

</script>

<template>
    
    <div class="px-1 mb-4">
        <i class="bi bi-file-earmark-code fs-3 me-2"></i>
        <span class="h3">Create Report</span>
    </div>
    <div class="toolbar mb-2 d-flex gap-2 justify-content-between">
      <button class="btn btn-primary" @click="saveReport">Save</button>
      <button class="btn btn-secondary" @click="previewReport">Preview</button>
    </div>
    <div class="markdown-editor d-flex flex-column h-100">
        <div class="d-flex flex-grow-1 border rounded overflow-hidden">
        <textarea v-model="markdownText" class="form-control flex-grow-1 border-0 p-3" style="resize: none;" placeholder="Write your markdown here..."></textarea>      
        <div class="preview flex-grow-1 p-3 border-start overflow-auto" v-html="renderedHtml"></div>
        </div>
    </div>
</template>

<style scoped>
.markdown-editor {
  display: flex;
  flex-direction: column;
  height: 80vh;
}

.toolbar {
  flex-shrink: 0;
}

textarea {
  font-family: monospace;
  min-width: 50%;
}

.preview {
  min-width: 50%;
  background-color: #f8f9fa;
}

.preview h1, .preview h2, .preview h3 {
  margin-top: 1rem;
}

.preview code {
  background-color: #e9ecef;
  padding: 2px 4px;
  border-radius: 4px;
}

.preview pre {
  background-color: #e9ecef;
  padding: 10px;
  border-radius: 6px;
  overflow-x: auto;
}
</style>
