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
        self.back_bt.bind('<Button-1>', self.sign_up_pressed_back)
    
    def sign_in_widgets(self):
        self.user_name_label = Label(self.sign_in_window, text  = 'Username')
        self.user_name_entry = Entry(self.sign_in_window, width = 35)
        self.pass_word_label = Label(self.sign_in_window, text  = 'Password')
        self.pass_word_entry = Entry(self.sign_in_window, show = '*', width = 35)
        self.sign_in_frame = Frame(self.sign_in_window)
        self.sign_in_bt = Button(self.sign_in_frame, text = 'Sign in')
        self.back_bt = Button(self.sign_in_frame, text = 'Back')
        self.sign_in_msg = Label(self.sign_in_frame, text = '')
        self.sign_in_bt.bind('<Button-1>', self.pressed_sign_in)
        self.back_bt.bind('<Button-1>', self.sign_in_pressed_back)
        

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

    def place_sign_in_widgets(self):
        self.user_name_label.pack(pady = 10)
        self.user_name_entry.pack(pady = 10)
        self.pass_word_label.pack(pady = 10)
        self.pass_word_entry.pack(pady = 10)
        self.sign_in_bt.grid(row = 0, column = 0, padx = 10)
        self.back_bt.grid(row = 0, column = 1)
        self.sign_in_msg.grid(row = 1, columnspan = 2)
        self.sign_in_frame.pack(pady = 15)
        
    def pressed_sign_up(self, event):
        m = Main()
        result_sign_up= m.signup(self.user_name_entry2.get(), self.pass_word_entry2.get(), self.birth_day_entry2.get(), self.email_entry2.get(), self.full_name_entry2.get())
        self.sign_up_msg2.config(text = result_sign_up)

    def pressed_sign_in(self, event):
        m = Main()
        result_sign_in = m.signin(self.user_name_entry.get(), self.pass_word_entry.get())
        if result_sign_in == 'Invalid username or password' or result_sign_in == 'Error':
            self.sign_in_msg.config(text = result_sign_in)
        elif result_sign_in == 'Done':
            if self.user_name_entry.get() == 'admin1' and self.pass_word_entry.get() == 'bookstore2024':
                self.sign_in_window.withdraw()
                AdminMenu(self)
            else:
                self.sign_in_window.withdraw()
                CustomerMenu(self)

    def sign_up_pressed_back(self, event):
        self.sign_up_window.withdraw()
        self.deiconify()

    def sign_in_pressed_back(self, event):
        self.sign_in_window.withdraw()
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

        self.set_bt.bind('<Button-1>', lambda event: self.set_data_window(event, parent))
        self.display_bt.bind('<Button-1>', lambda event: self.display_data_window(event, parent))
        self.update_bt.bind('<Button-1>', lambda event :self.update_data_window(event, parent))
        self.delete_bt.bind('<Button-1>', lambda event :self.delete_data_window(event, parent)) 
    
    def place_widgets(self):
        self.set_bt.grid(row = 0, column = 0)
        self.display_bt.grid(row = 0, column = 1)
        self.update_bt.grid(row = 1, column = 0) 
        self.delete_bt.grid(row = 1, column = 1)
        self.frame_1.pack(pady = 10, anchor = 'center', expand = True)

    def set_data_window(self, event, parent):
        self.withdraw()
        self.set_window = Toplevel(self)
        self.set_window.title(' Set Book')
        self.set_window.geometry(parent.center_window(300,460))
        self.set_data_widgets()
        self.place_set_data_widgets()
        self.set_window.protocol('WM_DELETE_WINDOW', lambda: self.close_set_window(parent))

    def display_data_window(self, event, parent):
        self.withdraw()
        self.display_window = Toplevel(self)
        self.display_window.title(' Display Data')
        self.display_window.geometry(parent.center_window(300,200))
        self.display_data_widgets()
        self.place_display_data_widgets()
        self.display_window.protocol('WM_DELETE_WINDOW', lambda: self.close_display_window(parent))

    def update_data_window(self, event, parent):
        self.withdraw()
        self.update_window = Toplevel(self)
        self.update_window.title(' Update Data')
        self.update_window.geometry(parent.center_window(300,330))
        self.update_data_widgets()
        self.place_update_data_widgets()
        self.update_window.protocol('WM_DELETE_WINDOW', lambda: self.close_update_window(parent))

    def delete_data_window(self, event, parent):
        self.withdraw()
        self.delete_window = Toplevel(self)
        self.delete_window.title(' Update Data')
        self.delete_window.geometry(parent.center_window(300,160))
        self.delete_data_widgets()
        self.place_delete_data_widgets()
        self.delete_window.protocol('WM_DELETE_WINDOW', lambda: self.close_delete_window(parent))

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
        self.summit_bt2 = Button(self.frame_2, text = 'Summit')
        self.back_bt2 = Button(self.frame_2, text = 'Back')
        self.msg_l2 = Label(self.frame_2, text= '')
        self.back_bt2.bind('<Button-1>', lambda event :self.pressed_back_bt(event, self.set_window))
        self.summit_bt2.bind('<Button-1>', self.pressed_set_book)
   
    def display_data_widgets(self):
        self.path_display_l = Label(self.display_window, text = 'Path')
        self.path_display_entry = Entry(self.display_window, width = 45)

        self.frame_3 = Frame(self.display_window)
        self.summit_bt3 = Button(self.frame_3, text = 'Summit')
        self.back_bt3 = Button(self.frame_3, text = 'Back')
        self.msg_l3 = Label(self.frame_3, text = '')
        self.back_bt3.bind('<Button-1>', lambda event :self.pressed_back_bt(event, self.display_window))
        self.summit_bt3.bind('<Button-1>', self.pressed_display_data)
    
    def update_data_widgets(self):
        self.path_l = Label(self.update_window, text = 'Path')
        self.path_entry = Entry(self.update_window)
        self.key_l = Label(self.update_window, text = 'Key')
        self.key_entry = Entry(self.update_window)
        self.change_l = Label(self.update_window, text = 'Change to')
        self.change_entry = Entry(self.update_window)

        self.frame_4 = Frame(self.update_window)
        self.summit_bt4 = Button(self.frame_4, text = 'Summit')
        self.back_bt4 = Button(self.frame_4, text = 'Back')
        self.msg_l4 = Label(self.frame_4, text = '')
        self.back_bt4.bind('<Button-1>', lambda event :self.pressed_back_bt(event, self.update_window))
        self.summit_bt4.bind('<Button-1>', self.pressed_update_data)

    def delete_data_widgets(self):
        self.path_l2 = Label(self.delete_window, text = 'Path')
        self.path_entry2 = Entry(self.delete_window, width = 45)
        
        self.frame_5 = Frame(self.delete_window)
        self.summit_bt5 = Button(self.frame_5, text = 'Summit')
        self.back_bt5 = Button(self.frame_5, text = 'Back')
        self.msg_l5 = Label(self.frame_5, text = '')
        self.back_bt5.bind('<Button-1>', lambda event :self.pressed_back_bt(event, self.delete_window))
        self.summit_bt5.bind('<Button-1>', self.pressed_delete_data)

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

        self.frame_2.pack(pady = 15)
        self.summit_bt2.grid(row = 0, column = 0, padx = 10)
        self.back_bt2.grid(row = 0, column = 1, padx = 10)
        self.msg_l2.grid(row = 1, columnspan = 2, pady = 5)
        
    def place_display_data_widgets(self):
        self.path_display_l.pack(pady = 15)
        self.path_display_entry.pack(pady = 15)
        self.frame_3.pack(pady = 15)
        self.summit_bt3.grid(row = 0, column = 0, padx =10)
        self.back_bt3.grid(row = 0, column = 1)
        self.msg_l3.grid(row = 1, columnspan = 2, pady = 5)

    def place_update_data_widgets(self):
        self.path_l.pack(pady = 10)
        self.path_entry.pack(pady = 10)
        self.key_l.pack(pady = 10)
        self.key_entry.pack(pady = 10)
        self.change_l.pack(pady = 10)
        self.change_entry.pack(pady = 10)
        self.frame_4.pack(pady = 15)
        self.summit_bt4.grid(row = 0, column = 0, padx = 10)
        self.back_bt4.grid(row = 0, column = 1)
        self.msg_l4.grid(row = 1, columnspan = 2,pady = 5)

    def place_delete_data_widgets(self):
        self.path_l2.pack(pady = 10)
        self.path_entry2.pack(pady = 10)
        self.frame_5.pack(pady = 15)
        self.summit_bt5.grid(row = 0, column = 0, padx = 10)
        self.back_bt5.grid(row = 0, column = 1)
        self.msg_l5.grid(row = 1, columnspan = 2, pady = 5)

    def close_display_window(self, parent):
        self.display_window.destroy()
        self.destroy()
        parent.destroy()

    def close_set_window(self, parent):
        self.set_window.destroy()
        self.destroy()
        parent.destroy()

    def close_update_window(self, parent):
        self.update_window.destroy()
        self.destroy()
        parent.destroy()

    def close_delete_window(self, parent):
        self.delete_window.destroy()
        self.destroy()
        parent.destroy()

    def close_admin_menu(self, parent):
        self.destroy()
        parent.destroy()

    def pressed_back_bt(self, event, window):
        window.withdraw()
        self.deiconify()

    def pressed_set_book(self, event):
        md = ManageDatabase()
        result = md.set_book(self.folder_entry.get(), self.category_entry.get(), self.title_entry.get(), self.ISBN_entry.get(), self.author_entry.get(), self.price_entry.get())
        self.msg_l2.config(text = result)

    def pressed_display_data(self, event):
        md = ManageDatabase()
        result = md.get_data(self.path_display_entry.get())
        self.msg_l3.config(text = result)

    def pressed_update_data(self, event):
        md = ManageDatabase()
        result = md.update_data(self.path_entry.get(), self.key_entry.get(), self.change_entry.get())
        self.msg_l4.config(text = result)

    def pressed_delete_data(self, event):
        md = ManageDatabase()
        result = md.delete_data(self.path_entry2.get())
        self.msg_l5.config(text = result)

class CustomerMenu(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(parent.center_window(350,350))
        self.mainloop()

if __name__ == '__main__':
    MainWindow()
