# Emotion-AI-Detector

AI Based Web application: Python web app using Flask and integrate Embeddable Watson AI libraries to make the web app showcase AI based abilities. 

## Description:
AI based app that perform analytics on customer feedback for their signature products. Emotion Detection System that processes feedback provided by the customer in text format and deciphers the associated emotion expressed.

Libraries used:
- Embeddable Watson AI

Tasks:
1. Send post request to correct function in the library and receive output
2. Convert response text into a dictinary
3. Package the application and test it
4. Run unit tests - create test file to run unit tests
5. Deploy the app
6. Incorporate error handling
7. Run static code analysis using PyLint library 

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
  ``` 
  python3 -m pip install requests
  ``` 
- then run python shell command
```$ python3 ```
- then run:
  ```
    from emotion_detection import emotion_detector
    emotion_detector("i love this new technology")
  ```     

2. Static code analysis
- Using PyLint
```
  pylint server.py
```
