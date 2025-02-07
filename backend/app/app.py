from flask import Flask, request, jsonify

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define uma rota para o endpoint principal
@app.route("/", methods=["GET"])
def home():
    return "Servidor Flask está funcionando!"

# Define uma rota para tratar requisições GET
@app.route("/dados", methods=["GET"])
def get_dados():
    # Exemplo de resposta JSON
    dados = {"mensagem": "Esta é uma resposta de exemplo", "status": "sucesso"}
    return jsonify(dados)

# Define uma rota para tratar requisições POST
@app.route("/envia-dados", methods=["POST"])
def post_dados():
    data = request.get_json()  # Recebe o JSON enviado na requisição
    resposta = {"dados_recebidos": data, "status": "sucesso"}
    return jsonify(resposta)

# Executa o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
