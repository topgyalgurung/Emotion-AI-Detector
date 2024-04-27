
#!/usr/bin/env python
# coding: utf-8

""" emotion_detection.py: emotion detection application using Watson NLP Library 
@author = "Topgyal Gurung"
@Date = "Production"
@Credit=
@Links= 

Function: Emotion Predict
Library: Watson NLP 

TODO:
1. CREATE AN EMOTION DETECTION APP USING WATSON NLP LIBRARY
2. FORMAT OUTPUT OF APP
3. PACKAGE THE APP
4. RUN UNIT TESTS
5. WEB DEPLOYMENT OF THE APP USING FLASK
6. INCORPORATE ERROR HANDLING
7. RUN STATIC CODE ANALYSIS

"""
import requests
import json

# Watson libraries are embedded. So only need to 

"""
    text to be analyzed is passed to the function as an argument 
    and is stored in the variable text_to_analyze. 
    The value being returned must be the text attribute of the response object as received from the Emotion Detection function.

"""
def emotion_detector(text_to_analyse):
    ''' send a post request to the correct function and receive output '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } } 

    req = requests.post(url,json=input_json,headers=header)
    # data=json.loads(requests.post(url,json=input_json,headers=header).text)
    json_response = json.loads(req.text)

    # Step 2: Extract required set of emotions

    if req.status_code == 200:
        return emotion_predictor(json_response)
    elif req.status_code == 400:
        return {"message":"no response to make"}
{
""" sample output: 
  'emotionPredictions': [
    {
      'emotion': {
        'anger': 0.584618,
        'disgust': 0.04331746,
        'fear': 0.027819801,
        'joy': 0.009122466,
        'sadness': 0.27680367
      },
      'target': '',
      'emotionMentions': [
        {
          'span': {
            'begin': 0,
            'end': 19,
            'text': 'i hate this new app'
          },
          'emotion': {
            'anger': 0.584618,
            'disgust': 0.04331746,
            'fear': 0.027819801,
            'joy': 0.009122466,
            'sadness': 0.27680367
          }
        }
      ]
    }
  ],
  'producerId': {
    'name': 'Ensemble Aggregated Emotion Workflow',
    'version': '0.0.1'
  }
}
"""
# access doctring which document python module, class, function or method 
print(emotion_detector.__doc__)

"""
json loads useful to have a JSON string to convert to python data structure
    response.json() for parsing json responses http requests using requests, specific handling json content
    json.loads() for deserializing json strings(text) into python data structure. 
"""

"""
2. Format output off  the app
# write code logic to find the dominant emotion (with highest score )
"""

def emotion_predictor(text):
     ''' return emotions with dominant emotion'''
     if all(value is None for value in text.values()):
        return text 
    else:
        emotion=text['emotionPredictions'][0]['emotion']
		result={
		   'anger':emotion['anger'],
		   "disgust":emotion['disgust'],
		   "fear":emotion['fear'],
		   "joy":emotion['joy'],
		   "sadness":emotion['sadness'],
		   "dominant_emotion": max(emotion,key=emotion.get)
		   }
		print(result)  

def main():
        emotion_detector(" i love this new application")

if __name__=="__main__":
    main()

