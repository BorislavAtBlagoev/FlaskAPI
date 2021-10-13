const users = {
  namespaced: true,
  state: {
    name: undefined,
    uid: undefined,
  },
  getters: {
    name(state) {
      return state.name;
    },
    uid(state) {
      return state.uid;
    },
  },
  mutations: {
    setName(state, name) {
      state.name = name;
    },
    setUid(state, uid) {
      state.uid = uid;
    },
  },
  actions: {
    setName({ commit }, payload) {
      commit("setName", payload);
    },
    setUid({ commit }, payload) {
      commit("setUid", payload);
    },
  },
};

export default users;
