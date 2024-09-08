import sqlite3

def delete_user_by_username(username):
    # Connect to the SQLite database
    conn = sqlite3.connect('task_wizard.db')
    cursor = conn.cursor()

    # SQL query to delete user by username where id is NULL
    sql_query = '''DELETE FROM registration WHERE user_name = ?'''
    
    try:
        # Execute the delete query
        cursor.execute(sql_query, (username,))
        conn.commit()
        
        # Check if any row is affected
        if cursor.rowcount > 0:
            print(f"User '{username}' has been deleted successfully.")
        else:
            print(f"No user found with username '{username}'.")
    
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the connection
        cursor.close()
        conn.close()

def delete_task_by_task_name(task_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('task_wizard.db')
    cursor = conn.cursor()

    # SQL query to delete user by username where id is NULL
    sql_query = '''DELETE FROM tasks WHERE task_name = ?'''
    
    try:
        # Execute the delete query
        cursor.execute(sql_query, (task_name,))
        conn.commit()
        
        # Check if any row is affected
        if cursor.rowcount > 0:
            print(f"User '{task_name}' has been deleted successfully.")
        else:
            print(f"No user found with username '{task_id}' where id is NULL.")
    
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the connection
        cursor.close()
        conn.close()

# # Example usage
delete_task_by_task_name('Task 1')
# delete_task_by_task_id(11)
# delete_task_by_task_id(8)

# delete_user_by_username('m@gmail.com')
# delete_user_by_username('munna')
# delete_user_by_username('muhammad')
# delete_user_by_username('ali')

import sqlite3

def delete_empty_records(db_path):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Define the query to delete empty records
    query = """
    DELETE FROM registration
    WHERE email IS NULL OR email = '';
    """

    # Execute the query
    cursor.execute(query)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

# Path to your SQLite database file
# db_path = 'path/to/your/database.db'
db_path = 'task_wizard.db'
# Call the function to delete empty records
delete_empty_records(db_path)
