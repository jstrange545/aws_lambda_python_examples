import json

def lambda_handler(event, context):
    logger.info(json.dumps({
        "event": event,
        "context": context,
        "message": "Function executed successfully."
    }))