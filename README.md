Projeto FatSecret API Integration
Este projeto é uma aplicação web que utiliza a API do FatSecret para buscar alimentos, visualizar detalhes e planejar refeições. O backend foi construído com Flask e o frontend com HTML e CSS. Este guia irá ajudá-lo a configurar o projeto em um novo computador.

Pré-requisitos
Antes de rodar o projeto, você precisa ter os seguintes programas instalados no seu computador:

Python 3.8+ (https://www.python.org/downloads/)
Pip (gerenciador de pacotes Python) — geralmente já vem instalado com o Python.
Git (opcional, mas útil para clonar repositórios) — https://git-scm.com/
Editor de código (ex: VSCode, PyCharm)
Passos para rodar o projeto
1. Clonando o repositório
Se você já tem o repositório no GitHub, clone-o para o seu computador. Se não, basta criar o repositório no GitHub e clonar ou baixar o projeto:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Ou, se preferir baixar como um arquivo .zip, clique em "Code" no GitHub e baixe o arquivo.

2. Criando o Ambiente Virtual
Navegue até o diretório do projeto no terminal e crie um ambiente virtual para isolar as dependências:

bash
Copiar código
cd nome-do-repositorio
python -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copiar código
venv\Scripts\activate
No macOS/Linux:
bash
Copiar código
source venv/bin/activate
3. Instalando as Dependências
Com o ambiente virtual ativado, instale as dependências do projeto usando o requirements.txt:

bash
Copiar código
pip install -r requirements.txt
Isso instalará todas as bibliotecas necessárias, como Flask, Flask-SQLAlchemy, requests, e python-dotenv.

4. Configurando o Arquivo .env
Você precisa criar um arquivo .env na raiz do projeto para armazenar as variáveis de ambiente, como as chaves da API do FatSecret.

Crie um arquivo chamado .env no diretório do projeto e adicione as seguintes variáveis de ambiente:

plaintext
Copiar código
FATSECRET_CLIENT_ID=seu_client_id_aqui
FATSECRET_CLIENT_SECRET=seu_client_secret_aqui
SECRET_KEY=uma_chave_secreta_aleatoria
Substitua os valores de FATSECRET_CLIENT_ID e FATSECRET_CLIENT_SECRET pelas suas credenciais da API do FatSecret. Você pode obter essas credenciais criando uma conta no FatSecret Developer.

5. Rodando o Projeto
Agora que tudo está configurado, você pode rodar o servidor Flask. No terminal, execute:

bash
Copiar código
flask run
O Flask irá iniciar o servidor, e você poderá acessar a aplicação em http://127.0.0.1:5000/ no seu navegador.

6. Testando a Aplicação
Acesse a URL da aplicação em seu navegador: http://127.0.0.1:5000/
Na página inicial, você poderá clicar no link "Buscar Alimentos" para realizar uma pesquisa.
Estrutura do Projeto
A estrutura do projeto é a seguinte:

bash
Copiar código
AP3-labI/
├── app/
│   ├── __init__.py        # Fábrica da aplicação
│   ├── routes.py          # Definição das rotas
│   ├── fatsecret_client.py # Cliente para a API do FatSecret
│   ├── templates/         # Templates HTML
│   │   ├── base.html      # Template base
│   │   └── home.html      # Página inicial
│   ├── static/            # Arquivos estáticos como CSS
│   │   └── style.css      # Arquivo CSS
├── .env                   # Variáveis de ambiente
├── config.py              # Configurações gerais do projeto
├── run.py                 # Ponto de entrada da aplicação
├── requirements.txt       # Dependências do projeto
└── venv/                  # Ambiente virtual
Contribuindo
Se você deseja contribuir para o projeto, siga os passos abaixo:

Faça um fork do repositório.
Clone seu fork no seu computador.
Crie uma nova branch para adicionar suas alterações.
Commit suas alterações e envie para o seu fork.
Abra um pull request para o repositório original.
