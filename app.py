from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from Capture_emotion import detect_emotion as de
import zipfile
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

# Load the music dataset
if not os.path.exists("data.csv"):
    with zipfile.ZipFile("data.zip", 'r') as zip_ref:
        zip_ref.extractall()
songs_df = pd.read_csv('data.csv')

def classify_song_emotion(valence, energy):
    # Define emotion classification rules based on valence and energy
    if valence > 0.7 and energy > 0.7:
        return 'happy'
    elif valence < 0.3 and energy < 0.4:
        return 'sad'
    elif valence > 0.5 and energy < 0.4:
        return 'calm'
    elif valence < 0.4 and energy > 0.7:
        return 'angry'
    else:
        return 'neutral'

def get_song_recommendations(emotion, limit=30):
    # Add emotion classification to the dataframe
    songs_df['emotion'] = songs_df.apply(
        lambda row: classify_song_emotion(row['valence'], row['energy']), 
        axis=1
    )
    
    # Filter songs by emotion and sort by popularity
    matching_songs = songs_df[songs_df['emotion'] == emotion.lower()]
    top_songs = matching_songs.sort_values(
        by='popularity', 
        ascending=False
    ).head(limit)
    
    # Convert to list of dictionaries
    recommendations = []
    for _, song in top_songs.iterrows():
        recommendations.append({
            'name': song['name'],
            'artist': song['artists'],
            'url': f"https://open.spotify.com/track/{song['id']}",
            'popularity': int(song['popularity'])
        })
    
    return recommendations

@app.route('/api/detect-emotion',methods=['POST'])
def detect_emtion():
    try:
        detected_emotion=de()
        return jsonify({
            'status': 'success',
            'emotion': detected_emotion,
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/emoji-recommendations', methods=['POST'])
def emoji_recommendations():
    try:
        data = request.json
        emoji = data['emoji']
        
        # Map emoji to emotion
        emoji_map = {
            '😊': 'happy',
            '😔': 'sad',
            '😠': 'angry',
            '😌': 'calm',
            '😐': 'neutral'
        }
        
        '''emotion = emoji_map.get(emoji,'unknown')'''
        recommendations = get_song_recommendations(emoji)
        
        return jsonify({
            'status': 'success',
            'emotion': emoji,
            'recommendations': recommendations
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

