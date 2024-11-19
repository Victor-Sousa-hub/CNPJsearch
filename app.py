from flask import Flask, render_template, jsonify, send_from_directory,request, jsonify, redirect, url_for, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import os
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message




app = Flask(__name__)
CORS(app)



# Configuração do app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Banco SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'naoresponda1527@gmail.com'
app.config['MAIL_PASSWORD'] = 'dlnm kjwf uhpf btah'

app.secret_key = os.urandom(24)
# Inicializar extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)  # E-mail único
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Senha criptografada

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Rota principal para exibir o formulário de busca
@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Busca o usuário pelo username
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        
        return render_template("login.html", error="Credenciais inválidas!")
    
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Validação básica
        if password != confirm_password:
            return render_template('register.html', error="As senhas não coincidem!")
        
        if User.query.filter_by(email=email).first():
            return render_template('register.html', error="E-mail já cadastrado!")
        
        # Hash da senha
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Criar usuário
        user = User(email=email, username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')



@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()

        if user:
            # Gera um código de redefinição (ou token)
            reset_code = os.urandom(4).hex()

            # Salve o código e o email na sessão
            session['reset_code'] = reset_code
            session['reset_email'] = email  # Salva o email na sessão

            # Envie o código por e-mail
            msg = Message('Redefinição de Senha', sender='noreply@demo.com', recipients=[email])
            msg.body = f'Seu código de redefinição é: {reset_code}'
            mail.send(msg)

            return redirect(url_for('confirm_reset'))
        return render_template('reset_password.html', error="E-mail não encontrado!")
    return render_template('reset_password.html')



@app.route('/confirm_reset', methods=['GET', 'POST'])
def confirm_reset():
    print("Entrou em confirm_reset.")  # Verificar se a rota está sendo chamada

    if request.method == 'POST':
        print("Recebeu uma solicitação POST.")  # Confirmar o método

        reset_code = request.form.get('reset_code')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        print(f"Reset Code: {reset_code}, New Password: {new_password}, Confirm Password: {confirm_password}")

        # Validação do código
        if reset_code != session.get('reset_code'):
            print("Código de redefinição inválido.")
            return render_template('confirm_reset.html', error="Código inválido!")

        # Validação das senhas
        if new_password != confirm_password:
            print("As senhas não coincidem.")
            return render_template('confirm_reset.html', error="As senhas não coincidem!")

        if len(new_password) < 8:
            print("Senha muito curta.")
            return render_template('confirm_reset.html', error="A senha deve ter pelo menos 8 caracteres.")

        reset_email = session.get('reset_email')
        print(f"Email na sessão: {reset_email}")

        if not reset_email:
            print("Nenhum email associado à redefinição de senha.")
            return render_template('confirm_reset.html', error="Nenhum email associado à redefinição de senha.")

        user = User.query.filter_by(email=reset_email).first()
        if user is None:
            print("Usuário não encontrado.")
            return "Usuário não encontrado para redefinição de senha.", 404

        try:
            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            db.session.commit()
            print("Senha redefinida com sucesso.")
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar a senha: {e}")
            return render_template('confirm_reset.html', error="Erro ao atualizar a senha. Tente novamente.")

        return redirect(url_for('login'))

    print("Exibindo o template de confirmação de redefinição.")
    return render_template('confirm_reset.html')




# Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout realizado com sucesso!"}), 200

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
