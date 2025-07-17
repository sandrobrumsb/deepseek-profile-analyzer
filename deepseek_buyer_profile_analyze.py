from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Cria o cliente da API OpenAI, usando a chave e o endpoint personalizado
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # Obtém a chave da variável de ambiente
    base_url="https://api.deepseek.com",  # URL base da API DeepSeek
)

# Define o modelo a ser utilizado na chamada da API
model = "deepseek-chat"


def to_load(nome_do_arquivo):
    """
    Função para carregar o conteúdo de um arquivo de texto.
    Recebe o nome do arquivo como parâmetro.
    Retorna o conteúdo do arquivo ou imprime erro em caso de falha.
    """
    try:
        with open(nome_do_arquivo, "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"error: {e}")


# Mensagem que define o comportamento esperado do modelo (prompt do sistema)
prompt_system = """
Identifique o perfil de compra para cada client a seguir.
O formato de saída deve ser:
client - descreva o perfil do client em 3 palavras.
"""

# Carrega a lista de compras dos clientes do arquivo CSV
prompt_user = to_load(r"dados\lista_de_compras_50_clientes.csv")

# Estimativa simples da quantidade de tokens na soma dos prompts
number_of_tokens = len((prompt_system + prompt_user).split())
print(f"Estimativa de tokens de entrada: {number_of_tokens}")

print(f"model Escolhido: {model}")

# Monta a lista de mensagens para enviar para a API de chat
message_list = [
    {"role": "system", "content": prompt_system},  # Instruções do sistema
    {"role": "user", "content": prompt_user},  # Dados do usuário para análise
]

# Chama o endpoint de chat completions da API OpenAI com as mensagens e modelo escolhidos
response = client.chat.completions.create(messages=message_list, model=model)

# Imprime o conteúdo da resposta do modelo (perfil de compra dos clientes)
print(response.choices[0].message.content)

