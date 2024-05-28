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
            path_input = input('Enter path to load data:')
            ref  = db.reference(path_input)
            return (ref.get())
        except:
            return 'Error'

    def update_data(self):
        print('Update Book Menu')
        child_input = input('Enter folder name:  ')
        path_input = input('Enter path to update data:')
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
        path_input = input('Enter path name :  ')
        try:
            hopper_ref = self.ref.child(path_input)
            hopper_ref.delete()
            return f'Deleted data in {self.ref}/{hopper_ref}'
        except:
            print('Error')

class Main:

    def __init__(self):
        self.ref  = db.reference('users')
        self.run_main()

    def signup(self): 
        print('Signup Menu')
        user_name_input = input('Username : ')
        pass_word_input = input('Password : ')
        birth_day_input = input('Birthday (YY-MM-DD, e.g.2004-06-18) : ')
        email_input = input('Email : ').lower()
        full_name_input = input('Fullname : ')

        users_ref = self.ref.child(user_name_input)
        users_ref.update({
            'birthday' : birth_day_input,
            'email' : email_input,
            'fullname' : full_name_input,
            'password' : pass_word_input
        })

    def signin(self):
        print('Signin Menu')
        self.user_name_input = input('Username : ')
        self.pass_word_input = input('Password : ')
        self.count = 1
        try:
            if self.user_name_input == 'admin1' and self.pass_word_input == 'bookstore2024':
                return 'admin'
            self.pass_word_users = self.ref.child(f'{self.user_name_input}/password')
            while not self.user_name_input in self.ref.get() or not  self.pass_word_input == self.pass_word_users.get():
                if self.count < 3:
                    self.count += 1
                    print('Try again\n')
                    self.user_name_input = input('Username : ')
                    self.pass_word_input = input('Password : ')
                elif self.count >= 3:
                    return 'Banned'
            return ('Done')
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
                elif result == 'admin':
                    print(result)
                    self.menu()
                    break
                else:
                    print(result)
                    CustomerMenu(self)
                    break
            elif select_input == '2':
                self.signup()
                self.run_main()
                break
            else:
                print('Try again')

class CustomerMenu:
    def __init__(self, parent):
        self.ref = db.reference('books')
        self.total = 0
        print('-'*20)
        print(f'Welcome, {parent.user_name_input}')
        self.select_menu()

    def show_customer_menu(self):
        print('-'*20)
        print('1.Browse')
        print('2.Buy')
        print('3.Exit')

    def select_menu(self):
        self.show_customer_menu()
        while True:
            selected_input = input('Select : ')
            if selected_input == '1':
                print(self.browse_menu())
                self.show_customer_menu()
            elif selected_input == '2':
                self.buy_menu()
                self.show_customer_menu()
            elif selected_input == '3':
                break
            else:
                print('Select number 1-3')

    def browse_menu(self):
        print('Browse Menu')
        category_input = input('Category : ')
        title_input = input('Title : ')
        try:
            print('-'*20)
            print('Result')
            if category_input != '':
                category_ref = self.ref.child(category_input)
                if title_input != '':
                    ISBN_ref = self.ref.child(category_input+'/'+title_input+'/ISBN')
                    author_ref = self.ref.child(category_input+'/'+title_input+'/author')
                    price_ref = self.ref.child(category_input+'/'+title_input+'/price')
                    result = 'Title  : '+title_input+'\n'+'ISBN   : '+ISBN_ref.get()+'\n'+'Author : '+author_ref.get()+'\n'+'Price  : '+price_ref.get()
                    return result
                return category_ref.get()
        except:
            return 'Error'

    def buy_menu(self):
        print('Buy Menu')
        category = input('Category : ').lower()
        title = input('Title : ')
        try:
            price_ref = self.ref.child(category+'/'+title+'/price')
            print('Price : '+price_ref.get())
            print('-'*20)
            print('Press c to check out')
            user_input = input('Press : ').lower()
            self.total = self.total + int(price_ref.get())
            if user_input == 'c':
                self.reciept()
        except:
            print('Error')

    def reciept(self):
        print('-'*20)
        print('Total :',self.total)
