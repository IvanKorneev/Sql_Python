import sqlite3

class SQLer:  

    #=======================================================================================
    #                                   CONSTRUCTOR
    #=======================================================================================
    def __init__(self, db:str='', table:str='', columns:list=[], fields:list=[]):

        self.db         = db if isinstance(db, str) and len(db) > 0 else './static/data/chinook.db'
        # self.db         = db if isinstance(db, str) and len(db) > 0 else './chinook.db'
        self.table      = table if isinstance(table, str) and len(table) > 0 and self.table_exists(table) else ''
        self.columns    = columns if isinstance(columns, (list, tuple)) and len(columns) > 0 else []
        self.fields     = fields if isinstance(fields, (list, tuple)) and len(fields) > 0 else []

    #=======================================================================================
    #                                   TABLE EXISTS
    #=======================================================================================
    def table_exists(self, table:str):
        if isinstance(table, str):
            result = False
            try:
                self.connection = sqlite3.connect(self.db)
                self.connection.execute(f"SELECT * FROM {table}")
            except:
                pass
            else:
                result = True
            finally:
                if self.connection:
                    self.connection.close()
                return result

    #=======================================================================================
    #                                   SQL EXECUTE
    #=======================================================================================
    def execute_sql(self, SQL:str='', message:str=''):
        try:
            self.connection = sqlite3.connect(self.db)
            cursor = self.connection.execute(SQL)
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        else:
            if message: print(message)
        finally:
            if cursor:
                column_names = [i[0] for i in cursor.description]
                result = [dict(zip(column_names,item)) for item in cursor]
            if self.connection: self.connection.close()
            return result
            


if __name__ == "__main__":
    sql = SQLer('./static/data/my_db.db', 'COMPANY')
    result = sql.execute_sql("SELECT * FROM company")
    print(result)




