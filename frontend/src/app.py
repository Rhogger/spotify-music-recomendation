import os
import pickle

import joblib
import pandas as pd
import streamlit as st
from ui.styles import load_styles


@st.cache_resource
def load_model():
    # Diretório onde está este arquivo (app.py)
    base_path = os.path.dirname(__file__)
    ia_path = os.path.abspath(os.path.join(base_path, "../../ia/src"))

    path_model = os.path.join(ia_path, "models/music_recommender_model.joblib")
    path_preprocessor = os.path.join(ia_path, "models/music_preprocessor.joblib")
    path_df = os.path.join(ia_path, "datasets/data_clean.csv")
    path_features = os.path.join(ia_path, "models/music_model_features.pkl")
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


def recomendar_musica(
    input_dict,
    df=df_model,
    model=model,
    preprocessor=preprocessor,
    features=features,
    top_n=5,
):
    input_df = pd.DataFrame([input_dict])[features]
    input_scaled = preprocessor.transform(input_df)
    distances, indices = model.kneighbors(input_scaled, n_neighbors=top_n)
    resultados = df.iloc[indices[0]].copy().reset_index(drop=True)
    resultados["distancia"] = distances[0]
    return resultados


st.set_page_config(page_title="Recomendações Spotify", page_icon="🎵", layout="wide")
st.markdown(load_styles(), unsafe_allow_html=True)

st.markdown(
    '<div class="header-title"><div class="spotify-icon">♪</div>Recomendações Spotify</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### Parâmetros")

    with st.form(key="reco_form"):
        st.markdown('<div class="slider-group">', unsafe_allow_html=True)
        pop = st.slider("Popularidade ", 0, 100, 50, 1, key="pop_slider")
        st.markdown(
            f"""
<div class="slider-label"><span>Popularidade </span><span>{pop}</span></div>
""",
            unsafe_allow_html=True,
        )

        dance = st.slider("Dançabilidade", 0, 100, 75, 1, key="dance_slider")
        st.markdown(
            f"""
<div class="slider-label"><span>Dançabilidade</span><span>{dance}</span></div>
""",
            unsafe_allow_html=True,
        )

        energy = st.slider("Energia", 0, 100, 80, 1, key="energy_slider")
        st.markdown(
            f"""
<div class="slider-label"><span>Energia </span><span>{energy}</span></div>
""",
            unsafe_allow_html=True,
        )

        speech = st.slider("Discurso", 0, 100, 80, 1, key="speechiness_slider")
        st.markdown(
            f"""
<div class="slider-label"><span>Discurso</span><span>{speech}</span></div>
""",
            unsafe_allow_html=True,
        )

        acoustic = st.slider("Acústica", 0, 100, 20, 1, key="acoustic_slider")
        st.markdown(
            f"""
<div class="slider-label"><span>Acústica</span><span>{acoustic}</span></div>
""",
            unsafe_allow_html=True,
        )

        instr = st.slider("Instrumentalidade", 0, 100, 60, 1, key="instr_slider")
        st.markdown(
            f"""
<div class="slider-label"><span>Instrumentalidade</span><span>{instr}</span></div>
""",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
        submit = st.form_submit_button("Gerar recomendação", use_container_width=True)

    if submit:
        input_dict = {
            "popularity": pop / 100.0,
            "danceability": dance / 100.0,
            "energy": energy / 100.0,
            "speechiness": speech / 100.0,
            "acousticness": acoustic / 100.0,
            "instrumentalness": instr / 100.0,
        }

        try:
            resultados = recomendar_musica(input_dict, top_n=10)
            st.session_state["last_recommendations"] = resultados
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
        "instrumentalness": instr / 100.0,
    }

    try:
        resultados = recomendar_musica(input_dict, top_n=10)
        st.session_state["last_recommendations"] = resultados
    except Exception as e:
        st.error(f"Erro ao gerar recomendação: {e}")

    display_songs = []

    # Verifica se há recomendações geradas pelo modelo
    if (
        "last_recommendations" in st.session_state
        and st.session_state["last_recommendations"] is not None
    ):
        resultados = st.session_state["last_recommendations"]

        # Converte o DataFrame em uma lista de dicionários compatível com o layout
        display_list = []
        for _, row in resultados.iterrows():
            display_list.append(
                {
                    "title": row.get("title", row.get("song", "Unknown Title")),
                    "artist": row.get("artist", row.get("artists", "Unknown Artist")),
                    "genres": row.get("genres", row.get("genre", "")),
                }
            )

    else:
        # Fallback: usa a lista estática padrão
        display_list = display_songs

    # Gera o HTML dos cards (mesmo estilo que você já tinha)
    html_tracks = '<div class="tracks-grid scrollable-list">'
    for song in display_list:
        html_tracks += f"""
        \n<div class="track-card">
            <!--<div class="track-image">🖼</div>-->
            <div class="track-title">{song["title"]}</div>
            <div class="track-artist">{song["artist"]}</div>
            <div class="track-genres">{song["genres"]}</div>
          </div>\n
        """
    # html_tracks += "</div>"

    st.markdown(html_tracks, unsafe_allow_html=True)
