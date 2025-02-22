<template>
  <card type="user">
    <p class="card-text"></p>
    <div class="author">
      <div class="block block-one"></div>
      <div class="block block-two"></div>
      <div class="block block-three"></div>
      <div class="block block-four"></div>
      <a href="#">
        <!-- <img class="avatar" src="img/anime6.png" alt="..." /> -->
        <!-- <h5 class="title">{{ user.fullName }}</h5> -->
      </a>
      <h3 class="card-title">
        {{ user.title }}
      </h3>
      <!-- <img class="figure-img" src="img/access.jpg" alt="..." />
      <p class = "figure-caption">Access Services. Retrieved from <a href = "https://parking.ubc.ca/">UBC Parking</a> </p> -->
    </div>
    <p class="card-description"></p>
     <p></p>
    <p class="card-description" style="margin: auto 4% 4% 4%;">
      {{ user.description }}
    </p>
    <p class="card-description" style="margin: auto 4% 4% 4%;">
      {{ user.description2 }}
    </p>
    <!-- <div slot="footer" class="button-container">
      <base-button icon round class="btn-facebook">
        <i class="fab fa-facebook"></i>
      </base-button>
      <base-button icon round class="btn-twitter">
        <i class="fab fa-twitter"></i>
      </base-button>
      <base-button icon round class="btn-google">
        <i class="fab fa-google-plus"></i>
      </base-button>
    </div> -->
  </card>
</template>
<script>
export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
};
</script>
<style></style>
