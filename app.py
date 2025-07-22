from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import pandas as pd
from Capture_emotion import detect_emotion as de


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/try-now')
def try_now():
    return render_template('try-now.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Load the music dataset
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
    app.run(debug=True, port=5000)
