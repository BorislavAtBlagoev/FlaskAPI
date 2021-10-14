<template>
  <div class="container convert">
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
          {{ buttonText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Convert",
  data() {
    return {
      placeholder: "Enter youtube URL",
      buttonText: "Convert",
      videoURL: undefined,
    };
  },
  computed: {},
  methods: {
    async convertVideo() {
      const url = { url: this.videoURL };
      await this.$store.dispatch("videos/convertVideo", url);
    },
  },
};
</script>

<style lang="scss" scoped>
.convert {
}
</style>
