<template>
  <div>
    <div class="login-logo">
      <img id="logo-principal" src="/Static/image/Icone.svg" alt="IExpert Computing">
    </div>
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <label for="username">Usuário</label>
        <input type="text" id="username" v-model="username" required>

        <label for="password">Senha</label>
        <input type="password" id="password" v-model="password" required>

        <button type="submit">Entrar</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // Aqui você pode adicionar a lógica de login
      console.log('Usuário:', this.username);
      console.log('Senha:', this.password);
    }
  }
};
</script>

<style scoped>
@import '/Static/css/styles.css';

/* Adicione estilos específicos para o componente, se necessário */
</style>
