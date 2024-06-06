from tkinter import *
from tkinter import ttk
from BookStore import *
from PIL import Image, ImageTk
from tkinter import scrolledtext
from tkinter import messagebox

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
        self.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self, parent))
        self.create_widgets(parent)
        self.place_widgets()
        self.mainloop()

    def create_widgets(self, parent):
        self.frame_1 = Frame(self)
        self.add_bt = Button(self.frame_1, text = '   Add book  ')
        self.display_bt = Button(self.frame_1, text = 'Display data')
        self.update_bt = Button(self.frame_1, text = 'Update data')
        self.delete_bt = Button(self.frame_1, text = 'Delete data')

        self.add_bt.bind('<Button-1>', lambda event: self.add_data_window(event, parent))
        self.display_bt.bind('<Button-1>', lambda event: self.display_data_window(event, parent))
        self.update_bt.bind('<Button-1>', lambda event :self.update_data_window(event, parent))
        self.delete_bt.bind('<Button-1>', lambda event :self.delete_data_window(event, parent)) 
    
    def place_widgets(self):
        self.add_bt.grid(row = 0, column = 0)
        self.display_bt.grid(row = 0, column = 1)
        self.update_bt.grid(row = 1, column = 0) 
        self.delete_bt.grid(row = 1, column = 1)
        self.frame_1.pack(pady = 10, anchor = 'center', expand = True)

    def add_data_window(self, event, parent):
        self.withdraw()
        self.add_window = Toplevel(self)
        self.add_window.title(' Add Book')
        self.add_window.geometry(parent.center_window(300,460))
        self.add_data_widgets()
        self.place_add_data_widgets()
        self.add_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.add_window, parent))

    def display_data_window(self, event, parent):
        self.withdraw()
        self.display_window = Toplevel(self)
        self.display_window.title(' Display Data')
        self.display_window.geometry(parent.center_window(300,200))
        self.display_data_widgets()
        self.place_display_data_widgets()
        self.display_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.display_window, parent))

    def update_data_window(self, event, parent):
        self.withdraw()
        self.update_window = Toplevel(self)
        self.update_window.title(' Update Data')
        self.update_window.geometry(parent.center_window(300,330))
        self.update_data_widgets()
        self.place_update_data_widgets()
        self.update_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.update_window, parent))

    def delete_data_window(self, event, parent):
        self.withdraw()
        self.delete_window = Toplevel(self)
        self.delete_window.title(' Delete Data')
        self.delete_window.geometry(parent.center_window(300,160))
        self.delete_data_widgets()
        self.place_delete_data_widgets()
        self.delete_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.delete_window, parent))

    def add_data_widgets(self):
        self.folder_l = Label(self.add_window, text = 'Folder')
        self.folder_entry = Entry(self.add_window)
        self.category_l = Label(self.add_window, text = 'Category')
        self.category_entry = Entry(self.add_window)
        self.title_l = Label(self.add_window, text = 'Title')
        self.title_entry = Entry(self.add_window)
        self.ISBN_l = Label(self.add_window, text = 'ISBN')
        self.ISBN_entry = Entry(self.add_window)
        self.author_l = Label(self.add_window, text = 'Author')
        self.author_entry = Entry(self.add_window)
        self.price_l = Label(self.add_window, text = 'Price')
        self.price_entry = Entry(self.add_window)

        self.frame_2 = Frame(self.add_window)
        self.summit_bt2 = Button(self.frame_2, text = 'Summit')
        self.back_bt2 = Button(self.frame_2, text = 'Back')
        self.msg_l2 = Label(self.frame_2, text= '')
        self.back_bt2.bind('<Button-1>', lambda event :self.pressed_back_bt(event, self.add_window))
        self.summit_bt2.bind('<Button-1>', self.pressed_add_book)
   
    def display_data_widgets(self):
        self.path_display_l = Label(self.display_window, text = 'Path')
        self.path_display_entry = Entry(self.display_window, width = 45)

        self.frame_3 = Frame(self.display_window)
        self.summit_bt3 = Button(self.frame_3, text = 'Summit')
        self.back_bt3 = Button(self.frame_3, text = 'Back')
        self.back_bt3.bind('<Button-1>', lambda event :self.pressed_back_bt(event, self.display_window))
        self.summit_bt3.bind('<Button-1>', self.pressed_display_data)

    def display_result_window(self):
        self.result_window = Toplevel()
        self.result_window.title(' Result')
        self.display_result_widgets()

    def display_result_widgets(self):
        try:
            md = ManageDatabase()
            result = list(md.get_data(self. path_display_entry.get()))
            result = '\n'.join(result)
        except: result = ['Error']
        self.result_text = scrolledtext.ScrolledText(self.result_window, wrap = WORD, width = 40, height = 10)
        self.result_text.insert(END, result)
        self.result_text.config(state = DISABLED)
        self.result_text.pack()
    
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

    def place_add_data_widgets(self):
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

    def on_close(self, window, parent):
        window.destroy()
        parent.destroy()

    def pressed_back_bt(self, event, window):
        window.withdraw()
        self.deiconify()

    def pressed_add_book(self, event):
        md = ManageDatabase()
        result = md.add_book(self.folder_entry.get(), self.category_entry.get(), self.title_entry.get(), self.ISBN_entry.get(), self.author_entry.get(), self.price_entry.get())
        self.msg_l2.config(text = result)

    def pressed_display_data(self, event):
        self.display_result_window()

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
        self.title(' Customer Menu')
        self.geometry(parent.center_window(350,220))
        self.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self, parent))
        self.main_widgets(parent)
        self.mainloop()

    def main_widgets(self, parent):
        self.get_image()
        self.create_widgets(parent)
        self.place_widgets()

    def create_widgets(self, parent):
        self.frame1 = Frame(self)
        self.welcome_l = Label(self.frame1, text = f'Welcome, {parent.user_name_entry.get()}')
        self.browse_bt = Button(self.frame1, image = self.ready_browse_img)
        self.buy_bt = Button(self.frame1, image = self.ready_buy_img)
        self.order_hist_bt = Button(self.frame1, image = self.ready_order_hist_img)
        self.browse_l = Label(self.frame1, text = 'Browse')
        self.buy_l = Label(self.frame1, text = 'Buy')
        self.order_hist_l = Label(self.frame1, text = 'Order History')

        self.browse_bt.bind('<Button-1>', lambda event: self.create_browse_menu_window(event, parent))
        self.buy_bt.bind('<Button-1>', lambda event: self.create_buy_menu_window(event, parent))
        self.order_hist_bt.bind('<Button-1>', lambda event: self.create_order_hist_window(event, parent))

    def create_browse_menu_window(self, event, parent):
        self.browse_window = Toplevel()
        self.browse_window.title('Browse Menu')
        self.browse_window.geometry(parent.center_window(250,160))
        self.browse_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.browse_window, parent))
        self.create_browse_menu_widgets(parent)
        self.place_browse_menu_widgets()

    def create_browsed_result_window(self, event, parent):
        self.browsed_result_window = Toplevel()
        mc = ManageCustomer(parent.user_name_entry.get())
        if self.category_var.get() != '' and self.title_entry.get() != '':
            result = mc.browse_title(self.category_var.get(), self.title_entry.get())
            result_label = Label(self.browsed_result_window, text = result, wraplength = 150)
            result_label.pack(anchor = 'w')
        elif self.category_var.get() != '' and self.title_entry.get() == '':
            books = mc.browse_category(self.category_var.get())
            result = '\n'.join(books)
            result_text = scrolledtext.ScrolledText(self.browsed_result_window, wrap = WORD,width=40, height=10)
            result_text.insert(END, result)
            result_text.config(state=DISABLED)
            result_text.pack()

    def create_buy_menu_window(self, event, parent):
        self.buy_window = Toplevel()
        self.buy_window.title('Browse Menu')
        self.buy_window.geometry(parent.center_window(250,200))
        self.buy_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.buy_window, parent))
        self.create_buy_menu_widgets(parent)
        self.place_buy_menu_widgets()

    def create_check_out_window(self, event, parent):
        self.buy_window.withdraw()
        self.check_out_window = Toplevel()
        self.check_out_window.title('Cart')
        self.check_out_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.check_out_window, parent))
        self.create_check_out_widgets(parent)
        self.place_check_out_window_widgets()

    def create_order_hist_window(self, event, parent):
        self.withdraw()
        self.order_hist_window = Toplevel()
        self.order_hist_window.title('Order History')
        self.create_order_hist_widgets(parent)
        self.place_order_hist_widgets()
        self.order_hist_window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.order_hist_window, parent))
    
    def create_browse_menu_widgets(self, parent):
        self.withdraw()
        self.category_title_widgets(parent, self.browse_window)
        self.frame2 = Frame(self.browse_window)
        self.ok_bt = Button(self.frame2, text = 'OK')
        self.back_bt = Button(self.frame2, text = 'Back')

        self.ok_bt.bind('<Button-1>', lambda event : self.create_browsed_result_window(event, parent))
        self.back_bt.bind('<Button-1>', lambda event: self.pressed_back(event, self.browse_window))

    def category_title_widgets(self, parent, window):
        mc = ManageCustomer(parent.user_name_entry.get())
        self.category_var = StringVar()
        self.category_list = mc.get_category()
        self.category_var.set('Select Category')
        self.category_option = OptionMenu(window, self.category_var, *self.category_list)
        self.title_l = Label(window, text = 'Title')
        self.title_entry = Entry(window)
    
    def create_buy_menu_widgets(self, parent):
        self.withdraw()
        self.category_title_widgets(parent,self.   buy_window)
        self.frame3 = Frame(self.buy_window)
        self.add_to_cart_bt = Button(self.frame3,   text = 'Add to Cart')
        self.my_cart_bt = Button(self.frame3,text = 'My Cart')
        self.frame4 = Frame(self.buy_window)
        self.back_bt2 = Button(self.frame4, text =  'Back')
        self.clear_cart_bt = Button(self.frame4,text = 'Clear cart')
        self.add_to_cart_bt.bind('<Button-1>',lambda   event: self.add_status(event,parent))
        self.my_cart_bt.bind('<Button-1>',lambda event: self.create_check_out_window(event,  parent))
        self.back_bt2.bind('<Button-1>',lambda     event: self.pressed_back(event, self.   buy_window))
        self.clear_cart_bt.bind('<Button-1>',lambda event: self.clear_card_process(event, parent))

    def create_check_out_widgets(self, parent):
        mc = ManageCustomer(parent.user_name_entry.get())
        if mc.show_cart() is None:
            cart_list = 'Empty'
        else:
            cart = [order[0] for order in mc.show_cart()]
            cart_list = "\n".join(cart)
        self.cart_text = scrolledtext.ScrolledText  (self.check_out_window, wrap = WORD,  width=40, height=10)
        self.cart_text.insert(END, cart_list)
        self.cart_text.config(state = DISABLED)
        self.total_l = Label(self.check_out_window,     text = 'Total')     
        self.frame5 = Frame(self.check_out_window)
        self.back_bt3 = Button(self.frame5, text=  'Back')
        self.check_out_bt = Button(self.frame5,text   = 'Check out')

        self.back_bt3.bind('<Button-1>', self. back_to_buy_menu)
        self.check_out_bt.bind('<Button-1>',lambda    event: self.pressed_check_out2(event, parent))
        
    def create_order_hist_widgets(self, parent):
        mc = ManageCustomer(parent.user_name_entry.get())
        order_hist_list = [hist[0] for hist in mc.show_order_history()]
        order_hist = '\n'.join(order_hist_list)
        self.order_hist_text = scrolledtext.ScrolledText(self.order_hist_window, wrap = WORD, width = 40, height = 10)
        self.order_hist_text.insert(END, order_hist)
        self.order_hist_text.config(state = DISABLED)
        self.back_bt4 = Button(self.order_hist_window, text = 'Back')

        self.back_bt4.bind('<Button-1>', lambda event: self.pressed_back(event, self.order_hist_window))

    def place_order_hist_widgets(self):
        self.order_hist_text.pack()
        self.back_bt4.pack(pady = 15)

    def place_browse_menu_widgets(self):
        self.category_option.pack(pady = 10)
        self.title_l.pack(pady = 10)
        self.title_entry.pack()
        self.frame2.pack(pady = 10)
        self.ok_bt.grid(row = 0, column = 0)
        self.back_bt.grid(row = 0, column = 1, padx = 10)

    def place_buy_menu_widgets(self):
        self.category_option.pack(pady = 10)
        self.title_l.pack(pady = 10)
        self.title_entry.pack()
        self.frame3.pack(pady = 15)
        self.frame4.pack()
        self.add_to_cart_bt.grid(row = 0, column = 0, padx = 10)
        self.my_cart_bt.grid(row = 0, column = 1)
        self.back_bt2.grid(row = 0, column = 0)
        self.clear_cart_bt.grid(row = 0, column = 1)
    
    def place_check_out_window_widgets(self):
        self.cart_text.pack()        
        self.total_l.pack()
        self.frame5.pack(pady = 10)
        self.back_bt3.grid(row = 0, column = 0, padx = 10)
        self.check_out_bt.grid(row = 0, column = 1)

    def pressed_back(self, event, window):
        window.withdraw()
        self.deiconify()

    def place_widgets(self):
        self.frame1.pack(anchor = 'center')
        self.welcome_l.grid(row = 0, column = 0, pady = 10)
        self.browse_bt.grid(row = 1, column = 0, pady = 10) 
        self.buy_bt.grid(row = 1, column = 1, pady = 10)
        self.order_hist_bt.grid(row = 1, column = 2, pady = 10)
        self.browse_l.grid(row = 2, column = 0)
        self.buy_l.grid(row = 2, column = 1)
        self.order_hist_l.grid(row = 2, column = 2)

    def pressed_check_out2(self, event, parent):            
        try:
            mc = ManageCustomer(parent.user_name_entry.get())
            total = mc.show_total()
            self.total_l.config(text = f'Total {total} THB', background = '#6B8A7A')
        except:
            self.total_l.config(text = 'Error')

    def get_image(self):
        browse_img = Image.open('magnifying_glass.jpg')
        resized_browse_img = browse_img.resize((100,100))
        self.ready_browse_img = ImageTk.PhotoImage(resized_browse_img)
        buy_img = Image.open('cart_original.jpg')
        resized_buy_img = buy_img.resize((100,100))
        self.ready_buy_img = ImageTk.PhotoImage(resized_buy_img)
        order_hist_img = Image.open('cart.jpg')
        resized_order_hist_img = order_hist_img.resize((100,100))
        self.ready_order_hist_img = ImageTk.PhotoImage(resized_order_hist_img)
  
    def add_status(self, event, parent):
        mc = ManageCustomer(parent.user_name_entry.get())
        try:
            result = mc.buy_menu(self.category_var.get(), self.title_entry.get())
            messagebox.showinfo('Cart status', message = result)
        except: messagebox.showerror('Cart status', 'Error')
    
    def back_to_buy_menu(self, event):
        self.check_out_window.withdraw()
        self.deiconify()

    def clear_card_process(self, event,  parent):
        m = ManageDatabase()        
        m.delete_data(f'users/{parent.user_name_entry.get()}/cart')
        messagebox.showinfo('Cart status', 'Done')

    def on_close(self, window, parent):
        window.destroy()
        parent.destroy()
