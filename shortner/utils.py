import string
import random 
from .models import ShortURL

# for generating a short_code of a url and check duplicate 
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
       short_code =  ''.join(random.choice(characters) for _ in range(length))
       if not ShortURL.objects.filter(short_code=short_code).exists():
           return short_code