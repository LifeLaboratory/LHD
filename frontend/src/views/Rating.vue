<template>
<a-row type="flex" justify="center" v-if="isLoaded">
  <a-col :span="12">
      <div class="box">
        <h2>Рейтинг</h2>
        <div class="button-group">
          <a-button block v-on:click="toProfile()">Вернуться в профиль</a-button>
        </div>
        <div class="rating-list">
          <table width="100%" border="1">
            <tr>
              <th>Имя</th>
              <th>Здоровье</th>
              <th>Питание</th>
              <th>Досуг</th>
              <th>Общение</th>
              <th>Деньги</th>
            </tr>
            <tr v-for="item in this.rating">
              <td @click.prevent="showPersonInfo(item)"><b style="cursor: pointer; text-decoration: underline;">{{item.name}}</b></td>
              <td>{{item.health}}</td>
              <td>{{item.food}}</td>
              <td>{{item.leisure}}</td>
              <td>{{item.communication}}</td>
              <td>{{item.value}}</td>
            </tr>
          </table>
        </div>
      </div>
    <div class="selectProfileModal" v-if="showModalOne">
      <div class="selectProfileModalTitle">{{selectPerson.name}}</div>
      <div class="selectProfileModalBody">
        <a-row class="title-profile">
          <a-col :span="8">
            <a-avatar :size="128" :src="this.selectPerson.pic" />
          </a-col>
          <a-col :span="16" class="mini-rating">
            <div>Имя: {{selectPerson.names}}</div>
            <div>Игры сыграно: {{selectPerson.count_game}}</div>
            <div>Максимально прожито дней: {{selectPerson.max_point}}</div>
          </a-col>
        </a-row>
      </div>
      <div class="selectProfileModalFooter">
        <button class="btn btn-primary" @click.prevent="showModalOne = !showModalOne">Закрыть</button>
      </div>
    </div>
  </a-col>
</a-row>
</template>

<script>
  import {getProfileInfo, getRating} from "../api/auth";

export default {
  data() {
    return {
      isLoaded: false,
      rating: [],
      showModalOne: false,
      selectPerson: undefined
    }
  },
  async beforeCreate() {
    // получение рейтинга пользователей
    let res = await getRating()
    if (res !== false) {
      console.log(res);
      this.rating = res.top;
      this.isLoaded = true;
    } else {
      this.$message.error('Ошибка получения персонажей');
    }
  },
  methods: {
    showPersonInfo: function(person) {
      let profile = getProfileInfo(person.id_user)
      if (profile !== false) {
        profile.then(val => {
          this.selectPerson = val;
          if (!this.showModalOne)
            this.showModalOne = !this.showModalOne
          console.log("Выбранный профиль: ", val)
        });
      }
    },
    toProfile: function () {
      this.$router.push('/start');
    }
  }
};
</script>
<style>
.rating-list {
  margin-top: 5px;
}
.selectProfileModal {
  box-shadow: 0px 1px 12px rgba(0, 0, 0, 0.4);
  margin:0 auto;
  position: absolute;
  z-index: 999;
  width: 600px;
  top: 20vh;
  border-radius: 5px;
  overflow: hidden;
}
.selectProfileModal .selectProfileModalTitle {
  background-color: #eee;
  text-align: left;
  padding: 8px 12px;
  font-size: 1.5em;
}
.selectProfileModal .selectProfileModalTitle .close {
  line-height: 32px;
  color: #5c4084;
}
.selectProfileModal .selectProfileModalBody {
  background-color: #fff;
  padding: 8px 12px;
  text-align: left;
  padding: 12px;
}
.selectProfileModal .selectProfileModalFooter {
  background-color: #eee;
  padding: 4px 12px;
  text-align: left;
}
</style>
