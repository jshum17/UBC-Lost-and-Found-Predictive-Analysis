<template>
  <div class="sidebar" :data="backgroundColor">
    <!--
            Tip 1: you can change the color of the sidebar's background using: data-background-color="white | black | darkblue"
            Tip 2: you can change the color of the active button using the data-active-color="primary | info | success | warning | danger"
        -->
    <!-- -->
    <div class="sidebar-wrapper" id="style-3">
      <div class="logo">
        <a
          href="#/dashboard"
          aria-label="sidebar mini logo"
          class="simple-text logo-mini"
        >
          <div :class="{ 'logo-img-rtl': $rtl.isRTL }">
            <img
              src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAdVBMVEUMIkQIIEMABzcAAC0ADzoAHEEAADIAGj8AADUAADAAFj8ADDmytr7///+UmaNBTGM7SGD4+frc3uJVXnGkqLK6vcSanqfBxMmJjpnu7/HKzdIAAAiOk58YKklfaHkAACPj5OcAACorOVMAABl/hZJvdoYFH0Lo00HFAAAAvElEQVR4AeTNhWHAIBAF0OD64+6+/4gldRmhODzuLvrfjXyeKAsLZ0IwxqQKoo017t08XMRjJCmyLC8sCQ9A+aa6go5c/WDTdnAsD3vV69/YDiOmGX7h2pI/kXXWLCWSp3D0G7sVzeaxi/D8iZTQt7THjDPGbCOi3jAEncuSgycBC4w7Vs3M/KZEZVgzlDJBlwOTrIEcmXkLFVHZN5e8d1/6ONzkXPW+eM8b3VRq+2yU8jvclZZavWwEJRYAWUgNmOXC7ekAAAAASUVORK5CYII="
              alt=""
            />
          </div>
        </a>
        <a href="#/dashboard" class="simple-text logo-normal">
          {{ title }}
        </a>
      </div>
      <slot> </slot>
      <ul class="nav">
        <!--By default vue-router adds an active class to each route link. This way the links are colored when clicked-->
        <slot name="links">
          <sidebar-link
            v-for="(link, index) in sidebarLinks"
            :key="index"
            :to="link.path"
            :name="link.name"
            :icon="link.icon"
          >
          </sidebar-link>
        </slot>
      </ul>
    </div>
  </div>
</template>
<script>
import SidebarLink from "./SidebarLink";

export default {
  props: {
    title: {
      type: String,
      default: "UBC Lost & Found",
    },
    backgroundColor: {
      type: String,
      default: "primary",
    },
    activeColor: {
      type: String,
      default: "success",
      validator: (value) => {
        let acceptedValues = [
          "primary",
          "info",
          "success",
          "warning",
          "danger",
        ];
        return acceptedValues.indexOf(value) !== -1;
      },
    },
    sidebarLinks: {
      type: Array,
      default: () => [],
    },
    autoClose: {
      type: Boolean,
      default: true,
    },
  },
  provide() {
    return {
      autoClose: this.autoClose,
      addLink: this.addLink,
      removeLink: this.removeLink,
    };
  },
  components: {
    SidebarLink,
  },
  computed: {
    /**
     * Styles to animate the arrow near the current active sidebar link
     * @returns {{transform: string}}
     */
    arrowMovePx() {
      return this.linkHeight * this.activeLinkIndex;
    },
    shortTitle() {
      return this.title
        .split(" ")
        .map((word) => word.charAt(0))
        .join("")
        .toUpperCase();
    },
  },
  data() {
    return {
      linkHeight: 65,
      activeLinkIndex: 0,
      windowWidth: 0,
      isWindows: false,
      hasAutoHeight: false,
      links: [],
    };
  },
  methods: {
    findActiveLink() {
      this.links.forEach((link, index) => {
        if (link.isActive()) {
          this.activeLinkIndex = index;
        }
      });
    },
    addLink(link) {
      const index = this.$slots.links.indexOf(link.$vnode);
      this.links.splice(index, 0, link);
    },
    removeLink(link) {
      const index = this.links.indexOf(link);
      if (index > -1) {
        this.links.splice(index, 1);
      }
    },
  },
  mounted() {
    this.$watch("$route", this.findActiveLink, {
      immediate: true,
    });
  },
};
</script>
