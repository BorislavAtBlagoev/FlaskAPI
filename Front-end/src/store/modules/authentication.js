const authentication = {
  namespaced: true,
  state: {
    isAuthenticated: false,
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
  },
  mutations: {
    setIsAuthenticated(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
  },
  actions: {
    setIsAuthenticated({ commit }, payload) {
      commit("setIsAuthenticated", payload);
    },
  },
};

export default authentication;
