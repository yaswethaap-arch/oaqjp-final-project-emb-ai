import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url,json = myobj,headers = header)
    print(response.status_code)
    if response.status_code == 200:
        formatted_text = json.loads(response.text)
        emotion = formatted_text['emotionPredictions'][0]['emotion']
    
        anger_score = emotion['anger']
        disgust_score = emotion['disgust']
        fear_score = emotion['fear']
        joy_score = emotion['joy']
        sadness_score = emotion['sadness']
        dominant_emotion = 'anger'
        if emotion[dominant_emotion] < disgust_score:
            dominant_emotion = 'disgust'
        if emotion[dominant_emotion] < fear_score:
            dominant_emotion = 'fear'
        if emotion[dominant_emotion] < joy_score:
            dominant_emotion = 'joy'
        if emotion[dominant_emotion] < sadness_score:
            dominant_emotion = 'sadness'
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    if dominant_emotion is None:
        return "Invalid test! Please Try again."
    else:
        return {'anger': anger_score, 
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
