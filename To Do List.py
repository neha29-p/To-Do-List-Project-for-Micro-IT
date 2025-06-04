# Run this cell first to install necessary packages
!pip install ipywidgets --quiet

import ipywidgets as widgets
from IPython.display import display, clear_output

# Storage for tasks
tasks = []

# Define task UI
task_box = widgets.VBox()

def update_task_display():
    """Refresh the task list UI."""
    task_items = []
    for i, task in enumerate(tasks):
        checkbox = widgets.Checkbox(value=task['done'], description=task['task'], indent=False)
        checkbox.layout.width = '90%'
        
        def on_checkbox_change(change, idx=i):
            tasks[idx]['done'] = change['new']
            update_task_display()

        checkbox.observe(on_checkbox_change, names='value')

        delete_btn = widgets.Button(description="🗑️", layout=widgets.Layout(width='40px'))
        def on_delete(btn, idx=i):
            tasks.pop(idx)
            update_task_display()
        delete_btn.on_click(on_delete)

        task_row = widgets.HBox([checkbox, delete_btn])
        task_items.append(task_row)

    task_box.children = task_items

# Add task widgets
task_input = widgets.Text(placeholder='Enter new task...')
add_button = widgets.Button(description='Add Task', button_style='success')

def on_add_task(btn):
    task_text = task_input.value.strip()
    if task_text:
        tasks.append({'task': task_text, 'done': False})
        task_input.value = ''
        update_task_display()

add_button.on_click(on_add_task)

# Display UI
display(widgets.HTML("<h2>📝 My To-Do List</h2>"))
display(widgets.HBox([task_input, add_button]))
display(task_box)