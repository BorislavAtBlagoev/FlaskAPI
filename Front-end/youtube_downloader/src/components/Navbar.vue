<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link :to="header.path"
        ><a class="navbar-brand">{{ header.title }}</a></router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <div v-for="(item, index) in navbarItems" :key="index">
            <li v-if="isAuthenticated" class="nav-item">
              <router-link :to="item.path"
                ><a class="nav-link active">{{ item.title }}</a></router-link
              >
            </li>
          </div>
        </ul>
        <p class="userName">{{ name }}</p>
        <button
          type="button"
          class="btn btn-success"
          v-if="!isAuthenticated"
          @click="login"
        >
          Login
        </button>
        <button type="button" class="btn btn-danger" v-else @click="logout">
          Logout
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
import {
  getAuth,
  signInWithPopup,
  GoogleAuthProvider,
  signOut,
} from "firebase/auth";
import store from "../store";
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  data() {
    return {
      header: {
        title: "Youtube Convert & Download",
        path: "/",
      },
      navbarItems: [
        {
          title: "Convert & Download",
          path: "/convert_download",
        },
      ],
    };
  },
  computed: {
    ...mapGetters("authentication", ["isAuthenticated"]),
    ...mapGetters("users", ["name", "uid"]),
  },
  methods: {
    login() {
      const provider = new GoogleAuthProvider();
      const auth = getAuth();
      signInWithPopup(auth, provider)
        .then((result) => {
          const user = result.user;
          store.dispatch("authentication/setIsAuthenticated", true);
          store.dispatch("users/setName", user.displayName);
          store.dispatch("users/setUid", user.uid);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    logout() {
      const auth = getAuth();
      signOut(auth)
        .then(() => {
          store.dispatch("authentication/setIsAuthenticated", false);
          store.dispatch("users/setName", undefined);
          store.dispatch("users/setUid", undefined);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
a {
  text-decoration: none;
}

.userName {
  font-size: 20px;
  color: #fff;
  margin: 0 10px 0 0;
}
</style>
