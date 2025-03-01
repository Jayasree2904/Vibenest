**VIBENEST**

Emotion-Based Music Recommendation System.
Vibenest is an innovative web application that uses artificial intelligence to recommend music based on your emotional state. By analyzing your facial expressions through your camera or by letting you select an emoji, Vibenest suggests personalized song recommendations that match your current mood.

#Features

##Dual Input Methods:

+Camera-based Emotion Detection: Using face-api.js and DeepFace to analyze your facial expressions in real-time.
+Emoji Selection: Manually select an emoji that represents your current mood.

###AI-Powered Emotion Analysis: 
  Advanced algorithms classify emotions into five categories:

+Happy 😊

+Sad 😔

+Calm 😌

+Angry 😠

+Neutral 😐

###Music Recommendations:
Get personalized Spotify song recommendations that match your detected emotion
Songs are classified based on valence and energy metrics
Recommendations are sorted by popularity for the best music discovery experience

##Technology Stack

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

ML/AI:

DeepFace for facial emotion recognition.
face-api.js for real-time facial detection in browser.
Custom classification algorithms for emotion-to-music mapping.

Data: Curated Spotify dataset with audio features including valence, energy, and popularity metrics

##How It Works:

The system captures your emotional state either through:

+Facial expression analysis using computer vision

+Direct emoji selection

The detected emotion is processed and mapped to a music mood category.
The application queries a database of songs pre-classified by emotional characteristics.
Vibenest returns a personalized list of song recommendations with Spotify links.

##Prerequisites

+Python 3.7+

+Flask

+OpenCV

+DeepFace

+Pandas

+scikit-learn
