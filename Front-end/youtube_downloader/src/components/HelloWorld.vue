<template>
  <div class="hello">
    <button type="button" class="btn btn-dark" @click="login">Google</button>
    <button @click="logout">Logout</button>
    <h2>
      <span>{{ name }}</span>
      <span> </span>
      <span>{{ email }}</span>
    </h2>
  </div>
</template>

<script>
import {
  getAuth,
  signInWithPopup,
  GoogleAuthProvider,
  signOut,
} from "firebase/auth";

export default {
  name: "HelloWorld",
  data() {
    return {
      name: undefined,
      email: undefined,
    };
  },
  props: {
    msg: String,
  },
  methods: {
    login() {
      const provider = new GoogleAuthProvider();
      const auth = getAuth();
      signInWithPopup(auth, provider)
        .then((result) => {
          const credential = GoogleAuthProvider.credentialFromResult(result);
          const token = credential.accessToken;
          const user = result.user;

          this.name = user.displayName;
          this.email = user.email;

          console.log(token);
          console.log("##############################");
          console.log(user);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    logout() {
      const auth = getAuth();
      signOut(auth)
        .then((response) => {
          this.name = "";
          this.email = "";
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
