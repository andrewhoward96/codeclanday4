from task_list import tasks




# Functions to complete:

# Get a list of uncompleted tasks


def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in tasks:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks


#print(get_uncompleted_tasks(tasks))

# Get a list of completed tasks


def get_completed_tasks(list):
    completed_tasks = []
    for task in tasks:
         if task["completed"] == True:
             completed_tasks.append(task)
    return completed_tasks


#print(get_completed_tasks(tasks))


    #  def get_completed_tasks(list):

    # Get tasks where time_taken is at least a given time




def get_tasks_taking_at_least(list, time):
    tasks_list = []
    for task in list:
         if task["time_taken"] >= time:
             tasks_list.append(task)
    return tasks_list

#print(get_tasks_taking_at_least(tasks, 30))

#def get_tasks_taking_at_least(list, time):


   

# Find a task with a given description


def get_task_with_description(list, description):
    for task in list:
        if description == task["description"]:
            return task


#print(get_task_with_description(tasks,"Feed Cat"))
    

# Extention (Function):

# Get a list of tasks by status


def get_tasks_by_status(list, status):
    task_by_status = []
    for task in list:
        if status == task["completed"]:
            task_by_status.append(task["description"])
    return task_by_status

#print(get_tasks_by_status(tasks, False))


def mark_task_complete(task):
    task["completed"] = True


def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task


def add_to_list(list, task):
    list.append(task)



