from datetime import date, datetime, timedelta

import plotly.graph_objects as go
import streamlit as st

from constants import html, misc
from helper import get_dynamodb_table, transform_recs


def show_last_date(all_recs):
    last_rec = all_recs[-1]
    last_date = last_rec[1]
    type = last_rec[2]
    last_date_n_type = 'Last date: {}; Type: {}'.format(last_date, type)
    st.text(last_date_n_type)


def show_circle(all_recs, current_date):
    last_rec = all_recs[-1]
    last_date = datetime.strptime(last_rec[1], '%Y-%m-%d').date()
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


def show_insert_new_rec(all_recs, current_date):
    last_rec = all_recs[-1]
    last_date = datetime.strptime(last_rec[1], '%Y-%m-%d').date()
    new_date = st.date_input('Pick a date:', key='current_date', value=current_date, min_value=last_date, max_value=date.today())
    date_type = st.selectbox('Pick a type:', ('1', '0', '-1'))
    st.button('Add Date', on_click=add_date, args=(all_recs, new_date, date_type))
        

def add_date(all_recs, new_date, date_type):
    new_id = len(all_recs) + 1
    item = {
        'date_id': new_id,
        'date_val': str(new_date),
        'date_type': date_type
    }

    table = get_dynamodb_table()
    response = table.put_item(Item=item)

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        st.toast("Item inserted successfully!", icon='🎉')
    else:
        st.toast("Error inserting item:" + str(response), icon='🚨')


def show_date_heatmap(all_recs):
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
    