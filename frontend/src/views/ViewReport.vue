<script setup>
    import { useRoute, useRouter } from 'vue-router';
    import { ref, onMounted, nextTick, watch } from 'vue'
    import { formatReport } from '@/utils/formatReport';
    import { marked } from 'marked'
    import html2pdf from 'html2pdf.js';

    const renderedHtml = ref(null)
    const reportPreview = ref(null)
    const route = useRoute()
    const router = useRouter()
    let id = route.params.id
    let editPath = `/edit-report/${id}`

    async function downloadReport() {
        const element = reportPreview.value;
          const opt = {
            margin:       10,
            filename:     'report.pdf',
            html2canvas:  {
                scale: 2,
                useCORS: true,
                scrollY: -window.scrollY
            },
            jsPDF: {
                unit: 'mm',
                format: 'a4',
                orientation: 'portrait'
            },
            pagebreak: {
                mode: ['css', 'legacy'],
                avoid: ['pre', 'table', 'blockquote']
            }
        };

        await html2pdf().set(opt).from(element).save();
    }

    async function loadReport(id) {
        try {
            const response  = await fetch(`/api/view-report/${id}`)
            const result = await response.json();
            
            if (!response.ok || !result.markdown) {
                router.push(`/`)
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
        loadReport(id)
    });

    watch(
        () => route.params.id,
        (newId) => {
            loadReport(newId)
            id = newId
            editPath = `/edit-report/${id}`
        }
    )

</script>

<template>
    <div class="preview overflow-auto py-3 px-1" ref="reportPreview" v-html="renderedHtml"></div>
    <div class="w-100 py-3"></div>
    <div class="position-fixed bottom-0 end-0 p-4"> 
        <div class="card shadow-lg border-0 bg-white p-2">
            <div class="d-flex gap-2">
                <button class="btn btn-primary px-4" @click="downloadReport">
                    <i class="bi bi-download"></i>
                    Download
                </button>
                <router-link :to="editPath" class="btn btn-secondary px-2">
                    <i class="bi bi-pencil"></i>
                    Edit
                </router-link>
            </div>
        </div>
    </div>
</template>
