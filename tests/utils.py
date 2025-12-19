import oracledb

def get_db_connection():
    return oracledb.connect("oracle/oracle@localhost:1521/")