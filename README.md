# CNPJsearch

**CNPJsearch** é uma aplicação web que permite consultar informações de empresas brasileiras utilizando seus CNPJs. O sistema é integrado a APIs para buscar dados cadastrais, atividades principais e secundárias, e gerar um enquadramento ambiental de forma automatizada.

## 📋 Funcionalidades

- Consulta de informações de empresas pelo CNPJ.
- Exibição de:
  - Razão Social.
  - Situação Cadastral.
  - Endereço completo.
  - Atividade principal e atividades secundárias.
  - Enquadramento ambiental (como Licença Ambiental, Alvará, etc.).
- Interface amigável com tabelas organizadas e mensagens claras de erros.

## 🛠️ Tecnologias Utilizadas

- **Frontend**:
  - HTML5, CSS3 e JavaScript.
- **Backend**:
  - Flask (Python).
  - Integração com APIs externas para consulta de CNPJs.
- **APIs**:
  - [CNPJ.ws](https://www.cnpj.ws/docs/api-publica/consultando-cnpj) (ou substitua pela API usada).
- **Outras Bibliotecas**:
  - Fetch API para requisições assíncronas.

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. **Python 3.8+** instalado no sistema.
2. **Instalar as dependências** listadas no arquivo `requirements.txt`.

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/Victor-Sousa-hub/CNPJsearch.git
   cd CNPJsearch
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure a chave da API no arquivo app.py: Substitua "SUA_CHAVE_DE_API" pela sua chave da API de consulta de CNPJs (exemplo: CNPJ.ws).

Inicie o servidor:

bash
Copiar código
python app.py
Acesse a aplicação: Abra o navegador e vá para http://127.0.0.1:5000.

📦 Estrutura do Projeto
plaintext
Copiar código
CNPJsearch/
├── app.py                 # Arquivo principal da aplicação Flask
├── templates/             # Diretório com os templates HTML
│   └── index.html         # Página inicial
├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   ├── style.css          # Estilização da página
│   └── script.js          # Lógica de busca e exibição de resultados
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
🖥️ Demonstração
Exemplo de Busca:


Exibição dos Resultados:
Razão Social: Empresa X
Situação Cadastral: Ativa
Atividades principais e secundárias exibidas em tabelas.
📝 Como Contribuir
Faça um fork deste repositório.
Crie uma nova branch:
bash
Copiar código
git checkout -b feature/nova-funcionalidade
Realize suas alterações e faça commit:
bash
Copiar código
git commit -m "Adiciona nova funcionalidade"
Envie para o repositório remoto:
bash
Copiar código
git push origin feature/nova-funcionalidade
Abra um Pull Request explicando suas alterações.
📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
