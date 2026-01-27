<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { listReports } from '@/utils/listReports';
import MarkdownEditor from '@/components/MarkdownEditor.vue';

const router = useRouter()
const markdownText = ref(`# New Report Title`)
const title = ref(null)
const error = ref(null)

async function handleSave(text, reportTitle) {
    markdownText.value = text
    title.value = reportTitle
    await saveReport()
}

async function saveReport() {
  try {
    const body = {"markdown": markdownText.value, "title": title.value}
        const response = await fetch("/api/save-report", {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json"
            }
        });

        const result = await response.json();
        
        if (!response.ok) {
          error.value = result
          throw new Error(`Response status: ${response.status}`)
        }
        listReports()
        router.push(`/view-report/${result.report_id}`)

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

    <div v-if="error" class="alert alert-danger d-flex align-items-center mx-2" role="alert">
        <i class="bi bi-exclamation-triangle me-2"></i>
        {{ error.message }}
    </div>

    <MarkdownEditor text="# Hello" @save="handleSave"/>

</template>
