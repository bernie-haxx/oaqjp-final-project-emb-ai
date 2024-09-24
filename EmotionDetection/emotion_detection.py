"""
Functions:
    - emotion_detector
Modules Imported
    - Requests
    - json
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Name: emotion_detector
    args: text_to_analyze
    return emotion_dict
    """

    # Group the url, header and object_response
    url = 'https://sn-watson-emotion.labs.skills.network/v1'\
          '/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { 'raw_document': { 'text': text_to_analyze }}

    # pass the response
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    #format the response into json
    formatted_response = json.loads(response.text)

    # Call the emotions dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Creating a new dictionary to save the emotions and dominant_emotion
    emotion_dict = {}

    # loop through assigning the keys
    for emotion, emotion_value in emotions.items():
        emotion_dict[emotion] = float(emotion_value)
    
    # getting the dominant emotion using the max and zip function
    # looking through all the keys in the dictionary emotion_dict through the use of zip
    # Selecting the second value which is representing the key
    dominant_emotion = max(zip(emotion_dict.values(), emotion_dict.keys()))[1]

    # Add the dominant emotion to the emotion_dict
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict
