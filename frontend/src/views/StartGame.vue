<template>
<a-row type="flex" justify="center">
  <a-col :span="12">
      <div class="box profile">
        <a-row class="title-profile">
          <a-col :span="8">
            <a-avatar :size="128" src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
          </a-col>
          <a-col :span="16" class="mini-rating">
            <div>Имя: Lalow</div>
            <div>Игры сыграно: 25 игр</div>
            <div>Максимально прожито дней: 243 дня</div>
          </a-col>
        </a-row>
        <div class="button-group">
          <a-button block>Начать игру</a-button>
          <a-button v-on:click="toRating()" block>Рейтинг</a-button>
          <a-button block>История выживания</a-button>
        </div>

        <div class="person-list">
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

            <a-button type="primary" class="form-button" style="margin-bottom: 5px; margin-top: 5px;">
              Продолжить игру
            </a-button>
          </div>
        </div>
      </div>
  </a-col>
</a-row>
</template>

<script>
import {getPerson} from "../api/auth";
export default {
  data: {
    persons: []
  },
  methods: {
    toRating: function() {
      this.$router.push('/rating');
    }
  },
  async beforeCreate() {

    // получение всех персонажей
    let res = await getPerson()
    if (res !== false) {
      console.log(res);
      this.persons = res;
    } else {
      this.$message.error('Ошибка получения персонажей');
    }
    //
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
  margin-top: 10px;
}
</style>
