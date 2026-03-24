# Updated Code with Visual Improvements
import tkinter as tk
from tkinter import messagebox, Listbox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Screen')
        self.root.geometry('400x300')
        self.root.configure(bg='#282c34')

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text='Welcome to Bright Space', bg='#282c34', fg='#61afef', font=('Helvetica', 16, 'bold'))
        self.title_label.pack(pady=(20, 10))

        self.entry_frame = tk.Frame(self.root, bg='#282c34')
        self.entry_frame.pack(pady=10)

        self.username_label = tk.Label(self.entry_frame, text='Username:', bg='#282c34', fg='#ffffff')
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.entry_frame, bg='#444d56', fg='#ffffff')
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.entry_frame, text='Password:', bg='#282c34', fg='#ffffff')
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.entry_frame, show='*', bg='#444d56', fg='#ffffff')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.login_button = tk.Button(self.root, text='Login', command=self.login, bg='#61afef', fg='#ffffff', font=('Helvetica', 12), activebackground='#528bba')
        self.login_button.pack(pady=(10, 5))

        self.listbox = Listbox(self.root, bg='#444d56', fg='#ffffff', font=('Helvetica', 10))
        self.listbox.pack(pady=(10, 5))

        # Sample items for the listbox
        for item in ['Item 1', 'Item 2', 'Item 3']:
            self.listbox.insert(tk.END, item)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            messagebox.showinfo('Success', 'Login successful!')
        else:
            messagebox.showwarning('Error', 'Please fill in all fields.')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()