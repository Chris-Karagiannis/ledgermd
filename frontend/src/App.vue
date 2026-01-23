<script setup>
  import Journals from './views/Journals.vue';
  import Sidebar from './components/Sidebar.vue';
import { router } from './router';
</script>

<template>
    <div class="d-flex vh-100 vw-100 ">
      <Sidebar/>
      
      <main class="content-area bg-white">
        <div class="container-fluid p-4">
          <router-view></router-view>
        </div>
      </main>
  </div>

</template>

<style scoped>
body, html {
  margin: 0;
  height: 100%;
  overflow: hidden;
}

.content-area {
  flex-grow: 1;
  height: 100%;
  overflow-y: auto; 
  background-color: #f8f9fa;
  position: relative; 
}

</style>
