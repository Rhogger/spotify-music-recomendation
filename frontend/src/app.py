import streamlit as st
import random
import joblib
import pickle
import pandas as pd
import numpy as np
import os

@st.cache_resource
def load_model():
    # Diretório onde está este arquivo (app.py)
    base_path = os.path.dirname(__file__)
    ia_path = os.path.abspath(os.path.join(base_path, "../../ia/src"))

    path_model = os.path.join(ia_path, "joblib/music_recommender_model.joblib")
    path_preprocessor = os.path.join(ia_path, "joblib/music_preprocessor.joblib")
    path_df = os.path.join(ia_path, "datasets/data_clean.csv")
    path_features = os.path.join(ia_path, "joblib/music_model_features.pkl")
    model = joblib.load(path_model)
    preprocessor = joblib.load(path_preprocessor)
    try:
        df = pd.read_csv(path_df)
    except Exception:
        df = None
        
    with open(path_features, "rb") as f:
        features = pickle.load(f)
    return model, preprocessor, df, features

model, preprocessor, df_model, features = load_model()

def recomendar_musica(input_dict, df=df_model, model=model, preprocessor=preprocessor, features=features, top_n=5):
    input_df = pd.DataFrame([input_dict])[features]
    input_scaled = preprocessor.transform(input_df)
    distances, indices = model.kneighbors(input_scaled, n_neighbors=top_n)
    resultados = df.iloc[indices[0]].copy().reset_index(drop=True)
    resultados['distancia'] = distances[0]
    return resultados


st.set_page_config(
    page_title="Recomendações Spotify",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<style>
:root {
    --spotify-green: #1DB954;
    --spotify-gray: #282828;
}

body, .main, .block-container {
    background: linear-gradient(180deg, #1a3a2e 0%, #0a1612 100%) !important;
    color: #fff !important;
}

.header-title {
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
}
.spotify-icon {
    width: 32px;
    height: 32px;
    background: #1db954;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 20px;
    color: #181818;
}
.slider-group {
    margin-bottom: 2rem;
}
.slider-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.75rem;
    font-size: 0.95rem;
}
.slider-label span:first-child {
    color: #b3b3b3;
}
.slider-label span:last-child {
    color: #fff;
    font-weight: 600;
}
.generate-button {
    width: 100%;
    padding: 1rem;
    background: #1db954;
    border: none;
    border-radius: 500px;
    color: #000;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    margin-top: 2rem;
    transition: transform 0.2s;
}
.generate-button:hover {
    transform: scale(1.02);
}
.tracks-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5rem;
}
.track-card {
    background: rgba(0,0,0,0.3);
    border-radius: 12px;
    padding: 1rem;
    transition: background 0.3s;
    cursor: pointer;
}
.track-card:hover {
    background: rgba(0,0,0,0.5);
}
.track-image {
    width: 100%;
    aspect-ratio: 1;
    background: linear-gradient(135deg, #e0e0e0 0%, #c0c0c0 100%);
    border-radius: 8px;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    font-size: 3rem;
}
.track-title {
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
    color: #fff;
}
.track-artist {
    font-size: 0.875rem;
    color: #b3b3b3;
    margin-bottom: 0.5rem;
}
.track-genres {
    font-size: 0.8rem;
    color: #1db954;
}
.scrollable-list {
    max-height: 800px;
    overflow-y: auto;
    padding-right: 10px;
}
.scrollable-list::-webkit-scrollbar {
    width: 8px;
}
.scrollable-list::-webkit-scrollbar-thumb {
    background-color: var(--spotify-green);
    border-radius: 10px;
}
.scrollable-list::-webkit-scrollbar-track {
    background: var(--spotify-gray);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="header-title"><div class="spotify-icon">♪</div>Recomendações Spotify</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### Parâmetros")

    with st.form(key="reco_form"):
        st.markdown('<div class="slider-group">', unsafe_allow_html=True)
        pop = st.slider("Popularidade ", 0, 100, 50, 1, key="pop_slider")
        st.markdown(f'''
<div class="slider-label"><span>Popularidade </span><span>{pop}</span></div>
''', unsafe_allow_html=True)

        dance = st.slider("Dançabilidade", 0, 100, 75, 1, key="dance_slider")
        st.markdown(f'''
<div class="slider-label"><span>Dançabilidade</span><span>{dance}</span></div>
''', unsafe_allow_html=True)

        energy = st.slider("Energia", 0, 100, 80, 1, key="energy_slider")
        st.markdown(f'''
<div class="slider-label"><span>Energia </span><span>{energy}</span></div>
''', unsafe_allow_html=True)
        
        speech = st.slider("Discurso", 0, 100, 80, 1, key="speechiness_slider")
        st.markdown(f'''
<div class="slider-label"><span>Discurso</span><span>{speech}</span></div>
''', unsafe_allow_html=True)

        acoustic = st.slider("Acústica", 0, 100, 20, 1, key="acoustic_slider")
        st.markdown(f'''
<div class="slider-label"><span>Acústica</span><span>{acoustic}</span></div>
''', unsafe_allow_html=True)

        instr = st.slider("Instrumentalidade", 0, 100, 60, 1, key="instr_slider")
        st.markdown(f'''
<div class="slider-label"><span>Instrumentalidade</span><span>{instr}</span></div>
''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        submit = st.form_submit_button("Gerar recomendação", use_container_width=True)

    if submit:
        input_dict = {
            "popularity": pop / 100.0,
            "danceability": dance / 100.0,
            "energy": energy / 100.0,
            "speechiness": speech / 100.0,
            "acousticness": acoustic / 100.0,
            "instrumentalness": instr / 100.0
        }

        try:
            resultados = recomendar_musica(input_dict, top_n=10)
            st.session_state['last_recommendations'] = resultados
        except Exception as e:
            st.error(f"Erro ao gerar recomendação: {e}")

with col2:
    st.markdown("### Músicas Recomendadas")

    input_dict = {
            "popularity": pop / 100.0,
            "danceability": dance / 100.0,
            "energy": energy / 100.0,
            "speechiness": speech / 100.0,
            "acousticness": acoustic / 100.0,
            "instrumentalness": instr / 100.0
    }

    try:
        resultados = recomendar_musica(input_dict, top_n=10)
        st.session_state['last_recommendations'] = resultados
    except Exception as e:
            st.error(f"Erro ao gerar recomendação: {e}")
        
    display_songs = []

    # Verifica se há recomendações geradas pelo modelo
    if "last_recommendations" in st.session_state and st.session_state["last_recommendations"] is not None:
        resultados = st.session_state["last_recommendations"]

        # Converte o DataFrame em uma lista de dicionários compatível com o layout
        display_list = []
        for _, row in resultados.iterrows():
            display_list.append({
                "title": row.get("title", row.get("song", "Unknown Title")),
                "artist": row.get("artist", row.get("artists", "Unknown Artist")),
                "genres": row.get("genres", row.get("genre", ""))
            })

    else:
        # Fallback: usa a lista estática padrão
        display_list = display_songs

    # Gera o HTML dos cards (mesmo estilo que você já tinha)
    html_tracks = '<div class="tracks-grid scrollable-list">'
    for song in display_list:
        html_tracks += f"""
        \n<div class="track-card">
            <!--<div class="track-image">🖼</div>-->
            <div class="track-title">{song['title']}</div>
            <div class="track-artist">{song['artist']}</div>
            <div class="track-genres">{song['genres']}</div>
          </div>\n
        """
    # html_tracks += "</div>"

    st.markdown(html_tracks, unsafe_allow_html=True)

