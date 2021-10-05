import json


def lambda_handler(event, context):
    """
    Get all stored TODOS, from TODOS table.

    Args:
        event (Dict[str, Any]): An event is a JSON-formatted document that
        contains information from the invoking service.
        When you invoke a function, you determine the structure and contents
        of the event.

        context: A context object is passed to your function by Lambda at
        runtime. This object provides methods and properties that provide
        information about the invocation, function, and runtime environment.

    Returns:
        json: with statusCode 200, and a massage with te str that was saved
        (in the HTTP response to the invocation request,
        serialized into JSON).
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
