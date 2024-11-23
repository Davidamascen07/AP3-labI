# app/fatsecret_client.py
import requests
import base64
from datetime import datetime, timedelta
import json
from urllib.parse import quote

class FatSecretClient:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://platform.fatsecret.com/rest/server.api"
        self.access_token = None
        self.token_expires = None

    def _get_access_token(self):
        """Obtém ou renova o token de acesso"""
        if self.access_token and self.token_expires > datetime.now():
            return self.access_token

        auth_string = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode()

        response = requests.post(
            "https://oauth.fatsecret.com/connect/token",
            headers={
                "Authorization": f"Basic {auth_string}",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data="grant_type=client_credentials&scope=basic"
        )
        
        if response.status_code != 200:
            raise Exception("Erro ao obter token de acesso")

        data = response.json()
        self.access_token = data["access_token"]
        self.token_expires = datetime.now() + timedelta(seconds=data["expires_in"])
        return self.access_token

    def _make_request(self, method, params=None):
        """Faz uma requisição para a API do FatSecret"""
        token = self._get_access_token()

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        default_params = {
            "format": "json",
            "method": method
        }

        if params:
            default_params.update(params)

        response = requests.post(
            self.base_url,
            headers=headers,
            params=default_params
        )

        if response.status_code != 200:
            raise Exception(f"Erro na requisição: {response.status_code}")

        return response.json()

    def search_foods(self, query, page_number=0, max_results=50):
        """Pesquisa alimentos pelo nome"""
        params = {
            "search_expression": quote(query),
            "page_number": page_number,
            "max_results": max_results
        }
        return self._make_request("foods.search", params)

    def get_food(self, food_id):
        """Obtém detalhes de um alimento específico"""
        params = {"food_id": food_id}
        return self._make_request("food.get", params)

    def get_recipe(self, recipe_id):
        """Obtém detalhes de uma receita específica"""
        params = {"recipe_id": recipe_id}
        return self._make_request("recipe.get", params)
