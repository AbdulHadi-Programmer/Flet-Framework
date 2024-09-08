from flet import *
from sqlite3 import *
# Define constants
PRIMARY_COLOR = "#4CAF50"  # Green
ACCENT_COLOR = "#FFC107"  # Amber
ERROR_COLOR = "#F44336"  # Red
TEXT_COLOR = "#FFFFFF"  # White

class TaskWizardApp:
    def __init__(self, page: Page):
        self.page = page
        self.tasks = []  # List to hold tasks
        self.show_login_page()  # Show login page on startup

    def show_login_page(self):
        self.page.clean()
        username_field = TextField(label="Username", width=330)
        password_field = TextField(label="Password", width=330, password=True)
        login_button = ElevatedButton(
            content=Text("Login"),
            bgcolor=PRIMARY_COLOR,
            color="#FFFFFF",
            on_click=self.handle_login
        )
        self.page.add(
            Column(
                [
                    Container(height=100),
                    username_field,
                    Container(height=10),
                    password_field,
                    Container(height=20),
                    login_button,
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True
            )
        )

    def show_dashboard(self, user_id):
        self.page.clean()
        welcome_message = Text(
            value="Welcome to the Task Dashboard",
            style="headlineMedium",
            size=30,
            weight="BOLD",
            text_align="center",
            color=TEXT_COLOR
        )

        add_task_button = ElevatedButton(
            content=Text("Add Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor=PRIMARY_COLOR,
            on_click=lambda _: self.show_add_task_form(user_id)
        )

        update_task_button = ElevatedButton(
            content=Text("Update Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor=PRIMARY_COLOR,
            on_click=lambda _: self.show_update_task_form(user_id)
        )

        read_task_button = ElevatedButton(
            content=Text("Read All Tasks", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor=ACCENT_COLOR,
            on_click=lambda _: self.show_read_tasks_page(user_id)
        )

        delete_task_button = ElevatedButton(
            content=Text("Delete Task", weight="bold"),
            width=300,
            color="#FFFFFF",
            bgcolor=ERROR_COLOR,
            on_click=lambda _: self.show_delete_task_form(user_id)
        )

        BTN = TextButton(text="Back to Login", on_click=lambda _: self.show_login_page())

        # Arrange buttons in a column
        dashboard_buttons = Column(
            [
                add_task_button,
                Container(height=10),
                read_task_button,
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
        username = self.username_field.value
        password = self.password_field.value
        
        try:
            conn = connect('task_wizard.db')  # Replace with your actual DB file path
            c = conn.cursor()
            
            c.execute("SELECT id FROM registration WHERE user_name=? AND password=?", (username, password))
            user_data = c.fetchone()
            
            if not username or not password:
                self.page.snack_bar = SnackBar(content=Text("Fill all fields!", color="White"))
                self.page.snack_bar.open = True
                self.page.update()

            if user_data:
                user_id = user_data[0]
                self.show_dashboard(user_id)

            else:
                self.page.snack_bar = SnackBar(content=Text("Invalid username or password!", color="White"))
                self.page.snack_bar.open = True
                self.page.update()
            
        except Error as e:
            self.page.add(Text(f"Database Error: {e}", color="RED"))

        finally:
            conn.close()

    def show_add_task_form(self, user_id):
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
            bgcolor=ACCENT_COLOR,
            padding=20
        ))

        def add_task(e):
            task_name = task_name_input.value.strip()
            task_description = task_description_input.value.strip()
            task_priority = task_priority_input.value.strip()
            task_status = task_status_input.value.strip()
            task_deadline = task_deadline_input.value.strip()

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
                self.show_dashboard(user_id)

        task_name_input = TextField(label="Task Name", width=330)
        task_description_input = TextField(label="Task Description", width=330)
        task_priority_input = TextField(label="Task Priority", width=330)
        task_status_input = TextField(label="Task Status", width=330)
        task_deadline_input = TextField(label="Task Deadline", width=330)

        submit_button = ElevatedButton(
            content=Text("Add Task"),
            bgcolor=PRIMARY_COLOR,
            color="#FFFFFF",
            on_click=add_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",
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

    def show_read_tasks_page(self, user_id):
        self.page.clean()

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
            bgcolor="green",
            padding=20,
        )

        task_items = []

        if not self.tasks:
            no_task_message = Container(
                content=Text("No tasks found.", color="#F44336", size=16),
                alignment=alignment.center,
                expand=True
            )
            task_items.append(no_task_message)
        else:
            for task in self.tasks:
                if task['priority'].lower() == 'high':
                    bg_color = colors.RED
                elif task['priority'].lower() == 'medium':
                    bg_color = PRIMARY_COLOR
                elif task['priority'].lower() == 'low':
                    bg_color = colors.LIGHT_BLUE
                else:
                    bg_color = colors.GREY

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
                    width=290,
                    height=200
                )

                task_items.append(task_container)

        def update_layout(event=None):
            screen_width = self.page.window_width

            if screen_width < 600:
                cards_per_row = 2
            elif screen_width < 1200:
                cards_per_row = 3
            else:
                cards_per_row = 5

            rows = []
            for i in range(0, len(task_items), cards_per_row):
                rows.append(
                    Row(
                        task_items[i:i + cards_per_row],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        expand=True
                    )
                )
            self.page.add(
                Column(
                    [
                        header,
                        Container(height=20),
                        *rows,
                        Container(height=20),
                        ElevatedButton(
                            content=Text("Back to Dashboard", weight="bold"),
                            bgcolor="#03A9F4",
                            color="#FFFFFF",
                            on_click=lambda e: self.show_dashboard(user_id)
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    expand=True
                )
            )

        update_layout()

    def show_update_task_form(self, user_id):
        self.page.clean()

        self.page.add(Container(
            content=Text(
                value="Update Task Page",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color="#FFFFFF"
            ),
            alignment=alignment.center,
            bgcolor=PRIMARY_COLOR,
            padding=20
        ))

        def update_task(e):
            task_name = task_name_input.value.strip()
            new_priority = new_priority_input.value.strip()
            new_status = new_status_input.value.strip()
            new_deadline = new_deadline_input.value.strip()

            if not task_name or not new_priority or not new_status or not new_deadline:
                self.page.snack_bar = SnackBar(Text("All fields are required!"), open=True)
            else:
                for task in self.tasks:
                    if task['name'] == task_name:
                        task['priority'] = new_priority
                        task['status'] = new_status
                        task['deadline'] = new_deadline
                        self.page.snack_bar = SnackBar(Text("Task Updated Successfully!"), open=True)
                        break
                else:
                    self.page.snack_bar = SnackBar(Text("Task not found!"), open=True)
                self.show_dashboard(user_id)

        task_name_input = TextField(label="Task Name", width=330)
        new_priority_input = TextField(label="New Task Priority", width=330)
        new_status_input = TextField(label="New Task Status", width=330)
        new_deadline_input = TextField(label="New Task Deadline", width=330)

        submit_button = ElevatedButton(
            content=Text("Update Task"),
            bgcolor=PRIMARY_COLOR,
            color="#FFFFFF",
            on_click=update_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard(user_id)
        )

        self.page.add(
            Column(
                [
                    Container(height=50),
                    task_name_input,
                    Container(height=10),
                    new_priority_input,
                    Container(height=10),
                    new_status_input,
                    Container(height=10),
                    new_deadline_input,
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

    def show_delete_task_form(self, user_id):
        self.page.clean()

        self.page.add(Container(
            content=Text(
                value="Delete Task Page",
                style="headlineMedium",
                size=30,
                weight="BOLD",
                font_family="Roboto",
                text_align="center",
                color="#FFFFFF"
            ),
            alignment=alignment.center,
            bgcolor=ERROR_COLOR,
            padding=20
        ))

        def delete_task(e):
            task_name = task_name_input.value.strip()

            if not task_name:
                self.page.snack_bar = SnackBar(Text("Task Name is required!"), open=True)
            else:
                for task in self.tasks:
                    if task['name'] == task_name:
                        self.tasks.remove(task)
                        self.page.snack_bar = SnackBar(Text("Task Deleted Successfully!"), open=True)
                        break
                else:
                    self.page.snack_bar = SnackBar(Text("Task not found!"), open=True)
                self.show_dashboard(user_id)

        task_name_input = TextField(label="Task Name", width=330)

        submit_button = ElevatedButton(
            content=Text("Delete Task"),
            bgcolor=ERROR_COLOR,
            color="#FFFFFF",
            on_click=delete_task
        )

        back_to_dashboard_button = ElevatedButton(
            content=Text("Back to Dashboard"),
            bgcolor="#03A9F4",
            color="#FFFFFF",
            on_click=lambda e: self.show_dashboard(user_id)
        )

        self.page.add(
            Column(
                [
                    Container(height=50),
                    task_name_input,
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

# Initialize the page with the necessary arguments
def main():
    page = Page(conn=None, session_id=None, loop=None)
    app = TaskWizardApp(page)
    page.update()

if __name__ == "__main__":
    main()