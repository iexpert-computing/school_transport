const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Verificar o diretório base
console.log("Diretório base:", __dirname);

// Servir arquivos estáticos da pasta 'Static'
app.use('/Static', express.static(path.resolve(__dirname, 'Static')));

// Definir a rota principal para servir o menu.html
app.get('/', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'templates', 'login.vue'), (err) => {
    if (err) {
      console.error("Erro ao carregar menu.html:", err);
      res.status(err.status).end();
    }
  });
});

// Iniciar o servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
