<template>
  <div class="convertDownload">
    <h1 class="header">Convert & Download</h1>
    <Convert v-if="videoName == undefiend" />
    <Download v-if="videoName" />
    <!-- <VideoList /> -->
  </div>
</template>

<script>
import Convert from "@/components/Convert.vue";
import Download from "@/components/Download.vue";
// import VideoList from "@/components/VideoList.vue";

import { mapGetters } from "vuex";

export default {
  name: "ConvertDownload",
  components: {
    Convert,
    Download,
    // VideoList,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters("videos", ["videoName"]),
  },
  methods: {},
  async created() {},
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
