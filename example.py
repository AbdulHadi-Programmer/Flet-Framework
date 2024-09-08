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

    def show_admin_login_page(self):
        self.page.clean()
        # Main heading at the top of the page (in red)
        self.page.add(Container(
            content=Text(
                value="Admin Page",
                style="headlineMedium",
                size=30,
                weight="bold",
                font_family="Roboto",
                text_align="center",
                color=TEXT_COLOR
            ),
            alignment=alignment.center,
            bgcolor=ERROR_COLOR,  # Red background only for the heading
            padding=20,
        ))

        admin_username_field = TextField(label="Admin Username", width=330)
        admin_password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)

        admin_login_form = Column(
            [
                Text(value="Admin", style="headlineMedium", text_align="center", font_family="Roboto", weight="Bold"),
                Container(height=10),
                admin_username_field,
                Container(height=10),
                admin_password_field,
                Container(height=20),
                ElevatedButton(content=Text("Admin", weight="bold"), width=150, color=TEXT_COLOR, bgcolor=ERROR_COLOR,
                              on_click=lambda e: self.handle_admin_login(admin_username_field.value,
                                                                         admin_password_field.value)),
                Container(height=10),
                TextButton(text="Back to Login", on_click=lambda _: self.show_login_page())
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        self.page.add(Container(
            content=admin_login_form,
            alignment=alignment.center,
            bgcolor=BACKGROUND_COLOR,  # White background for the form container
            expand=True
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
                    on_click=lambda e: self.handle_registration(username_field.value, email_field.value,
                                                                 password_field.value)
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
                Container(height=10),  # Spacer
                ElevatedButton(
                    content=Text("Admin", weight="bold"),
                    width=150,
                    color=TEXT_COLOR,
                    bgcolor=ERROR_COLOR,  # Red background for the button
                    on_click=lambda _: self.show_admin_login_page(),
                ),
                TextButton(content=Text("See User Dashboard", weight="bold"),
                           on_click=lambda _: self.show_user_dashboard_page())
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

    def create_button_dash(self, text):
        return ElevatedButton(
            content=Text(text, weight="bold"),
            width=250,
            color=TEXT_COLOR,
            bgcolor=ACCENT_COLOR,  # Blue background for the button
            on_click=lambda e: print("This Button is Not Functional Yet"),
        )

    def show_user_dashboard_page(self):
        self.page.clean()
        # Main heading at the top of the page (in blue)
        self.page.add(Container(
            content=Text(
                value="Dashboard Page",
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

        dashboard_form = Column(
            [
                Text(value="All the Main Functionality", style="headlineMedium", text_align="center",
                     font_family="Roboto", weight="Bold"),
                Container(height=20),  # Spacer
                self.create_button_dash("Add Task"),  # Correct the onclick event
                Container(height=10),  # Spacer
                self.create_button_dash("Read All Task"),  # Correct the onclick event
                Container(height=10),  # Spacer
                self.create_button_dash("Update Task"),  # Correct the onclick event
                Container(height=10),  # Spacer
                self.create_button_dash("Delete Task"),  # Correct the onclick event
                Container(height=10),  # Spacer
                

                TextButton(content=Text("Back to Login", weight="bold"), on_click=lambda _: self.show_login_page()),
                Container(height=15),  # Spacer
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True
        )

        self.page.add(Container(
            content=dashboard_form,
            alignment=alignment.center,
            bgcolor=BACKGROUND_COLOR,  # White background for the form container
            expand=True
        ))

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
                    on_click=lambda e: self.handle_login()
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
    

def main(page: Page):
    TaskWizardApp(page)


app(target=main)
