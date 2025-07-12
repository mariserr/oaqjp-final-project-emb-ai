"""
This is the emotion_detector() function using Watson NLP library.
"""

import requests
import json

def emotion_detector(text_to_analyze):

    #Task 2 Create an emotion detecion app using Watson NLP Library

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)
    text = response.text
    
    # return text 
    #end task 2

    #Task 3: Format the output of the application

    # Convert the response text into a dictionary using the json library functions.
    responseFormated = json.loads(response.text)

    print (response.status_code)

    # There is an error in the response
    if  response.status_code != 200 :
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_key = None
    
    # Response is OK (200)
    elif response.status_code == 200:
        
        # Extract the required set of emotions along with their scores
        emotions = responseFormated['emotionPredictions'][0]['emotion']

        # anger_score = responseFormated["emotionPredictions"][0]["emotion"]["anger"]
        anger_score = emotions.get('anger', 0)
        # disgust_score = responseFormated["emotionPredictions"][0]["emotion"]["disgust"]
        disgust_score = emotions.get('disgust', 0)
        # fear_score = responseFormated["emotionPredictions"][0]["emotion"]["fear"]
        fear_score = emotions.get('fear', 0)
        # joy_score = responseFormated["emotionPredictions"][0]["emotion"]["joy"]
        joy_score = emotions.get('joy', 0)
        # sadness_score = responseFormated["emotionPredictions"][0]["emotion"]["sadness"]
        sadness_score = emotions.get('sadness', 0)

        # Write the code logic to find the dominant emotion, which is the emotion with the highest score
        emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        dominant_emotion_index = emotion_list.index(max(emotion_list))
        emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion_key = emotion_keys[dominant_emotion_index]

    # Modify the function to return the required output format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_key
    }

    return result
