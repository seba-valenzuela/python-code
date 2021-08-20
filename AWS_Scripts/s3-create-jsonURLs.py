import boto3
import json
import pprint

# This program creates a json file
# with temporary URLs for bucket objects, organized by folder
# For use with javascript that generates links to bucket objects for website

# create a session to retrieve 'admin' credentials from ~/.aws/credentials
session = boto3.Session(profile_name='admin')

# use your credentials to create a low-level client with the s3 service
s3 = session.client('s3')

# Store dictionary of objects from bucket that starts with the prefix 'band-music'
response = s3.list_objects_v2(Bucket='sebavalenzuela.com', Prefix='band-music')

folder_list = []
url_json = {}

# (the value of 'Contents' is a list of dictionaries)
# For all the dictionaries in the 'Contents' list,
# IF they don't end with '/' (meaning, if its not a directory)...
for i in response['Contents']:
    if i['Key'].endswith('/') != True:

        # get the directory of the current Key, save as string in 'dir'
        full_path = i['Key']
        # this retrieves the folder after 'band-music/'
        dir = full_path.split("/")[1]
        # capitalize the directory name, updat variable
        dir = dir.capitalize()
        # this retrieves the file name
        filename = full_path.split("/")[2]

        # if the name of the directory ('dir') is not in folder_list:
        # add it to folder_list,
        # and add an item to dictionary 'url_json' where key is current 'dir' and value is empty list
        if dir not in folder_list:
            folder_list.append(dir)
            url_json[folder_list[-1]] = []

        # generate a temporary URL for the current bucket object
        url = s3.generate_presigned_url('get_object', Params={'Bucket':'sebavalenzuela.com', 'Key':i['Key']}, ExpiresIn=3600)

        # Append the newly created URL to a list in the 'url_json' dictionary,
        # whose key is the last directory in 'folder_list'
        url_json[folder_list[-1]].append(url)
