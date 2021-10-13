<template>
  <div class="convertDownload">
    <h1 class="header">Convert & Download</h1>
    <Convert />
  </div>
</template>

<script>
import Convert from "@/components/Convert.vue";

export default {
  name: "ConvertDownload",
  components: {
    Convert,
  },
  data() {
    return {};
  },
  computed: {},
  methods: {},
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
