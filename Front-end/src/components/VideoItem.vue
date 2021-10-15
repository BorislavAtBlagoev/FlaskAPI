<template>
  <div class="videoItem">
    {{ videoItem.name }}
    {{ videoItem.uid }}
  </div>
</template>

<script>
export default {
  name: "VideoItem",
  props: {
    videoItem: Object,
  },
};
</script>
