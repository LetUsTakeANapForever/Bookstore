from tkinter import *
from tkinter import ttk
from BookStore import *

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title('Welcome')
        self.geometry(self.center_window(150,130))
        self.resizable(0,0)
        self.set_up_widgets()
        self.place_widgets()
        self.mainloop()
    
    def center_window(self, w, h):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = screen_width//2 - w//2
        y = screen_height//2 - h//2
        return f'{w}x{h}+{x}+{y}'

    def set_up_widgets(self):
        self.label = Label(self, text='Welcome')
        self.sign_in_button = Button(self, text='Sign in')
        self.sign_in_button.bind('<Button-1>', self.open_sign_in_window)
        self.sign_up_button = Button(self, text='Sign up')
        self.sign_up_button.bind('<Button-1>', self.open_sign_up_window)

    def open_sign_up_window(self, event):
        self.withdraw()
        self.create_sign_up_window()

    def open_sign_in_window(self, event):
        self.withdraw()
        self.create_sign_in_window()

    def place_widgets(self):
        self.label.pack(pady=10)
        self.sign_in_button.pack(pady=5)
        self.sign_up_button.pack(pady=5)

    def create_sign_in_window(self):
        self.sign_in_window = Toplevel()
        self.sign_in_window.title('Sign in Menu')
        self.sign_in_window.geometry(self.center_window(250,270))
        self.sign_in_window.protocol('WM_DELETE_WINDOW', self.close_sign_in_window)
        
        self.sign_in_widgets()
        self.place_sign_in_widgets()

    def create_sign_up_window(self):
        self.sign_up_window = Toplevel()
        self.sign_up_window.title('Sign up Menu')
        self.sign_up_window.geometry(self.center_window(350,550))
        self.sign_up_window.protocol('WM_DELETE_WINDOW', self.close_sign_up_window)

        self.sign_up_widgets()
        self.place_sign_up_widgets()
        
    def sign_up_widgets(self):
        self.user_name_label2 = Label(self.sign_up_window, text = 'Username')
        self.user_name_entry2 = Entry(self.sign_up_window, width = 35)
        self.pass_word_label2 = Label(self.sign_up_window, text = 'Password')
        self.pass_word_entry2 = Entry(self.sign_up_window, width = 35)
        self.birth_day_label2 = Label(self.sign_up_window, text = 'Birthday')
        self.birth_day_entry2 = Entry(self.sign_up_window, width = 35)
        self.birth_day_entry2.insert(0, '(e.g. 2024-05-25)')
        self.email_label2 = Label(self.sign_up_window, text = 'Email')
        self.email_entry2 = Entry(self.sign_up_window, width = 35)
        self.full_name2 = Label(self.sign_up_window, text = 'Full name')
        self.full_name_entry2 = Entry(self.sign_up_window, width = 35)
        self.frame_sign_up = Frame(self.sign_up_window)
        self.sign_up_bt2 = Button(self.frame_sign_up, text = 'Sign up')
        self.back_bt = Button(self.frame_sign_up, text = 'Back')
        self.sign_up_msg2 = Label(self.frame_sign_up, text = '')
        self.sign_up_bt2.bind('<Button-1>', self.pressed_sign_up)
        self.back_bt.bind('<Button-1>', self.pressed_back)

    def place_sign_up_widgets(self):
        self.user_name_label2.pack(pady = 10)
        self.user_name_entry2.pack(pady = 10)
        self.pass_word_label2.pack(pady = 10)
        self.pass_word_entry2.pack(pady = 10)
        self.birth_day_label2.pack(pady = 10)
        self.birth_day_entry2.pack(pady = 10)
        self.birth_day_entry2.pack(pady = 10)
        self.email_label2.pack(pady = 10)
        self.email_entry2.pack(pady = 10)
        self.full_name2.pack(pady = 10)
        self.full_name_entry2.pack(pady = 10)
        self.sign_up_bt2.grid(row = 0, column = 0)
        self.back_bt.grid(row = 0, column = 1)
        self.sign_up_msg2.grid(row = 1, columnspan = 2)
        self.frame_sign_up.pack(pady = 20)

    def sign_in_widgets(self):
        self.user_name_label = Label(self.sign_in_window, text  = 'Username')
        self.user_name_entry = Entry(self.sign_in_window, width = 35)
        self.pass_word_label = Label(self.sign_in_window, text  = 'Password')
        self.pass_word_entry = Entry(self.sign_in_window, show = '*', width = 35)
        self.sign_in_frame = Frame(self.sign_in_window)
        self.sign_in_bt = Button(self.sign_in_frame, text = 'Sign in')
        self.sign_in_msg = Label(self.sign_in_frame, text = '')
        self.sign_in_bt.bind('<Button-1>', self.pressed_sign_in)
        self.m = Main()

    def place_sign_in_widgets(self):
        self.user_name_label.pack(pady = 10)
        self.user_name_entry.pack(pady = 10)
        self.pass_word_label.pack(pady = 10)
        self.pass_word_entry.pack(pady = 10)
        self.sign_in_bt.pack()
        self.sign_in_msg.pack(pady = 10) 
        self.sign_in_frame.pack(pady = 15)
        
    def pressed_sign_up(self, event):
        m = Main()
        result_sign_up= m.signup(self.user_name_entry2.get(), self.pass_word_entry2.get(), self.birth_day_entry2.get(), self.email_entry2.get(), self.full_name_entry2.get())
        self.sign_up_msg2.config(text = result_sign_up)

    def pressed_sign_in(self, event):
        result_sign_in = self.m.signin(self.user_name_entry.get(), self.pass_word_entry.get())
        if result_sign_in == 'Invalid username or password' or result_sign_in == 'Error':
            self.sign_in_msg.config(text = result_sign_in)
        elif result_sign_in == 'Done':
            if self.user_name_entry.get() == 'admin1' and self.pass_word_entry.get() == 'bookstore2024':
                self.sign_in_window.withdraw()
                AdminMenu(self)
            else:
                self.sign_in_window.withdraw()
                CustomerMenu(self)

    def pressed_back(self, event):
        self.sign_up_window.withdraw()
        self.deiconify()
        
    def close_sign_in_window(self):
        self.sign_in_window.destroy()
        self.destroy()

    def close_sign_up_window(self):
        self.sign_up_window.destroy()
        self.destroy()  
        
class AdminMenu(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Welcome, admin1')
        self.geometry(parent.center_window(190,130))
        self.protocol('WM_DELETE_WINDOW', lambda: self.close_admin_menu(parent))
        self.create_widgets(parent)
        self.place_widgets()
        self.mainloop()

    def create_widgets(self, parent):
        self.frame_1 = Frame(self)
        self.set_bt = Button(self.frame_1, text = '   Set book  ')
        self.display_bt = Button(self.frame_1, text = 'Display data')
        self.update_bt = Button(self.frame_1, text = 'Update data')
        self.delete_bt = Button(self.frame_1, text = 'Delete data')

        self.set_bt.bind('<Button-1>', lambda event :self.set_data_window(event, parent))
        self.display_bt.bind('<Button-1>', self.display_data_window)
        self.update_bt.bind('<Button-1>', self.update_data_window) 
        self.delete_bt.bind('<Button-1>', self.delete_data_window) 
    
    def place_widgets(self):
        self.set_bt.grid(row = 0, column = 0)
        self.display_bt.grid(row = 0, column = 1)
        self.update_bt.grid(row = 1, column = 0) 
        self.delete_bt.grid(row = 1, column = 1)
        self.frame_1.pack(pady = 10, anchor = 'center', expand = True)

    def set_data_window(self, event, parent):
        self.withdraw()
        self.set_window = Toplevel(self)
        self.set_window.geometry(parent.center_window(300,440))
        self.set_data_widgets()
        self.place_set_data_widgets()
        self.set_window.protocol('WM_DELETE_WINDOW', lambda: self.close_set_window(parent))

    def set_data_widgets(self):
        self.folder_l = Label(self.set_window, text = 'Folder')
        self.folder_entry = Entry(self.set_window)
        self.category_l = Label(self.set_window, text = 'Category')
        self.category_entry = Entry(self.set_window)
        self.title_l = Label(self.set_window, text = 'Title')
        self.title_entry = Entry(self.set_window)
        self.ISBN_l = Label(self.set_window, text = 'ISBN')
        self.ISBN_entry = Entry(self.set_window)
        self.author_l = Label(self.set_window, text = 'Author')
        self.author_entry = Entry(self.set_window)
        self.price_l = Label(self.set_window, text = 'Price')
        self.price_entry = Entry(self.set_window)

        self.frame_2 = Frame(self.set_window)
        self.summit_bt = Button(self.frame_2, text = 'Summit')
        self.msg_l = Label(self.frame_2, text= '')
    
    def display_data_window(self, event):
        pass

    def update_data_window(self, event):
        pass

    def delete_data_window(self, event):
        pass 

    def place_set_data_widgets(self):
        self.folder_l.pack(pady = 5)
        self.folder_entry.pack(pady = 5)
        self.category_l.pack(pady = 5) 
        self.category_entry.pack(pady = 5)
        self.title_l.pack(pady = 5)
        self.title_entry.pack(pady = 5) 
        self.ISBN_l.pack(pady = 5) 
        self.ISBN_entry.pack(pady = 5) 
        self.author_l.pack(pady = 5) 
        self.author_entry.pack(pady = 5)
        self.price_l.pack(pady = 5)
        self.price_entry.pack(pady = 5)

        self.summit_bt.grid(row = 0, column = 0, padx = 15)
        self.msg_l.grid(row = 0, column = 1, padx = 15)
        self.frame_2.pack(pady = 20)

    def close_set_window(self, parent):
        self.set_window.destroy()
        self.destroy()
        parent.destroy()

    def close_admin_menu(self, parent):
        self.destroy()
        parent.destroy()

class CustomerMenu(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(parent.center_window(350,350))
        self.mainloop()

if __name__ == '__main__':
    MainWindow()
