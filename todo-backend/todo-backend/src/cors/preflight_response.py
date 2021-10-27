import json

from cors_headers import APIHeaders


def lambda_handler(event, context):
    """
    This is a function to enable CORS policy
     Args:
        event (Dict[str, Any]): An event is a JSON-formatted document that
        contains information from the invoking service.
        When you invoke a function, you determine the structure and contents
        of the event.
        context: A context object is passed to your function by Lambda at
        runtime. This object provides methods and properties that provide
        information about the invocation, function, and runtime environment.
    Returns
        Json with statusCode 200 and headers with allow_headers:"Content-Type",
        allow_origin:"*", allow_methods:"OPTIONS,POST,GET"
    """
    return {
        'statusCode': 200,
        'headers': APIHeaders.generate_headers(),
        'body': json.dumps('Hello from Lambda!')
    }
