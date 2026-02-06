<script setup>
    import { ref, onMounted, watch } from 'vue'
    import { useRouter, useRoute } from 'vue-router';
    import { listReports } from '@/utils/listReports';
    import MarkdownEditor from '@/components/MarkdownEditor.vue';

    const router = useRouter()
    const route = useRoute()
    const markdownText = ref(null)
    const title = ref(null)
    const error = ref(null)
    const id = route.params.id

    async function handleSave(text, reportTitle) {
        markdownText.value = text
        title.value = reportTitle
        await saveReport()
    }

    async function saveReport() {
        try {
            const body = {"markdown": markdownText.value, "title": title.value}
                const response = await fetch(`/api/update-report/${id}`, {
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

    async function loadReport(id) {
        try {
            const response  = await fetch(`/api/view-report/${id}`)
            const result = await response.json();
            
            if (!response.ok || !result.markdown) {
                router.push(`/`)
                throw new Error(`Response status: ${response.status}`)
            }
            
            markdownText.value = result.raw
            title.value = result.title

        } catch (error) {
            console.error(error)
        }
    }

    onMounted(async () => {
        loadReport(id)
    });

    watch(
        () => route.params.id,
        (newId) => {
            loadReport(newId)
        }
    )
</script>

<template>
    <main class="content-area py-4 px-2">
        <div class="px-1 mb-4">
            <i class="bi bi-file-earmark-code fs-3 me-2"></i>
            <span class="h3">Edit Report</span>
        </div>

        <div v-if="error" class="alert alert-danger d-flex align-items-center mx-2" role="alert">
            <i class="bi bi-exclamation-triangle me-2"></i>
            {{ error.message }}
        </div>
        
        <MarkdownEditor v-if="markdownText" :text="markdownText" :title="title" @save="handleSave"/>
    </main>
</template>