import requests
import base64

# Substitua com suas credenciais da dashboard Spotify Developer
CLIENT_ID="a503dfb97b5447de98f9f01e87cd25bd"
CLIENT_SECRET="10932faa1bfd403f9e3f5a75e009b8b7"

# Endpoint oficial para obter token
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Combine Client ID e Secret e converta em base64 (para o header Authorization)
auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_bytes = auth_string.encode("utf-8")
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

# Cabeçalhos da requisição
headers = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Corpo da requisição
data = {
    "grant_type": "client_credentials"
}

# Fazendo a requisição POST
response = requests.post(TOKEN_URL, headers=headers, data=data)

# Verifica se deu certo
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info["access_token"]
    print("✅ Access Token gerado com sucesso!")
    print("Token:", access_token)
else:
    print("❌ Erro ao obter token:", response.status_code, response.text)
