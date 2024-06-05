import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class ManageDatabase:
    def __init__(self):
        self.ref  = db.reference('')
        self.title = None
        self.ISBN = None
        self.author = None
        self.price = None

    def set_key(self, key):
        self.key = key
    
    def get_key(self):
        return str(self.key)
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return str(self.value)
    
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_ISBN(self, ISBN):
        self.ISBN = ISBN
    
    def get_ISBN(self):
        return str(self.ISBN)
    
    def set_author(self, author):
        self.author = author
    
    def get_author(self):
        return str(self.author)
    
    def set_price(self, price):
        self.price = price
    
    def get_price(self):
        return str(self.price)

    def add_book(self, folder, category, title, ISBN, author, price):
        self.set_title(title)
        self.set_ISBN(ISBN)
        self.set_author(author)
        self.set_price(price)
        folder = str(folder).lower()
        category = str(category).lower()
        try:
            ref  = db.reference(folder)
            users_ref = ref.child(category)
            users_ref.update({
                self.get_title() : {
                    'ISBN' : self.get_ISBN(),
                    'author' : self.get_author(),
                    'price' : self.get_price()
                }
            })
            return 'Done'
        except:
            return('Error')

    def get_data(self, path):
        try:
            ref  = db.reference(path)
            return ('Data',ref.get())
        # return csv file
        except:
            return 'Error'

    def update_data(self, path, key, change):
        try:
            users_ref = self.ref.child(path)
            self.set_key(key)
            self.set_value(change)
            users_ref.update({
                self.get_key() : self.get_value()
            })
            return 'Done'
        except:
            return 'Error'
    
    def delete_data(self, path):
        try:
            hopper_ref = self.ref.child(path)
            hopper_ref.delete()
            return f'Deleted data in {path}'
        except:
            return 'Error'

class Main:

    def __init__(self):
        self.ref  = db.reference('users')

    def signup(self, username, pass_word, birthday, email, fullname): 
        user_name_input = username
        pass_word_input = pass_word
        birth_day_input = birthday
        email_input = str(email).lower()
        full_name_input = fullname

        users_ref = self.ref.child(user_name_input)
        users_ref.update({
            'birthday' : birth_day_input,
            'email' : email_input.lower(),
            'fullname' : full_name_input,
            'password' : pass_word_input
        })
        return 'Done'

    def signin(self, username, pass_word):
        self.user_name_input = username
        self.pass_word_input = pass_word 
        try:
            self.pass_word_users = self.ref.child(f'{self.user_name_input}/password')
            while not self.user_name_input in self.ref.get() or not  self.pass_word_input == self.pass_word_users.get():
                    return 'Invalid username or password'
            return 'Done'
        except:
            return 'Error'

class ManageCustomer:
    def __init__(self, user):
        self.current_user = user
        self.ref = db.reference('')
        self.ref_books = db.reference('books')
        self.ref_users = db.reference('users')
        self.cart_ref = self.ref_users.child(self.current_user+'/cart')
        self.history_ref = self.ref_users.child(self.current_user+'/order_history')
        self.total = 0

    def set_total(self, price, qty):
        self.total = self.total + float(price)*qty
    
    def get_total(self):
        return self.total
    
    def get_category(self):
        try:
            self.categories = list(self.ref_books.get())
            return self.categories
        except Exception as e: print(e) 

    def browse_title(self, category, title):
        try:
            ISBN_ref = self.ref_books.child(category+'/' +title+'/ISBN')
            author_ref = self.ref_books.child(category+'/'   +title+'/author')
            price_ref = self.ref_books.child(category+'/'    +title+'/price')
            result = f'Title  : {title}\nISBN   : {ISBN_ref.get()}\nAuthor : {author_ref.get()}\nPrice  : {price_ref.get()}'
            if (ISBN_ref.get() or author_ref.get() or price_ref.get()) is None:
                return ' Error'
            return result
        except: return 'Error'

    def browse_category(self, category):
            try:
                books = list(self.ref_books.child(category).get())
                return books
            except: return 'Error'

    def buy_menu(self, category, title):
        try:
            price_ref = self.ref_books.child(category+'/'+title+'/price')
            if price_ref.get() is None:
                return 'Error'
            self.add_to_cart(title, price_ref.get())
            return 'Successfully added'
        except: print('Error')

    def show_total(self):
        try:
            in_cart = list(self.cart_ref.get())
            for order in in_cart:
                if not order is None:    
                    price_ref = self.ref_users.child(self.current_user+'/cart/'+order+'/price')
                    qty_ref = self.ref_users.child(self.current_user+'/cart/'+order+'/quantity')
                    self.add_to_order_history(order, price_ref.get())
                    self.set_total(price_ref.get(), qty_ref.get())
            self.cart_ref.delete()
            return '%.2f' %self.get_total()
        except: return 'Error'
    
    def show_cart(self):
        cart_list = []
        try:
            in_cart = list(self.cart_ref.get())
            for order in in_cart:
                if not order is None:    
                    price_ref = self.ref_users.child(self.current_user+'/cart/'+order+'/price')
                    qty_ref = self.ref_users.child(self.current_user+'/cart/'+order+'/quantity')
                    item = [(f'{order} {price_ref.get()} THB (qty:{qty_ref.get()})')]
                    cart_list.append(item)
            return cart_list
        except: print('Empty')

    def add_to_cart(self, title, price):
        try:
            qty = 1
            if not self.cart_ref.get() is None:
                if title in list(self.cart_ref.get()):
                    qty_ref = self.ref_users.child(self.current_user+'/cart/'+title+'/quantity')
                    qty = qty_ref.get() + 1
            self.cart_ref.update({
                title : {
                    'price' : price,
                    'quantity' : qty
                }      
            })
        except: print('Error')

    def add_to_order_history(self, title, price):
        try:
            cart_qty_ref = self.ref_users.child(self.current_user+'/cart/'+title+'/quantity')
            qty = cart_qty_ref.get()
            if not self.history_ref.get() is None:
                if title in list(self.history_ref.get()):
                    qty_ref = self.ref_users.child(self.current_user+'/order_history/'+title+'/quantity')
                    qty = qty_ref.get() + cart_qty_ref.get()        
            self.history_ref.update({
                title : {
                    'price' : price,
                    'quantity' : qty
                }  
            })
        except: print('Error')

    def show_order_history(self):
        order_hist = []
        try:
            if self.history_ref.get() is None:
                order_hist = [['Empty']]
            else:
                orders_hist = list(self.history_ref.get())
                for order in orders_hist:
                    price_ref = self.ref_users.child(f'{self.current_user}/order_history/{order}/price')
                    qty_ref = self.ref_users.child(f'{self.current_user}/order_history/{order}/quantity')
                    hist_list = [f'- {order} {price_ref.get()} THB (qty:{qty_ref.get()})']
                    order_hist.append(hist_list)
            return order_hist
        except: return 'Error'
