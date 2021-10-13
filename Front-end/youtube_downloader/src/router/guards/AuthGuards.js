import store from "../../store";

export const isAuthenticated = (to, from, next) => {
  if (store.state.authentication.isAuthenticated) {
    next();
  } else {
    next({ path: "/" });
  }
};

export const isManager = (to, from, next) => {
  if (store.state.authentication.userData.roles === "Manager") {
    next();
  } else {
    next({ path: "/goals" });
  }
};
