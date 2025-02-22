<template>
  <div>
    <div class="row">
      <div class="col-md-8" style="margin: auto;">
        <user-card :user="user"></user-card>
      </div>
    </div>

    <div class="row">
      <div class="col-md-8" style="margin: auto;">
        <div class="card card-user">
          <div class="card-body">
            <h3 class="card-title" style="text-align: center; margin-top: 25px;">UBC Lost & Found</h3> 
            <div class="image-container">
              <img class="figure-img img-fluid" src="img/access.jpg" alt="..." />
              <p class="figure-caption card-description" style="margin-top: 0;">Access Services. Retrieved from <a href="https://parking.ubc.ca/">UBC Parking</a></p>
              <p class="card-text"></p>
              <p></p>
              <p class="card-description" style="margin-top: 0;">6200 University Boulevard</p>
              <p class="card-description" style="margin-top: 0;">Vancouver, British Columbia, V6T 1Z4</p>
              <p class="card-description" style="margin-top: 0;">Telephone: 604 822 6786</p>
            </div>
              <div class="author">
                <div class="rotate8">
                  <div class="block block-one"></div>
                  <div class="block block-two"></div>
                  <div class="block block-three"></div>
                  <div class="block block-four"></div>
                </div>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import UserCard from "./Profile/UserCard";
export default {
  components: {
    UserCard,
  },
  data() {
    return {
      user: {
        fullName: "UBC Lost & Found Dashboard",
        title: "About",
        description: `Losing personal belongings is a common and often frustrating experience for students and staff at UBC. Items ranging from everyday essentials like wallets and keys to electronics and jewelry frequently end up in the lost and found. While the university maintains a central lost and found system, the lack of systematic analysis in these services can lead to inefficiencies, making it harder to identify trends and optimize recovery processes. `,
        description2: `Through analyzing the UBC lost and found database, this dashboard web app is designed to uncover patterns in lost items, predict future trends, and provide data-driven insights for students and staffs using the UBC lost and found services.`,
      },
    };
  },
};
</script>
<style scoped>
.image-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.image-container img {
  max-width: 60%;
  height: auto;
}

.text-container {
  text-align: left;
  width: 100%;
  max-width: 60%;
}

.rotate8{ /*vertical flip*/ /*upside-down mirror*/
-webkit-transform:rotate(180deg); 
  -moz-transform: rotate(180deg); 
  -ms-transform: rotate(180deg); 
  -o-transform: rotate(180deg); 
  transform: rotate(180deg); 
}
</style>
