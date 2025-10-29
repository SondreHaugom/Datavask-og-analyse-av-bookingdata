import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def diagram():
    # Leser den filtrerte CSV-filen
    filtered_data = pd.read_csv('kjoretoy_resultat.csv')
    # behandler starttid som datetime
    filtered_data['Starttid'] = pd.to_datetime(filtered_data['Starttid'], errors='coerce')
    # legger til en kolonne for år-måned
    filtered_data['År-måned'] = filtered_data['Starttid'].dt.to_period('M')
    # grupperer data etter år-måned og teller antall bookinger
    bookings = filtered_data.groupby('År-måned').size()

    # Lager linjediagram
    plt.figure(figsize=(16, 6))
    plt.plot(bookings.index.astype(str), bookings.values, marker='o')
    plt.title("Kjøretøy Bookinger per måned (2011-2026)")
    plt.xlabel("År-Måned")
    plt.ylabel("Antall Bookinger")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


diagram()