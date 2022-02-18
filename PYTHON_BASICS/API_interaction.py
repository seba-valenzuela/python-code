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
            submissionCount = value['submission_count']

            # check if submissionCount is greater than threshold
            if submissionCount > threshold:
                usernames.append(value['username'])

        # go to the next page
        page += 1

    # return usernames
    return usernames

names = getUsernames(10)
print(names)