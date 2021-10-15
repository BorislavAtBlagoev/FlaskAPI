import { createRouter, createWebHistory } from "vue-router";
import { isAuthenticated } from "./guards/AuthGuards";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue"),
  },
  {
    path: "/convert_download",
    name: "Downloads",
    component: () =>
      import(
        /* webpackChunkName: "convertDownload" */ "../views/ConvertDownload.vue"
      ),
    beforeEnter: isAuthenticated,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
