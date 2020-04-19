<template>
<a-row type="flex" justify="center" v-if="isLoaded">
  <a-col :span="12">
      <div class="box profile">
        <a-row class="title-profile">
          <a-col :span="8">
            <a-avatar :size="128" :src="this.profileUser.pic" />
          </a-col>
          <a-col :span="16" class="mini-rating">
            <div>Имя: {{profileUser.names}}</div>
            <div>Игры сыграно: {{profileUser.count_game}}</div>
            <div>Максимально прожито дней: {{profileUser.max_point}}</div>
          </a-col>
        </a-row>
        <div class="button-group">
          <a-button v-if="newGame" @click="toChoicePers" block>Начать игру</a-button>
          <a-button v-if="!newGame" @click="toGame" block>Продолить игру</a-button>
          <a-button @click="toRating" block>Рейтинг</a-button>
        </div>

        <div class="person-list">
          <h1 block>История выживания</h1>
          <div v-for="item in persons" style="border: 1px solid black;">
            <img :src="item.pic" height="40" width="40" style="margin-top: 5px;"/>
            <h3>{{item.name}}</h3>
            <p>{{item.description}}</p>

            <table width="100%" border="1">
              <tr>
                <th>Здоровье</th>
                <th>Питание</th>
                <th>Досуг</th>
                <th>Общение</th>
                <th>Деньги</th>
              </tr>
              <tr>
                <td>{{item.health}}</td>
                <td>{{item.food}}</td>
                <td>{{item.leisure}}</td>
                <td>{{item.communication}}</td>
                <td>{{item.value}}</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
  </a-col>
</a-row>
</template>

<script>
  import {getPerson, getProfile} from "../api/auth";
  import { getGame } from "@/api/game"
export default {
  data() {
    return {
      newGame: Boolean,
      isLoaded: false,
      persons: [],
      profileUser: undefined,
    }
  },
  methods: {
    toChoicePers: function() {
      this.$router.push('/choice')
    },
    toRating: function() {
      this.$router.push('/rating');
    },
    getMyProfile: function () {
      // получение информации о пользователе
      let profile = getProfile()
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser)
        });
      } else {
        this.$message.error('Ошибка получения профиля');
      }
    },
    getAllPerson: function () {
      // получение всех персонажей
      let res = getPerson()
      if (res !== false) {
        res.then(val => {
          this.persons = val;
          console.log("Персонажи: ", this.persons);
        });
      } else {
        this.$message.error('Ошибка получения персонажей');
      }
    }
  },

  created: async function () {
    let res = await getGame(localStorage.getItem('token'))
    if (res == false) {
      this.newGame = true
    } else {
      this.newGame = false
    }
    console.log("Проверка игры", res)
  },
  mounted() {
    this.getMyProfile();
    this.getAllPerson();
    this.isLoaded = true;
  },
};
</script>
<style>
.profile .button-group {
  margin-top: 20px;
}
.profile .button-group button{
  margin-top: 5px;
}
.mini-rating {
  margin-top: 10px;
}
.mini-rating div {
  text-decoration: underline;
  font-size: 16px;
  text-align: left;
}
.title-profile {
 
}
.ant-avatar {
  background: #ad768f;
  border: 1px #440522 solid;
}
#components-form .form {
  max-width: 300px;
}
#components-form .form-button {
  width: 100%;
}
.person-list {
  margin-top: 20px;
}
</style>
