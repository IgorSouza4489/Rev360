from controllers.user_controller import list_users, show_user_details
from config import logger

#Utilizei também Logging para algumas partes do código para melhor rastreamento.

def main():
    while True:
        print("\n1. Listar todos os usuários")
        print("2. Buscar usuário por ID")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                list_users()
            case '2':
                try:
                    user_id = int(input("Digite o ID do usuário: "))
                    show_user_details(user_id)
                except ValueError:
                    print("Por favor, insira um ID válido (número).")
            case '3':
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    logger.info("Iniciando aplicação")
    main()
