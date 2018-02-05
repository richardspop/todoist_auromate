
from todoist.api import TodoistAPI
import datetime

def getProjID(api, name):
    projs = api.state['projects']
    for x in projs:
        if x['name'] == name:
            return x['id']
    return -1

def addTaskEveryHour(api, proj_ID, prefix):
    now = datetime.datetime.now()
    hr = now.hour + 1
    curr = hr
    prev = ""
    next = ""
    for x in range((hr + 1), 23):
        if curr > 12:
            prev = str(curr - 12) + "pm"
            next = str(x - 12) + "pm"
        elif x > 12:
            prev = str(curr)
            next = str(x - 12) + "pm"
        else:
            prev = str(curr)
            next = str(x)
        task_name = prefix + str(prev) + " to " + str(next)
        curr = x
        print task_name
        api.items.add(task_name, proj_ID, date_string="Today " + next)
    api.commit()
    return 0

if __name__ == "__main__":

    api = TodoistAPI('<token here>')
    api.sync()
    proj_ID = getProjID(api, "Personal")
    if proj_ID == -1:
        exit(-1)
    proj = api.projects.get_by_id(proj_ID)
    #print proj

    err = addTaskEveryHour(api, proj_ID, "stay in diet from ")
    if err == -1:
        exit(-1)