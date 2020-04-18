<template>
<a-row type="flex" justify="center">
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
              <td><b>{{item.name}}</b></td>
              <td>{{item.health}}</td>
              <td>{{item.food}}</td>
              <td>{{item.leisure}}</td>
              <td>{{item.communication}}</td>
              <td>{{item.value}}</td>
            </tr>
          </table>
        </div>
      </div>
  </a-col>
</a-row>
</template>

<script>
import {getRating} from "../api/auth";

export default {
  data: {
    rating: []
  },
  async beforeCreate() {
    // получение рейтинга пользователей
    let res = await getRating()
    if (res !== false) {
      console.log(res);
      this.rating = res.top;
    } else {
      this.$message.error('Ошибка получения персонажей');
    }
  },
  methods: {
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
</style>
