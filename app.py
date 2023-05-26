import sqlite3
import streamlit as st
from datetime import date, datetime

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

date_types = list(cur.execute('''
    SELECT "date_type" FROM "MyDate"
'''))
current_score = 0
for item in date_types:
    current_score += item[0]
st.text('Current score: ' + str(current_score))

today = datetime.today()
last_date = datetime.strptime(last_date, '%Y-%m-%d')
date_diff = (today - last_date).days
circle = '<div class="circle"><b>{}</b></div>'.format(date_diff)
style = """
<style>
    .circle {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #d3e607;
        text-align: center;
        font-size: larger;
        line-height: 50px;
        color: rgb(0, 0, 0);
        float: left;
        margin: 25px 0 0px 50px;
    }
</style>
"""
st.markdown(circle, unsafe_allow_html=True)
st.markdown(style, unsafe_allow_html=True)

new_date = st.date_input('Pick a date:', date.today())
date_type = st.selectbox('Pick a type:', ('1', '0', '-1', '2'))
if st.button('Add Date'):
    cur.execute('''
        INSERT INTO "MyDate" (my_date, date_type)
        VALUES (?, ?)
    ''', (new_date, date_type))
    con.commit()
