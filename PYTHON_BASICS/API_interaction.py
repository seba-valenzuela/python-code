import requests
import json

# HackerRank - Get usernames higher than a specified threshold

def getUsernames(threshold):
    # set variables
    usernames = []
    page = 1
    totalPages = 1

    while page <= totalPages: # so you're not searching pages with no data
        # make request for each page
        apiRequest = requests.get('https://jsonmock.hackerrank.com/api/article_users/search?page=' + str(page))
        articles = apiRequest.json()['data']

        # set totalPages value
        if page == 1:
            totalPages = apiRequest.json()['total_pages']
    
        # get data for each user
        for value in articles:
            # this means: "look at the 'submission count' data in each user (articles)"
            submissionCount = value['submission_count']

            # check if submissionCount is greater than threshold
            if submissionCount > threshold:
                usernames.append(value['username'])

        # go to the next page
        page += 1

    # return usernames
    return usernames

names = getUsernames(1000)
print(names)
print()


# Corey Schafer: xkcd python

r = requests.get('https://xkcd.com/353/')
# print(dir(r))     # this will show you all the "attributes and methods you can get through this response object"
# print(help(r))    # more detailed explanation of everything from this object
# print(r.text)     # this displays the page as HTML text
# print(r. content) # you can download an image like this (represented in bytes)
# print(r. headers) # Headers

# Test Queries with httpbin.org!
payload = {'page': 2, 'count': 25}
# create a "requests get" object with specific parameters
httpbin = requests.get('https://httpbin.org/get', params=payload)


print(httpbin.url)



