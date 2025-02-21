<template>
  <footer class="footer">
    <div class="container-fluid">
      <ul class="nav">
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/jshum17/UBC-Lost-and-Found-Predictive-Analysis">
            GitHub
          </a>
        </li>
        <li class="nav-item">
          <button class="nav-link btn btn-link" @click="showCredits" style="font-weight: 400;">
            Credits
          </button>
        </li>
      </ul>
      <div class="copyright">
        © {{ year }} made with <i class="tim-icons icon-heart-2"></i> by
        <a href="https://www.binarcode.com" target="_blank" rel="noopener"
          >Binar Code</a
        >&nbsp;&
        <a href="https://www.creative-tim.com" target="_blank" rel="noopener"
          >Creative Tim</a
        >
        for a better web.
      </div>
    </div>

    <!-- Modal -->
    <div v-if="isModalVisible" class="modal-overlay" @click="hideCredits">
      <div class="modal-content" @click.stop>
        <h5>Credits</h5>
        <p>Web design by Binar Code and Creative Tim.</p>
        <button class="btn btn-primary" @click="hideCredits">Close</button>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear(),
      isModalVisible: false,
    };
  },
  methods: {
    showCredits() {
      this.isModalVisible = true;
    },
    hideCredits() {
      this.isModalVisible = false;
    },
  },
};
</script>
<style>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}
</style>
