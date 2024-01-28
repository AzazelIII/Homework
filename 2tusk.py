import random

Your_ticket=[]
def get_numbers_ticket(min, max, quantity) :
    if min>=1 and max<=1000:                    #обмедження доступного діапазону
        while len(Your_ticket)<quantity:        
    
         random_nomber=random.randint(min, max) # генератор випадкових чисел
    
         if random_nomber not in Your_ticket:   # захист від повторів

          Your_ticket.append(random_nomber)
    else :
       print("invalid range, chose range 1  -  1000")
get_numbers_ticket(1,49,6)                        # Сюди вписувати діапазон і кількість чисел для генерації 
Your_ticket.sort()                                  #Сортування 

print("Your ticket:",Your_ticket)