# FatSecret API Integration

Uma aplicação web que integra com a API do FatSecret para busca de alimentos, visualização de detalhes e planejamento de refeições.

## 📋 Sobre o Projeto

Este projeto consiste em:
- Backend construído com Flask
- Frontend em HTML e CSS
- Integração com a API do FatSecret
- Sistema de busca e visualização de alimentos
- Funcionalidades para planejamento de refeições

## 🚀 Começando

### Pré-requisitos

- Python 3.8+
- Pip (gerenciador de pacotes Python)
- Git (opcional)
- Editor de código (VSCode, PyCharm, etc.)

### 🔧 Instalação

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Configure o Ambiente Virtual**
   ```bash
   # Criar ambiente virtual
   python -m venv venv

   # Ativar ambiente virtual
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Variáveis de Ambiente**
   
   Crie um arquivo `.env` na raiz do projeto:
   ```plaintext
   FATSECRET_CLIENT_ID=seu_client_id_aqui
   FATSECRET_CLIENT_SECRET=seu_client_secret_aqui
   SECRET_KEY=uma_chave_secreta_aleatoria
   ```

5. **Execute o Projeto**
   ```bash
   flask run
   ```

   Acesse a aplicação em: http://127.0.0.1:5000/

## 📁 Estrutura do Projeto

```
AP3-labI/
├── app/
│   ├── __init__.py        # Fábrica da aplicação
│   ├── routes.py          # Definição das rotas
│   ├── fatsecret_client.py# Cliente para a API do FatSecret
│   ├── templates/         # Templates HTML
│   │   ├── base.html     
│   │   └── home.html     
│   ├── static/           # Arquivos estáticos
│   │   └── style.css     
├── .env                   # Variáveis de ambiente
├── config.py             # Configurações do projeto
├── run.py               # Ponto de entrada
├── requirements.txt     # Dependências
└── venv/               # Ambiente virtual
```

## 🔑 Configuração da API FatSecret

1. Crie uma conta no [FatSecret Developer](https://platform.fatsecret.com/api/)
2. Obtenha suas credenciais (Client ID e Client Secret)
3. Adicione as credenciais ao arquivo `.env`

## 🤝 Contribuindo

1. Faça um fork do repositório
2. Crie uma branch para sua feature
   ```bash
   git checkout -b feature/NovaFeature
   ```
3. Commit suas alterações
   ```bash
   git commit -m 'Adicionando nova feature'
   ```
4. Push para a branch
   ```bash
   git push origin feature/NovaFeature
   ```
5. Abra um Pull Request

## 📫 Suporte

Para suporte, abra uma issue no repositório ou entre em contato com a equipe de desenvolvimento.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
