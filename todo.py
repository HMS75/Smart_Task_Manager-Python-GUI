#To Do List 

import tkinter as tk
root=tk.Tk()
root.title("To-Do List")
root.geometry("275x600")

label = tk.Label(root, text="To-Do List ~ ", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=4)

entry = tk.Entry(root, width=15, font=("Arial", 20), justify="right")
entry.grid(row=1, column=0, columnspan=4, ipadx=8, ipady=8)
            
def saveTasks():
    print("Saving tasks:", listbox.get(0, tk.END))  # Debugging
    with open("tasks.txt", "w") as file:
        for i in range(listbox.size()):
            file.write("TODO:" + listbox.get(i) + "\n")
        for i in range(completedListbox.size()):
            file.write("DONE:" + completedListbox.get(i) + "\n")

def addTask():
    taskText = entry.get().strip()
    if taskText:  # Only add if not empty
        listbox.insert(tk.END, taskText)
        entry.delete(0, tk.END)
    
taskAdd = tk.Button(root, text="Add Task", command=addTask)
taskAdd.grid(row=2, column=3)
    
listbox = tk.Listbox(root, width=40, height=10) #creating a listbox
listbox.grid(row=4, column=0, columnspan=4)

label1 = tk.Label(root, text="Completed tasks!", font=("Arial", 14))
label1.grid(row=5, column=0, columnspan=4)

completedListbox = tk.Listbox(root, width=40, height=10) #creating listbox for completed tasks
completedListbox.grid(row=6, column=0, columnspan=4)

label1 = tk.Label(root, text="List of Tasks to be Completed!", font=("Arial", 14))
label1.grid(row=3, column=0, columnspan=4)

def deleteTask():
    selectedTask = listbox.curselection() # get index
    if selectedTask:
        listbox.delete(selectedTask[0]) # removes task from listbox

def markDone():
    selectedTask = listbox.curselection() # get index
    if selectedTask:
        taskText = listbox.get(selectedTask[0]) # gets task's text
        listbox.delete(selectedTask[0]) # removes task from listbox
        completedListbox.insert(tk.END, "✔️"+ taskText)
        
taskDel = tk.Button(root, text="Delete Task", command=deleteTask)
taskDel.grid(row=2, column=2)

done = tk.Button(root, text="Done", command=markDone)
done.grid(row=2, column=1)

save = tk.Button(root, text="Save Task", command=saveTasks)
save.grid(row=2, column=0)

def loadTasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                print("Loading:", task)  # Debugging
                if task.startswith("TODO:"):
                    listbox.insert(tk.END, task[5:])  # Remove "TODO:"
                elif task.startswith("DONE:"):
                    completedListbox.insert(tk.END, task[5:])  # Remove "DONE:"
    except FileNotFoundError:
        print("No saved tasks found.")  # Debugging
        
loadTasks()
root.mainloop()