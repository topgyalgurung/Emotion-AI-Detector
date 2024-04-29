"""
Emotion Detection Server
Author: Topgyal
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app=Flask(__name__)

@app.route('/')
def render_page():
    '''render index html template ''' 
    return render_template('index.html')

@app.route('/emotionDetector')
def emo_detector():
    '''takes user input and return response based on text '''
    user_input=request.args.get('textToAnalyze')
    response=emotion_predictor(emotion_detector(user_input))
    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']
    dominant_emotion=response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is \
        'anger': { anger},\
        'disgust' :{ disgust },\
        'fear ': { fear }, \
        'joy' : { joy }, \
        'sadness' : { sadness }, \
        'dominant_emotion': '\033[1m'{dominant_emotion}'\033[0m' . "


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
