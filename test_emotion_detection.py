import unittest
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result1=emotion_predictor(emotion_detector("I am glad this happened"))
        self.assertEqual(result1['dominant_emotion'],'joy')

    def test_anger(self):
        result1=emotion_predictor(emotion_detector("I am really mad about this"))
        self.assertEqual(result1['dominant_emotion'],'anger')

    def test_disgust(self):
        result1=emotion_predictor(emotion_detector("I feel disgusted just hearing about this"))
        self.assertEqual(result1['dominant_emotion'],'disgust')

    def test_sadness(self):
        result1=emotion_predictor(emotion_detector("I am so sad about this"))
        self.assertEqual(result1['dominant_emotion'],'sadness')

    def test_fear(self):

        result1=emotion_predictor(emotion_detector("I am really afraid that this will happen"))
        self.assertEqual(result1['dominant_emotion'],'fear')


if __name__=="__main__":
    unittest.main()