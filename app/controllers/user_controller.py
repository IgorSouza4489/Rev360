from services.user_service import get_all_users, get_user_by_id, get_posts_by_user_id

#A camada de controle gerencia a interação do usuário com o sistema.


#Função que lista usuários, utiliza a função do service
def list_users():
    users = get_all_users()
    for user in users:
        print(f"ID: {user.user_id} - Nome: {user.name}")

#- Email: {user.email}
#Função que mostra detalhes, utiliza a função do service

def show_user_details(user_id):
    user = get_user_by_id(user_id)
    if user:
        print(f"Nome: {user.name}")
        print(f"Email: {user.email}")
        posts = get_posts_by_user_id(user_id)
        if posts:
            print("\nPosts do Usuário:")
            for post in posts:
                print(f" - {post}")
        else:
            print("Este usuário não tem posts.")
    else:
        print(f"Erro: Usuário com ID {user_id} não encontrado.")
