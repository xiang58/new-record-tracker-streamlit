import streamlit as st
from datetime import date, datetime

from constants import html, misc, sql
from db_connector import db_connector

@db_connector
def get_last_record(conn):
    cur = conn.cursor()
    result = list(cur.execute(sql.GET_LAST_DATE))
    return result

def show_last_date():
    last_rec = get_last_record()
    last_date = last_rec[0][1]
    type = last_rec[0][2]
    last_date_n_type = 'Last date: {}; Type: {}'.format(last_date, type)
    st.text(last_date_n_type)

@db_connector
def show_score(conn):
    cur = conn.cursor()
    date_types = list(cur.execute(sql.GET_DATE_TYPE))
    current_score = 0
    for item in date_types:
        current_score += item[0]
    st.text('Current score: ' + str(current_score))

def show_circle(current_date):
    last_rec = get_last_record()
    last_date = datetime.strptime(last_rec[0][1], '%Y-%m-%d').date()
    date_diff = (current_date - last_date).days

    background_index = date_diff
    if date_diff < 0:
        background_index = 0
    if date_diff > 7:
        background_index = 7

    circle = html.CIRCLE.format(date_diff)
    style = html.CIRCLE_STYLE.format(misc.COLORS[background_index])
    st.markdown(circle, unsafe_allow_html=True)
    st.markdown(style, unsafe_allow_html=True)

@db_connector
def show_insert_new_rec(conn):
    cur = conn.cursor()
    last_rec = get_last_record()
    last_date = datetime.strptime(last_rec[0][1], '%Y-%m-%d').date()
    new_date = st.date_input('Pick a date:', key='current_date', min_value=last_date, max_value=date.today())
    date_type = st.selectbox('Pick a type:', ('1', '0', '-1', '2'))
    if st.button('Add Date'):
        cur.execute(sql.ADD_DATE, (new_date, date_type))
