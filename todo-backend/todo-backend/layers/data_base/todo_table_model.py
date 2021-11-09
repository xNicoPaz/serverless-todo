import pymysql
import boto3
import json


def get_secret():
    """
    Access to SecretManager

    Returns:
         json: value of SecretString
    """
    secret_name = "TODO-Secrets"
    region_name = "us-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    response = client.get_secret_value(
        SecretId=secret_name
    )
    return json.loads(response["SecretString"])


class TodosModel:
    """
    model for todos-table
    """
    def __init__(self):

        sec = get_secret()

        # create database connection
        conn = pymysql.connect(
            user=sec["username"],
            password=sec["password"],
            host=sec["host"],
            port=sec["port"]
        )
        self.cursor = conn.cursor()

    def start_database(self):
        # connect database
        cursor = self.cursor
        # create db
        cursor.execute('''drop database todolist''')
        cursor.connection.commit()
        cursor.execute('''create database todolist''')
        cursor.connection.commit()
        cursor.execute('''use todolist''')
        sql = '''
        create table todo (
        id int not null auto_increment,
        title text,
        description text,
        primary key (id)
        )'''
        cursor.execute(sql)
        cursor.connection.commit()
        return "ok"
