import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def diagram():
    filtered_data = pd.read_csv('kjoretoy_resultat.csv')

    x_values = list(range(1, 13))  # 1-12 for månedene
    month_labels = ["jan", "feb", "mars", "april", "mai", "juni", "juli", "aug", "sep", "okt", "nov", "des"]
    filtered_data['Starttid'] = pd.to_datetime(filtered_data['Starttid'], errors='coerce')
    bookings = filtered_data.groupby(filtered_data['Starttid'].dt.month).size()

    plt.title("Kjøretøy Bookinger 2011-2026")
    plt.xticks(x_values, month_labels, rotation=45)  # Måneder på x-aksen
    plt.bar(bookings.index, bookings.values)
    for i, v in enumerate(bookings.values):
        plt.text(bookings.index[i], v + 1, str(v), ha='center') 
    
    plt.show()

diagram()