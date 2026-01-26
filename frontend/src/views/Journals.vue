<script setup>
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import LineItem from '@/components/LineItem.vue';
    import Tooltip from '@/components/Tooltip.vue';
    
    
    const error = ref(null)
    const date = ref(null)
    const narration = ref(null)
    const accounts = ref(null)
    const total = ref(0)
    const router = useRouter();

    const lineItems = ref([
        { account_id: null, description: '', amount: null }
    ])

    function addItem() {
        lineItems.value.push({ account_id: null, description: '', amount: null })
    }

    function sumTotal() {
        let val = 0
    
        lineItems.value.forEach(item => {
            val += Number(item.amount)
        });

        return val
    }

    function deleteItem(index) {
        lineItems.value.splice(index, 1)
        total.value = sumTotal()
    }

    async function saveJournal() {
        try {
            const body = {date: date.value, narration: narration.value, entries: lineItems.value}
            const response = await fetch("/api/post-journal", {
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
            
            router.go(0);

        } catch (error) {
            console.error(error)
        }
    }

    function formatTotal(total) {
        if (total >= 0) {
            return `$${total.toLocaleString('en-AU', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`   
        } else {
            return `-$${Math.abs(total).toLocaleString('en-AU', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`
        }
        
    }

    onMounted(async () => {
        try {
          const response  = await fetch(`/api/accounts`)
          accounts.value = await response.json();       
        } catch (error) {
            console.error(error)
        }
    });

</script>

<template>
    <div class="page-scroll">
    <div class="px-1 mb-4">
        <i class="bi bi-pencil-square fs-3 me-2"></i>
        <span class="h3">Create Journal Entry</span>
    </div>
    <div class="card mb-4 border-0 shadow-sm">
        <div class="card-body bg-light rounded">
            <div class="row g-3">
                <div class="col-md-3">
                    <label for="date" class="form-label fw-bold">Transaction Date</label>
                    <input type="date" id="date" class="form-control" v-model="date">
                </div>
                <div class="col-md-9">
                    <label for="narration" class="form-label fw-bold">Narration</label>
                    <input type="text" id="narration" class="form-control" v-model="narration">
                </div>
            </div>
        </div>
    </div>

    <div v-if="error" class="alert alert-danger d-flex align-items-center mx-2" role="alert">
        <i class="bi bi-exclamation-triangle me-2"></i>
        {{ error.message }}
    </div>
    <p class="fw-bold fs-5 text-end px-3 m-0" :class="total === 0 ? 'text-secondary' : 'text-danger'">
        Out of balance by: {{ formatTotal(total) }}
    </p>
    <table class="table table-hover align-middle border mt-2">
        <thead >
            <tr>
                <th class="col-3 col-md-3">Account</th>
                <th class="col-5 col-md-7">Description</th>
                <th class="col-3 col-md-2">
                    <Tooltip text="Negative values represent credits. Positive values represent debits.">Amount</Tooltip>
                </th>
                <th class="col-1 col-md-1"></th>
            </tr>
        </thead>
        <tbody>
            <LineItem v-for="(item, index) in lineItems" :key="index" v-model="lineItems[index]" :accounts="accounts" @delete="deleteItem(index)" @total="total = sumTotal()"></LineItem>

            <tr>
                <td colspan="5" class="text-center p-0">
                    <button class="btn btn-light w-100 py-3 rounded-0" @click="addItem">
                        <i class="bi bi-plus-lg fs-4 text-secondary"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
    </div>
    <div class="position-fixed bottom-0 end-0 p-4"> 
        <div class="card shadow-lg border-0 bg-white p-2">
            <div class="d-flex gap-2">
                <button class="btn btn-primary px-4" @click="saveJournal">Save</button>
            </div>
        </div>
    </div>
    
</template>


<style scoped>
.page-scroll {
  height: 100%;
  overflow-y: auto;
}
</style>
