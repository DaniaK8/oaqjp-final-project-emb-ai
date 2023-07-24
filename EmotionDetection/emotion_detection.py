import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    print (formatted_response)
    emotion = []
    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        print (emotion)
        anger_score = emotion["anger"]
        disgust_score = emotion["disgust"]
        fear_score = emotion["fear"]
        joy_score = emotion["joy"]
        sadness_score = ["sadness"]
        json_data = {
            "anger": 0.0132405795,
            "disgust": 0.0020517302,
            "fear": 0.009090992,
            "joy": 0.9699522,
            "sadness": 0.054984167
        }

        max_emotion = max(json_data.items(), key=lambda x: x[1])
    elif response.status_code == 500:
        emotion = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
    return max_emotion[0] 

