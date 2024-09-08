from flet import *


# Example color constants
PRIMARY_COLOR = "#2FF924"  # Green
SECONDARY_COLOR = "#FFC107"  # Yellow
ACCENT_COLOR = "#03A9F4"  # Blue
BACKGROUND_COLOR = "#FFFFFF"  # White
TEXT_COLOR = "#212121"  # Dark Gray
ERROR_COLOR = "#FF2400"  # Red

# # # Dark Theme Color Constants
# PRIMARY_COLOR = "#1B5E20"       # Dark Green
# SECONDARY_COLOR = "#FFA000"     # Dark Amber
# ACCENT_COLOR = "#0288D1"        # Darker Blue
# BACKGROUND_COLOR = "#121212"    # Almost Black
# TEXT_COLOR = "#E0E0E0"          # Light Gray
# ERROR_COLOR = "#D32F2F"         # Dark Red


class TaskWizardApp:
    def __init__(self, page: Page):
        self.tasks = []
        self.page = page
        self.page.title = "Task Wizard"
        self.page.bgcolor = BACKGROUND_COLOR  # White background for the whole page
        self.show_home_page()


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

        registration_form = Column(
            [
                Text(value="Create an Account", style="headlineMedium", text_align="center", font_family="Roboto",
                     weight="Bold"),
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
                Container(height=20),  # Spacer
                ElevatedButton(
                    content=Text("Register", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=ACCENT_COLOR,  # Blue background for the button
                    on_click=lambda _: self.handle_registration(username_field.value, email_field.value, password_field.value)
                ),
                Container(height=15),  # Spacer
                TextButton(content=Text("Back to Login", weight="bold"),
                           on_click=lambda _: self.show_login_page())
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        self.page.add(Container(
            content=registration_form,
            alignment=alignment.center,
            bgcolor=BACKGROUND_COLOR,  # White background for the form container
            expand=True
        ))

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

        username_field = TextField(label="Username", width=330)
        password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)

        login_form = Column(
            [
                Container(height=60),  # Spacer
                Text(value="Login", color=TEXT_COLOR, style="headlineMedium", text_align="center", font_family="Roboto",
                     weight="Bold"),
                Container(height=10),  # Spacer
                username_field,
                Container(height=10),  # Spacer
                password_field,
                TextButton(text="Forget Password?", on_click=lambda _: self.forget_password_page()),
                ElevatedButton(
                    content=Text("Login", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=PRIMARY_COLOR,  # Green background for the button
                    on_click=lambda _: self.handle_login()
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
                Container(height=10),  # Spacer
                TextButton(content=Text("See User Dashboard", weight="bold"),
                           on_click=lambda _: self.show_dashboard())
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
    
    # BLUE DASHBOARD PAGE: 
    def show_dashboard(self):
        self.page.clean()
    
        self.page.add(Container(
            content=Text(
                value="Task Wizard Dashboard Page",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                # color=TEXT_COLOR
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
        
        # Buttons for CRUD operations
        add_task_button = ElevatedButton(
            content=Text("Add Task", weight="bold"),
            width=300,
            # color=TEXT_COLOR,
            color="#FFFFFF",
            bgcolor=ACCENT_COLOR,  # Blue background
            on_click=lambda _: self.show_add_task_form()
        )

        read_tasks_button = ElevatedButton(
            content=Text("Read All Tasks", weight="bold"),
            width=300,
            # color=TEXT_COLOR,
            color="#FFFFFF",
            bgcolor=ACCENT_COLOR,  # Blue background
            on_click=lambda _: self.show_read_tasks_page()
        )

        update_task_button = ElevatedButton(
            content=Text("Update Task", weight="bold"),
            width=300,
            # color=TEXT_COLOR,
            color="#FFFFFF", 
            bgcolor=ACCENT_COLOR,  # Yellow background
            on_click=lambda _: self.show_update_task_form()
        )

        delete_task_button = ElevatedButton(
            content=Text("Delete Task", weight="bold"),
            width=300,
            # color= TEXT_COLOR,
            color="#FFFFFF", 
            bgcolor=ACCENT_COLOR,  # Red background
            on_click=lambda _: self.show_delete_task_form()
        )
        BTN = TextButton(text="Back to Login", on_click=lambda _: self.show_login_page())

        # Arrange buttons in a column
        dashboard_buttons = Column(
            [
                add_task_button,
                Container(height=10),
                read_tasks_button,
                Container(height=10),
                update_task_button,
                Container(height=10),
                delete_task_button,
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
        print("Login clicked")
        # Your login logic here


    def handle_registration(self, username, email, password):
        print(f"Registering user {username} with email {email}")
        # Your registration logic here

    def handle_admin_login(self, admin_username, admin_password):
        print(f"Admin login with username {admin_username}")
        # Your admin login logic here

    def forget_password_page(self):
        self.page.clean()
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
            bgcolor=PRIMARY_COLOR,  # Green background only for the heading
            padding=20
        ))
        email = TextField(label="Write your Registered Email", width=330)
        question = TextField(label="What is the most Favourite Thing you have?", width=330)

        login_form = Column(
            [
                Container(height=60),  # Spacer
                Text(value="Answer the Question\n And You Get the Account Access", text_align="center", font_family="Roboto", weight="Bold", size=20),
                Container(height=10),  # Spacer
                email,
                Container(height=10),  # Spacer
                question,
                Container(height=20),  # Spacer
                ElevatedButton(
                    content=Text("Login", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=PRIMARY_COLOR,  # Green background for the button
                    on_click=lambda _: self.handle_login()
                ),
                Container(height=20),  # Spacer
                TextButton(text="Back to Login Page", on_click=lambda _: self.show_login_page())
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
    
    # CRUD Functionality of App Written Here 
    def show_add_task_form(self):
        self.page.clean()

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
            bgcolor=PRIMARY_COLOR,  # Green background
            color="#FFFFFF",
            on_click=add_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",  # Blue background
            color="#FFFFFF",
            # on_click=lambda e: self.show_user_dashboard_page()
            on_click=lambda e: self.show_dashboard()
        )

        self.page.add(
            Column(
                [
                    # Text(value="Add Task", size=24, weight="bold"),
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

    # THIS CODE PROPERLY RUN WITH 3 CARDS AND THE SCROLL IS MISSING BUT THIS IS AN IMP CODE:
    # def show_read_tasks_page(self):
    #     self.page.clean()

    #     # Header
    #     self.page.add(
    #         Container(
    #             content=Text(
    #                 value="Display All Task Page",
    #                 style="headlineMedium",
    #                 size=30,
    #                 weight="BOLD",
    #                 font_family="Roboto",
    #                 text_align="center",
    #                 color="white"
    #             ),
    #             alignment=alignment.center,
    #             bgcolor="green",  # Replace with ACCENT_COLOR if defined
    #             padding=20,
    #         )
    #     )

    #     task_items = []

    #     # Check if there are any tasks to display
    #     if not self.tasks:
    #         task_items.append(Text("No tasks found.", color="#F44336"))
    #     else:
    #         for task in self.tasks:
    #             # Determine the background color based on priority
    #             if task['priority'].lower() == 'high':
    #                 bg_color = colors.RED
    #             elif task['priority'].lower() == 'medium':
    #                 bg_color = colors.LIGHT_GREEN
    #             elif task['priority'].lower() == 'low':
    #                 bg_color = colors.LIGHT_BLUE
    #             else:
    #                 bg_color = colors.GREY  # Default background color

    #             # Create a card for each task
    #             task_container = Container(
    #                 content=Column([
    #                     Text(f"Task: {task['name']}", color="white"),
    #                     Text(f"Description: {task['description']}", color="white"),
    #                     Text(f"Task Priority: {task['priority']}", color="white"),
    #                     Text(f"Task Status: {task['status']}", color="white"),
    #                     Text(f"Task Deadline: {task['deadline']}", color="white")
    #                 ]),
    #                 padding=10,
    #                 border=border.all(1, color=colors.BLACK),
    #                 border_radius=8,
    #                 bgcolor=bg_color,
    #                 width=285,  # Adjust width as needed
    #                 height=200  # Adjust height as needed
    #             )

    #             task_items.append(task_container)

    #     # Back to Dashboard Button
    #     back_to_dashboard_button = ElevatedButton(
    #         content=Text("Back to Dashboard"),
    #         bgcolor="#03A9F4",  # Blue background
    #         color="#FFFFFF",
    #         on_click=lambda e: self.show_dashboard()
    #     )
        
    #     # Make Responsive with 2 card on mobile and if the screen size increase then adjust the card with that specific sizes
    #     # Create rows with 3-4 cards each
    #     rows = []
    #     for i in range(0, len(task_items), 5):  # Adjust the number of cards per row
    #         rows.append(Row(task_items[i:i+5], spacing=15))  # Adjust spacing as needed

    #     # Add all the rows to a scrollable column
    #     scrollable_content = Column(
    #         rows + [Container(height=20), back_to_dashboard_button],  # Add some spacing at the end
    #         spacing=20,
    #         alignment=MainAxisAlignment.CENTER,
    #         horizontal_alignment=CrossAxisAlignment.CENTER,
    #         scroll="auto"  # Enable vertical scrolling
    #     )

    #     self.page.add(scrollable_content)

    def show_read_tasks_page(self):
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

        # Check if there are any tasks to display
        if not self.tasks:
            no_task_message = Container(
                content=Text("No tasks found.", color="#F44336", size=16),
                alignment=alignment.center,
                expand=True
            )
            task_items.append(no_task_message)
        else:
            for task in self.tasks:
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
                        Text(f"Description: {task['description']}", color="white" , weight="bold" ),
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

        # Responsive handling: Adjust the number of cards per row
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

        # Back to Dashboard Button, centered within a Container
        back_to_dashboard_button = Container(
            content=ElevatedButton(
                content=Text("Back to Dashboard"),
                bgcolor="#03A9F4",  # Blue background
                color="#FFFFFF",
                on_click=lambda e: self.show_dashboard()
            ),
            alignment=alignment.center,
            padding=10
        )

        # Initial layout update
        update_layout()

        # Add a listener to update the layout on screen resize
        self.page.on_resize = update_layout

    

    def show_update_task_form(self):
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
            self.show_dashboard()

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
            on_click=lambda e: self.show_dashboard()
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

    def show_delete_task_form(self):
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
            self.show_dashboard()

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
            on_click=lambda e: self.show_dashboard()
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
    

def main(page: Page):
    TaskWizardApp(page)

app(target=main)
