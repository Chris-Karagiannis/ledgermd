<script setup>
  import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <div class="d-flex vh-100 vw-100">
    <Sidebar />

    <main class="content-area py-4 px-2">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.content-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;       /* 🔑 required for nested scrolling */
  overflow: hidden;    /* prevent double scrollbars */
}
</style>
