import os.path
import sqlite3

def db_connector(f):
    
    def _with_connection(*args, **kwargs):
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'new_record_tracker.db'))
        conn = sqlite3.connect(db_path)
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
