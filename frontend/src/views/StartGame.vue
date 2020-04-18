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
          <a-button block>Рейтинг</a-button>
          <a-button block>История выживания</a-button>
        </div>

        <div class="person-list">
          <div v-for="item in this.persons" style="border: 1px solid black;">
            <img :src="item.pic" height="40" width="40" style="margin-top: 5px;"/>
            <h3>{{item.name}}</h3>
            <p>{{item.description}}</p>
            <a-button type="primary" class="form-button" style="margin-bottom: 5px;">
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
  async beforeCreate() {

    // получение всех персонажей
    let res = await getPerson()
    if (res != null) {
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
</style>
