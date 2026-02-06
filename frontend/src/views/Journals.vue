<script setup>
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import LineItem from '@/components/LineItem.vue';
    
    
    const error = ref(null)
    const date = ref(null)
    const narration = ref(null)
    const accounts = ref(null)
    const total = ref(0)
    const router = useRouter();

    const lineItems = ref([
        { account_id: null, description: '', amount: null },
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
        
        // round to cents to avoid floating point issues
        return Math.round(val * 100) / 100 
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
    <main class="content-area py-4 px-2">
        <div class="page-scroll">
        <div class="page-title px-1 mb-4">
            <i class="bi bi-pencil-square fs-3"></i>
            <span class="h3 m-0">Create Journal Entry</span>
        </div>
        <div class="card mb-4 border-0 shadow-sm card-metadata">
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
        <p class="balance-indicator text-end px-3 m-0" :class="total === 0 ? 'text-secondary' : 'text-danger'">
            Out of balance by: {{ formatTotal(total) }}
        </p>
        <table class="table table-hover align-middle border mt-2 ledger-table">
            <thead >
                <tr>
                    <th class="col-3 col-md-3">Account</th>
                    <th class="col-5 col-md-7">Description</th>
                    <th class="col-3 col-md-2">Amount</th>
                    <th class="col-1 col-md-1"></th>
                </tr>
            </thead>
            <tbody>
                <LineItem v-for="(item, index) in lineItems" :key="index" v-model="lineItems[index]" :accounts="accounts" @delete="deleteItem(index)" @total="total = sumTotal()"></LineItem>

                <tr>
                    <td colspan="5" class="text-center p-0">
                        <button class="add-line-item-btn w-100 py-3" @click="addItem">
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
    </main>
</template>


<style scoped>
.content-area {
  min-height: 100vh;
  background: linear-gradient(
    180deg,
    rgba(248, 249, 250, 0.6),
    rgba(255, 255, 255, 0.9)
  );
  padding-bottom: 120px;
}

.page-scroll {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  height: 100%;
  overflow-y: auto;
}

.card-metadata {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(4px);
  border-radius: 10px;
}

.balance-indicator {
  font-size: 0.95rem;
  letter-spacing: 0.2px;
}

.balance-indicator.text-danger {
  font-weight: 600;
}

.ledger-table {
  width: 100%;
  min-width: 100%;
  border-radius: 10px;
  overflow: hidden;
}

.ledger-table thead {
  background-color: rgba(248, 249, 250, 0.9);
}

.ledger-table th {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--bs-secondary);
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.ledger-table tbody tr {
  transition: background-color 0.15s ease;
}

.ledger-table tbody tr:hover {
  background-color: rgba(13, 110, 253, 0.04);
}

.add-line-item-btn {
  background: transparent;
  border: none;
  transition: background-color 0.15s ease;
}

.add-line-item-btn:hover {
  background-color: rgba(13, 110, 253, 0.06);
}

.save-card {
  backdrop-filter: blur(6px);
  background: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  padding: 0.5rem;
}

.save-card button {
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.save-card button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(13, 110, 253, 0.25);
}

.card-metadata .form-control {
  border-radius: 6px;
  transition: box-shadow 0.15s ease, border-color 0.15s ease;
}

.card-metadata .form-control:focus {
  box-shadow: 0 0 0 0.2rem rgba(13, 110, 253, 0.25);
  border-color: var(--bs-primary);
}

.ledger-table tbody tr td {
  transition: background-color 0.2s ease, color 0.2s ease;
}


</style>
