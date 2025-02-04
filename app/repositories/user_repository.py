import requests
from config import BASE_URL
from config import logger

#Repository é a camada de interação com o banco de dados, nesse caso os dados virão de uma API pública sem Token, existe uma validação abaixo.



#Função para buscar usuários
def get_users():
    try:
        logger.info("Buscando lista de usuários")
        response = requests.get(f'{BASE_URL}/users')
        response.raise_for_status()
        logger.info("Lista de usuários recebida com sucesso.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao se conectar à API: {e}")
        return []
    
#Função para buscar posts dos usuários
def get_user_posts(user_id):
    try:
        logger.info("Buscando posts do usuário")
        response = requests.get(f'{BASE_URL}/posts?userId={user_id}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao se conectar à API: {e}")
        return []
