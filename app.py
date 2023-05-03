import sqlite3
import streamlit as st

con = sqlite3.connect(
    'C:\\Users\\xiang\\Desktop\\Programs\\Coding\\Database\\SQLite\\db\\new_record_tracker.db'
)
cur = con.cursor()
result = list(cur.execute('''
    SELECT * FROM "MyDate"
    ORDER BY "id" DESC
    LIMIT 1
'''))

last_date = result[0][1]
type = result[0][2]
last_date_n_type = 'Last date: {}; Type: {}'.format(last_date, type)
st.text(last_date_n_type)
