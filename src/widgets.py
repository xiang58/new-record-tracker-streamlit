import plotly.graph_objects as go
import streamlit as st
import time
from datetime import date, datetime, timedelta

from constants import html, misc, sql
from db_connector import db_connector
from helper import transform_recs


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


def show_insert_new_rec():
    last_rec = get_last_record()
    last_date = datetime.strptime(last_rec[0][1], '%Y-%m-%d').date()
    new_date = st.date_input('Pick a date:', key='current_date', min_value=last_date, max_value=date.today())
    date_type = st.selectbox('Pick a type:', ('1', '0', '-1'))
    st.button('Add Date', on_click=add_date, args=(new_date, date_type))
        

@db_connector
def add_date(conn, new_date, date_type):
    cur = conn.cursor()
    cur.execute(sql.ADD_DATE, (new_date, date_type))


@db_connector
def get_all_recs(conn):
    cur = conn.cursor()
    result = list(cur.execute(sql.GET_ALL_RECS))
    return result


def show_date_heatmap():
    all_recs = get_all_recs()
    first_day = datetime.strptime(all_recs[0][1], '%Y-%m-%d').date()
    today = datetime.today().date()
    num_days = (today - first_day).days + 1

    dates = [(today - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(num_days, -1, -1)]
    z = transform_recs(all_recs, dates)
    colorscale = [
        [0, 'rgb(255, 255, 255)'], 
        [1/15, 'rgb(193, 247, 195)'], [2/15, 'rgb(153, 232, 156)'], [3/15, 'rgb(90, 199, 93)'], [4/15, 'rgb(46, 171, 50)'], [5/15, 'rgb(15, 145, 19)'],
        [6/15, 'rgb(252, 231, 154)'], [7/15, 'rgb(227, 197, 89)'], [8/15, 'rgb(204, 169, 45)'], [9/15, 'rgb(171, 137, 12)'], [10/15, 'rgb(138, 107, 1)'],
        [11/15, 'rgb(252, 189, 189)'], [12/15, 'rgb(232, 146, 146)'], [13/15, 'rgb(212, 83, 83)'], [14/15, 'rgb(196, 29, 29)'], [1, 'rgb(158, 2, 2)'],
    ]

    fig = go.Figure(data=go.Heatmap(x=dates, y=[''], z=z, zmin=0, zmax=15, colorscale=colorscale))

    fig.update_layout(title='Sample')

    st.plotly_chart(fig, theme="streamlit")
    