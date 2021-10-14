<template>
  <div class="container convert">
    <Loading
      v-model:active="isLoading"
      :loader="dots"
      :lock-scroll="true"
      :opacity="0.8"
      :height="200"
      :width="200"
      blur="10px"
      background-color="#000"
      color="#fff"
    />
    <div class="input-group mb-3">
      <input
        type="text"
        class="form-control"
        v-model.trim="videoURL"
        :placeholder="placeholder"
      />
      <div class="input-group-append">
        <button
          class="btn btn-outline-secondary"
          type="button"
          @click="convertVideo"
        >
          {{ convertButtonText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";

export default {
  name: "Convert",
  components: {
    Loading,
  },
  data() {
    return {
      placeholder: "Enter youtube URL",
      convertButtonText: "Convert",
      videoURL: undefined,
      isLoading: false,
    };
  },
  computed: {},
  methods: {
    async convertVideo() {
      this.isLoading = true;
      const url = { url: this.videoURL };
      await this.$store.dispatch("videos/convertVideo", url);
      this.isLoading = false;
    },
  },
};
</script>

<style lang="scss" scoped>
.convert {
}
</style>
