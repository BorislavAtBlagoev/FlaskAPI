<template>
  <div class="convertDownload">
    <h1 class="header">Convert & Download</h1>
    <Convert v-if="videoName == undefiend" />
    <Download v-if="videoName" />
    <!-- <ul>
      <li v-for="(video, index) in getUserVideos()" :key="index">
        {{ video.name }} {{ video.uid }}
      </li>
    </ul> -->
  </div>
</template>

<script>
import Convert from "@/components/Convert.vue";
import Download from "@/components/Download.vue";
import { mapGetters } from "vuex";

export default {
  name: "ConvertDownload",
  components: {
    Convert,
    Download,
  },
  data() {
    return {
      isLoading: false,
    };
  },
  computed: {
    ...mapGetters("videos", ["videos", "videoName"]),
    ...mapGetters("users", ["uid"]),
  },
  methods: {
    getUserVideos() {
      return this.videos.filter((video) => video.uid == this.uid);
    },
    load() {
      this.isLoading = true;
    },
  },
  async created() {
    await this.$store.dispatch("videos/getVideos");
  },
};
</script>

<style lang="scss" scoped>
.convertDownload {
  text-align: center;
}

.header {
  font-size: 60px;
  margin: 50px 0 30px 0;
}
</style>
