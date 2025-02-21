<template>
  <footer class="footer">
    <div class="container-fluid">
      <ul class="nav">
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/jshum17/UBC-Lost-and-Found-Predictive-Analysis" target="_blank">
            GitHub
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="showCredits" style="cursor: pointer">
            Credits
          </a>
        </li>
      </ul>
      <div class="copyright">
        © {{ year }}
      </div>
    </div>

    <!-- Modal -->
    <div v-if="isModalVisible" class="modal-overlay" @click="hideCredits">
      <div class="modal-content" @click.stop>
        <h5>Credits</h5>
        <p>Designed with elements from
          <a href="https://www.binarcode.com" target="_blank" rel="noopener">Binar Code</a>
          &
          <a href="https://www.creative-tim.com" target="_blank" rel="noopener">Creative Tim</a>
        </p>
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
      document.body.style.overflow = 'hidden'; // Prevent background scrolling
    },
    hideCredits() {
      this.isModalVisible = false;
      document.body.style.overflow = 'auto'; // Restore scrolling
    },
  },
};
</script>

<style scoped>
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
  animation: fadeIn 0.3s ease-out;
}

.modal-content {
  width: 35%;
  min-width: 300px; 
  max-width: 500px; 
  background: #e8ecef; 
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  border: 3px solid; 
  border-image: linear-gradient(to right, #4767bc, #7289cc) 1;
  animation: slideIn 0.3s ease-out;
}

/* Optional animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { transform: translateY(-20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* Style improvements */
.modal-content h5 {
  margin-bottom: 15px;
  color: #333;
}

.modal-content p {
  margin-bottom: 20px;
  color: #666;
}

.btn-primary {
  background-color: #4767bc;
  border-color: #4767bc;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: #7289cc;
  border-color: #7289cc;
}
</style>