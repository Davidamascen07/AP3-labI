from flask import Blueprint, render_template, request, jsonify
from app.fatsecret_client import FatSecretClient
import os

app_routes = Blueprint('app_routes', __name__)

# Inicialize o cliente FatSecret
fatsecret = FatSecretClient(
    client_id=os.getenv('FATSECRET_CLIENT_ID'),
    client_secret=os.getenv('FATSECRET_CLIENT_SECRET')
)

@app_routes.route('/')
def home():
    return render_template('home.html')

@app_routes.route('/search-foods', methods=['GET'])
def search_foods():
    query = request.args.get('query', '')  # Pega o valor do campo 'query' do formulário
    foods = []
    if query:
        try:
            # Chama o método da API para buscar os alimentos
            results = fatsecret.search_foods(query)
            print("Resultados da API:", results)  # Log para verificar os dados retornados

            # Extrai os alimentos da resposta
            foods = results.get('foods', {}).get('food', [])

            # Se não houver alimentos, mostra o que foi retornado da API
            if not foods:
                print("Nenhum alimento encontrado na resposta da API.")

        except Exception as e:
            return render_template('search.html', error=str(e))
    
    return render_template('search.html', foods=foods)

