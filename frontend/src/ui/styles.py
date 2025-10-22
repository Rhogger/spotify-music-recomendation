def load_styles() -> str:
    return """
    <style>
        :root {
            --background
            --spotify-green: #1DB954;
            --spotify-gray: #282828;
        }

        body, .main, .block-container {
            background: linear-gradient(180deg, #1a3a2e 0%, #0a1612 100%) !important;
            color: #fff !important;
        }
        
        .stAppHeader {
            display: none;
        }
        
        .stMainBlockContainer {
            padding: 0px;
            overflow: hidden;
        }
        
        .stMainBlockContainer {
            background: #122017 !important;
        }
        
        .stMainBlockContainer > div {
            gap: 0;
        }
        
        .stMainBlockContainer > div > div:first-child{
            display: none;
        }
        
        .stMainBlockContainer > div > div:last-child{
            padding-top: 71.4px;
        }
        
        div:has(.stForm) {
            height: 100%;
        }
        
        .stForm{
            padding: 0px;
        }
        
        .stForm > div {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .stColumn {
            padding: 32px;
        }
        
        .stColumn:first-child {
            border-width: 0px 1px 0px 0px;
            border-color: #2A362E;
            border-style: solid;
        }
        
                
        .stColumn:last-child {
            overflow-y: auto;
            height: calc(100vh - 71.4px);
        }
        
        .stColumn:last-child::-webkit-scrollbar {
            width: 8px;
        }
        
        .stColumn:last-child::-webkit-scrollbar-thumb {
            background-color: var(--spotify-green);
            border-radius: 10px;
        }
        
        .stColumn:last-child::-webkit-scrollbar-track {
            background: var(--spotify-gray);
        }

        .header-title {
            position: absolute;
            top: 0px;
            left: 0px;
            
            width: 100%;
            display: flex;
            align-items: center;
            gap: 1rem;
            font-size: 1.5rem;
            font-weight: 700;
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #2A362E;
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
        
        h3 {
            padding: 0px !important;
            margin-bottom: 16px !important;
        }
        
        h3 > span {
            display: none !important;
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

        button[data-testid="stBaseButton-primaryFormSubmit"] > div > p {
            font-weight: 700;
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
            padding-bottom: 32px;
        }
    </style>
"""
