<script setup>
    const model = defineModel()
    function formatAmount() {
        if (!model.value.amount) return
        model.value.amount = Number(model.value.amount).toFixed(2)
    }
    defineProps({
        accounts: Array
    })
</script>

<template>
    <tr>
        <td>
            <select class="form-select" aria-label="Default select example" v-model="model.account">
                <option :value="null" disabled><span class="text-muted">Select</span></option>
                <option v-for="acc in accounts" :key="acc.id" :value="acc.id">{{ acc.id }} - {{ acc.name }}</option>
            </select>
        </td>
        <td>
            <input type="text" class="form-control" v-model="model.description">
        </td>
        <td>
            <input type="number" class="form-control text-end" placeholder="0.00" v-model="model.amount" @blur="formatAmount">
        </td>
        <td>
            <button class="btn btn-danger" @click="$emit('delete')">
                <i class="bi bi-trash"></i>
            </button>
        </td>
    </tr>
</template>

<script>

</script>