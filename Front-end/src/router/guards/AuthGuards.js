import store from "../../store";

export const isAuthenticated = (to, from, next) => {
  if (store.state.authentication.isAuthenticated) {
    next();
  } else {
    next({ path: "/" });
  }
};
