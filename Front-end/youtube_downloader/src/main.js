import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyAiy2sZ36RAWP_EGCDtkKOQZZK5HCup0aQ",
  authDomain: "converter-d47dc.firebaseapp.com",
  projectId: "converter-d47dc",
  storageBucket: "converter-d47dc.appspot.com",
  messagingSenderId: "178533857416",
  appId: "1:178533857416:web:35627b5fdc9b0bc636c73d",
  measurementId: "G-J0B158HR72",
};

initializeApp(firebaseConfig);

createApp(App).use(store).use(router).mount("#app");
