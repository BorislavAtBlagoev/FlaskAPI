<template>
  <div class="videoList container">
    <div class="row">
      <div
        class="col d-flex justify-content-center"
        v-for="(item, index) in getUserVideos"
        :key="index"
      >
        <VideoItem :videoItem="item" />
      </div>
    </div>
  </div>
</template>

<script>
import VideoItem from "./VideoItem";
import { mapGetters } from "vuex";

export default {
  name: "VideoList",
  components: {
    VideoItem,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters("videos", ["videos", "videoName"]),
    ...mapGetters("users", ["userId"]),
    getUserVideos() {
      return this.videos.filter((video) => video.userId == this.userId);
    },
  },
  methods: {},
  async created() {
    await this.$store.dispatch("videos/getVideos");
  },
};
</script>

<style lang="scss" scoped>
ul {
  list-style-type: none;
}

.videoList {
  margin-top: 100px;
  text-align: center;
}
</style>
