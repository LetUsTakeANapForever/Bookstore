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
        return str("'"+self.key+"'")
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return str("'"+self.value+"'")
    
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_ISBN(self, ISBN):
        self.ISBN = ISBN
    
    def get_ISBN(self):
        return str("'"+self.ISBN+"'")
    
    def set_author(self, author):
        self.author = author
    
    def get_author(self):
        return str("'"+self.author+"'")
    
    def set_price(self, price):
        self.price = price
    
    def get_price(self):
        return str("'"+self.price+"'")

    def set_book(self):
        print('Set Book Menu')
        folder_input = input('Enter folder name to set data:')
        child_input = input('Enter category name:  ')
        
        title_input = input('Title : ')
        ISBN_input = input('ISBN : ')
        author_input = input('Author : ')
        price_input = input('Price : ')

        self.set_title(title_input)
        self.set_ISBN(ISBN_input)
        self.set_author(author_input)
        self.set_price(price_input)
        try:
            ref  = db.reference(folder_input)
            users_ref = ref.child(child_input)
            users_ref.set({
                self.get_title() : {
                    'ISBN' : self.get_ISBN(),
                    'author' : self.get_author(),
                    'price' : self.get_price()
                }
            })
        except:
            print('Error')

    def get_data(self):
        print('Load Book Menu')
        try:
            path_input = input('Enter path(s) to load data:')
            ref  = db.reference(path_input)
            return (ref.get())
        except:
            return 'Error'

    def update_data(self):
        print('Update Book Menu')
        child_input = input('Enter folder name:  ')
        path_input = input('Enter path(s) to update data:')
        update_input = input('update data to:')
        try:
            self.set_value(path_input)
            users_ref = self.ref.child(child_input)
            users_ref.update({
                self.get_value() : f'{update_input}'
            })
        except:
            print('Error')
    
    def delete_data(self):
        print('Delete Book Menu')
        path_input = input('Enter path(s) name :  ')
        try:
            hopper_ref = self.ref.child(path_input)
            hopper_ref.delete()
            return f'Deleted data in {self.ref}/{hopper_ref}'
        except:
            print('Error')

class Main:

    def __init__(self):
        self.ref  = db.reference('users')

    def signup(self, username, pass_word, birthday, email, fullname): 
        print('Signup Menu')
        user_name_input = username
        pass_word_input = pass_word
        birth_day_input = birthday
        email_input = str(email).lower()
        full_name_input = fullname

        users_ref = self.ref.child(user_name_input)
        users_ref.update({
            'Birthday' : birth_day_input,
            'Email' : email_input.lower(),
            'Fullname' : full_name_input,
            'Password' : pass_word_input
        })
        return 'Done'

    def signin(self, username, pass_word):
        self.user_name_input = username
        self.pass_word_input = pass_word 
        try:
            self.pass_word_users = self.ref.child(f'{self.user_name_input}/Password')
            while not self.user_name_input in self.ref.get() or not  self.pass_word_input == self.pass_word_users.get():
                    return 'Invalid username or password'
            return 'Done'
        except:
            return 'Error'

    def show_menu(self):
        print('Menu'.center(14, '-'))
        print('1.Set data')
        print('2.Display data')
        print('3.Update data')
        print('4.Delete data')
        print('5.Open menu')
        print('6.Exit')

    def menu(self):
        self.show_menu()
        while True:
            my_input = input('Select : ')
            data = ManageDatabase()
            if my_input == '6':
                break
            elif my_input == '1':
                data.set_book()
            elif my_input == '2':
                print(data.get_data())
            elif my_input == '3':
                print(data.update_data())
            elif my_input == '4':
                print(data.delete_data())
            elif my_input == '5':
                self.show_menu()
                continue
            else: 
                print('Try again')
            print('Done'+'\nPress 5 to open menu')

    def run_main(self):
        print('Welcome'.center(26, '-'))
        print('1.Sign in')
        print('2.Sign up')
        while True:
            select_input = input('Select : ')
            if select_input == '1':
                result = self.signin()
                if result == 'Banned' or result == 'Error':
                    print(result)
                    break
                else:
                    print(result)
                    self.menu()
                    break
            elif select_input == '2':
                self.signup()
                self.run_main()
                break
            else:
                print('Try again')

class Cart:
    pass
