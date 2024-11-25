// main.js
new Vue({
  el: '#app',
  data: {
    username: '',
    password: '',
  },
  methods: {
    login() {
      // Aqui você pode adicionar a lógica para autenticação
      if (this.username && this.password) {
        console.log('Logando com:', this.username, this.password);
        alert('Login efetuado com sucesso!');
      } else {
        alert('Por favor, insira usuário e senha.');
      }
    }
  },
 //template: `
    //<div class="login-form">
    //  <h2>Login</h2>
    //  <form @submit.prevent="login">
    //    <label for="username">Usuário</label>
    //    <input type="text" id="username" v-model="username" required>

    //    <label for="password">Senha</label>
    //    <input type="password" id="password" v-model="password" required>

    //    <button type="submit">Entrar</button>
    //  </form>
    //</div>
  //`
});
