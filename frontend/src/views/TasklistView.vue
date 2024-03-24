<template>
  <div class="tasklist">
    <Tasklist />
  </div>
</template>

<script>
import Tasklist from '@/components/Tasklist.vue';

export default {
  name: "TasklistView",
  components: {
    Tasklist
  }
}
</script>