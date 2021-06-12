class Atm:
    def __init__(self,card_number,pin):
        self.card_number = card_number
        self.pin = pin

    def check_balance(self):
        print("Your balance is 1000000")
        main()

    def withdrawal_amount(self,amount):
        new_amount = 1000000-amount
        print("You have withdrawn "+ str(amount)+'. Your remaining balanace is ' + str(new_amount))
        main()

def main():
    Card_number = input("Insert your card number : ")
    Pin_number = input("Insert your PIN number : ")
    new_user = Atm(Card_number,Pin_number)

    print("Choose your activity ")
    print("1. Balance Enquiry   2. Withdrawal")
    Activity = int(input("Enter the activity number : "))

    if(Activity==1):
        new_user.check_balance()
    elif(Activity==2):
        amount = int(input("Enter the amount you wish to withdraw "))
        new_user.withdrawal_amount(amount)
    else:
        print("Please enter a valid number")
        main()
        
main()