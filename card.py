import flet as ft

def main(page: ft.Page):
    # Sample tasks list (replace with your actual tasks list)
    tasks = [
        {
            'name': 'Complete Project',
            'description': 'Finish the final phase of the project.',
            'priority': 'medium',
            'status': 'In Progress',
            'deadline': '2024-09-10'
        },
        {
            'name': 'Write Report',
            'description': 'Prepare the final report.',
            'priority': 'high',
            'status': 'Pending',
            'deadline': '2024-09-15'
        },
        # Add more tasks as needed
    ]

    task_items = []

    for task in tasks:
        # Determine the background color based on priority
        if task['priority'].lower() == 'high':
            bg_color = ft.colors.RED
        elif task['priority'].lower() == 'medium':
            bg_color = ft.colors.LIGHT_GREEN
        elif task['priority'].lower() == 'low':
            bg_color = ft.colors.LIGHT_BLUE
        else:
            bg_color = ft.colors.LIGHT_GRAY  # Default background color

        # Creating text widgets for labels and values
        task_name_label = ft.Text("Task: ", size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
        task_name_value = ft.Text(task['name'], size=16, color=ft.colors.WHITE)
        
        description_label = ft.Text("Description: ", size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
        description_value = ft.Text(task['description'], size=16, color=ft.colors.WHITE)
        
        priority_label = ft.Text("Task Priority: ", size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
        priority_value = ft.Text(task['priority'], size=16, color=ft.colors.WHITE)
        
        status_label = ft.Text("Task Status: ", size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
        status_value = ft.Text(task['status'], size=16, color=ft.colors.WHITE)
        
        deadline_label = ft.Text("Task Deadline: ", size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
        deadline_value = ft.Text(task['deadline'], size=16, color=ft.colors.WHITE)

        # Combine the label and value pairs into a Column
        content = ft.Column([
            ft.Row([task_name_label, task_name_value]),
            ft.Row([description_label, description_value]),
            ft.Row([priority_label, priority_value]),
            ft.Row([status_label, status_value]),
            ft.Row([deadline_label, deadline_value])
        ])

        container = ft.Container(
            content=content,
            padding=ft.padding.all(10),  # Consistent padding
            border=ft.border.all(1, color=ft.colors.BLACK),  # Border around the card
            border_radius=ft.border_radius.all(8),  # Rounded corners
            bgcolor=bg_color,
            width=350  # Width of each card
        )

        task_items.append(container)

    # Creating rows with 4 cards each
    rows = []
    for i in range(0, len(task_items), 4):
        rows.append(ft.Row(task_items[i:i+4], spacing=10))  # Add some spacing between cards

    # Add all the rows to the page
    for row in rows:
        page.add(row)

ft.app(target=main)
