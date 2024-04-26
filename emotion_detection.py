
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
    - CREATE AN EMOTION DETECTION APP USING WATSON NLP LIBRARY
    - FORMAT OUTPUT OF APP
    - PACKAGE THE APP
    - RUN UNIT TESTS
    - WEB DEPLOYMENT OF THE APP USING FLASK
    - INCORPORATE ERROR HANDLING
    - RUN STATIC CODE ANALYSIS

"""
import requests,json

# Watson libraries are embedded. So only need to 

    """
    text to be analyzed is passed to the function as an argument 
    and is stored in the variable text_to_analyze. 
    The value being returned must be the text attribute of the response object as received from the Emotion Detection function.

    """
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } } 
    # send a post request to the correct function and receive output 
    req = requests.post(url,json=input_json,headers=header)

    if req.status_code == 200:
        return (req.json())
    elif req.status_code == 400:
        return {"message":"no response to make"}

