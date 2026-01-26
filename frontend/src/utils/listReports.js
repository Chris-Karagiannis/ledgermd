import { ref } from 'vue';

export const reports = ref(null)

export async function listReports() {
    try {
        const response = await fetch(`/api/list-reports`)
        const result = await response.json();

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`)
        }

        reports.value = result
    } catch (error) {
        console.error(error)
    }
}