<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo_lhd.png" width="50%" style="margin-top: 50px;">
    <h1 style="margin-top: 50px; margin-bottom: 50px;">Выживешь в суровых условиях хакатона в карантин?!</h1>
    <a-button type="primary" class="start-button" v-on:click="toAuth">
      Начать выживание
    </a-button>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  methods: {
    toAuth(e) {
      this.$router.push('/auth')
    },
  },
}
</script>

<style>
  .start-button {
    width: 400px;
    height: 400px;
    border-radius: 50%;
    font-size: 24pt;
  }
</style>
