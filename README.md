**VIBENEST**

Emotion-Based Music Recommendation System.
Vibenest is an innovative web application that uses artificial intelligence to recommend music based on your emotional state. By analyzing your facial expressions through your camera or by letting you select an emoji, Vibenest suggests personalized song recommendations that match your current mood.

**Features:-**

***Dual Input Methods:***

+Camera-based Emotion Detection: Using face-api.js and DeepFace to analyze your facial expressions in real-time.

+Emoji Selection: Manually select an emoji that represents your current mood.

***AI-Powered Emotion Analysis:*** 
  Advanced algorithms classify emotions into five categories:

+Happy 😊

+Sad 😔

+Calm 😌

+Angry 😠

+Neutral 😐

***Music Recommendations:***
Get personalized Spotify song recommendations that match your detected emotion.
Songs are classified based on valence and energy metrics,
recommendations are sorted by popularity for the best music discovery experience.

***Technology Stack:***

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

ML/AI:
DeepFace for facial emotion recognition.
face-api.js for real-time facial detection in browser.
Custom classification algorithms for emotion-to-music mapping.

Data: This project uses the [Spotify Dataset from Kaggle](https://www.kaggle.com/datasets/sanjanchaudhari/spotify-dataset), which includes song metadata and audio features like valence, energy, and popularity. These features are crucial for our emotion-based classification system.

***How It Works:***

The system captures your emotional state either through:

+Facial expression analysis using computer vision

+Direct emoji selection

The detected emotion is processed and mapped to a music mood category.
The application queries a database of songs pre-classified by emotional characteristics.
Vibenest returns a personalized list of song recommendations with Spotify links.

***Prerequisites:***

+Python 3.7+

+Flask

+OpenCV

+DeepFace

+Pandas

+scikit-learn

***Installation***

1.Clone the repository

    git clone https://github.com/Jayasree2904/vibenest.git
    cd vibenest

2.Install required Python packages

    pip install -r requirements.txt

3.Download the [Spotify Dataset from Kaggle](https://www.kaggle.com/datasets/sanjanchaudhari/spotify-dataset) and save it as data.csv in the project root directory.

4.Start the Flask backend server

    python app.py

5.Open index.html in your browser or serve it with a simple HTTP server

    python -m http.server 8000

6.Navigate to http://localhost:8000 in your web browser
