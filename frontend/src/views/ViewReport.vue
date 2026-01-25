<script setup>
    import { useRoute, useRouter } from 'vue-router';
    import { ref, onMounted, nextTick } from 'vue'
    import { formatReport } from '@/utils/formatReport';
    import { marked } from 'marked'

    const renderedHtml = ref(null)
    const route = useRoute()
    const router = useRouter()
    const id = route.query.id

    onMounted(async () => {
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
    });

</script>

<template>
    <div class="preview flex-grow-1 p-3 overflow-auto" v-html="renderedHtml"></div>
</template>