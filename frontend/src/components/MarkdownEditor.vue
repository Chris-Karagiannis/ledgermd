<script setup>
    import { ref, nextTick, onMounted } from 'vue'
    import { marked } from 'marked'
    import { formatReport } from '@/utils/formatReport';
    import { defineProps } from 'vue';

    const props = defineProps({
        text: {
            type: String,
            default: '# New Report Title'
        },
        title : {
            type: String
        }
    });

    const markdownText = ref(props.text)
    const renderedHtml = ref(null)
    const title = ref(props.title)

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

    onMounted(async () => {
        await previewReport()
    });

</script>

<template>
    <div class="toolbar mb-2 d-flex gap-2 justify-content-between">
        <div class="input-group w-50">
            <input v-model="title" class="form-control" placeholder="Report title" />
            <button class="btn btn-primary" @click="$emit('save', markdownText, title)">Save</button>
        </div>
        <button class="btn btn-secondary" @click="previewReport">Preview</button>
    </div>
    <div class="markdown-editor d-flex flex-column h-100">
        <div class="d-flex flex-grow-1 border rounded overflow-hidden">
            <textarea v-model="markdownText" class="form-control flex-grow-1 border-0 p-3" style="resize: none;"
                placeholder="Write your markdown here..."></textarea>
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