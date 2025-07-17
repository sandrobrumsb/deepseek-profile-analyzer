# 🤖🛍️ Análise de Perfil de Compradores com DeepSeek
---

**O que ele faz:**  
Este script utiliza o modelo `deepseek-chat` da API DeepSeek para **analisar uma lista de compras de 50 clientes** e gerar um **perfil de compra resumido em 3 palavras para cada cliente**.

Ele realiza:

- Leitura de um arquivo `.csv` contendo os dados de compras  
- Geração de mensagens para o modelo com instruções específicas  
- Envio das mensagens via API DeepSeek  
- Exibição do perfil resumido retornado pelo modelo  

---

## 🚀 Como rodar os scripts

Siga os passos abaixo para executar qualquer um dos projetos deste repositório:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
```
### 2. Instale as 📚 Bibliotecas:
```bash
pip install -r requirements.txt
```
### 3. 📦 Crie o Arquivo `.env`:

- Adicione no arquivo `.env` as suas chaves de API:
  ```env
  OPENAI_API_KEY=your_openai_key_here
  DEEPSEEK_API_KEY=your_deepseek_key_here
---#
