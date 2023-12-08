import secrets

def generate_verification_token():
    token_length = 32
    verification_token = secrets.token_hex(token_length)
    
    return verification_token