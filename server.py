"""
Server Module
Host: 0.0.0.0
Port : 5000
Debug : True

Imports:
    - Flask from flask
    - render_template from flask
    - emotion_detector from EmotionDetection
"""
from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection.emotion_detection import emotion_detector

# Initialize flask 
app = Flask(" Emotion Detection App")


@app.route("/emotionDetector")
def emot_detector():
    """
    Route: /emotionDetector
    Input: None
    Get Requests: textToAnalyze
    return: 
        For the given statement, the system response is 'anger': {result['anger']},\
        'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and\
        'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)

    return f"For the given statement, the system response is 'anger': {result['anger']},\
        'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and\
        'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True) 
