<template>
  <div class="container convert">
    <div class="input-group mb-3">
      <input type="text" class="form-control" :placeholder="placeholder" />
      <div class="input-group-append">
        <button class="btn btn-outline-secondary" type="button">
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
    };
  },
};
</script>

<style lang="scss" scoped>
.convert {
}
</style>
