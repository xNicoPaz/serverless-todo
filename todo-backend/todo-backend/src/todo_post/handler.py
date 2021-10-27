import json
import sys
from typing import Dict
import pymysql
import sys

from cors_headers import APIHeaders
from todo_table_model import TodosModel
from request import Request

# Input Validation
def validate_event(event: Dict) -> Request:
    """
    Takes event as a Dict
    returns email as a str
    """
    if not "body" in event or event["body"] is None or not "title" in event["body"]:
        raise Exception("missing ´title´ field")

    if not "description" in event["body"]:
        raise Exception("missing ´description´ field")

    field = event.get("body", {})
    print(field)
    # Looks for attribute
    title = field.split('"')[3]
    description = field.split('"')[-2]

    if title == "":
        raise Exception("field ´title´ cant be empty")
    if description == "":
        raise Exception("field ´description´ cant be empty")

    # Looks for attribute
    req = Request()
    req.title, req.description = title, description
    return req


def lambda_handler(event, context):
    """
    records a entry to TODOS table.

    QueryString:
        takes a TODOMassage as a QS to ve stored in the table

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
    # Get STR from event
    try:
        req = validate_event(event)
    except Exception as e:
        return {
            "statusCode": 400,
            "headers": APIHeaders.generate_headers(),
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
        cursor.execute('''use todolist''')

        cursor.execute('''INSERT INTO todo(title, description) VALUES ('%s', '%s')''' %
                       (req.title, req.description,))
        cursor.connection.commit()

        return {
            "statusCode": 200,
            "headers": APIHeaders.generate_headers(),
            "body": json.dumps({
                "message": "´{}´ added to Todo-List".format(req.title)
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
        }
