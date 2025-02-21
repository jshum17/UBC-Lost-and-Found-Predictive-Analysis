<template>
  <nav
    class="navbar navbar-expand-lg navbar-absolute"
    :class="{ 'bg-white': showMenu, 'navbar-transparent': !showMenu }"
  >
    <div class="container-fluid">
      <div class="navbar-wrapper">
        <div
          class="navbar-toggle d-inline"
          :class="{ toggled: $sidebar.showSidebar }"
        >
          <button
            type="button"
            class="navbar-toggler"
            aria-label="Navbar toggle button"
            @click="toggleSidebar"
          >
            <span class="navbar-toggler-bar bar1"></span>
            <span class="navbar-toggler-bar bar2"></span>
            <span class="navbar-toggler-bar bar3"></span>
          </button>
        </div>
        <a class="navbar-brand" href="#">{{ routeName }}</a>
      </div>
      <button
        class="navbar-toggler"
        type="button"
        @click="toggleMenu"
        data-toggle="collapse"
        data-target="#navigation"
        aria-controls="navigation-index"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-bar navbar-kebab"></span>
        <span class="navbar-toggler-bar navbar-kebab"></span>
        <span class="navbar-toggler-bar navbar-kebab"></span>
      </button>

      <collapse-transition>
        <div class="collapse navbar-collapse show" v-show="showMenu">
          <ul class="navbar-nav" :class="$rtl.isRTL ? 'mr-auto' : 'ml-auto'">
            <li class="nav-item">
              <a class="nav-link" @click="toggleTheme" style="cursor: pointer;">
                <i :class="isLightMode ? 'tim-icons icon-light-3' : 'tim-icons icon-light-3'"></i>
              </a>
            </li>
          </ul>
        </div>
      </collapse-transition>
    </div>
  </nav>
</template>
<script>
import { CollapseTransition } from "vue2-transitions";
import Modal from "@/components/Modal";

export default {
  components: {
    CollapseTransition,
    Modal,
  },
  computed: {
    routeName() {
      const { name } = this.$route;
      return this.capitalizeFirstLetter(name);
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
  },
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchModalVisible: false,
      searchQuery: "",
      isLightMode: false,
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleNotificationDropDown() {
      this.activeNotifications = !this.activeNotifications;
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    toggleTheme() {
      this.isLightMode = !this.isLightMode;
      this.applyTheme();
    },
    applyTheme() {
      const html = document.documentElement;
      if (this.isLightMode) {
        html.classList.add('light-mode');
      } else {
        html.classList.remove('light-mode');
      }
      localStorage.setItem('theme', this.isLightMode ? 'light' : 'dark');
    },
    loadTheme() {
      const savedTheme = localStorage.getItem('theme');
      this.isLightMode = savedTheme === 'light';
      this.applyTheme();
    },
  },
  created() {
    this.loadTheme(); // Load saved theme on component creation
  },
};
</script>

<style lang="scss">
@import "@/assets/sass/black-dashboard.scss";

.light-mode {
  @extend .white-content;
}

</style>
