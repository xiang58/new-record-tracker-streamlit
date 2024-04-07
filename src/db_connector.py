import sqlite3

from constants import sql

def db_connector(f):
    
    def _with_connection(*args, **kwargs):
        conn = sqlite3.connect(sql.SQL_PATH)
        try:
            rv = f(conn, *args, **kwargs)
        except Exception:
            conn.rollback()
            raise
        else:
            conn.commit()
        finally:
            conn.close()
        return rv

    return _with_connection
