# import boto3
# import pandas as pd
# from decouple import config
# from io import StringIO
# #
# dic = {
#     'fname': ['Kay', 'Kola', 'Kazim'],
#     'lname': ['Flaming', 'Fash', 'Flenjo'],
#     'Salary': [2000, 2500, 3000]
# }
#
# df = pd.DataFrame(dic)
#
#
# # def create_bucket(df, bucket_name, file_name):
# #     s3 = boto3.client('s3')
# #     s3.create_bucket(Bucket=bucket_name)
# #     s3.upload_file(file_name, bucket_name, file_name)
# #     print(f"{file_name} uploaded to S3 bucket {bucket_name}")
# #
#
# def create_bucket(df, bucket_name, file_name):
#     s3 = boto3.client('s3', aws_access_key_id='access_key', aws_secret_access_key='secret_key')
#     # s3 = boto3.client('s3')
#     # csv_buffer = StringIO()
#     # df.to_csv(csv_buffer, index=False)
#     # s3.create_bucket(Bucket=bucket_name)
#     # s3.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
#     # print(f"{file_name} uploaded to S3 bucket {bucket_name}")
#
#     s3_client = boto3.client('s3')
#     s3_client.create_bucket(Bucket=bucket_name)
#     csv_buffer = StringIO()
#     df.to_csv(csv_buffer, index=False)
#     s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
#     print(f'File "{file_name}" uploaded to bucket "{bucket_name}"')
#
#
# # Define the bucket name and file name
# bucket_name = 'styco2590'
# file_name = 'my-file.csv'
#
# # # Create an S3 client
# # s3_client = boto3.client('s3')
# #
# # # Create the S3 bucket
# # s3_client.create_bucket(Bucket=bucket_name)
# #
# # # Define the data to write to the CSV file
# # # data = {'name': ['John', 'Jane', 'Bob'], 'age': [30, 25, 40]}
# # # df = pd.DataFrame(data)
# #
# # # Convert the dataframe to CSV format
# # csv_buffer = StringIO()
# # df.to_csv(csv_buffer, index=False)
# #
# # # Upload the CSV file to the S3 bucket
# # s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())
# #
# # print(f'File "{file_name}" uploaded to bucket "{bucket_name}"')
#
# # secret_key = config("secret_access_key")
# # access_key = config("access_key_id")
#
# # bucket_name = 'styco2590'
# # file_name = 'house_p.csv'
#
# create_bucket(df, 'styco2590', 'my-file.csv')

import boto3
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# bucket_name = "uk-naija-testing-testing"

def create_s3_bucket(bucket_name):
    """
    Creates an S3 bucket with the given name
    """
    # Create an S3 client
    s3 = boto3.resource('s3',
                        aws_access_key_id=os.getenv('access_key_id'),
                        aws_secret_access_key=os.getenv("secret_access_key"))
    #s3 = boto3.resource('s3')

    # Create the bucket
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})

    print(f'S3 bucket {bucket_name} created successfully')

s3testing = create_s3_bucket("apesticococos2309je03")
#print(s3testing)
