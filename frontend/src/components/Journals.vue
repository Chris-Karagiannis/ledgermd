<script setup>
    import { ref, onMounted, computed} from 'vue';
    import LineItem from './LineItem.vue';
    import Tooltip from './Tooltip.vue';
    
    const error = ref(null)
    const date = ref(null)
    const narration = ref(null)
    const accounts = ref(null)
    const total = ref(0)

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
            
            window.location.reload()

        } catch (error) {
            console.error(error)
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

    <div v-if="error" class="alert alert-danger d-flex align-items-center" role="alert">
        <i class="bi bi-exclamation-triangle me-2"></i>
        {{ error.message }}
    </div>
    <p class="fw-bold fs-5 text-end px-3 m-0" :class="total === 0 ? 'text-secondary' : 'text-danger'">
        Out of balance by: {{
            total >= 0 ? `$${total.toLocaleString('en-AU', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}` :  `-$${Math.abs(total).toLocaleString('en-AU', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`
        }}
    </p>
    <table class="table table-hover align-middle">
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

    <div class="pb-5 mb-5">
    </div>

    <div class="fixed-bottom bg-white border-top p-3 shadow-lg">
        <div class="d-flex justify-content-end gap-2 m-0">
            <button class="btn btn-primary px-5 fw-bold" @click="saveJournal">Save</button>
            <button class="btn btn-light px-5">Cancel</button>
        </div>
    </div>
    
</template>


<style scoped></style>
