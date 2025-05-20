import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Webhook handler triggered.")

    # Handle Microsoft Graph validation token
    validation_token = req.params.get('validationToken')
    if validation_token:
        logging.info("Validation request received.")
        return func.HttpResponse(validation_token, status_code=200, mimetype="text/plain")

    # Handle actual change notification
    try:
        body = req.get_json()
        logging.info(f"Received notification: {body}")
        # You can parse body["value"] for actual change data
        return func.HttpResponse(status_code=202)
    except Exception as e:
        logging.error(f"Error parsing request: {e}")
        return func.HttpResponse("Invalid request", status_code=400)
