
from datetime import datetime

def get_days_from_today(date):                            

    current_datetime = datetime.now()                           # Сьогоднішня дата 

    datetime_object = datetime.strptime(date, "%Y-%m-%d") # перетворення тексту в формат дати 


    days_since = current_datetime-datetime_object # Розрахунок кількості днів
    print(days_since)


get_days_from_today("2021-10-09")                           





