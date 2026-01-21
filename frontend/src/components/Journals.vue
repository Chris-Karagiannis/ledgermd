<script setup>
    import { ref } from 'vue';
    import LineItem from './LineItem.vue';
    
    const date = ref(null)
    const narration = ref(null)

    const lineItems = ref([
        { account: null, description: '', amount: null }
    ])

    function addItem() {
        lineItems.value.push({ account: null, description: '', amount: null })
    }

    
    function deleteItem(index) {
        lineItems.value.splice(index, 1)
    }

    function saveJournal() {
        let total = 0
        lineItems.value.forEach(item => {
            total += Number(item.amount)
        });
        console.log(total)
    }

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
    
    <table class="table table-hover align-middle">
        <thead >
            <tr>
                <th class="col-3 col-md-2">Account</th>
                <th class="col-5 col-md-7">Description</th>
                <th class="col-3 col-md-2">Amount</th>
                <th class="col-1 col-md-1"></th>
            </tr>
        </thead>
        <tbody>
            <LineItem v-for="(item, index) in lineItems" :key="index" v-model="lineItems[index]" @delete="deleteItem(index)"></LineItem>

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
