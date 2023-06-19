SQL_PATH = 'C:\\Users\\xiang\\Desktop\\Programs\\Coding\\Database\\SQLite\\db\\new_record_tracker.db'

GET_LAST_DATE = '''
    SELECT * FROM "MyDate"
    ORDER BY "id" DESC
    LIMIT 1
'''

GET_DATE_TYPE = 'SELECT "date_type" FROM "MyDate"'

ADD_DATE = '''
    INSERT INTO "MyDate" (my_date, date_type)
    VALUES (?, ?)
'''
