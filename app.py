from flask import Flask, render_template, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

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


# Caminho para o arquivo JSON
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
JSON_FILE = os.path.join(DATA_DIR, 'Enquadramento.json')

@app.route('/enquadramento', methods=['GET'])
def get_enquadramento():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = f.read()
        return jsonify(eval(data))  # Converte a string para um objeto JSON
    except FileNotFoundError:
        return jsonify({"error": "Arquivo JSON não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Servir arquivos estáticos (HTML, JS, CSS)
@app.route('/<path:filename>')
def serve_static(filename):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    return send_from_directory(static_dir, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
