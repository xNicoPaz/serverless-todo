import json
import sys
from typing import Dict, Any
import pymysql
import sys

from cors_headers import APIHeaders
from todo_table_model import TodosModel
from request import Request

# Input Validation
def validate_event(event: Dict) -> int:
    """
    Takes event as Dict
    returns id as  int
    """
    if not "pathParameters" in event or event["pathParameters"] is None or not "id" in event["pathParameters"]:
        raise Exception("missing ´id´ in path")

    field = event.get("pathParameters", {})
    # Looks for attribute
    req = Request()
    req.id = int(field.get("id"))
    return req


def lambda_handler(event, context):
    """
    Gets an entry by id from TODOS table.

    Body:
        id field

    Args:
        event (Dict[str, Any]): An event is a JSON-formatted document that
        contains information from the invoking service.
        When you invoke a function, you determine the structure and contents
        of the event.

        context: A context object is passed to your function by Lambda at
        runtime. This object provides methods and properties that provide
        information about the invocation, function, and runtime environment.

    Returns:
        json: with all entries stored (in the HTTP response to the invocation
        request, serialized into JSON).
    """

    print(event)
    
    # Get id from event
    try:
        req: Int = validate_event(event)
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": str(e)
            }),
        }

    # Connect to sql Platform
    try:
        db = TodosModel()
    except Exception as e:
        print(f"Error connecting to DB: {e}")
        sys.exit(1)

    # Get Cursor
    try:
        cursor = db.cursor
        cursor.execute('''USE todolist''')

        cursor.execute('''SELECT * FROM todo WHERE id=('{}')'''.format(req.id))
        data = cursor.fetchall()
        items = data[0]
        message = {"id": items[0], "title": items[1], "description": items[2]}
        return {
            "statusCode": 200,
            "headers": APIHeaders.generate_headers(),
            "body": json.dumps(str(message)),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
        }
