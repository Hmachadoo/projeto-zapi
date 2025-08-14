from supabase import Client 
from logger_config import logger

def search_contacts(supabase_client: Client):
    try:
        logger.info("Buscando contatos no Supabase.")
        response = supabase_client.table('numeros_wpp').select("contact_name, phone").execute()
        
        if response.data:
            logger.info(f"{len(response.data)} contatos encontrados.")
            return response.data
        else:
            logger.warning("Nenhum contato encontrado no Supabase.")
            return []
            
    except Exception as e:
        logger.error(f"Erro ao buscar contatos no Supabase: {e}")
        return None