<template>
  <div class="download">
    <h2>Video Name: {{ videoName }}</h2>
    <button type="button" class="btn btn-dark" @click="downloadAudio">
      {{ downloadButtonText }}
    </button>
    <span> | </span>
    <button type="button" class="btn btn-dark" @click="nextDownload">
      {{ nextDownloadButtonText }}
    </button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Download",
  data() {
    return {
      downloadButtonText: "Download",
      nextDownloadButtonText: "Next Download",
    };
  },
  computed: {
    ...mapGetters("videos", ["videoName"]),
  },
  methods: {
    downloadAudio() {
      const AWS = require("aws-sdk");

      const s3bucket = new AWS.S3({
        accessKeyId: process.env.VUE_APP_AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.VUE_APP_AWS_SECRET_ACCESS_KEY,
        signatureVersion: "v4",
        region: process.env.VUE_APP_AWS_REGION,
      });

      var params = {
        Key: `${this.videoName}.mp3`,
        Bucket: process.env.VUE_APP_BUCKET_NAME,
      };

      s3bucket.getObject(params, (err, data) => {
        if (err) {
          throw err;
        }
        var fileURL = window.URL.createObjectURL(new Blob([data.Body]));
        var fileLink = document.createElement("a");

        fileLink.href = fileURL;
        fileLink.setAttribute("download", `${this.videoName}.mp3`);
        document.body.appendChild(fileLink);

        fileLink.click();
      });
    },
    nextDownload() {
      this.$store.dispatch("videos/clearVideoName");
    },
  },
};
</script>
