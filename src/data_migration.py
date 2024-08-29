import boto3
import json
import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('C:\\Users\\xiang\\Desktop\\Programs\\Coding\\Database\\SQLite\\db\\new_record_tracker.db')
# cursor = conn.cursor()

# # Query all data from the table
# cursor.execute("SELECT * FROM mydate")
# rows = cursor.fetchall()

# # Get column names
# column_names = [description[0] for description in cursor.description]

# # Create a list of dictionaries
# data = [dict(zip(column_names, row)) for row in rows]

# # Write data to a JSON file
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)

# # Close the connection
# conn.close()

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Reference the table
table = dynamodb.Table('new_record_tracker')

# Batch write data
with table.batch_writer() as batch:
    for item in data:
        batch.put_item(Item=item)

