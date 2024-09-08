# import sqlite3 
from sqlite3 import *
from flet import *


# conn = connect("task_wizard.db")
conn = connect("task_wizard.db", check_same_thread=False, timeout=10)

# Create a Cursor:
c = conn.cursor()
# Create the `registration` table
c.execute("""
CREATE TABLE IF NOT EXISTS registration (
    id INTEGER UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    user_name TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL,
    security_qna TEXT UNIQUE NOT NULL
)
""")

# Create the `tasks` table
c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    task_description TEXT,
    task_priority TEXT,
    task_status TEXT,
    deadline DATE,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES registration(id)
)
""")

# Commit changes and close the connection
conn.commit()

# Example color constants
PRIMARY_COLOR = "#2FF924"  # Green
SECONDARY_COLOR = "#FFC107"  # Yellow
ACCENT_COLOR = "#03A9F4"  # Blue
BACKGROUND_COLOR = "#FFFFFF"  # White
TEXT_COLOR = "#212121"  # Dark Gray
ERROR_COLOR = "#FF2400"  # Red


class TaskWizardApp:
    def __init__(self, page: Page):
        self.tasks = []
        self.page = page
        self.page.title = "Task Wizard"
        self.page.bgcolor = BACKGROUND_COLOR  # White background for the whole page
        self.show_home_page()
        self.db_connection = connect("task_wizard.db", timeout=10)
        self.db_cursor = self.db_connection.cursor()


    def show_home_page(self):
        title = Text(
            value="Task Wizard",
            color=PRIMARY_COLOR,  # Green text color for the title
            size=40,
            weight="bold",
            text_align=TextAlign.CENTER
        )

        self.page.add(
            Container(
                content=title,
                alignment=alignment.center,
                expand=True  # Ensures the container takes full height and width of the page
            )
        )

        import time
        time.sleep(3)
        self.show_login_page()

    def forget_password_page(self):
        self.page.clean()
        
        # Display the "Forget Password" heading
        self.page.add(Container(
            content=Text(
                value="Forget Password Page",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color=TEXT_COLOR
            ),
            alignment=alignment.center,
            bgcolor=PRIMARY_COLOR,  # Green background for the heading
            padding=20
        ))

        # Text fields for email and security question
        email_input = TextField(label="Write your Registered Email", width=330)
        question_input = TextField(label="What is the most Favourite Thing you have?", width=330)

        def check_credentials(e):
            email = email_input.value
            question = question_input.value
            
            # Connect to your database and perform the query
            try:
                # Assuming you've already set up the database connection
                c.execute("SELECT id FROM registration WHERE email=? AND security_qna=?", (email, question))
                user_data = c.fetchone()
                
                # Check if any fields are empty
                if not email or not question:
                    self.page.snack_bar = SnackBar(content=Text("Fill all fields!", color="White"))
                    self.page.snack_bar.open = True
                    self.page.update()

                if user_data:
                    user_id = user_data[0]  # Fetch user id from the database
                    self.show_dashboard(user_id)  # Pass the user id to the dashboard page

                else :
                    self.page.snack_bar = SnackBar(content=Text("Invalid username or password!", color="White"))
                    self.page.snack_bar.open = True
                    self.page.update()
                
                user_data = self.get_user_data(email, question)  # Your function to fetch user data
            
            except Error as e:
                self.page.add(Text(f"Database Error: {e}", color="RED"))
            

        # Create the form layout
        login_form = Column(
            [
                Container(height=60),  # Spacer
                Text(value="Answer the Question\n And You Get the Account Access", text_align="center", font_family="Roboto", weight="Bold", size=20),
                Container(height=10),  # Spacer
                email_input,
                Container(height=10),  # Spacer
                question_input,
                Container(height=20),  # Spacer
                ElevatedButton(
                    content=Text("Login", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=PRIMARY_COLOR,  # Green background for the button
                    on_click=check_credentials  # Call the function to check credentials
                ),
                Container(height=20),  # Spacer
                TextButton(text="Back to Login Page", on_click=lambda _: self.show_login_page())
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        # Add the form to the page
        self.page.add(Container(
            content=login_form,
            alignment=alignment.center,
            bgcolor=BACKGROUND_COLOR,  # White background for the form container
            expand=True,
            padding=20
        ))


    def show_registration_page(self):
        self.page.clean()
        # Main heading at the top of the page (in blue)
        self.page.add(Container(
            content=Text(
                value="Register Page",
                style="headlineMedium",
                size=30,
                weight="bold",
                font_family="Roboto",
                text_align="center",
                color=TEXT_COLOR
            ),
            alignment=alignment.center,
            bgcolor=ACCENT_COLOR,  # Blue background only for the heading
            padding=20
        ))

        fullname_field = TextField(label='Full Name', width=330)
        username_field = TextField(label="Username", width=330)
        email_field = TextField(label="Email", width=330)
        password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)
        ask_field = TextField(label="What is the most Favourite Thing you have?", width=330)
        userid = TextField(label="Write the Unique Id for User", width=330)

        # Registration form with all fields and buttons
        registration_form = Column(
            [
                # Text(value="Create an Account", style="headlineMedium", text_align="center", font_family="Roboto", weight="Bold"),
                Container(height=10),  # Spacer
                fullname_field,
                Container(height=10),  # Spacer
                username_field,
                Container(height=10),  # Spacer
                email_field,
                Container(height=10),  # Spacer
                password_field,
                Container(height=10),  # Spacer
                ask_field,
                Container(height=10),  # Spacer
                userid,
                Container(height=10),  # Spacer
                ElevatedButton(
                    content=Text("Register", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=ACCENT_COLOR,
                    on_click=lambda _: self.handle_registration(
                        userid.value,
                        fullname_field.value, 
                        username_field.value, 
                        email_field.value, 
                        password_field.value, 
                        ask_field.value,
                    )
                ),
                Container(height=10),  # Spacer
                TextButton(content=Text("Back to Login", weight="bold"), on_click=lambda _: self.show_login_page())
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        # Add registration form to the page
        self.page.add(Container(
            content=registration_form,
            alignment=alignment.center,
            bgcolor=BACKGROUND_COLOR,  # White background for the form container
            expand=True,
            padding=20
        ))

    # def handle_registration(self, full_name, user_name, email, password, security_qna):
    #     try:
    #         # Inserting data into the registration table
    #         c.execute('''
    #             INSERT INTO registration (full_name, user_name, email, password, security_qna)
    #             VALUES (?, ?, ?, ?, ?)
    #         ''', (full_name, user_name, email, password, security_qna))
    #         user_data = c.fetchone()

    #         # Commit changes to the database
    #         conn.commit()
    
    #         self.page.add(SnackBar(Text("Registration successful!", color=PRIMARY_COLOR, bgcolor=TEXT_COLOR)))
    #         self.page.snack_bar.open = True
    #         self.page.update()
    #         # self.show_dashboard(user_id)
        
    #     except IntegrityError:
    #         self.page.add(Text(value="Error: Username or Email already exists!", color=ERROR_COLOR))

    #     if user_data:
    #         user_id = user_data[0]  # Fetch user id from the database
    #         self.show_dashboard(user_id)  # Pass the user id to the dashboard page

    #     else :
    #         self.page.snack_bar = SnackBar(content=Text("Invalid username or password!", color="White"))
    #         self.page.snack_bar.open = True
    #         self.page.update()
            
    #     user_data = self.get_user_data(password)  # Your function to fetch user data
    def handle_registration(self, userid, full_name, user_name, email, password, security_qna):
        try:
            conn = connect('task_wizard.db')
            c = conn.cursor()
            # Insert data into the registration table
            c.execute('''
                INSERT INTO registration (id, full_name, user_name, email, password, security_qna)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (userid, full_name, user_name, email, password, security_qna))
            
            # Commit changes to the database
            conn.commit()
            
            # Fetch the newly inserted user ID
            # user_id = c.lastrowid  # Use lastrowid to get the ID of the last inserted row

            # Show success Snackbar
            self.page.add(SnackBar(Text("Registration successful!", color=PRIMARY_COLOR, bgcolor=TEXT_COLOR, open=True)))
            # self.page.snack_bar.open = True
            self.page.update()
            self.show_dashboard(userid)

            # Clear fields after registration
            self.clear_fields()

            # Redirect to dashboard
        
        except IntegrityError:
            self.page.add(SnackBar(Text(value="Error: Username or Email already exists!", color=ERROR_COLOR, open=True)))
            # self.page.snack_bar.open = True
            self.page.update()
    
    def clear_fields(self):
        # Clear the input fields on the registration page
        self.fullname_field.value = ""
        self.username_field.value = ""
        self.email_field.value = ""
        self.password_field.value = ""
        self.ask_field.value = ""
        self.userid = ""

        #####################################################################################
        # SHOW DASHBOARD PAGE WITH USER ID , CHECK LOGIC ON LOGIN PAGE
        #####################################################################################
    def get_user_data(self, username, password):
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            return c.fetchone()
        except Error as e:
            print(f"Error fetching user data: {e}")
            return None


    
    def show_login_page(self):
        self.page.clean()

        # Main heading at the top of the page (in green)
        self.page.add(Container(
            content=Text(
                value="Welcome to Task Wizard",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color=TEXT_COLOR
            ),
            alignment=alignment.center,
            bgcolor=PRIMARY_COLOR,  # Green background only for the heading
            padding=20
        ))

        self.username_field = TextField(label="Username", width=330)
        self.password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)

        login_form = Column(
            [
                Container(height=60),  # Spacer
                Text(value="Login", color=TEXT_COLOR, style="headlineMedium", text_align="center", font_family="Roboto",
                     weight="Bold"),
                Container(height=10),  # Spacer
                self.username_field,
                Container(height=10),  # Spacer
                self.password_field,
                TextButton(text="Forget Password?", on_click=lambda _: self.forget_password_page()),
                ElevatedButton(
                    content=Text("Login", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=PRIMARY_COLOR,  # Green background for the button
                    on_click=lambda e: self.handle_login()
                ),
                Container(height=20),  # Spacer
                Text(value="Don't have an account?", size=16, text_align="center", color='DARK_BLUE'),
                ElevatedButton(
                    content=Text("Sign Up", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=ACCENT_COLOR,  # Blue background for the button
                    on_click=lambda _: self.show_registration_page()
                ),
                # Container(height=10),  # Spacer
                # TextButton(content=Text("See User Dashboard", weight="bold"),
                #            on_click=lambda _: self.show_dashboard())
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        self.page.add(Container(
            content=login_form,
            alignment=alignment.center,
            bgcolor=BACKGROUND_COLOR,  # White background for the form container
            expand=True,
            padding=20
        ))
        
    def show_dashboard(self, user_id):
        self.page.clean()
        
        # Make this in read task function because it fetch data on this page :
        # # Fetch user-specific tasks from the database
        try:
            conn = connect('task_wizard.db', timeout=10)  
            c = conn.cursor()

            # Query to fetch tasks specific to the logged-in user
            c.execute("SELECT task_name, task_status FROM tasks WHERE user_id=?", (user_id,))
            tasks = c.fetchall()

            if tasks:
                task_list = []
                for task in tasks:
                    task_name, task_status = task
                    task_list.append(Text(f"Task: {task_name}, Status: {task_status}", color="#212121", size=18))
                
                task_display = Column(task_list, alignment=MainAxisAlignment.CENTER)

            else:
                task_display = Text("No tasks available for this user.", color="#212121", size=18)

        except Error as e:
            task_display = Text(f"Error fetching tasks: {e}", color="RED")
        
        finally:
            conn.close()

        # Add heading and display user tasks
        self.page.add(Container(
            content=Text(
                value=f"Task Wizard Dashboard -{user_id}",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color="#FFFFFF",
            ),
            alignment=alignment.center,
            bgcolor=ACCENT_COLOR,  # Green background only for the heading
            padding=20
        ))

        welcome_message = Text(
            value="Manage your tasks efficiently",
            color="#212121",  # Dark Gray text color
            size=18,
            weight="BOLD",
            text_align=TextAlign.CENTER
        )
####################################################################################################
####################################################################################################
        # Add buttons for other task management features (CRUD)
        add_task_button = ElevatedButton(
            content=Text("Add Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor=ACCENT_COLOR,  # Blue background
            on_click=lambda _: self.show_add_task_form(user_id)
        )

        update_task_button = ElevatedButton(
            content=Text("Update Task", weight="bold"),
            width=300,
            color="#FFFFFF", 
            bgcolor=ACCENT_COLOR,  # Yellow background
            on_click=lambda _: self.show_update_task_form(user_id)
        )

        read_task_button = ElevatedButton(
            content = Text("Read All Task", weight="bold"),
            width = 300, 
            color = "#FFFFFF",
            bgcolor = ACCENT_COLOR,
            on_click=lambda _: self.show_read_tasks_page(user_id)
        )

        delete_task_button = ElevatedButton(
            content=Text("Delete Task", weight="bold"),
            width=300,
            color="#FFFFFF", 
            bgcolor=ACCENT_COLOR,  # Red background
            on_click=lambda _: self.show_delete_task_form(user_id)
        )
####################################################################################################
####################################################################################################

        BTN = TextButton(text="Back to Login", on_click=lambda _: self.show_login_page())

        # Arrange buttons in a column
        dashboard_buttons = Column(
            [
                add_task_button,     # Add Task Button 
                Container(height=10),
                read_task_button,    # Read All Task Button
                Container(height=10),
                update_task_button,  # Update Specific Button
                Container(height=10),
                delete_task_button,  # Delete Specific Task Button
                Container(height=10),
                BTN
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        # Add everything to the page
        self.page.add(
            Container(
                content=Column(
                    [Container(height=20), welcome_message, Container(height=30), dashboard_buttons],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    expand=True
                ),
                alignment=alignment.center,
                expand=True,
                padding=20
            )
        )
    
    def handle_login(self):
        username = self.username_field.value
        password = self.password_field.value
        
        try:
            # Open the database connection
            conn = connect('task_wizard.db')  # Replace with your actual DB file path
            c = conn.cursor()
            
            # Query to find the user in the database
            c.execute("SELECT id FROM registration WHERE user_name=? AND password=?", (username, password))
            user_data = c.fetchone()
            
            # Check if any fields are empty
            if not username or not password:
                self.page.snack_bar = SnackBar(content=Text("Fill all fields!", color="White"))
                self.page.snack_bar.open = True
                self.page.update()

            if user_data:
                user_id = user_data[0]  # Fetch user id from the database
                self.show_dashboard(user_id)  # Pass the user id to the dashboard page

            else :
                self.page.snack_bar = SnackBar(content=Text("Invalid username or password!", color="White"))
                self.page.snack_bar.open = True
                self.page.update()
            
            # This below has an error occured 
            # user_data = self.get_user_data(username, password)  # Your function to fetch user data
        
        except Error as e:
            self.page.add(Text(f"Database Error: {e}", color="RED"))

        finally:
            conn.close()  # Close the database connection

    ################################################################################################################
    # CRUD Functionality of App Written Here 
    ################################################################################################################
#     def show_add_task_form(self, user_id):
#         self.page.clean()

#         self.page.add(Container(
#             content=Text(
#                 value="Add Task Page",
#                 style="headlineMedium",
#                 size=30,
#                 weight="BOLD",
#                 font_family="Roboto",
#                 text_align="center",
#                 color="#FFFFFF"
#             ),
#             alignment=alignment.center,
#             bgcolor=ACCENT_COLOR,  # Green background only for the heading
#             padding=20
#         ))

#         def add_task(e):
#             task_name = task_name_input.value.strip()
#             task_description = task_description_input.value.strip()
#             task_priority = task_priority_input.value.strip()
#             task_status = task_status_input.value.strip()
#             task_deadline = task_deadline_input.value.strip()

#             # Check if any of the fields are empty
#             if not task_name or not task_description or not task_priority or not task_status or not task_deadline:
#                 self.page.snack_bar = SnackBar(Text("All fields are required!"), open=True)
#             else:
#                 self.tasks.append({
#                     'name': task_name,
#                     'description': task_description,
#                     'priority': task_priority,
#                     'status': task_status,
#                     'deadline': task_deadline
#                 })
#                 self.page.snack_bar = SnackBar(Text("Task Added Successfully!"), open=True)
#                 self.show_dashboard(user_id)
# # # Create the `tasks` table:
# # c.execute("""CREATE TABLE IF NOT EXISTS tasks (
# #     task_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     task_name TEXT NOT NULL,
# #     task_description TEXT,
# #     task_priority TEXT,
# #     task_status TEXT,
# #     deadline DATE,
# #     user_id INTEGER,
# #     FOREIGN KEY (user_id) REFERENCES registration(id)
# # )
# # """)
# # conn.commit()

#         task_name_input = TextField(label="Task Name", width=330)
#         task_description_input = TextField(label="Task Description", width=330)
#         task_priority_input = TextField(label="Task Priority", width=330)
#         task_status_input = TextField(label="Task Status", width=330)
#         task_deadline_input = TextField(label="Task Deadline", width=330)

#         submit_button = ElevatedButton(
#             content=Text("Add Task"),
#             bgcolor=PRIMARY_COLOR,  # Green background
#             color="#FFFFFF",
#             on_click=add_task
#         )

#         back_to_dashboard_button = ElevatedButton(
#             content=Text("Back to Dashboard"),
#             bgcolor="#03A9F4",  # Blue background
#             color="#FFFFFF",
#             # on_click=lambda e: self.show_user_dashboard_page()
#             on_click=lambda e: self.show_dashboard(user_id)
#         )

#         self.page.add(
#             Column(
#                 [
#                     # Text(value="Add Task", size=24, weight="bold"),
#                     Container(height=50),
#                     task_name_input,
#                     Container(height=10),
#                     task_description_input,
#                     Container(height=10),
#                     task_priority_input,
#                     Container(height=10),
#                     task_status_input,
#                     Container(height=10),
#                     task_deadline_input,
#                     Container(height=20),
#                     submit_button,
#                     Container(height=20),
#                     back_to_dashboard_button
#                 ],
#                 alignment=MainAxisAlignment.CENTER,
#                 horizontal_alignment=CrossAxisAlignment.CENTER,
#                 expand=True
#             )
#         )

# Assuming `conn` and `c` are your database connection and cursor:

    def show_add_task_form(self, user_id):
        self.page.clean()
        conn = connect('task_wizard.db', timeout=10)
        c = conn.cursor()

        self.page.add(Container(
            content=Text(
                value="Add Task Page",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color="#FFFFFF"
            ),
            alignment=alignment.center,
            bgcolor=ACCENT_COLOR,  # Green background only for the heading
            padding=20
        ))

        def add_task(e):
            task_name = task_name_input.value.strip()
            task_description = task_description_input.value.strip()
            task_priority = task_priority_input.value.strip()
            task_status = task_status_input.value.strip()
            task_deadline = task_deadline_input.value.strip()

            # Check if any of the fields are empty
            if not task_name or not task_description or not task_priority or not task_status or not task_deadline:
                self.page.snack_bar = SnackBar(Text("All fields are required!"), open=True)
            else:
                try:
                    # Insert the task into the tasks table
                    c.execute("""
                        INSERT INTO tasks (task_name, task_description, task_priority, task_status, deadline, user_id)
                        VALUES (?, ?, ?, ?, ?, ?)""",
                        (task_name, task_description, task_priority, task_status, task_deadline, user_id)
                    )
                    conn.commit()  # Commit the transaction
                    c.execute("PRAGMA foreign_keys = ON")
                    print(f"Task Name: {task_name}, Task Description: {task_description}, Task Priority: {task_priority}, Task Status: {task_status}, Task Deadline: {task_deadline}, User ID: {user_id}")

                    # self.page.snack_bar = SnackBar(Text("Task Added Successfully!"), open=True)
                    self.page.overlay.append(SnackBar(Text("Task Added Successfully!")))
                    self.show_dashboard(user_id)

                except Error as error:
                    # Log the error for debugging
                    print(f"Error occurred: {error}")
                    # self.page.add(snack_bar = SnackBar(Text(f"Database Error: {error}"), open=True))
                    # page.overlay.append(snack_bar)
                except Exception as e:
                    # Log unexpected errors
                    print(f"An unexpected error occurred: {e}")
                    self.page.snack_bar = SnackBar(Text(f"Error: {e}"), open=True)

        # Input fields
        task_name_input = TextField(label="Task Name", width=330)
        task_description_input = TextField(label="Task Description", width=330)
        task_priority_input = TextField(label="Task Priority", width=330)
        task_status_input = TextField(label="Task Status", width=330)
        task_deadline_input = TextField(label="Task Deadline (YYYY-MM-DD)", width=330)

        submit_button = ElevatedButton(
            content=Text("Add Task"),
            bgcolor=PRIMARY_COLOR,  # Green background
            color="#FFFFFF",
            on_click=add_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard(user_id)
        )

        self.page.add(
            Column(
                [
                    Container(height=50),
                    task_name_input,
                    Container(height=10),
                    task_description_input,
                    Container(height=10),
                    task_priority_input,
                    Container(height=10),
                    task_status_input,
                    Container(height=10),
                    task_deadline_input,
                    Container(height=20),
                    submit_button,
                    Container(height=20),
                    back_to_dashboard_button
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True
            )
        )

# # Create the `tasks` table:
# c.execute("""CREATE TABLE IF NOT EXISTS tasks (
#     task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     task_name TEXT NOT NULL,
#     task_description TEXT,
#     task_priority TEXT,
#     task_status TEXT,
#     deadline DATE,
#     user_id INTEGER,
#     FOREIGN KEY (user_id) REFERENCES registration(id)
# )
# """)
# conn.commit()



    
    # def show_read_tasks_page(self, user_id):
    #     self.page.clean()

    #     # Header
    #     header = Container(
    #         content=Text(
    #             value="Display All Task Page",
    #             style="headlineMedium",
    #             size=30,
    #             weight="BOLD",
    #             font_family="Roboto",
    #             text_align="center",
    #             color="white"
    #         ),
    #         alignment=alignment.center,
    #         bgcolor="green",  # Replace with ACCENT_COLOR if defined
    #         padding=20,
    #     )

    #     task_items = []

    #     # Check if there are any tasks to display
    #     if not self.tasks:
    #         no_task_message = Container(
    #             content=Text("No tasks found.", color="#F44336", size=16),
    #             alignment=alignment.center,
    #             expand=True
    #         )
    #         task_items.append(no_task_message)
    #     else:
    #         for task in self.tasks:
    #             # Determine the background color based on priority
    #             if task['priority'].lower() == 'high':
    #                 bg_color = colors.RED
    #             elif task['priority'].lower() == 'medium':
    #                 bg_color = PRIMARY_COLOR
    #             elif task['priority'].lower() == 'low':
    #                 bg_color = colors.LIGHT_BLUE
    #             else:
    #                 bg_color = colors.GREY  # Default background color

    #             # Create a card for each task
    #             task_container = Container(
    #                 content=Column([
    #                     Text(f"Task: {task['name']}", color="white", weight="bold"),
    #                     Text(f"Description: {task['description']}", color="white" , weight="bold" ),
    #                     Text(f"Task Priority: {task['priority']}", color="white", weight="bold"),
    #                     Text(f"Task Status: {task['status']}", color="white", weight="bold"),
    #                     Text(f"Task Deadline: {task['deadline']}", color="white", weight="bold")
    #                 ]),
    #                 padding=10,
    #                 border=border.all(1, color=colors.BLACK),
    #                 border_radius=8,
    #                 bgcolor=bg_color,
    #                 width=290,  # Adjust width as needed
    #                 height=200  # Adjust height as needed
    #             )

    #             task_items.append(task_container)

    #     # Responsive handling: Adjust the number of cards per row
    #     def update_layout(event=None):
    #         screen_width = self.page.window_width

    #         if screen_width < 600:  # Mobile
    #             cards_per_row = 2
    #         elif screen_width < 1200:  # Tablet or smaller laptop screens
    #             cards_per_row = 3
    #         else:  # Desktop or larger screens
    #             cards_per_row = 5

    #         # Create rows with cards per row based on screen size
    #         rows = []
    #         for i in range(0, len(task_items), cards_per_row):
    #             rows.append(Row(task_items[i:i+cards_per_row], spacing=15))  # Adjust spacing as needed

    #         # Scrollable content including the tasks and the button
    #         scrollable_content = Column(
    #             rows,
    #             spacing=20,
    #             alignment=MainAxisAlignment.CENTER,
    #             horizontal_alignment=CrossAxisAlignment.CENTER,
    #             scroll="auto"  # Enable vertical scrolling
    #         )

    #         # Clear and re-add the elements to update the layout
    #         self.page.clean()
    #         self.page.add(
    #             Column(
    #                 [
    #                     header,
    #                     scrollable_content,
    #                     back_to_dashboard_button  # This will always be centered at the bottom
    #                 ],
    #                 expand=True,
    #                 alignment=MainAxisAlignment.CENTER,
    #                 scroll="auto"  # Ensure the entire page is scrollable
    #             )
    #         )

    #     # Back to Dashboard Button, centered within a Container
    #     back_to_dashboard_button = Container(
    #         content=ElevatedButton(
    #             content=Text("Back to Dashboard"),
    #             bgcolor="#03A9F4",  # Blue background
    #             color="#FFFFFF",
    #             on_click=lambda e: self.show_dashboard(user_id)
    #         ),
    #         alignment=alignment.center,
    #         padding=10
    #     )

    #     # Initial layout update
    #     update_layout()

    #     # Add a listener to update the layout on screen resize
    #     self.page.on_resize = update_layout

    ## This below code is correctly working but the task is not displaying, as the task is being saved in database.

    # def show_read_tasks_page(self, user_id):
    #     self.page.clean()

    #     # Header
    #     header = Container(
    #         content=Text(
    #             value="Display All Task Page",
    #             style="headlineMedium",
    #             size=30,
    #             weight="BOLD",
    #             font_family="Roboto",
    #             text_align="center",
    #             color="white"
    #         ),
    #         alignment=alignment.center,
    #         bgcolor="green",  # Replace with ACCENT_COLOR if defined
    #         padding=20,
    #     )

    #     task_items = []

    #     # Fetch tasks filtered by the user_id
    #     user_tasks = self.get_tasks_by_user(user_id)

    #     # Check if there are any tasks to display
    #     if not user_tasks:
    #         no_task_message = Container(
    #             content=Text("No tasks found.", color="#F44336", size=16),
    #             alignment=alignment.center,
    #             expand=True
    #         )
    #         task_items.append(no_task_message)
    #     else:
    #         for task in user_tasks:
    #             print(f"Task: {task}")  # Print task to see structure

    #             # Check if the task belongs to the current user (filtering)
    #             if task['user_id'] == user_id:
    #                 # Determine the background color based on priority
    #                 if task['priority'].lower() == 'high':
    #                     bg_color = colors.RED
    #                 elif task['priority'].lower() == 'medium':
    #                     bg_color = PRIMARY_COLOR
    #                 elif task['priority'].lower() == 'low':
    #                     bg_color = colors.LIGHT_BLUE
    #                 else:
    #                     bg_color = colors.GREY  # Default background color
                
    #             if 'user_id' not in task:
    #                 print(f"Task missing 'user_id' key: {task}")
    #             elif task['user_id'] == user_id:
    #                 print(f"Task belongs to user {user_id}: {task}")
    #                 # Determine the background color and display the task
    #             else:
    #                 print(f"Task does not belong to user {user_id}: {task}")

    #             # Create a card for each task
    #             task_container = Container(
    #                 content=Column([
    #                     Text(f"Task: {task['name']}", color="white", weight="bold"),
    #                     Text(f"Description: {task['description']}", color="white" , weight="bold"),
    #                     Text(f"Task Priority: {task['priority']}", color="white", weight="bold"),
    #                     Text(f"Task Status: {task['status']}", color="white", weight="bold"),
    #                     Text(f"Task Deadline: {task['deadline']}", color="white", weight="bold")
    #                     ]),
    #                     padding=10,
    #                     border=border.all(1, color=colors.BLACK),
    #                     border_radius=8,
    #                     bgcolor=bg_color,
    #                     width=290,  # Adjust width as needed
    #                     height=200  # Adjust height as needed
    #                 )

    #             task_items.append(task_container)
    def show_read_tasks_page(self, user_id):
        self.page.clean()

        # Header
        header = Container(
            content=Text(
                value="Display All Task Page",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color="white"
            ),
            alignment=alignment.center,
            bgcolor="green",  # Replace with ACCENT_COLOR if defined
            padding=20,
        )

        task_items = []

        # Fetch tasks filtered by the user_id
        user_tasks = self.get_tasks_by_user(user_id)
        print(f"User Tasks for {user_id}: {user_tasks}")  # Debug tasks

        # Check if there are any tasks to display
        if not user_tasks:
            no_task_message = Container(
                content=Text("No tasks found.", color="#F44336", size=16),
                alignment=alignment.center,
                expand=True
            )
            task_items.append(no_task_message)
        else:
            for task in user_tasks:
                print(f"Task: {task}")  # Debug task structure
                # if 'user_id' not in task:
                #     print(f"Task missing 'user_id' key: {task}")
                # elif task['user_id'] == user_id:
                #     print(f"Task belongs to user {user_id}: {task}")
                if 'user_id' in task:
                    print(f'Task Belongs to user {user_id}: {task}')


                    # Determine the background color based on priority
                    if task['priority'].lower() == 'high':
                        bg_color = colors.RED
                    elif task['priority'].lower() == 'medium':
                        bg_color = PRIMARY_COLOR
                    elif task['priority'].lower() == 'low':
                        bg_color = colors.LIGHT_BLUE
                    else:
                        bg_color = colors.GREY  # Default background color

                    # Create a card for each task
                    task_container = Container(
                        content=Column([
                            Text(f"Task: {task['name']}", color="white", weight="bold"),
                            Text(f"Description: {task['description']}", color="white", weight="bold"),
                            Text(f"Task Priority: {task['priority']}", color="white", weight="bold"),
                            Text(f"Task Status: {task['status']}", color="white", weight="bold"),
                            Text(f"Task Deadline: {task['deadline']}", color="white", weight="bold")
                        ]),
                        padding=10,
                        border=border.all(1, color=colors.BLACK),
                        border_radius=8,
                        bgcolor=bg_color,
                        width=290,  # Adjust width as needed
                        height=200  # Adjust height as needed
                    )

                    task_items.append(task_container)
                    self.page.add(task_container)
                    self.page.update()
                    
        # Back to Dashboard Button, centered within a Container
        back_to_dashboard_button = Container(
            content=ElevatedButton(
                content=Text("Back to Dashboard"),
                bgcolor="#03A9F4",  # Blue background
                color="#FFFFFF",
                on_click=lambda e: self.show_dashboard(user_id)
            ),
            alignment=alignment.center,
            padding=10
        )

        # Define the update_layout function before calling it
        def update_layout(event=None):
            screen_width = self.page.window_width

            if screen_width < 600:  # Mobile
                cards_per_row = 2
            elif screen_width < 1200:  # Tablet or smaller laptop screens
                cards_per_row = 3
            else:  # Desktop or larger screens
                cards_per_row = 5

            # Create rows with cards per row based on screen size
            rows = []
            for i in range(0, len(task_items), cards_per_row):
                rows.append(Row(task_items[i:i+cards_per_row], spacing=15))  # Adjust spacing as needed

            # Scrollable content including the tasks and the button
            scrollable_content = Column(
                rows,
                spacing=20,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                scroll="auto"  # Enable vertical scrolling
            )

            # Clear and re-add the elements to update the layout
            self.page.clean()
            self.page.add(
                Column(
                    [
                        header,
                        scrollable_content,
                        back_to_dashboard_button  # This will always be centered at the bottom
                    ],
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    scroll="auto"  # Ensure the entire page is scrollable
                )
            )

        # Initial layout update
        update_layout()

        # Add a listener to update the layout on screen resize
        self.page.on_resize = update_layout
# ###########################################################################################################
# NEW FUNCTION ADDED BELOW: 
# ###########################################################################################################
     # Function to create a new task
    def create_task(self, task_data):
        user_id = task_data.get('user_id')
        
        # Ensure user_id is valid
        if not user_id:
            raise ValueError("User ID is required to create a task")

        # SQL query to insert the task data into the database
        query = """
        INSERT INTO tasks (user_id, name, description, priority, status, deadline)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        
        # The values to insert
        values = (
            user_id,
            task_data['name'],
            task_data['description'],
            task_data['priority'],
            task_data['status'],
            task_data['deadline']
        )
        
        # Execute the query using your database connection
        self.db.execute(query, values)


    def show_update_task_form(self, user_id):
        self.page.clean()

        self.page.add(Container(
            content=Text(
                value="Update Specific Task with Detail",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color=TEXT_COLOR
            ),
            alignment=alignment.center,
            bgcolor=ACCENT_COLOR,  # Green background only for the heading
            padding=20
        ))

        def update_task(e):
            task_name = task_name_input.value
            new_description = new_task_description_input.value
            new_priority = new_task_priority_input.value
            new_status = new_task_status_input.value
            new_deadline = new_task_deadline_input.value
            # Check if any of the fields are empty
            if not task_name or not new_description or not new_priority or not new_status or not new_deadline:
                self.page.snack_bar = SnackBar(Text("All fields are required!"), open=True)

            for task in self.tasks:
                if task['name'] == task_name:
                    task['description'] = new_description
                    task['priority'] = new_priority
                    task['status'] = new_status
                    task['deadline'] = new_deadline
                    self.page.snack_bar = SnackBar(Text("Task Updated Successfully!"), open=True)
                    break
            else:
                self.page.snack_bar = SnackBar(Text("Task Not Found!"), open=True)
            self.show_dashboard(user_id)

        task_name_input = TextField(label="Task Name" , width=330)
        new_task_description_input = TextField(label="New Task Description", width=330)
        new_task_priority_input = TextField(label="New Task Priority", width=330)
        new_task_status_input = TextField(label="New Task Status", width=330)
        new_task_deadline_input = TextField(label="New Task Deadline", width=330)

        submit_button = ElevatedButton(
            content=Text("Update Task", weight='bold'),
            # color=TEXT_COLOR, 
            color="#FFFFFF", 
            bgcolor=PRIMARY_COLOR,  # Green background
            on_click=update_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            # on_click=lambda e: self.show_user_dashboard_page()
            on_click=lambda e: self.show_dashboard(user_id)
        )

        self.page.add(
            Column(
                [
                    Container(height=40),
                    task_name_input,
                    Container(height=10),
                    new_task_description_input,
                    Container(height=10),
                    new_task_priority_input,
                    Container(height=10),
                    new_task_status_input,
                    Container(height=10),
                    new_task_deadline_input,
                    Container(height=10),
                    submit_button,
                    Container(height=20),
                    back_to_dashboard_button
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True
            )
        )

    def show_delete_task_form(self, user_id):
        self.page.clean()

        self.page.add(Container(
            content=Text(
                value="Delete Task",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color=TEXT_COLOR
            ),
            alignment=alignment.center,
            bgcolor=ERROR_COLOR,  # Green background only for the heading
            padding=20
        ))

        def delete_task(e):
            task_name = task_name_input.value
            for task in self.tasks:
                if task['name'] == task_name:
                    self.tasks.remove(task)
                    self.page.snack_bar = SnackBar(Text("Task Deleted Successfully!"), open=True)
                    break
            else:
                self.page.snack_bar = SnackBar(Text("Task Not Found!"), open=True)
            self.show_dashboard(user_id)

        task_name_input = TextField(label="Task Name", width=330)

        submit_button = ElevatedButton(
            content=Text("Delete Task"),
            bgcolor=ERROR_COLOR,  # Red background
            color="#FFFFFF",
            on_click=delete_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            # on_click=lambda e: self.show_user_dashboard_page()
            on_click=lambda e: self.show_dashboard(user_id)
        )

        self.page.add(
            Column(
                [
                    # Text(value="Delete Task", size=24, weight="bold"),
                    Container(height=40),
                    task_name_input,
                    Container(height=10),
                    submit_button,
                    Container(height=20),
                    back_to_dashboard_button
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True
            )
        )
    def get_tasks_by_user(self, user_id):
        # Fetch tasks filtered by user_id from the database
        c.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        tasks = c.fetchall()
        # Convert your database rows to dictionaries or modify as needed
        return [{"name": row[1], "description": row[2], "priority": row[3], "status": row[4], "deadline": row[5]} for row in tasks]



# Start the Flet app:
def main(page: Page):
    app = TaskWizardApp(page)

app(target=main)
