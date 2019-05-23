#You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.

amount=int(input("enter the amount: "))
no_of_5rs=int(input("enter the no of 5rs: "))*5
no_of_1rs=int(input("enter the no of 1rs: "))*1
if(amount<no_of_5rs or amount<no_of_1rs):
  a=int(amount/5)
  b=amount%5
  print(a)
  c=int(b/1)
  print(c)
elif(amount>no_of_5rs or amount>no_of_1rs):
  print(-1) 
