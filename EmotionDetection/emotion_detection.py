# import requests  # Import the requests library to handle HTTP requests

# def emotion_detector(text_to_analyse):  # Define a function named emotion detector that takes a string input (text_to_analyse)
#     url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detector service
#     myobj ={ "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
#     response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
#     return response.text  # Return the response text from the API

# import requests
# import json

# def emotion_detector(text_to_analyse):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
#     myobj = { "raw_document": { "text": text_to_analyse } }
    
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
#     response = requests.post(url, json=myobj, headers=header)
    
#     # Convert response text to dictionary
#     formatted_response = json.loads(response.text)
    
#     # Extract emotion scores
#     emotions = formatted_response['emotionPredictions'][0]['emotion']
    
#     anger_score = emotions['anger']
#     disgust_score = emotions['disgust']
#     fear_score = emotions['fear']
#     joy_score = emotions['joy']
#     sadness_score = emotions['sadness']
    
#     # Find dominant emotion
#     emotion_scores = {
#         'anger': anger_score,
#         'disgust': disgust_score,
#         'fear': fear_score,
#         'joy': joy_score,
#         'sadness': sadness_score
#     }
    
#     dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
#     # Final output format
#     return {
#         'anger': anger_score,
#         'disgust': disgust_score,
#         'fear': fear_score,
#         'joy': joy_score,
#         'sadness': sadness_score,
#         'dominant_emotion': dominant_emotion
#     }



# emotion_detection.py to handle blank entries
import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detect emotions for a given text.
    Returns None values for all keys if input is blank or API returns 400.
    """
    # Handle blank input
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Handle API returning 400 (bad request)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse response
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
