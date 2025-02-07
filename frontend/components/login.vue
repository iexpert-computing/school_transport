<template>
  <div class="login-container">
    <div class="login-box">
      <div class="login-logo">
        <img src="../Static/img/logo.png" alt="EDU Logo" />
      </div>
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Login</label>
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="Digite seu login"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Digite sua senha"
            required
          />
        </div>
        <div class="form-options">
          <label>
            <input type="checkbox" v-model="stayLoggedIn" />
            Me mantenha conectado
          </label>
          <a href="#" @click="forgotPassword">Esqueci minha senha</a>
        </div>
        <button type="submit" class="login-button">Entrar no sistema</button>
      </form>
      <p class="footer-text">
        Sistema AMIGO © Todos os direitos reservados. Versão: 2.41.10.0
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      stayLoggedIn: false,
    };
  },
  methods: {
    handleLogin() {
      // Lógica para autenticação de login
      if (this.username === "usuario" && this.password === "senha") {
        alert("Login bem-sucedido!");
      } else {
        alert("Login ou senha incorretos.");
      }
    },
    forgotPassword() {
      // Lógica para recuperação de senha
      alert("Redirecionar para recuperação de senha");
    },
  },
};
</script>

<style scoped src="../Static/css/styles.css"></style>
