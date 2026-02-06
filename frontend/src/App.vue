<script setup>
  import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <div class="d-flex vh-100 vw-100">
    <Sidebar />

    <transition name="slide" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<style>
.content-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;
  overflow: hidden;
}

.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-enter-from {
  transform: translateX(20px);
  opacity: 0;
}

.slide-leave-to {
  transform: translateX(-20px);
  opacity: 0;
}

html,
body {
  overflow-x: hidden;
}

.page-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--bs-body-color);
  padding-left: 0.25rem;
}

.page-title i {
  color: var(--bs-primary);
}

</style>
