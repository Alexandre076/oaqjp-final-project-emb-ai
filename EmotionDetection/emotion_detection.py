import requests
import json
def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    emotion_predictions = json.loads(response.text)

    #Extract the emotion scores
    anger_score = emotion_predictions['emotionPredictions'][0]['emotion']['anger']
    disgust_score = emotion_predictions['emotionPredictions'][0]['emotion']['disgust']
    fear_score = emotion_predictions['emotionPredictions'][0]['emotion']['fear']
    joy_score = emotion_predictions['emotionPredictions'][0]['emotion']['joy']
    sadness_score = emotion_predictions['emotionPredictions'][0]['emotion']['sadness']

    #Determine the dominante emotion
    dominant_emotion = max(emotion_predictions['emotionPredictions'][0]['emotion'], key=emotion_predictions['emotionPredictions'][0]['emotion'].get)

    result = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }

    #Return output formated
    return result
    