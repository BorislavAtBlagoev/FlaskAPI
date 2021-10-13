import { createStore } from "vuex";
import authentication from "./modules/authentication";
import users from "./modules/users";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: { authentication, users },
});
