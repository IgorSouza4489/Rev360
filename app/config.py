import logging

BASE_URL = 'https://jsonplaceholder.typicode.com'


# Configuração do logging
logging.basicConfig(
    level=logging.INFO,  # Nível do log (DEBUG, INFO, WARNING, ERROR, CRITICAL). Não usei todos.
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Salvar logs em um arquivo (Opcional)
        logging.StreamHandler()  # Exibir logs no console
    ]
)

logger = logging.getLogger(__name__)
