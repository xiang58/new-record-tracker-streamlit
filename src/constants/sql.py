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

GET_ALL_RECS = 'SELECT * FROM "MyDate"'
