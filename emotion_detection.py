import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url,json = myobj,headers = header)
    formatted_text = json.loads(response.text)
    print(formatted_text['emotionPredictions'])
    emotion = formatted_text[1]
    print("emotion "+emotion)
    anger_score = emotion['anger']
    disgust_score = formatted_text['emotionPredictions']['emotion']['disgust']
    fear_score = formatted_text['emotionPredictions']['emotion']['fear']
    joy_score = formatted_text['emotionPredictions']['emotion']['joy']
    sadness_score = formatted_text['emotionPredictions']['emotion']['sadness']

    return {'anger': anger_score, 
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
            }
