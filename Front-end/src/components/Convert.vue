<template>
  <div class="container convert">
    <Loading
      v-model:active="isLoading"
      :lock-scroll="true"
      :opacity="0.8"
      :height="200"
      :width="200"
      loader="dots"
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
          class="btn btn-outline-dark"
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
import { mapGetters } from "vuex";
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
  computed: {
    ...mapGetters("users", ["userId"]),
  },
  methods: {
    async convertVideo() {
      this.isLoading = true;
      const payload = { url: this.videoURL, userId: this.userId };
      await this.$store.dispatch("videos/convertVideo", payload);
      this.isLoading = false;
    },
  },
};
</script>
