#!/usr/bin/env python3

text={
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
def emotion_predictor(text):
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
	emotion_predictor(text)
	
if __name__== "__main__":
	main()