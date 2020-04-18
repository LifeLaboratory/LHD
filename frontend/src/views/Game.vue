<template>
  <div class="game-container"> 
      <div class="top-menu">
        <div class="actual-day">
          День - 5
        </div>
      </div>

      <div class="center-menu">
        <div class="card-box">
          
        </div>
      </div>



      <div class="bottom-menu">
        <a-row class="profile-game">
          <a-col :span="4">
            <a-avatar :size="128" src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
          </a-col>
          <a-col :span="16" class="stats-game">
            <div>Профессия: Работяга</div>
            <div>
              <div style="display: inline-block">
                <a-icon type="heart" theme="twoTone" twoToneColor="#eb2f96" />
              </div>
              <a-progress :percent="30" :strokeColor="{  '0%': '#eb2f96', '100%': '#eb2f96'}" />
            </div>

            <div>
              <div style="display: inline-block">
                <a-icon type="coffee" style="color:rgb(235, 134, 47);" />
              </div>
              <a-progress :percent="30" :strokeColor="{  '0%': 'rgb(235, 134, 47)', '100%': 'rgb(235, 134, 47)'}" />
            </div>

            <div>
              <div style="display: inline-block">
                <a-icon type="smile" theme="twoTone" twoToneColor="rgb(62, 181, 98)" />
              </div>
              <a-progress :percent="30" :strokeColor="{  '0%': 'rgb(62, 181, 98)', '100%': 'rgb(62, 181, 98)'}" />
            </div>

            <div>
              <div style="display: inline-block">
                <a-icon type="home" theme="twoTone" twoToneColor="rgb(59, 47, 235)" />
              </div>
              <a-progress :percent="30" :strokeColor="{  '0%': 'rgb(59, 47, 235)', '100%': 'rgb(59, 47, 235)'}" />
            </div>
          </a-col>
        </a-row>
      </div>
  </div>
</template>

<script>

export default {
  data: {
   
  },
  methods: {
    
  },

};
</script>
<style>
.card-box {
  margin-top: 50px;
}
.actual-day {
  font-size: 24px;
  background: rgba(255,255,255,0.8);
  border-radius: 0px 0px 5px 5px;
  width: 50%;
  top:0px;
  margin-left: 25%;
}
.game-container {
  height: 100vh;
  width: 100vw;
}

.center-menu {
  vertical-align: middle;
}

.stats-game {
  margin-left: 30px;
  margin-top: 10px;
  text-align: left
}

.ant-progress-line {
  margin-left: 10px;
  width: 80% !important;
}

.bottom-menu{
  border: solid 1.2px black;
  border-radius: 5px 5px 0px 0px;
  left: 25%;
  width: 50%;
  min-width: 550px;
  background: rgba(255,255,255,0.8);
  position: absolute;
  bottom: 0px;
}

</style>
