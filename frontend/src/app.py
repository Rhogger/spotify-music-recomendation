import os
import pickle

import joblib
import pandas as pd
import streamlit as st
from ui.components import header, slider_with_label, track_card_html
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

header()

col1, col2 = st.columns([1, 2], gap=None)

with col1:
    with st.form(key="reco_form", border=False):
        with st.container():
            st.markdown("### Parâmetros")

            pop = slider_with_label(
                "Popularidade", "Indica a popularidade da música", "pop_slider"
            )
            dance = slider_with_label(
                "Dançabilidade", "Indica quão dançável é a música", "dance_slider"
            )
            energy = slider_with_label(
                "Energia",
                "Indica quão energética e vibrante é a música",
                "energy_slider",
            )
            speech = slider_with_label(
                "Discurso",
                "Indica quão a música tem presença de palavras faladas",
                "speechiness_slider",
            )
            acoustic = slider_with_label(
                "Acústica",
                "Indica quão presente são os sons com equipaa música",
                "acoustic_slider",
            )
            instr = slider_with_label(
                "Instrumentalidade", "Instrumentalidade", "instr_slider"
            )

        submit = st.form_submit_button(
            "Gerar recomendação", use_container_width=True, type="primary"
        )

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
            resultados = recomendar_musica(input_dict, top_n=50)
            st.session_state["last_recommendations"] = resultados
        except Exception as e:
            st.error(f"Erro ao gerar recomendação: {e}")

with col2:
    with st.container():
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
            resultados = recomendar_musica(input_dict, top_n=50)
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
                        "artist": row.get(
                            "artist", row.get("artists", "Unknown Artist")
                        ),
                        "genres": row.get("genres", row.get("genre", "")),
                    }
                )

        else:
            # Fallback: usa a lista estática padrão
            display_list = display_songs

        html_tracks = '<div class="tracks-grid scrollable-list">'
        for song in display_list:
            html_tracks += track_card_html(song)

        st.markdown(html_tracks, unsafe_allow_html=True)
