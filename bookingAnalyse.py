# Importerer nødvendige biblioteker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

KJORETOY_ARRAY = os.getenv("KJORETOY_ARRAY").split(",")

# Funksjon for å lese CSV-filen
def read_csv_file(): 
    try: 
        # Leser CSV-filen
        csv_file = pd.read_csv("bookingdata2025.csv")
        # Sjekker om filen er tom
        if csv_file.empty:
            print("CSV-filen er tom.")
            return None
        return csv_file
    # Håndterer potensielle feil under filinnlesing
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
        return None
    except pd.errors.EmptyDataError:
        print("CSV-filen innholder ingen data.")
        return None
    except pd.errors.ParserError:
        print("feil under parsing av CSV-filen.")
        return None
    except Exception as e:
        print(f"En feil oppstod: {e}")
        return None
    
# Funksjon for å rense data
def clean_data(csv_file):
        if csv_file is not None:
            csv_file = csv_file.drop_duplicates(subset=["Ressurs","Epost","Starttid","Slutttid","Organisator","Tittel"])
            # Fjerner rader med ugyldige tider
            mask = (csv_file["Starttid"] == "00:00:00") & (csv_file["Slutttid"] == "00:00:00")
            if mask.any():
                csv_file = csv_file.drop(csv_file[mask].index)
        return csv_file

# Funksjon for å filtrere data
def filter_data():
    # henter renset data
    csv_file = read_csv_file()
    csv_file = clean_data(csv_file)
    kolonne = 'Ressurs'
    # filtrerer data basert på spesifikke kjøretøy
    kjoretoy_filtrering = csv_file[csv_file[kolonne].isin(KJORETOY_ARRAY)]

    # Behandler dato og tid for filtrert data
    kjoretoy_filtrering['date'] = pd.to_datetime(kjoretoy_filtrering['Starttid'], errors='coerce')
    kjoretoy_filtrering = kjoretoy_filtrering.set_index('date')
    kjoretoy_filtrering = kjoretoy_filtrering.sort_index()
    # Lagrer filtrert data til ny CSV-fil
    kjoretoy_filtrering.to_csv('kjoretoy_resultat.csv', header=True)  




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
    
    plt.show()


    
# Kaller funksjonen for å utføre datafiltrering
filter_data()
# Kaller funksjonen for å vise diagram
diagram()