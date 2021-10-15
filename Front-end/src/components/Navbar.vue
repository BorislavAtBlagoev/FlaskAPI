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
    ...mapGetters("users", ["name", "userId"]),
  },
  methods: {
    login() {
      const provider = new GoogleAuthProvider();
      const auth = getAuth();
      signInWithPopup(auth, provider)
        .then((result) => {
          const user = result.user;

          this.$store.dispatch("authentication/setIsAuthenticated", true);
          this.$store.dispatch("users/setName", user.displayName);
          this.$store.dispatch("users/setUserId", user.uid);

          this.$router.push({ path: "/convert_download" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    logout() {
      const auth = getAuth();
      signOut(auth)
        .then(() => {
          this.$store.dispatch("authentication/setIsAuthenticated", false);
          this.$store.dispatch("users/setName", undefined);
          this.$store.dispatch("users/setUid", undefined);

          this.$router.push({ path: "/" });
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
