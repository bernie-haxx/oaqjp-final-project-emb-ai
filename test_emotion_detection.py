"""
Writing Tests Area
Modules Imported
    - Unittest
    - EmotionDetection
Fuctions/Classes:
    - TestEmotionDetection
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test Class Inheriting TestCase from Unittest
    """
    def test_emotion(self):
        """
        Function: test_emotion

        Statements tested
        Statement	                                    Dominant Emotion
        - I am glad this happened	                    joy
        - I am really mad about this	                anger
        - I feel disgusted just hearing about this	    disgust
        - I am so sad about this	                    sadness
        - I am really afraid that this will happen	f   ear
        """
        self.assertEqual(
            emotion_detector('I am glad this happened')['dominant_emotion'],
            'joy')
        self.assertEqual(
            emotion_detector('I am really mad about this')['dominant_emotion'],
            'anger')
        self.assertEqual(
            emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'],
            'disgust')
        self.assertEqual(
            emotion_detector('I am so sad about this')['dominant_emotion'],
            'sadness')
        self.assertEqual(
            emotion_detector('I am really afraid that this will happen')['dominant_emotion'],
            'fear')

unittest.main()