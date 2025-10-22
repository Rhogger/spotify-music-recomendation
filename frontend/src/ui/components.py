import streamlit as st


def slider_with_label(label, tooltip, key):
    return st.slider(label, 0, 100, 0, 1, key=key, help=tooltip)


def track_card_html(song: dict) -> str:
    return f"""
        \n<div class="track-card">
            <div class="track-image">🖼</div>
            <div class="track-title">{song["title"]}</div>
            <div class="track-artist">{song["artist"]}</div>
            <div class="track-genres">{song["genres"]}</div>
        </div>\n
        """


def header():
    return st.markdown(
        '<div class="header-title"><div class="spotify-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="15%" fill="#3bd75f"/><circle cx="256" cy="256" fill="#fff" r="192"/><g fill="none" stroke="#3bd75f" stroke-linecap="round"><path d="m141 195c75-20 164-15 238 24" stroke-width="36"/><path d="m152 257c61-17 144-13 203 24" stroke-width="31"/><path d="m156 315c54-12 116-17 178 20" stroke-width="24"/></g></svg></div>Recomendações Spotify</div>',
        unsafe_allow_html=True,
    )
