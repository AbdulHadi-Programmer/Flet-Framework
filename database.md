1. Registration Table:
FULL_NAME |  USER_NAME  | EMAIL          | PASSWORD | SECURITY_QUESTION  |
Abc       |  abc012     | abc@gmail.com  | 123      | Python             |

2. Task Table:
| TASK_NAME   | TASK_DESCRIPTION          | TASK_PRIORITY  | TASK_STATUS  | TASK_DEADLINE
| Task Wizard | Project to make for Group | High           | in progress  | 06/09/2024

- 1 Table for each user that is the task table -- This is a good option becuase each user is separated from one another.
- 1 Table contain all members task detail but in that we have to write the full_name or id to connect.


# This function is use to store the new user detail into database
def add_new_user():
    pass

# For Login Page Authentication
def check_the_registered_user():
    pass

# Make a task Table 
# One to Many Relationship -- 1 task table that contain all user task detail with thier specific keys.
def add_task_to_specific_user():
    pass

# Filter Task by User Id :
# this function can be furthur used by display all tasks page.
def filter_task_by_user():
    pass

# Null , Integer, Blob, Real, Text
