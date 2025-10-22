def load_styles() -> str:
    return """
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
"""
