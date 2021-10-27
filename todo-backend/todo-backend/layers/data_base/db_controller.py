import pymysql


class TodosModel:
    """
    model for todos-table
    """
    def __init__(self):
        # create database connection
        conn = pymysql.connect(
            user="admin",
            password="zaregoadmin",
            host="database-2.ceel3tfeb3zg.us-west-2.rds.amazonaws.com",
            port=3306
        )
        self.cursor = conn.cursor()
        pass

    @classmethod
    def start_database(self):
        # connect database
        cursor = self.cursor
        # create db
        cursor.execute('''create database todolist''')
        cursor.connection.commit()
        cursor.execute('''use todolist''')
        sql = '''
        create table todo (
        id int not null auto_increment,
        title text,
        description,
        primary key (id)
        )'''
        cursor.execute(sql)
        cursor.connection.commit()
        return
