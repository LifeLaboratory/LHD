<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>

@font-face {
  font-family: bit; /* Имя шрифта */
  src: url(/fonts/8bit.ttf); /* Путь к файлу со шрифтом */
 }

h1, h2, h3, h4, h5, h6 {
  color: #310a0a !important; 
}

.box {
  padding: 10px 15px;
  border-radius: 5px;
  border: solid #520202 2px;
  background: rgba(255,255,255, 0.7)
}

.ant-btn-primary {
  background: #5a0000 !important;
  border-color: #100b0b !important;
}

body {
  background: url('/img/background.jpg') no-repeat;
  background-size: cover;
  backdrop-filter: opacity(0.5) blur(3px);
}

#app {
  font-family: bit;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}
 
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
