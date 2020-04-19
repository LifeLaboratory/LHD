<template>
  <div class="game-container"> 
      <div class="top-menu">
        <div class="actual-day">
          День - {{day}}
        </div>
      </div>

    <div class="outer" style="height:80vh; width: 50%; margin-left: 25%" v-if="descr != ''">
      <div class="inner">


        <div class="card-box">
          <div style="margin-top: 50px; font-size: 20px; word-wrap: break-word; padding-left: 10px; padding-right: 10px;">
              <b>{{descr}}</b>
          </div>
        </div>
        <div style="
            width: 70%;
            margin-left: 15%;
            background: rgba(255,255,255,0.8);
            padding-bottom: 15px;
            height: 90px;
            ">
            <a-button :disabled="dis" @click="sendAnswer('left')">{{left}} </a-button>
            <a-button :disabled="dis"  @click="sendAnswer('right')">{{right}}</a-button>
        </div>
      </div>
    </div>

      <div class="bottom-menu">
        <a-row class="profile-game">
          <a-col :span="4">
            <a-avatar :size="128" :src="pic" />
          </a-col>
          <a-col :span="16" class="stats-game">
            <div>Профессия: {{user.name}}</div>
            <div>
              <div style="display: inline-block">
                <a-icon type="heart" theme="twoTone" twoToneColor="#eb2f96" />
              </div>
              <a-progress :percent="user.health" :strokeColor="{  '0%': '#eb2f96', '100%': '#eb2f96'}" />
            </div>

            <div>
              <div style="display: inline-block">
                <a-icon type="coffee" style="color:rgb(235, 134, 47);" />
              </div>
              <a-progress :percent="user.eat" :strokeColor="{  '0%': 'rgb(235, 134, 47)', '100%': 'rgb(235, 134, 47)'}" />
            </div>

            <div>
              <div style="display: inline-block">
                <a-icon type="smile" theme="twoTone" twoToneColor="rgb(62, 181, 98)" />
              </div>
              <a-progress :percent="user.comm" :strokeColor="{  '0%': 'rgb(62, 181, 98)', '100%': 'rgb(62, 181, 98)'}" />
            </div>

            <div>
              <div style="display: inline-block">
                <a-icon type="home" theme="twoTone" twoToneColor="rgb(59, 47, 235)" />
              </div>
              <a-progress :percent="user.home" :strokeColor="{  '0%': 'rgb(59, 47, 235)', '100%': 'rgb(59, 47, 235)'}" />
            </div>
          </a-col>
        </a-row>
      </div>
  </div>
</template>

<script>
import { newGame, reloadGame, sendAnswer } from '@/api/game'
export default {
  data() {
    return {
      dis: false,
      user: {
        name: '',
        health: 0,
        eat: 0,
        comm: 0,
        home: 0
      },

      pic: '',
      day: 0,
      left: '', 
      right: '',
      descr: '',

      leftAction: {

      }

    }
  },
  methods: {
   async startNewGame() {
      let res = await newGame(localStorage.getItem('session'), 1)
      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer

      this.pic = res.pic
      this.user.name = res.name
      this.user.health = res.health
      this.user.eat = res.food
      this.user.comm = res.communication
      this.user.home = res.leisure

    },

    reloadGame() {

    },

    async sendAnswer(ans){
      this.dis = true
      let res = await sendAnswer(localStorage.getItem('session'), ans)
      this.day = res.round
      this.descr = res.description
      this.left = res.left_answer
      this.right = res.right_answer


      this.user.name = res.name
      this.user.health = res.health
      this.user.eat = res.food
      this.user.comm = res.communication
      this.user.home = res.leisure
      this.dis = false
    }
    
  },
  mounted() {
    this.startNewGame();
  },

};
</script>
<style>
.right {
  margin-left: 15px;
}

.left {
  margin-right: 15px;
}

.left > .ant-btn-icon-only {
  width: 64px;
  height: 64px;
}

.right > .ant-btn-icon-only {
  width: 64px;
  height: 64px;
}

.outer:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}

.inner {
  width: 100%;
  display: inline-block;
  vertical-align: middle;
}

.outer {
  text-align: center;
}

.left, .right, .card-box {
  display: inline-block;
}
.center-menu {
  margin-top: 80px;
  width: 30%;
  margin-left: 35%;
}
.card-box {
  width: 70%;
  height: 300px;
  background: rgba(255,255,255,0.8);
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
