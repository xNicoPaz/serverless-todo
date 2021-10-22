import json
import sys
from typing import Dict

import pymysql

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
    attribute = int(field.get("id"))
    return attribute


def lambda_handler(event, context):
    """
    Deletes entrys by id afrom TODOS table.

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
        id = validate_event(event)
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": str(e)
            }),
        }

    # Connect to sql Platform
    try:
        conn = pymysql.connect(
            user="admin",
            password="zaregoadmin",
            host="database-2.c8tf9evwzkno.us-west-2.rds.amazonaws.com",
            port=3306
        )
    except Exception as e:
        print(f"Error connecting to mysql Platform: {e}")
        sys.exit(1)

    # Get Cursor
    try:
        cursor = conn.cursor()
        cursor.execute('''USE todolist''')

        cursor.execute('''DELETE FROM todo WHERE id=('%s')''' % (id))
        cursor.connection.commit()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "´{}´ deleted from Todo-List".format(id)
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
        }
