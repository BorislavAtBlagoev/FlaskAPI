const users = {
  namespaced: true,
  state: {
    name: undefined,
    userId: undefined,
  },
  getters: {
    name(state) {
      return state.name;
    },
    userId(state) {
      return state.userId;
    },
  },
  mutations: {
    setName(state, name) {
      state.name = name;
    },
    setUserId(state, userId) {
      state.userId = userId;
    },
  },
  actions: {
    setName({ commit }, payload) {
      commit("setName", payload);
    },
    setUserId({ commit }, payload) {
      commit("setUserId", payload);
    },
  },
};

export default users;
