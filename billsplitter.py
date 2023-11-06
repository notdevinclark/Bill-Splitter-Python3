import random


class BillSplitter:
    def __init__(self):
        self.guest_count = 0
        self.guest_dict = dict()
        self.names = []
        self.bill = 0
        self.total_per_guest = 0
        self.lucky_person = False
        self.lucky_name = None
        self.total_per_guest = 0

    def process(self):
        self.get_guest_count()
        self.get_guest_names()
        self.get_bill_amount()
        self.is_anyone_lucky()
        self.split_the_bill()

    def get_guest_count(self):
        print('Enter the number of friends joining (including you):')
        self.guest_count = int(input())

        if self.guest_count <= 0:
            print('No one is joining for the party')
            exit(0)

    def get_guest_names(self):
        print('Enter the name of every friend (including you), each on a new line:')
        for guest in range(self.guest_count):
            name = input()
            self.guest_dict[name] = 0

    def get_bill_amount(self):
        print('Enter the total bill value:')
        self.bill = int(input())

    def is_anyone_lucky(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

        if input().lower() == 'yes':
            self.lucky_person = True
            names = [*self.guest_dict]
            random_num = random.randint(0, len(names) - 1)
            self.lucky_name = names[random_num]
            print(f"{self.lucky_name} is the lucky one!")
        else:
            print('No one is going to be lucky.')

    def split_the_bill(self):
        number_of_paying_customers = self.guest_count - 1 if self.lucky_person else self.guest_count
        try:
            if self.bill % number_of_paying_customers == 0:
                self.total_per_guest = self.bill // number_of_paying_customers
            else:
                self.total_per_guest = round(self.bill / number_of_paying_customers, 2)
        except ZeroDivisionError:
            print('You can not divide by Zero')

        for key, _value in self.guest_dict.items():
            self.guest_dict[key] = self.total_per_guest

        if self.lucky_person:
            self.guest_dict[self.lucky_name] = 0

        print(self.guest_dict)


app = BillSplitter()
app.process()

