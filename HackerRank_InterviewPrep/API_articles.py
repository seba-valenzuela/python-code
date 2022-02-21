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
    article_name = []
    page = 1
    total_pages = 5

    while page <= total_pages: # so you're not searching pages with no data
        request = requests.get(url + str(page))
        data = request.json()['data'] # store only the data json (individual articles)

        if page == 1: # if you're on page 1, get the total number of pages
            total_pages = request.json()['total_pages']
        
        # create dictionary with all entries
        for article in data:
            # if the 'num_comments' section is not null, add this value to an array
            if article['num_comments'] is not None:
                # save the num_comments value tied with a unique ID, created_at
                top_article_comments.update({article['num_comments']:article['created_at']})
        page += 1
    
    sorted_comments = sorted(top_article_comments.items())
    
    top_comments_final = sorted_comments[-limit:]
    print(top_comments_final)
    created_by_IDs = [item[1] for item in top_comments_final]
    print(created_by_IDs)

    page = 1
    total_pages = 5
    # while page <= total_pages: # so you're not searching pages with no data
    #     for article in data:
    #         # if the article matches the created_at unique ID
    #         if article['created_at'] == 

    #     page += 1

    


    # next, get top articles based on limit
    # for key in top_article_comments:

    


    # ordered decreasing by comment count
    # then decreasing alphabetically for those with the same comment count
    
    # 1. Get the article name:
    #   if the title field is not null, use 'title'
    #   else, if the 'story_title' field is not null, use 'story_title'
    #   if both fields are null, ignore the article

    # 2. Sort the titles decreasing by comment count

# if __name__ == '__main__':

topArticles(5)