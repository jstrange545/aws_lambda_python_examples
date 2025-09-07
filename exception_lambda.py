def lambda_handler(event, context):
    try:
        # processing logic here
    except Exception as e:
        # Log the error and handle it gracefully
        logging.error(f"Error processing event: {e}")
        return {"statusCode": 500, "body": "Internal Server Error"}