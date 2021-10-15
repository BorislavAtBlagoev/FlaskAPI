import { createStore } from "vuex";
import authentication from "./modules/authentication";
import users from "./modules/users";
import videos from "./modules/videos";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: { authentication, users, videos },
});
