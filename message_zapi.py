import requests
from logger_config import logger
import os
from dotenv import load_dotenv

load_dotenv()

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_SECURITY_TOKEN = os.getenv("ZAPI_SECURITY_TOKEN")

def send_message_zapi(phone: str, contact_name: str):
    if not phone.startswith("55"):
        phone = "".join(filter(str.isdigit, phone))
        if not phone.startswith("55"):
                phone = "55" + phone
        logger.info(f"Enviando para: {phone}")

    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    
    message = f"Olá {contact_name}, tudo bem com você?"
    
    payload = {
        "phone": phone,
        "message": message,        
    }
    
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_SECURITY_TOKEN
    }
    
    try:
        logger.info(f"Enviando mensagem para {contact_name} ({phone})...")
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            logger.info(f"Mensagem enviada com sucesso para {contact_name}.")
            return True
        else:
            logger.error(f"Falha ao enviar mensagem para {contact_name}. Status: {response.status_code}, Resposta: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de conexão ao enviar mensagem para {contact_name}: {e}")
        return False


