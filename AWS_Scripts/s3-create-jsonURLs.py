import boto3
import json

# This program creates a json file
# with temporary URLs for bucket objects, organized by folder
# For use with javascript that generates links to bucket objects for website

# Create S3 service object that you can use to call S3 methods
s3 = boto3.resource('s3')

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
        # capitalize the directory name, update variable
        dir = dir.capitalize()
        # this retrieves the file name
        filename = full_path.split("/")[2]

        # if the name of the directory ('dir') is not in folder_list:
        # add it to folder_list,
        # and add an item to dictionary 'url_json' where key is current 'dir' and value is empty list
        if dir not in folder_list:
            folder_list.append(dir)
            url_json[folder_list[-1]] = []

        # Replace spaces in filename with "_" for URL
        filename_noSpaces = filename.replace(" ", "+")
        # Create URL
        url = "https://s3.amazonaws.com/sebavalenzuela.com/band-music/%s/%s" % (dir.lower(), filename_noSpaces)

        # create a dictionary for each bucket object
        # store the object's name (Key) and URL (value)
        object_dict = {filename_noSpaces:url}

        # Append the newly created URL to a list in the 'url_json' dictionary,
        # whose key is the last directory in 'folder_list'
        url_json[folder_list[-1]].append(object_dict)

## Create s3object, specify bucket name and new file name
s3object = s3.Object('sebavalenzuela.com', 'url_list.json')

# Create a JSON file and PUT it in the s3object
s3object.put(
    Body=(bytes(json.dumps(url_json).encode('UTF-8')))
)