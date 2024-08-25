# import os
# import sqlite3

# def db_connector(f):

#     env = os.getenv('STREAMLIT_ENV', 'dev')
#     db_path = ''

#     if env == 'dev':
#         db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'new_record_tracker_dev.db'))
#     elif env == 'prod':
#         db_path = 'C:\\Users\\xiang\\Desktop\\Programs\\Coding\\Database\\SQLite\\db\\new_record_tracker.db'
#     else:
#         raise Exception('Unknown env')
    
#     def _with_connection(*args, **kwargs):
#         conn = sqlite3.connect(db_path)
#         try:
#             rv = f(conn, *args, **kwargs)
#         except Exception:
#             conn.rollback()
#             raise
#         else:
#             conn.commit()
#         finally:
#             conn.close()
#         return rv

#     return _with_connection
