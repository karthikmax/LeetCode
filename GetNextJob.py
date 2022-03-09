
def getNextJob (limit,runningjobs,pendingjobs):
    '''
    `running`: dict(name, scheduled_start_ts) - dict of jobs that are currently running, eg. {'test1': 1570476917, 'test2': 1570476817}
  `pending`: dict(name, scheduled_start_ts) - dict of jobs that have yet to run, eg. {'test3': 1570476988, 'test4': 1570476919}
	`name`: string - name of the job
	`scheduled_start_ts`: int - epoch timestamp of the time that the job is scheduled to run
  `limit`: int - maximum number of running job


    Function to fetch next job from a dictionary. Return none if limit is met else return the next job. Asked in an interview
    '''

    lengthofrunning = len(runningjobs)
    
    if lengthofrunning == limit:
        nextJob = None
    else:
        for k,v in pending.items():
            if v == min(pending.values()):
                nextJob = k
    
    return nextJob

running = {'test1': 1570476917, 'test2': 1570476817}
pending =  {'test3': 1570476988, 'test4': 1570476919}
limit = 3
result = getNextJob(limit,running,pending)
print(result)