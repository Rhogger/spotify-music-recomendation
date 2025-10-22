import base64
from urllib.parse import quote

import requests

# ===== CONFIGURAÇÕES =====
CLIENT_ID = "a503dfb97b5447de98f9f01e87cd25bd"
CLIENT_SECRET = "10932faa1bfd403f9e3f5a75e009b8b7"

TRACK_NAME = "Eenie Meenie"
ARTIST_NAME = "Sean Kingston"
GENRES = ["pop", "r&b", "hip hop"]  # só para refinar a busca


# ===== FUNÇÃO PARA GERAR TOKEN =====
def get_access_token(client_id, client_secret):
    token_url = "https://accounts.spotify.com/api/token"
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


# ===== FUNÇÃO PARA BUSCAR MÚSICA =====
def search_track(track_name, artist_name, genres, access_token):
    search_url = "https://api.spotify.com/v1/search"

    # Monta query mais detalhada
    genre_query = " ".join(genres)
    query = f"track:{track_name} artist:{artist_name} {genre_query}"
    encoded_query = quote(query)

    headers = {"Authorization": f"Bearer {access_token}"}
    params = {
        "q": encoded_query,
        "type": "track",
        "limit": 3,
    }

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    items = data.get("tracks", {}).get("items", [])
    if not items:
        print("❌ Nenhum resultado encontrado.")
        return None

    # Itera pelos resultados encontrados
    for idx, track in enumerate(items, start=1):
        track_name = track["name"]
        artist_name = ", ".join([a["name"] for a in track["artists"]])
        album_name = track["album"]["name"]
        images = track["album"].get("images", [])
        image_url = images[0]["url"] if images else None

        print(f"\n🔹 Resultado {idx}")
        print(f"🎵 Música: {track_name}")
        print(f"👤 Artista(s): {artist_name}")
        print(f"💿 Álbum: {album_name}")
        print(f"🖼️ Imagem: {image_url}")

    return items[0]["album"]["images"][0]["url"]


# ===== EXECUÇÃO =====
if __name__ == "__main__":
    token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    search_track(TRACK_NAME, ARTIST_NAME, GENRES, token)
