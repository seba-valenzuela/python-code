#!/bin/python3

from asyncio.windows_events import NULL
import math
import os
import random
import re
import sys
from urllib import request
import requests

#
# Complete the 'topArticles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER limit as parameter.
# base url for copy/paste:
# https://jsonmock.hackerrank.com/api/articles?page=<pageNumber>
#

url = 'https://jsonmock.hackerrank.com/api/articles?page='

def topArticles(limit):
    # Write your code here
    top_article_comments = {}
    article_names = []
    page = 1

    request = requests.get(url + str(page))
    data = request.json()['data'] # store only the data json (individual articles)
    total_pages = request.json()['total_pages']

    # Search each page
    while page <= total_pages: # so you're not searching pages with no data
        
        # create dictionary with all entries
        for article in data:
            # if the 'num_comments' section is not null, add this value to an array
            if article['num_comments'] is not None:
                # save the num_comments value tied with a unique ID ('created_at')
                top_article_comments.update({article['num_comments']:article['created_at']})
        page += 1
    
    print(top_article_comments)

    # Sort from HIGHEST to LOWEST number of comments
    sorted_comments = sorted(top_article_comments.items(), reverse=True)
    print(sorted_comments)
    
    # get the top [limit] number of comments
    top_comments_final = sorted_comments[:limit]
    print(top_comments_final)

    # store the unique IDs of these top comments
    created_by_IDs = [item[1] for item in top_comments_final]
    print(created_by_IDs)

    # Get a string of Article Names
    page = 1
    # Search each page
    # while page <= total_pages:
        for article in data:
            # if 'created_at' is an item in our list
            if article['created_at'] in created_by_IDs:
                # if the title field is not null, use 'title'
                if article['title'] is not None:
                    # add it to final list
                    # article_names.append(article['title'])
                    article_names.insert(created_by_IDs.index(article['created_at']),article['title'])
                # else, if the 'story_title' field is not null, use 'story_title'
                elif article['story_title'] is not None:
                    # article_names.append(article['story_title'])
                    article_names.insert(created_by_IDs.index(article['created_at']),article['story_title'])
                # else:
                #     print('ignore article') # if both fields are null, ignore the article
        # page += 1
    return article_names

print(topArticles(5))