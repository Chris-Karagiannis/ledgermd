<script setup>
    import { ref, onMounted } from 'vue';
    import { listReports, reports } from '@/utils/listReports';

    onMounted(async () => {
        reports.value = listReports()
    });


</script>

<template>
    <div class="d-flex flex-column flex-shrink-0 p-3 bg-body-tertiary overflow-auto" style="width: 280px;">
        <div class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
            <i class="bi bi-book ms-2 fs-4"></i>
            <span class="fs-4 px-2">ledger.md</span> 
        </div>
        <hr>
        <ul class="nav nav-flush flex-column mb-auto">
            <li class="nav-item">
                <router-link to="/" class="nav-link link-body-emphasis" exact-active-class="active">
                    <i class="bi bi-pencil-square me-1"></i>
                    Create Journal Entry
                </router-link>
            </li>

            <li class="nav-item">
                <router-link to="/create-report" class="nav-link link-body-emphasis" exact-active-class="active">
                    <i class="bi bi-file-earmark-code me-1"></i>
                    Create Report
                </router-link>
            </li>
            
            <hr>
            <div class="small fw-semibold text-muted px-3 mb-1">
                Reports
            </div>
            
            <li class="nav-item" v-for="report in reports">
                <router-link :to="`/view-report/${report.id}`" class="nav-link link-body-emphasis pb-0">
                    {{ report.title }}
                </router-link>
            </li>          
        </ul>
    </div>
</template>