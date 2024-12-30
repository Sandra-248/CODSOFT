import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.input_frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.input_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.input_frame, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.contact_listbox = tk.Listbox(root, width=50, height=15)
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind("<Double-1>", self.load_contact_details)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.update_contact_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def load_contact_details(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact['name'])

            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact['phone'])

            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact['email'])

            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, contact['address'])

    def search_contact(self):
        search_term = self.name_entry.get().strip()
        if search_term:
            results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
            self.contact_listbox.delete(0, tk.END)
            for contact in results:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

            if not results:
                messagebox.showinfo("No Results", "No contacts found.")
        else:
            messagebox.showwarning("Warning", "Enter a name or phone to search.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.contacts[index] = {
                "name": self.name_entry.get().strip(),
                "phone": self.phone_entry.get().strip(),
                "email": self.email_entry.get().strip(),
                "address": self.address_entry.get().strip()
            }
            self.update_contact_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Warning", "Select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_contact_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Select a contact to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
