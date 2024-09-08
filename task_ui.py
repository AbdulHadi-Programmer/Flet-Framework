from flet import *
########## This is the original code but without forget password page and it does not have new field that are added and also the green color is change.
# Example color constants
PRIMARY_COLOR = "#4CAF50"       # Green
SECONDARY_COLOR = "#FFC107"     # Yellow
ACCENT_COLOR = "#03A9F4"        # Blue
BACKGROUND_COLOR = "#FFFFFF"    # White
TEXT_COLOR = "#212121"          # Dark Gray
ERROR_COLOR = "#F44336"         # Red

def show_admin_login_page(page: Page):
    page.clean()
    # Main heading at the top of the page (in red)
    page.add(Container(
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
            ElevatedButton(content=Text("Admin", weight="bold"), width=150, color=TEXT_COLOR, bgcolor=ERROR_COLOR, on_click=lambda e: handle_admin_login(page, admin_username_field.value, admin_password_field.value)),
            Container(height=10),
            TextButton(text="Back to Login", on_click=lambda _: show_login_page(page))
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(Container(
        content=admin_login_form,
        alignment=alignment.center,
        bgcolor=BACKGROUND_COLOR,  # White background for the form container
        expand=True
    ))

def show_registration_page(page: Page):
    page.clean()

    # Main heading at the top of the page (in blue)
    page.add(Container(
        
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
    fullname_field = TextField(label='Full Name', width= 330)
    username_field = TextField(label="Username", width=330)
    email_field = TextField(label="Email", width=330)
    password_field = TextField(label="Password", password=True, can_reveal_password=True, width=330)
    ask_field = TextField(label="What is the most Favourite Thing you have?", width= 330)

    registration_form = Column(
        [
            Text(value="Create an Account", style="headlineMedium", text_align="center", font_family="Roboto", weight="Bold"),
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
                on_click=lambda e: handle_registration(page, username_field.value, email_field.value, password_field.value)
            ),
            Container(height=15),  # Spacer
            TextButton(content=Text("Back to Login", weight="bold"), on_click=lambda _: show_login_page(page))
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(Container(
        content=registration_form,
        alignment=alignment.center,
        bgcolor=BACKGROUND_COLOR,  # White background for the form container
        expand=True
    ))

def show_login_page(page: Page):
    page.clean()

    # Main heading at the top of the page (in green)
    page.add(Container(
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
            Text(value="Login", style="headlineMedium", text_align="center", font_family="Roboto", weight="Bold"),
            Container(height=10),  # Spacer
            username_field,
            Container(height=10),  # Spacer
            password_field,
            ###########################################################################################################################################
            # Make a simple page that ask a question that can also ask in register page and if the answer is correct then user would easily navigate to thier profie and task CRUD
            #######################################################################################################################################
            TextButton(text="Forget Password?", on_click=lambda _: print("Forget Password clicked")),
            ElevatedButton(
                content=Text("Login", weight="bold"),
                width=150,
                color=TEXT_COLOR,
                bgcolor=PRIMARY_COLOR,  # Green background for the button
                on_click=lambda e: handle_login(page)
            ),
            Container(height=20),  # Spacer
            Text(value="Don't have an account?", size=16, text_align="center", color='BLUE'),
            ElevatedButton(
                content=Text("Sign Up", weight="bold"),
                width=150,
                color=TEXT_COLOR,
                bgcolor=PRIMARY_COLOR,  # Green background for the button
                on_click=lambda _: show_registration_page(page)
            ),
            Container(height=10),  # Spacer
            ElevatedButton(
                content=Text("Admin", weight="bold"),
                width=150,
                color=TEXT_COLOR,
                bgcolor=ERROR_COLOR,  # Red background for the button
                on_click=lambda _: show_admin_login_page(page),
            )
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(Container(
        content=login_form,
        alignment=alignment.center,
        bgcolor=BACKGROUND_COLOR,  # White background for the form container
        expand=True, 
        padding=20
    ))

def ask_question():
    ask = "What is the most Favourite Thing you have?"
    return ask


# Placeholder function implementations
def handle_login(page: Page):
    print("Login button clicked")

def handle_admin_login(page: Page, username: str, password: str):
    print(f"Admin Login: Username={username}, Password={password}")

def handle_registration(page: Page, username: str, email: str, password: str):
    print(f"Register: Username={username}, Email={email}, Password={password}")
    show_login_page(page)

def home_page(page: Page):
    page.title = "Task Wizard"
    page.bgcolor = BACKGROUND_COLOR  # White background for the whole page

    title = Text(
        value="Task Wizard",
        color=PRIMARY_COLOR,  # Green text color for the title
        size=40,
        weight="bold",
        text_align=TextAlign.CENTER
    )

    page.add(
        Container(
            content=title,
            alignment=alignment.center,
            expand=True  # Ensures the container takes full height and width of the page
        )
    )

def main(page: Page):
    home_page(page)
    import time
    time.sleep(3)
    show_login_page(page)

app(target=main)