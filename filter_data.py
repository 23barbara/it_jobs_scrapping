'''
this file serves to filter and organize
relevant jobs from the job titles gathered from craigslist
'''


jobs_collection = [] # stores jobs found from scrapping

# make a string of each line and add to collection
f = open('job_titles.txt', 'r')
for line in f:
    jobs_collection.append(str(line).lower())
f.close()


# create a function that finds all jobs with specific key_word and
# returns job posts with the given input keyword
def job_category(keyword):
    results = []
    keyword = str(keyword)
    
    # search by job post
    for job in jobs_collection:
        # split job words into an auxiliary list
        aux = job.split()
        if keyword in aux:
            results.append(job)   # if job contains keyword, store in result
    return results


# organize jobs into lists for each category
data_jobs = job_category('data') + job_category('analyst')
software_jobs = job_category('software')
web_jobs = job_category('web') + job_category('developer')































