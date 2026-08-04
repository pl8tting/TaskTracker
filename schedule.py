import tkinter as tk
from tkinter import ttk
import sv_ttk
import pywinstyles
import json
import os

root = tk.Tk()
root.geometry('600x400')
pywinstyles.apply_style(root,'mica')

treeview = ttk.Treeview(root,show='tree')
treeview.grid(column=0,row=0)

treeview.insert("", "end", text="Not Done",iid="Not Done")
treeview.insert("", "end", text="Completed",iid='Completed')
treeview.insert("", "end", text="Long Term",iid='Long Term')

task_name_entry = ttk.Entry(root)
task_name_entry.place(x=250,y=0)
task_name_entry.insert(0, "Your Task")

value = ['Not Done','Completed','Long Term']
combo = ttk.Combobox(root, values=value, state='readonly')
combo.place(x=250,y=40)

d = 0
ids = [0]

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        data = json.load(file)

    ids = data["ids"]

    for item in data["tasks"]:
        treeview.insert(
            item["parent"],
            "end",
            iid=item["iid"],
            text=item["text"]
        )

def add():
    task = task_name_entry.get()
    parents = combo.get()
    for i in ids:
        d = ids[len(ids)-1]
        d += 1
    ids.append(d)
    id = d
    treeview.insert(parents, "end", iid=str(id), text=task)

add_button = ttk.Button(root, text='Add',width=25,command=add)
add_button.place(x=250,y=80)

move1 = ttk.Label(root, text='Move task to another category')
move1.place(x=250,y=150 )

second_combo = ttk.Combobox(root, values=value,state='readonly')
second_combo.place(x=250,y=180)

move = ttk.Label(root, text='What task?')
move.place(x=250,y=220)

third_combo = ttk.Combobox(root,values=[] ,state='readonly')
third_combo.place(x=250,y=240)

def get_child_name(event):
    parent = second_combo.get()
    children = list(treeview.get_children(parent))
    childrens_name = []
    for i in children:
        childrens_name.append(treeview.item(i,'text'))
    third_combo['values'] = childrens_name

second_combo.bind("<<ComboboxSelected>>", get_child_name)

move2 = ttk.Label(root, text='To what category?')
move2.place(x=250,y=270)

fourth_combo = ttk.Combobox(root,values=value ,state='readonly')
fourth_combo.place(x=250,y=290)

def move_task():
    initial_parent = second_combo.get()
    task_to_move = third_combo.get()
    next_parent = fourth_combo.get()
    initial_children = list(treeview.get_children(initial_parent))
    for i in initial_children:
        if treeview.item(i,'text') == task_to_move:
            item_id = i
    treeview.move(item_id, next_parent, "end")

move_button = ttk.Button(root,text='Move to new category',command=move_task)
move_button.place(x=250,y=330)

def save_data():
    data = {
        "ids": ids,
        "tasks": []
    }

    for parent in value:
        for child in treeview.get_children(parent):
            data["tasks"].append({
                "iid": child,
                "parent": parent,
                "text": treeview.item(child, "text")
            })

    with open("tasks.json", "w") as file:
        json.dump(data, file)

    root.destroy()

root.protocol("WM_DELETE_WINDOW", save_data)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
scrollbar.place(x=580, y=0, width=20, height=400)
treeview.configure(yscrollcommand=scrollbar.set)

sv_ttk.set_theme("dark")

root.mainloop()