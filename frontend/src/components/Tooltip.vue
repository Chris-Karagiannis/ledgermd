<script setup>
defineProps({
  text: {
    type: String,
    required: true
  }
})
</script>

<template>
  <span class="tooltip-box">
    <slot></slot>
    <span class="tooltiptext">
      {{ text }}
    </span>
  </span>
</template>

<style scoped>
.tooltip-box {
  position: relative;
  display: inline-block;
}

.tooltiptext {
  visibility: hidden;
  opacity: 0;
  pointer-events: none;
  position: absolute;
  bottom: calc(100% + 6px);
  left: 50%;
  transform: translateX(-50%);
  width: max-content;
  max-width: 320px;
  padding: 0.35rem 0.6rem;
  font-size: 0.75rem;
  line-height: 1.4;
  color: #fff;
  background-color: #212529;
  border-radius: 0.375rem;
  white-space: normal;
  text-align: center;
  z-index: 1080;
  transition: opacity 0.15s ease-in-out;
}

.tooltip-box:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}


.tooltiptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-width: 5px;
  border-style: solid;
  border-color: #212529 transparent transparent transparent;
}
</style>