<template>
<a-row type="flex" justify="center">
  <a-col :span="12">
    <div class="box">
      <h2> Регистрация </h2>
        <a-form
          id="components-form"
          :form="form"
          class="form"
          @submit="handleSubmit"
        >
          <a-form-item>
            <a-input
              v-decorator="[
                'login',
                { rules: [{ required: true, message: 'Введите имя!' }] },
              ]"
              placeholder="Username"
            >
              <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input
              v-decorator="[
                'password',
                { rules: [{ required: true, message: 'Введите пароль!' }] },
              ]"
              type="password"
              placeholder="Password"
            >
              <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-button type="primary" html-type="submit" class="form-button">
              Зарегестрироваться
            </a-button>
            или
            <router-link to="/auth" style="color: #5a0000">
              Войти
            </router-link>
          </a-form-item>
        </a-form>
      </div>
    </a-col>
</a-row>
</template>

<script>
import * as authApi from '@/api/auth.js'
export default {
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'normal_login' });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields( async (err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
          let res = await authApi.registerUser(values)
          if (res != null) {
            console.log(res);
            localStorage.setItem('session', res.session);
            this.$router.push('/start')
          } else {
            this.$message.error('Пользователь с таким именем уже существует');
          }
        }
      });
    },
  },
};
</script>
<style>
#components-form .form {
  max-width: 300px;
}
#components-form .form-button {
  width: 100%;
}
</style>