<template>
  <div class="videoItem">
    <div class="card">
      <div class="card-body">
        <h4 class="videoName">{{ videoItem.name }}</h4>
        <a :href="videoItem.url" target="_blank"
          ><button type="button" class="btn btn-dark">Show</button></a
        >
        <span> | </span>
        <button
          type="button"
          class="btn btn-danger"
          @click="deleteVideo(videoItem._id)"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "VideoItem",
  props: {
    videoItem: Object,
  },
  methods: {
    async deleteVideo(id) {
      await this.$store.dispatch("videos/deleteVideo", id);
      await this.$store.dispatch("videos/getVideos");
    },
  },
};
</script>

<style lang="scss" scoped>
.videoItem {
  width: 320px;
  margin: 0 0 20px 0;
}

.card {
  background-color: #cccccc;
}

.videoName {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  height: 35px;
}
</style>
