import re
from urllib.parse import urlparse, parse_qs

def convert_whatsapp_link(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    if 'phone' in query_params:
        phone_number = query_params['phone'][0]
        return f"https://wa.me/{phone_number}"
    
    return "URL inválida"

# Exemplo de uso:
url = "https://web.whatsapp.com/send?phone=5547991620888&text=SALE%20MIG%20%7C%20%2050%25%20OFF%20~%20a%20promo%20mais%20esperada%20do%20ver%C3%A3o!"
print(convert_whatsapp_link(url))