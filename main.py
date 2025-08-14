import os
from dotenv import load_dotenv
from supabase import Client, create_client
from logger_config import logger
from supabase_client import search_contacts
from message_zapi import send_message_zapi

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def main():
    logger.info("Iniciando o processo de envio de mensagens")
     
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception as e:
        logger.error(f"Erro ao inicializar o cliente Supabase: {e}")
        return

    contacts = search_contacts(supabase)
    
    if contacts:
        success= 0
        failure = 0
        for contact in contacts[:3]:
            contact_name = contact.get("contact_name")
            phone = contact.get("phone")
            
            if contact_name and phone:
                if send_message_zapi(phone, contact_name):
                    success += 1
                else:
                    failure += 1
            else:
                logger.warning(f"Contato com dados incompletos ignorado: {contact}")
                falhas += 1
        
        logger.info(f"Envios bem-sucedidos: {success}")
        logger.info(f"Envios com falha: {failure}")

    logger.info("Processo finalizado.")

if __name__ == "__main__":
    main()
