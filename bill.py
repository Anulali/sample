#write a python program to calculate the final bill amount to be paid by a customer. 
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if(distance_in_kms<=3):
          delivery_charge=0
    elif(distance_in_kms>=6 and distance_in_kms<=6 ):
          delivery_charge=distance_in_kms*3
    else:
          delivery_charge=distance_in_kms*6
    if(food_type=='V'):
          food_cost=120*quantity_ordered   
          bill_amount=food_cost+delivery_charge
            
          return bill_amount
    elif(food_type=='N'):
          food_cost=150*quantity_ordered
          bill_amount=food_cost+delivery_charge
         
          return bill_amount

bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
