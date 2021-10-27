import json
import pymysql
import sys

from db_controller import TodosModel


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

        cursor.execute('''SELECT * FROM todo''')
        message = cursor.fetchall()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": str(message)
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e)
            }),
        }
