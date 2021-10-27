import json
import sys
from typing import Dict
import pymysql
import sys

from db_controller import TodosModel

# Input Validation
def validate_event(event: Dict) -> str:
    """
    Takes event as a Dict
    returns email as a str
    """
    if not "body" in event or event["body"] is None or not "todo" in event["body"]:
        raise Exception("missing ´todo´ field")

    field = event.get("body", {})
    # Looks for attribute
    attribute = field.split('"')[-2]
    if attribute == "":
        raise Exception("field ´todo´ cant be empty")
    return attribute


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
        todo = validate_event(event)
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
        cursor.execute('''use todolist''')

        cursor.execute('''INSERT INTO todo(todo) values('%s')''' % (todo))
        cursor.connection.commit()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "´{}´ added to Todo-List".format(todo)
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
        }
