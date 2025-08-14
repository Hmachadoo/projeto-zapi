Envio de Mensagens Personalizadas via Z-API

Este projeto em Python lê contatos cadastrados no Supabase e envia uma mensagem personalizada para cada um via Z-API.

Mensagem enviada:

Olá {{nome_contato}}, tudo bem com você?

🚀 Tecnologias utilizadas

Python 3.10+

Supabase (banco de dados)

Z-API (envio de mensagens via WhatsApp)

python-dotenv (gerenciamento de variáveis de ambiente)

requests (requisições HTTP)

Configuração da tabela no Supabase

Crie uma tabela chamada contatos com as seguintes colunas:

Coluna	Tipo	Observação

id	uuid	PK (gerado automaticamente)

nome_contato	text	Nome do contato

telefone	text	Número de telefone com DDI (ex: +5511999999999)

🔑 Variáveis de ambiente

Crie um arquivo .env na raiz do projeto com:

SUPABASE_URL=sua_url_do_supabase

SUPABASE_KEY=sua_chave_do_supabase

ZAPI_INSTANCE_ID=seu_id_da_instancia_zapi

ZAPI_TOKEN=seu_token_da_zapi

ZAPI_SECURITY_TOKEN = seu_token_de_seguranca_do_zapi

⚙️ Como rodar o projeto

Clonar o repositório

git clone https://github.com/Hmachadoo/projeto-zapi

cd projeto-zapi

Instalar as dependências

pip install -r requirements.txt

Configurar variáveis de ambiente

Criar o arquivo .env conforme explicado acima.

Executar o script

python main.py

📌 Funcionamento

O script conecta ao Supabase e busca os contatos cadastrados.

Para cada contato, envia uma mensagem via Z-API no formato:

Olá {{nome_contato}}, tudo bem com você?


É possível enviar para até 3 números diferentes (ou menos, caso tenha menos cadastrados).

🛡️ Boas práticas implementadas

Uso de .env para chaves sensíveis

Tratamento de erros e logs básicos

Código organizado e legível

Commits claros e objetivos

📄 Licença

Este projeto foi desenvolvido apenas para projeto pessoal.