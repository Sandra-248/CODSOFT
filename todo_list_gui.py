import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        
        self.tasks = []

        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

    
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    
        self.mark_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.mark_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=3, column=0, padx=10, pady=5)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=3, column=1, padx=10, pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=3, column=2, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"name": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[Completed]" if task['completed'] else "[Pending]"
            self.task_listbox.insert(tk.END, f"{task['name']} {status}")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def save_tasks(self):
        filename = "tasks.json"
        with open(filename, "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Info", f"Tasks saved to {filename}.")

    def load_tasks(self):
        filename = "tasks.json"
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            self.update_task_listbox()
            messagebox.showinfo("Info", f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error reading tasks file. Ensure it is valid JSON.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
