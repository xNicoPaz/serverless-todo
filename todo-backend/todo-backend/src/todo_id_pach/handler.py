import json
import sys
from typing import Dict
import pymysql
import sys

from db_controller import TodosModel

# Input Validation
def validate_event(event: Dict) -> Dict:
    """
    Takes event as Dict
    returns a Dict with id and todo
    """
    if not "pathParameters" in event or event["pathParameters"] is None or not "id" in event["pathParameters"]:
        raise Exception("missing ´id´ in path")

    field = event.get("pathParameters", {})
    id = int(field.get("id"))

    if not "body" in event or event["body"] is None or not "todo" in event["body"]:
        raise Exception("missing ´todo´ field")

    field = event.get("body", {})
    todo = field.split('"')[-2]

    return {"id": id, "todo": todo}


def lambda_handler(event, context):
    """
    PATCHES an entry by id from TODOS table.

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
        attributes = validate_event(event)
        id = attributes["id"]
        todo = attributes["todo"]
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

        cursor.execute('''UPDATE todo SET todo = ('%s') WHERE id=('%s')''' % (todo, id))
        cursor.connection.commit()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "id:{} updated to {}".format(id, todo)
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
        }
