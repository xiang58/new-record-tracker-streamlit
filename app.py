import sqlite3
import streamlit as st

con = sqlite3.connect(
    'C:\\Users\\xiang\\Desktop\\Programs\\Coding\\Database\\SQLite\\db\\new_record_tracker.db'
)
cur = con.cursor()
result = cur.execute('''
    SELECT * FROM "MyDate"
    ORDER BY "id" DESC
    LIMIT 1
''')
st.text(list(result))
