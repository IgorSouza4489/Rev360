from repositories.user_repository import get_users, get_user_posts
from dtos.user_dto import UserDTO
from config import logger


#Service é a camada de lógica e regra de negócio, nela temos funções que vem da camada de dados (Repository) e que são transmitidas utilizando DTO
#Para assim transferir dados entre camadas de aplicação e em ocasiões mais complexas evitar uso de dados desnecessários e por consequência ser um script mais rápido.


#Função para retornar todos os usuários.
def get_all_users():
    logger.info("Obtendo todos os usuários...")
    users_data = get_users()
    return [UserDTO(user['id'], user['name'], user['email']) for user in users_data]

#Função para retornar usuário por ID.
def get_user_by_id(user_id):
    logger.info("Obtendo usuário por ID")
    users_data = get_users()
    user_data = next((user for user in users_data if user['id'] == user_id), None)
    if user_data:
        return UserDTO(user_data['id'], user_data['name'], user_data['email'])
    return None

#Função para retornar posts do usuário por ID de usuário.
def get_posts_by_user_id(user_id):
    logger.info("Obtendo posts do usuário por ID de usuário.")
    posts_data = get_user_posts(user_id)
    return [post['title'] for post in posts_data]
