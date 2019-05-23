#Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveler has. The program should identify and display the amount the traveler should provide in the currency he has, to get the specified amount in INR.
def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    if(current_currency_name=='Euro'):
      current_currency_amount=amount_needed_inr*0.01417
      return current_currency_amount
    elif(current_currency_name=='British Pound'):
       current_currency_amount=amount_needed_inr*0.0100
       return current_currency_amount
    elif(current_currency_name=='Australian Dollar'):
       current_currency_amount=amount_needed_inr*0.02140 
       return current_currency_amount 
    elif(current_currency_name=='Canadian Dollar'):  
       current_currency_amount=amount_needed_inr*0.02027
       return current_currency_amount   
currency_needed=convert_currency(2000,"Euro")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
