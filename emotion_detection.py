import requests
import json

def emotion_detector(text_to_analyse):
    """
    Sends text to Watson NLP EmotionPredict function
    and returns the 'text' attribute from the response.
    """

    # URL of the EmotionPredict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Required headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # JSON payload with the text
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Send POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check for successful response
    if response.status_code == 200:
        result = response.json()
        # Return the 'text' attribute from the response object
        return result.get('text', None)
    else:
        # Optional: raise an error if the request fails
        raise Exception(f"Emotion detection failed: {response.status_code} - {response.text}")
