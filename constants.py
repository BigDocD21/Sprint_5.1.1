import uuid
import string
import random

BASE_URL = "https://stellarburgers.education-services.ru"
WAIT_TIMEOUT = 30

def generate_unique_email():
    unique_id = str(uuid.uuid4())[:8]
    return f"test_user_{unique_id}@example.com"

def generate_unique_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(12))