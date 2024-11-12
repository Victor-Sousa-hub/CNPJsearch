from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Rota principal para exibir o formulário de busca
@app.route("/")
def index():
    return render_template("index.html")

# Rota para busca de CNPJ
@app.route("/api/busca_cnpj/<cnpj>/")
def busca_cnpj(cnpj):
    # Validação simples de CNPJ (apenas comprimento)
    if len(cnpj) != 14 or not cnpj.isdigit():
        return jsonify({"success": False, "error": "CNPJ inválido."})

    # Simulação de busca no banco de dados ou API externa
    if cnpj == "12345678000195":  # Exemplo de CNPJ
        return jsonify({
            "success": True,
            "result": {
                "empresa": "Empresa Exemplo LTDA",
                "endereco": "Rua Exemplo, 123",
                "cidade": "São Paulo",
                "estado": "SP"
            }
        })
    return jsonify({"success": False, "error": "CNPJ não encontrado."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
