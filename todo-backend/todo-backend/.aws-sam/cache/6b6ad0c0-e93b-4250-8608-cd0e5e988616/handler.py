import json
import pymysql
import sys


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
        print("hello imports didnt crash")
        conn = pymysql.connect(
            user="admin",
            password="zaregoadmin",
            host="database-2.c8tf9evwzkno.us-west-2.rds.amazonaws.com",
            port=3306
        )
    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cursor = conn.cursor()
    cursor.execute('''use todolist''')

    sql = '''select * from todo'''
    cursor.execute(sql)
    message = cursor.fetchall()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": str(message)
        }),
    }
