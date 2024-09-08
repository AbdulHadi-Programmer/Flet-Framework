# Now I am learning Flet from basic, each and every component

import flet as ft
import time

# Make a Page inside a function:
def main(page: ft.Page):
    # Add a Simple text Widget and with some property that includes value, size, and color.
    t = ft.Text(value='Hello World', size=30, color='yellow')
    page.add(t)  # 1st easy method to add anything on the app
    
    # 2nd Method, both ways are the same, but the above is easy to use.
    # page.controls.append(t)
    # page.update()
    
    # Now We can run a loop and update the value like this:
    t1 = ft.Text()   
    page.add(t1)
    for i in range(3):
        t1.value = f"Step {i}"
        page.update()  # You can modify control properties and the UI will be updated on the next page.update()
        time.sleep(1)

    # Add a Row with some text widgets
    page.add(
        ft.Row(controls=[  # Make a Row Widget and control is a property in which a list is made 
            ft.Text("A"), 
            ft.Text("B"),
            ft.Text("C")
        ])
    )
    
    # Add a Row to add an input field and elevated button
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.TextField(label="Your name", password=True), # make a password input
            ft.ElevatedButton(text="Say my name!")
        ])
    )
    # Make an click action button function mean whenever a user click this below elevated button run this below function.
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
    
    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    # Write a new Function, Let check what it works 
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    ## Now we can learn some new properties like : 
    ## visible, disabled, buttons, Event Handling, TextBox, CheckBox, Dropdown
    ## Visible:
    n = ft.Text(value='Abdul Hadi', visible=False)
    m = ft.Text(value='Salman', visible=True)
    ## Disable:
    # Every control has disabled property which is false by default - control and all its children are enabled. disabled property is mostly used with data entry controls like TextField, Dropdown, Checkbox, buttons. However, disabled could be set to a parent control and its value will be propagated down to all children recursively.
    first_name = ft.TextField()
    last_name = ft.TextField()
    first_name.disabled = True
    last_name.disabled = True
    page.add(first_name, last_name, n, m)
    ## Column :
    # you can put form controls into container, e.g. Column and then set disabled for the column:
    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)
    ## Buttons:
    # Button is the most essential input control which generates click event when pressed:
    btn = ft.ElevatedButton('click me')
    page.add(btn)

# ft.app(target=main)



## Event Handling:
# Buttons with events in "Counter" app:
def counter(page: ft.Page):
    page.title = "Flet counter example"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="left", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment= ft.MainAxisAlignment.CENTER,
        ),
    )
    

ft.app(target=counter)