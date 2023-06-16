import sqlite3
import streamlit as st
from constants import html, misc, sql
from datetime import date, datetime

def main():
    if 'current_date' not in st.session_state:
        st.session_state['current_date'] = date.today()

    con = sqlite3.connect(sql.SQL_PATH)
    cur = con.cursor()
    result = list(cur.execute(sql.GET_LAST_DATE))

    last_date = result[0][1]
    type = result[0][2]
    last_date_n_type = 'Last date: {}; Type: {}'.format(last_date, type)
    st.text(last_date_n_type)

    date_types = list(cur.execute(sql.GET_DATE_TYPE))
    current_score = 0
    for item in date_types:
        current_score += item[0]
    st.text('Current score: ' + str(current_score))

    last_date = datetime.strptime(last_date, '%Y-%m-%d').date()
    date_diff = (st.session_state['current_date'] - last_date).days
    background_index = date_diff
    if date_diff < 0:
        background_index = 0
    if date_diff > 7:
        background_index = 7

    circle = html.CIRCLE.format(date_diff)
    style = html.CIRCLE_STYLE.format(misc.COLORS[background_index])
    st.markdown(circle, unsafe_allow_html=True)
    st.markdown(style, unsafe_allow_html=True)

    new_date = st.date_input('Pick a date:', key='current_date', min_value=last_date, max_value=date.today())
    date_type = st.selectbox('Pick a type:', ('1', '0', '-1', '2'))
    if st.button('Add Date'):
        cur.execute(sql.ADD_DATE, (new_date, date_type))
        con.commit()

if __name__ == '__main__':
    main()
