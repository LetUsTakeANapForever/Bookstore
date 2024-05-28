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

    def set_book(self, folder, category, title, ISBN, author, price):
        self.set_title(title)
        self.set_ISBN(ISBN)
        self.set_author(author)
        self.set_price(price)
        try:
            ref  = db.reference(folder)
            users_ref = ref.child(category)
            users_ref.set({
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

class Cart:
    pass
