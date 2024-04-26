# Emotion-AI-Detector
AI Based Web application

- Emotion Detection System that processes feedback provided by the customer in text format and deciphers the associated emotion expressed.

Libraries used:
- Embeddable Watson AI


# Installation:
- install Flask using pip
- create python virtual environment
  - python3 -m venv venv
- install required libraries
  - pip3 install -r requirements.txt
  
# Running Flask
- Export Settings: 
  - export FLASK_APP = app.py
  - FLASK_DEBUG=True
- flask run --emotion_detection

## Testing

1. Using Python Shell
- first make sure requests library is installed 
  - python3 -m pip install requests
- then run python shell command
  - $ python3.11
- then run:
  - >>> from emotion_detection import emotion_detector
  - >>> emotion_detector("i love this new technology")
- Expected output in JSON:
  - >>> {'emotionPredictions': [{'emotion': {'anger': 0.25520793, 'disgust': 0.020005126, 'fear': 0.062086333, 'joy': 0.08512125, 'sadness': 0.17719638}, 'target': '', 'emotionMentions': [{'span': {'begin': 0, 'end': 15, 'text': 'text_to_analyse'}, 'emotion': {'anger': 0.25520793, 'disgust': 0.020005126, 'fear': 0.062086333, 'joy': 0.08512125, 'sadness': 0.17719638}}]}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': )
        {'emotionPredictions': [{'emotion': {'anger': 0.25520793, 'disgust': 0.020005126, 'fear': 0.062086333, 'joy': 0.08512125, 'sadness': 0.17719638}, 'target': '', 'emotionMentions': [{'span': {'begin': 0, 'end': 15, 'text': 'text_to_analyse'}, 'emotion': {'anger': 0.25520793, 'disgust': 0.020005126, 'fear': 0.062086333, 'joy': 0.08512125, 'sadness': 0.17719638}}]}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}