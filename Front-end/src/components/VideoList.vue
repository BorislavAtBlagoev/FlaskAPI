<template>
  <div class="videoList">
    <ul>
      <VideoItem
        v-for="(item, index) in getUserVideos()"
        :key="index"
        :videoItem="item"
      />
    </ul>
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
    ...mapGetters("users", ["uid"]),
  },
  methods: {
    getUserVideos() {
      return this.videos.filter((video) => video.uid == this.uid);
    },
  },
  async created() {
    await this.$store.dispatch("videos/getVideos");
  },
};
</script>

<style lang="scss" scoped>
ul {
  list-style-type: none;
}
</style>
