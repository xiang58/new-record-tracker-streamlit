import streamlit as st
from datetime import date
import boto3
from botocore.exceptions import ClientError


import widgets as wd

def main():
    # if 'current_date' not in st.session_state:
    #     st.session_state['current_date'] = date.today()

    # wd.show_last_date()
    # wd.show_circle(st.session_state['current_date'])
    # wd.show_insert_new_rec(st.session_state['current_date'])
    # wd.show_date_heatmap()
    
    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Specify the table
    table = dynamodb.Table('new_record_tracker')

    # Query the table
    response = table.scan()

    # Print the items from the response
    st.text(response['Items'])
    


if __name__ == '__main__':
    main()
