#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys


def crawl(url, depth, maxDepth, visited=None):
    """
    Given an absolute URL, print each hyperlink found within the document.

    Your task is to make this into a recursive function that keeps following
    links until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached

    You will need to change this function's signature to fulfill this
    assignment.
    """

    try:
        if visited is None:
            visited = set({})
        if depth > maxDepth: #base case
            return
        for i in range(depth):
            print("\t", end ='')
        print(url)
        #print("\tTODO: Print this URL with indentation indicating the depth of recursion")
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return 

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)
                
                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    URLparsed = urlparse(absoluteURL)
                    myLink = URLparsed.scheme + "://" + URLparsed.netloc + URLparsed.path + URLparsed.params + URLparsed.query
                    if myLink not in visited:
                        visited.add(myLink)
                        crawl(myLink, depth + 1, maxDepth, visited)
    # This is for if it has been visited already or doesn't start with https. Loop again.

        #print("\n\tTODO: Don't just print URLs found in this document, visit them!")
        #print("\tTODO: Trim fragments ('#' to the end) from URLs")
        #print("\tTODO: Use a data structure to track whether you've already visited a URL")
        #print("\tTODO: Call crawl() on unvisited newly formed URLs")
        #print("\tTODO: Don't visit a URL if you've reached the max depth of recursion")

    except Exception as e:
        print(f"crawl(): {e}")
    return


## An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
else:
    url = sys.argv[1]

parsed = urlparse(url)
if parsed.scheme == '' or parsed.netloc == '':
    print("Error: Invalid URL supplied.\nPlease supply an absolute URL to this program")
    sys.exit(2)

## The user may override the default recursion depth of 3
maxDepth = 3
if len(sys.argv) > 2:
    maxDepth = int(sys.argv[2])

plural = 's'
if maxDepth == 1:
    plural = ''
depth = 0
print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
crawl(url, depth, maxDepth)
