import os
from crontab import CronTab

import getpass


def get_current_cron_jobs():
    my_cron = CronTab(user=getpass.getuser())
    for job in my_cron:
        print(job)




def creating_new_cron_job(file_name, name_of_job, minute='*', hour='*', day_of_month='*', month='*', day_of_week='*'):
    # Need to check how to determine if python3 or python to be put
    my_cron = CronTab(user=getpass.getuser())
    location = os.path.join(os.getcwd(), file_name)
    job = my_cron.new(command='python3 {}'.format(location), comment=name_of_job)
    if minute != '*':
        job.minute.every(minute)
    if hour != '*':
        job.hour.every(hour)
    if day_of_month != '*':
        job.month.every(day_of_month)
    if month != "*":
        job.day.every(month)
    # if day_of_week != "*":
    my_cron.write()

def is_cron_job_present_or_not(comment):
    my_cron = CronTab(user=getpass.getuser())
    for job in my_cron:
        if job.comment == comment:
            return True
    return False


# creating_new_cron_job('cron_jobs.py', 'first_job', 1)
# get_current_cron_jobs()

print(is_cron_job_present_or_not('first_job'))