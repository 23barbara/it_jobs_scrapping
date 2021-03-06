'''
this is the web scrapping file
will scrap job listings from craigslist from the Information Technology Category
and store them in a .txt file
'''

from bs4 import BeautifulSoup
import requests

# url from website
# this website contains IT job posts in the city of NY
url = 'https://newyork.craigslist.org/d/software-qa-dba-etc/search/sof'

# use requests to get the website
response = requests.get(url)

# create a soup with the html content
soup = BeautifulSoup(response.text)

# find all job posts
jobs = soup.find_all('a', class_='result-title')

# get the job titles
job_titles = [job.text for job in jobs]

# write the job openings into a text file
f = open("job_titles.txt", 'w')
for title in job_titles:
    f.write(title + '\n')
f.close()






