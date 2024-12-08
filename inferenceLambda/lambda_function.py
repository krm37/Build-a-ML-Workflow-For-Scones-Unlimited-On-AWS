import json


THRESHOLD = .93

def lambda_handler(event, context):
    
    # Grab the inferences directly from the body
    inferences = event['body']['inferences']
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(inference > THRESHOLD for inference in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)  # event'i JSON formatına dönüştürmek için json.dumps kullanıyoruz
    }