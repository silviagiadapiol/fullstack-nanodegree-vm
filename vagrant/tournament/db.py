import psycopg2


class DB:

    def __init__(self, db_con_str="dbname=tournament"):
        """
        Creates a database connection with the connection string provided
        :param str db_con_str: Contains the database connection string,
        with a default value when no argument is passed to the parameter
        """
        self.conn = psycopg2.connect(db_con_str)

    def cursor(self):
        """
        Returns the current cursor of the database
        """
        return self.conn.cursor()

    def execute(self, sql_query_string, and_close=False):
        """
        Executes SQL queries
        :param str sql_query_string: Contain the query string to be executed
        :param bool and_close: If true, closes the database connection after
        executing and commiting the SQL Query
        """
        cursor = self.cursor()
        cursor.execute(sql_query_string)
        if and_close:
            self.conn.commit()
            self.close()
        return {"conn": self.conn, "cursor": cursor if not and_close else None}

    def executeAndCloseConnection(self, sql_query_string):
        """
        Executes SQL queries
        :param str sql_query_string: Contain the query string to be executed
        cloding the connection at the end of execution
        """
        return self.execute(sql_query_string, True)

    def executeInsertAndCloseConnection(self, sql_query_string, sql_param):
        """
        Executes SQL queries
        :param str sql_query_string: Contain the query string to be executed
        :param str: Contain the value to insert
        executing and commiting the SQL Query
        closing the connection at the end of execution
        """
        cursor = self.cursor()
        cursor.execute(sql_query_string, sql_param)
        self.conn.commit()
        self.close()

    def close(self):
        """
        Closes the current database connection
        """
        return self.conn.close()
