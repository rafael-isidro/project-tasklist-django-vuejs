import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignupView from "../views/SignupView.vue";
import TasklistView from "../views/TasklistView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupView,
  },
  {
    path: "/tasklist",
    name: "tasklist",
    component: TasklistView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const protectedRoutes = ["tasklist"];

router.beforeEach((to, from, next) => {
  const isProtected = protectedRoutes.includes(to.name);
  if (isProtected && !localStorage.getItem("token")) {
    next({
      path: "/",
      query: { redirect: to.fullPath },
    });
  } else {
    if (
      !isProtected &&
      localStorage.getItem("token") &&
      (to.name == "home" || to.name == "signup")
    ) {
      next({
        path: "/tasklist",
      });
    } else {
      next();
    }
  }
});

export default router;
