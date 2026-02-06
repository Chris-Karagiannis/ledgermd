<script setup>
    import { ref, onMounted } from 'vue';
    import { listReports, reports } from '@/utils/listReports';

    onMounted(async () => {
        reports.value = listReports()
    });

</script>

<template>   
    <div class="sidebar d-flex flex-column flex-shrink-0 p-3 overflow-auto" style="width: 280px;">
        <div class="sidebar-header d-flex align-items-center">
            <i class="bi bi-book ms-2 fs-4"></i>
            <span class="fs-4 px-2">ledger.md</span> 
        </div>
        <hr>
        <ul class="nav nav-flush flex-column mb-auto">
            <li class="nav-item">
                <router-link to="/" title="Create Journal Entry" class="nav-link link-body-emphasis" exact-active-class="active">
                    <i class="bi bi-pencil-square me-1"></i>
                    Create Journal Entry
                </router-link>
            </li>

            <li class="nav-item">
                <router-link to="/create-report" title="Create Report" class="nav-link link-body-emphasis" exact-active-class="active">
                    <i class="bi bi-file-earmark-code me-1"></i>
                    Create Report
                </router-link>
            </li>
            
            <hr>
            <div class="sidebar-section-label">
                Reports
            </div>
            
            <li class="nav-item" v-for="report in reports">
                <router-link :to="`/view-report/${report.id}`" class="nav-link link-body-emphasis">
                    {{ report.title }}
                </router-link>
            </li>          
        </ul>
    </div>
</template>

<style scoped>
.sidebar {
  width: 280px;
  height: 100vh;
  border-right: 1px solid rgba(0, 0, 0, 0.06);
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.95),
    rgba(248, 249, 250, 0.95)
  );
  backdrop-filter: blur(6px);
  transition: box-shadow 0.25s ease;
}

.sidebar:hover {
  box-shadow: 4px 0 12px rgba(0, 0, 0, 0.04);
}

.sidebar-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem 0.25rem 0.75rem;
}

.sidebar-header i {
  color: var(--bs-primary);
}

.sidebar-header span {
  font-weight: 600;
  letter-spacing: 0.2px;
}

.sidebar .nav-link {
  position: relative;
  overflow: hidden;
  border-radius: 6px;
  padding: 0.45rem 0.75rem;
  margin: 0.15rem 0;
  color: var(--bs-body-color);
  transition: background-color 0.15s ease, color 0.15s ease;
}

.sidebar .nav-link:hover {
  background-color: rgba(13, 110, 253, 0.08);
  color: var(--bs-primary);
}

.sidebar .nav-link::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(13, 110, 253, 0.12),
    transparent
  );
  opacity: 0;
  transform: translateX(-100%);
}

.sidebar .nav-link:hover::before {
  opacity: 1;
  transform: translateX(100%);
  transition: transform 0.6s ease;
}

.sidebar .nav-link.active {
  background-color: rgba(13, 110, 253, 0.15);
  color: var(--bs-primary);
  font-weight: 500;
}

.sidebar .nav-link.active::after {
  content: "";
  position: absolute;
  left: 0;
  top: 20%;
  height: 60%;
  width: 3px;
  border-radius: 2px;
  background-color: var(--bs-primary);
}

.sidebar .nav-link i {
  width: 1.25rem;
  text-align: center;
  opacity: 0.85;
}

.sidebar-section-label {
  text-transform: uppercase;
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  color: var(--bs-secondary);
  padding: 0.5rem 0.75rem 0.25rem;
}

.sidebar .nav-item .nav-link {
  font-size: 0.9rem;
  padding: 0.45rem 0.75rem;
  padding-left: 1.75rem;
  color: var(--bs-secondary);
}


.sidebar .nav-item .nav-link:hover {
  color: var(--bs-primary);
}

.sidebar hr {
  margin: 0.75rem 0;
  opacity: 0.08;
}


</style>