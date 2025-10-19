import streamlit as st
import random

st.set_page_config(
    page_title="Spotify Recommendations",
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
    '<div class="header-title"><div class="spotify-icon">♪</div>Spotify Recommendations</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### Recommendation Parameters")

    with st.form(key="reco_form"):
        st.markdown('<div class="slider-group">', unsafe_allow_html=True)
        pop = st.slider("Popularity", 0, 100, 50, 1, key="pop_slider")
        st.markdown(f'''
<div class="slider-label"><span>Popularity</span><span>{pop}</span></div>
''', unsafe_allow_html=True)

        dance = st.slider("Danceability", 0, 100, 75, 1, key="dance_slider")
        st.markdown(f'''
<div class="slider-label"><span>Danceability</span><span>{dance}</span></div>
''', unsafe_allow_html=True)

        energy = st.slider("Energy", 0, 100, 80, 1, key="energy_slider")
        st.markdown(f'''
<div class="slider-label"><span>Energy</span><span>{energy}</span></div>
''', unsafe_allow_html=True)

        vocal = st.slider("Vocality", 0, 100, 30, 1, key="vocal_slider")
        st.markdown(f'''
<div class="slider-label"><span>Vocality</span><span>{vocal}</span></div>
''', unsafe_allow_html=True)

        acoustic = st.slider("Acousticness", 0, 100, 20, 1, key="acoustic_slider")
        st.markdown(f'''
<div class="slider-label"><span>Acousticness</span><span>{acoustic}</span></div>
''', unsafe_allow_html=True)

        instr = st.slider("Instrumentalness", 0, 100, 60, 1, key="instr_slider")
        st.markdown(f'''
<div class="slider-label"><span>Instrumentalness</span><span>{instr}</span></div>
''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        submit = st.form_submit_button("Gerar recomendação", use_container_width=True)

    if submit:
        st.session_state.generate_music = True
        if "filtered_songs" in st.session_state:
            del st.session_state.filtered_songs

with col2:
    st.markdown("### Recommended Tracks")

    display_songs = [
        {
            "title": "Blinding Lights",
            "artist": "The Weeknd",
            "genres": "Pop"
        },
        {
            "title": "Levitating",
            "artist": "Dua Lipa",
            "genres": "Dance Pop"
        },
        {
            "title": "Good 4 U",
            "artist": "Olivia Rodrigo",
            "genres": "Pop Rock"
        },
        {
            "title": "Stay",
            "artist": "The Kid LAROI & Justin Bieber",
            "genres": "Pop"
        },
        {
            "title": "Industry Baby",
            "artist": "Lil Nas X ft. Jack Harlow",
            "genres": "Hip Hop"
        },
        {
            "title": "Heat Waves",
            "artist": "Glass Animals",
            "genres": "Indie Pop"
        },
        {
            "title": "Bad Habits",
            "artist": "Ed Sheeran",
            "genres": "Pop"
        },
        {
            "title": "Peaches",
            "artist": "Justin Bieber ft. Daniel Caesar",
            "genres": "R&B"
        },
        {
            "title": "Montero",
            "artist": "Lil Nas X",
            "genres": "Hip Hop"
        },
        {
            "title": "Kiss Me More",
            "artist": "Doja Cat ft. SZA",
            "genres": "R&B"
        },
        {
            "title": "Positions",
            "artist": "Ariana Grande",
            "genres": "R&B"
        },
        {
            "title": "Watermelon Sugar",
            "artist": "Harry Styles",
            "genres": "Pop Rock"
        },
        {
            "title": "drivers license",
            "artist": "Olivia Rodrigo",
            "genres": "Pop"
        },
        {
            "title": "Save Your Tears",
            "artist": "The Weeknd",
            "genres": "Synthpop"
        },
        {
            "title": "As It Was",
            "artist": "Harry Styles",
            "genres": "Pop"
        },
        {
            "title": "Easy On Me",
            "artist": "Adele",
            "genres": "Pop"
        },
        {
            "title": "Telepatía",
            "artist": "Kali Uchis",
            "genres": "R&B"
        },
        {
            "title": "bad guy",
            "artist": "Billie Eilish",
            "genres": "Electropop"
        },
        {
            "title": "Dance Monkey",
            "artist": "Tones and I",
            "genres": "Alternative/Indie"
        },
        {
            "title": "Sunflower",
            "artist": "Post Malone & Swae Lee",
            "genres": "Hip Hop"
        },
        {
            "title": "Someone You Loved",
            "artist": "Lewis Capaldi",
            "genres": "Pop"
        }
    ]

    if hasattr(st.session_state, 'generate_music') and st.session_state.generate_music:
        filtered_tracks = random.sample(display_songs, len(display_songs))
    else:
        filtered_tracks = display_songs

    html_tracks = '<div class="tracks-grid scrollable-list">'
    for song in filtered_tracks:
        html_tracks += f"""
          \n<div class="track-card">
            <div class="track-image">🖼</div>
            <div class="track-title">{song['title']}</div>
            <div class="track-artist">{song['artist']}</div>
            <div class="track-genres">{song['genres']}</div>
          </div>\n
        """

    st.markdown(html_tracks, unsafe_allow_html=True)

