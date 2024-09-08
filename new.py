# from flet import *

# # Example color constants
# PRIMARY_COLOR = "#2FF924"  # Green
# SECONDARY_COLOR = "#FFC107"  # Yellow
# ACCENT_COLOR = "#03A9F4"  # Blue
# BACKGROUND_COLOR = "#FFFFFF"  # White
# TEXT_COLOR = "#212121"  # Dark Gray
# ERROR_COLOR = "#FF2400"  # Red


# class TaskWizardApp:
#     def __init__(self, page: Page):
#         self.page = page
#         self.page.title = "Task Wizard"
#         self.page.bgcolor = BACKGROUND_COLOR  # White background for the whole page
#         self.show_home_page()

#     def show_home_page(self):
#         home_page = HomePage(self.page, self)
#         home_page.display()

#     def show_login_page(self):
#         login_page = LoginPage(self.page, self)
#         login_page.display()

#     def show_registration_page(self):
#         registration_page = RegistrationPage(self.page, self)
#         registration_page.display()

#     def show_admin_login_page(self):
#         admin_login_page = AdminLoginPage(self.page, self)
#         admin_login_page.display()

#     # def show_user_dashboard_page(self):
#     #     user_dashboard_page = UserDashboardPage(self.page, self)
#     #     user_dashboard_page.display()

#     def show_forget_password_page(self):
#         forget_password_page = ForgetPasswordPage(self.page, self)
#         forget_password_page.display()

#     def handle_login(self, username, password):
#         print(f"Login attempt for {username}")
#         # Your login logic here

#     def handle_registration(self, username, email, password):
#         print(f"Registering user {username} with email {email}")
#         # Your registration logic here

#     def handle_admin_login(self, admin_username, admin_password):
#         print(f"Admin login with username {admin_username}")
#         # Your admin login logic here


# class HomePage:
#     def __init__(self, page: Page, app: TaskWizardApp):
#         self.page = page
#         self.app = app

#     def display(self):
#         self.page.clean()
#         title = Text(
#             value="Task Wizard",
#             color=PRIMARY_COLOR,  # Green text color for the title
#             size=40,
#             weight="bold",
#             text_align=TextAlign.CENTER
#         )

#         self.page.add(
#             Container(
#                 content=title,
#                 alignment=alignment.center,
#                 expand=True  # Ensures the container takes full height and width of the page
#             )
#         )

#         import time
#         time.sleep(3)
#         self.app.show_login_page()


# class LoginPage:
#     def __init__(self, page: Page, app: TaskWizardApp):
#         self.page = page
#         self.app = app

#     def display(self):
#         self.page.clean()
#         # Main heading at the top of the page (in green)
#         self.page.add(Container(
#             content=Text(
#                 value="Welcome to Task Wizard",
#                 style="headlineMedium",
#                 size=30,
#                 weight="BOLD",
#                 font_family="Roboto",
#                 text_align="center",
#                 color=TEXT_COLOR
#             ),
#             alignment=alignment.center,
#             bgcolor=PRIMARY_COLOR,  # Green background only for the heading
#             padding=20
#         ))

#         username_field = TextField(label="Username", width=330)
#         password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)

#         login_form = Column(
#             [
#                 Container(height=60),  # Spacer
#                 Text(value="Login", color=TEXT_COLOR, style="headlineMedium", text_align="center", font_family="Roboto",
#                      weight="Bold"),
#                 Container(height=10),  # Spacer
#                 username_field,
#                 Container(height=10),  # Spacer
#                 password_field,
#                 TextButton(text="Forget Password?", on_click=lambda _: self.app.show_forget_password_page()),
#                 ElevatedButton(
#                     content=Text("Login", weight="bold"),
#                     width=150,
#                     color=TEXT_COLOR,
#                     bgcolor=PRIMARY_COLOR,  # Green background for the button
#                     on_click=lambda e: self.app.handle_login(username_field.value, password_field.value)
#                 ),
#                 Container(height=20),  # Spacer
#                 Text(value="Don't have an account?", size=16, text_align="center", color='DARK_BLUE'),
#                 ElevatedButton(
#                     content=Text("Sign Up", weight="bold"),
#                     width=150,
#                     color=TEXT_COLOR,
#                     bgcolor=ACCENT_COLOR,  # Blue background for the button
#                     on_click=lambda _: self.app.show_registration_page()
#                 ),
#                 Container(height=10),  # Spacer
#                 ElevatedButton(
#                     content=Text("Admin", weight="bold"),
#                     width=150,
#                     color=TEXT_COLOR,
#                     bgcolor=ERROR_COLOR,  # Red background for the button
#                     on_click=lambda _: self.app.show_admin_login_page(),
#                 ),
#                 TextButton(content=Text("See User Dashboard", weight="bold"),
#                            on_click=lambda _: self.app.show_user_dashboard_page())
#             ],
#             alignment=MainAxisAlignment.CENTER,
#             horizontal_alignment=CrossAxisAlignment.CENTER,
#             expand=True
#         )

#         self.page.add(Container(
#             content=login_form,
#             alignment=alignment.center,
#             bgcolor=BACKGROUND_COLOR,  # White background for the form container
#             expand=True,
#             padding=20
#         ))


# class RegistrationPage:
#     def __init__(self, page: Page, app: TaskWizardApp):
#         self.page = page
#         self.app = app

#     def display(self):
#         self.page.clean()
#         # Main heading at the top of the page (in blue)
#         self.page.add(Container(
#             content=Text(
#                 value="Register Page",
#                 style="headlineMedium",
#                 size=30,
#                 weight="bold",
#                 font_family="Roboto",
#                 text_align="center",
#                 color=TEXT_COLOR
#             ),
#             alignment=alignment.center,
#             bgcolor=ACCENT_COLOR,  # Blue background only for the heading
#             padding=20
#         ))

#         fullname_field = TextField(label='Full Name', width=330)
#         username_field = TextField(label="Username", width=330)
#         email_field = TextField(label="Email", width=330)
#         password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)
#         ask_field = TextField(label="What is the most Favourite Thing you have?", width=330)

#         registration_form = Column(
#             [
#                 Text(value="Create an Account", style="headlineMedium", text_align="center", font_family="Roboto",
#                      weight="Bold"),
#                 Container(height=10),  # Spacer
#                 fullname_field,
#                 Container(height=10),  # Spacer
#                 username_field,
#                 Container(height=10),  # Spacer
#                 email_field,
#                 Container(height=10),  # Spacer
#                 password_field,
#                 Container(height=10),  # Spacer
#                 ask_field,
#                 Container(height=20),  # Spacer
#                 ElevatedButton(
#                     content=Text("Register", weight="bold"),
#                     width=150,
#                     color=TEXT_COLOR,
#                     bgcolor=ACCENT_COLOR,  # Blue background for the button
#                     on_click=lambda e: self.app.handle_registration(username_field.value, email_field.value,
#                                                                      password_field.value)
#                 ),
#                 Container(height=15),  # Spacer
#                 TextButton(content=Text("Back to Login", weight="bold"),
#                            on_click=lambda _: self.app.show_login_page())
#             ],
#             alignment=MainAxisAlignment.CENTER,
#             horizontal_alignment=CrossAxisAlignment.CENTER,
#             expand=True
#         )

#         self.page.add(Container(
#             content=registration_form,
#             alignment=alignment.center,
#             bgcolor=BACKGROUND_COLOR,  # White background for the form container
#             expand=True
#         ))


# class AdminLoginPage:
#     def __init__(self, page: Page, app: TaskWizardApp):
#         self.page = page
#         self.app = app

#     def display(self):
#         self.page.clean()
#         # Main heading at the top of the page (in red)
#         self.page.add(Container(
#             content=Text(
#                 value="Admin Page",
#                 style="headlineMedium",
#                 size=30,
#                 weight="bold",
#                 font_family="Roboto",
#                 text_align="center",
#                 color=TEXT_COLOR
#             ),
#             alignment=alignment.center,
#             bgcolor=ERROR_COLOR,  # Red background only for the heading
#             padding=20,
#         ))

#         admin_username_field = TextField(label="Admin Username", width=330)
#         admin_password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)

#         admin_login_form = Column(
#             [
#                 Text(value="Admin", style="headlineMedium", text_align="center", font_family="Roboto", weight="Bold"),
#                 Container(height=10),
#                 admin_username_field,
#                 Container(height=10),
#                 admin_password_field,
#                 Container(height=20),
#                 ElevatedButton(content=Text("Admin", weight="bold"),
#                               width=150,
#                               color=TEXT_COLOR,
#                               bgcolor=ERROR_COLOR,  # Red background for the button
#                               on_click=lambda e: self.app.handle_admin_login(admin_username_field.value,
#                                                                              admin_password_field.value)
#                               ),
#                 Container(height=10),
#                 ElevatedButton(content=Text("Back to Login", weight="bold"),
#                               width=150,
#                               color=TEXT_COLOR,
#                               bgcolor=ACCENT_COLOR,  # Blue background for the button
#                               on_click=lambda _: self.app.show_login_page()
#                               )
#             ],
#             alignment=MainAxisAlignment.CENTER,
#             horizontal_alignment=CrossAxisAlignment.CENTER,
#             expand=True
#         )

#         self.page.add(Container(
#             content=admin_login_form,
#             alignment=alignment.center,
#             bgcolor=BACKGROUND_COLOR,  # White background for the form container
#             expand=True
#         ))


# class ForgetPasswordPage:
#     def __init__(self, page: Page, app: TaskWizardApp):
#         self.page = page
#         self.app = app

#     def display(self):
#         self.page.clean()
#         # Main heading at the top of the page (in red)
#         self.page.add(Container(
#             content=Text(
#                 value="Forget Password",
#                 style="headlineMedium",
#                 size=30,
#                 weight="bold",
#                 font_family="Roboto",
#                 text_align="center",
#                 color=TEXT_COLOR
#             ),
#             alignment=alignment.center,
#             bgcolor=ERROR_COLOR,  # Red background only for the heading
#             padding=20
#         ))

#         email_field = TextField(label="Email", width=330)
#         secret_key_field = TextField(label="Secret Key", width=330)

#         forget_password_form = Column(
#             [
#                 Text(value="Enter Your Details", style="headlineMedium", text_align="center", font_family="Roboto",
#                      weight="Bold"),
#                 Container(height=10),  # Spacer
#                 email_field,
#                 Container(height=10),  # Spacer
#                 secret_key_field,
#                 Container(height=20),  # Spacer
#                 ElevatedButton(
#                     content=Text("Submit", weight="bold"),
#                     width=150,
#                     color=TEXT_COLOR,
#                     bgcolor=PRIMARY_COLOR,  # Green background for the button
#                     # Add on_click event to handle forget password logic
#                 ),
#                 Container(height=15),  # Spacer
#                 TextButton(content=Text("Back to Login", weight="bold"),
#                            on_click=lambda _: self.app.show_login_page())
#             ],
#             alignment=MainAxisAlignment.CENTER,
#             horizontal_alignment=CrossAxisAlignment.CENTER,
#             expand=True
#         )

#         self.page.add(Container(
#             content=forget_password_form,
#             alignment=alignment.center,
#             bgcolor=BACKGROUND_COLOR,  # White background for the form container
#             expand=True
#         ))


# def main(page:Page):
#     TaskWizardApp(page).show_home_page()



#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
from flet import *

class TaskWizardDashboard:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Task Wizard Dashboard"
        self.page.bgcolor = "#FFFFFF"  # White background

        self.tasks = []  # Initialize an empty list for tasks

        self.show_dashboard()

    def show_dashboard(self):
        self.page.clean()

        title = Text(
            value="Task Wizard Dashboard",
            color="#03A9F4",  # Blue text color
            size=30,
            weight="bold",
            # bgcolor="#008000",  
            text_align=TextAlign.CENTER,
            # expand=True
        )

        welcome_message = Text(
            value="Manage your tasks efficiently",
            color="#212121",  # Dark Gray text color
            size=18,
            text_align=TextAlign.CENTER
        )

        # Buttons for CRUD operations
        add_task_button = ElevatedButton(
            content=Text("Add Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor="#4CAF50",  # Green background
            on_click=lambda e: self.show_add_task_form()
        )

        read_tasks_button = ElevatedButton(
            content=Text("Read All Tasks", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor="#03A9F4",  # Blue background
            on_click=lambda e: self.show_read_tasks_page()
        )

        update_task_button = ElevatedButton(
            content=Text("Update Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor="#FFC107",  # Yellow background
            on_click=lambda e: self.show_update_task_form()
        )

        delete_task_button = ElevatedButton(
            content=Text("Delete Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor="#F44336",  # Red background
            on_click=lambda e: self.show_delete_task_form()
        )

        # Arrange buttons in a column
        dashboard_buttons = Column(
            [
                add_task_button,
                Container(height=10),
                read_tasks_button,
                Container(height=10),
                update_task_button,
                Container(height=10),
                delete_task_button
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        # Add everything to the page
        self.page.add(
            Container(
                content=Column(
                    [title, Container(height=20), welcome_message, Container(height=50), dashboard_buttons],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    expand=True
                ),
                alignment=alignment.center,
                expand=True,
                padding=20
            )
        )

    def show_add_task_form(self):
        self.page.clean()

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
                self.tasks.append({
                    'name': task_name,
                    'description': task_description,
                    'priority': task_priority,
                    'status': task_status,
                    'deadline': task_deadline
                })
                self.page.snack_bar = SnackBar(Text("Task Added Successfully!"), open=True)
                self.show_dashboard()

        task_name_input = TextField(label="Task Name", width=330)
        task_description_input = TextField(label="Task Description", width=330)
        task_priority_input = TextField(label="Task Priority", width=330)
        task_status_input = TextField(label="Task Status", width=330)
        task_deadline_input = TextField(label="Task Deadline", width=330)

        submit_button = ElevatedButton(
            content=Text("Add Task"),
            bgcolor="#4CAF50",  # Green background
            color="#FFFFFF",
            on_click=add_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard()
        )

        self.page.add(
            Column(
                [
                    Text(value="Add Task", size=24, weight="bold"),
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

    def show_read_tasks_page(self):
        self.page.clean()

        task_items = []
        ## Add the bg color functionality that is for each priority color will be different.
        for task in self.tasks:
            task_items.append(Text(f"Task: {task['name']}, Description: {task['description']}, Task Priority: {task['priority']}, Task Status: {task['status']}, Task Deadline: {task['deadline']}"))

        if not task_items:
            task_items.append(Text("No tasks found.", color="#F44336"))

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard()
        )

        self.page.add(
            Column(
                [
                    Text(value="All Tasks", size=24, weight="bold"),
                    *task_items,
                    Container(height=20),
                    back_to_dashboard_button
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True
            )
        )

    def show_update_task_form(self):
        self.page.clean()

        def update_task(e):
            task_name = task_name_input.value
            new_description = new_task_description_input.value
            new_priority = new_task_priority_input.value
            new_status = new_task_status_input.value
            new_deadline = new_task_deadline_input.value
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
            self.show_dashboard()

        task_name_input = TextField(label="Task Name" , width=330)
        new_task_description_input = TextField(label="New Task Description", width=330)
        new_task_priority_input = TextField(label="New Task Priority", width=330)
        new_task_status_input = TextField(label="New Task Status", width=330)
        new_task_deadline_input = TextField(label="New Task Deadline", width=330)

        submit_button = ElevatedButton(
            content=Text("Update Task"),
            bgcolor="#FFC107",  # Yellow background
            color="#FFFFFF",
            on_click=update_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard()
        )

        self.page.add(
            Column(
                [
                    Text(value="Update Task", size=24, weight="bold"),
                    Container(height=50),
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

    def show_delete_task_form(self):
        self.page.clean()

        def delete_task(e):
            task_name = task_name_input.value
            for task in self.tasks:
                if task['name'] == task_name:
                    self.tasks.remove(task)
                    self.page.snack_bar = SnackBar(Text("Task Deleted Successfully!"), open=True)
                    break
            else:
                self.page.snack_bar = SnackBar(Text("Task Not Found!"), open=True)
            self.show_dashboard()

        task_name_input = TextField(label="Task Name", width=330)

        submit_button = ElevatedButton(
            content=Text("Delete Task"),
            bgcolor="#F44336",  # Red background
            color="#FFFFFF",
            on_click=delete_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard()
        )

        self.page.add(
            Column(
                [
                    Text(value="Delete Task", size=24, weight="bold"),
                    Container(height=50),
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

def main(page: Page):
    TaskWizardDashboard(page)

app(target=main)
