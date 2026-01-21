<script setup>
    const model = defineModel()
    function formatAmount() {
        if (!model.value.amount) return
        model.value.amount = Number(model.value.amount).toFixed(2)
    }
</script>

<template>
    <tr>
        <td>
            <select class="form-select" aria-label="Default select example" v-model="model.account">
                <option selected>Open this select menu</option>
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </td>
        <td>
            <input type="text" class="form-control" v-model="model.narration">
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