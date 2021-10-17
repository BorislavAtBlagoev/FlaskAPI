import axios from "axios";

const videos = {
  namespaced: true,
  state: {
    videos: [],
    videoName: undefined,
  },
  getters: {
    videos(state) {
      return state.videos;
    },
    videoName(state) {
      return state.videoName;
    },
  },
  mutations: {
    setVideos(state, videos) {
      state.videos = videos;
    },
    setVideoName(state, videoName) {
      state.videoName = videoName;
    },
  },
  actions: {
    async getVideos({ commit }) {
      try {
        const { data } = await axios.get(
          `${process.env.VUE_APP_API_BASE_URL}/${process.env.VUE_APP_API_VIDEO_LIST_ENDPOINT}`
        );
        commit("setVideos", data);
      } catch (err) {
        console.error(err);
      }
    },
    async convertVideo({ commit }, payload) {
      await axios
        .post(
          `${process.env.VUE_APP_API_BASE_URL}/${process.env.VUE_APP_API_CONVERT_VIDEO_ENDPOINT}`,
          payload
        )
        .then((response) => {
          commit("setVideoName", response.data);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async deleteVideo(_, payload) {
      await axios
        .delete(
          `${process.env.VUE_APP_API_BASE_URL}/${process.env.VUE_APP_API_VIDEO_ENDPOINT}/${payload}`
        )
        .then()
        .catch((err) => {
          console.error(err);
        });
    },
    async clearVideoName({ commit }) {
      commit("setVideoName", undefined);
    },
  },
};

export default videos;
