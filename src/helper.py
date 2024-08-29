import boto3
import streamlit as st


def get_dynamodb_table():
    dynamodb = boto3.resource(
        'dynamodb', region_name='us-east-1', 
        aws_access_key_id=st.secrets["aws_access_key_id"],
        aws_secret_access_key=st.secrets["aws_secret_access_key"]
    )
    return dynamodb.Table('new_record_tracker')


def get_all_recs():
    table = get_dynamodb_table()
    response = table.scan()
    items = response['Items']
    all_recs = [
        [
            int(item['date_id']), item['date_val'], int(item['date_type'])
        ] 
        for item in items
    ]
    all_recs.sort(key=lambda x: x[0])
    return all_recs


def transform_recs(all_recs, dates):
    d = {date: [] for date in dates}

    for rec in all_recs:
        date = rec[1]
        if date in d:
            d[date].append(rec[2])

    return [[compute_score(d[date]) for date in dates]]


def compute_score(recs):
    score = 0
    if not recs:
        return score
    
    date_type = 1
    if -1 in recs: date_type = -1
    elif 0 in recs: date_type = 0

    if date_type == 1:
        score = len(recs)
    elif date_type == 0:
        score = 5 + recs.count(0)
    else:
        score = 10 + recs.count(-1)

    return score
