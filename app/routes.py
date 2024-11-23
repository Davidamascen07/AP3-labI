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
    query = request.args.get('query', '')
    foods = []
    if query:
        try:
            results = fatsecret.search_foods(query)
            foods = results.get('foods', {}).get('food', [])
        except Exception as e:
            return render_template('search.html', error=str(e))
    return render_template('search.html', foods=foods)
