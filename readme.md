# Datavask og analyse av bookingdata

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Status](https://img.shields.io/badge/Status-Under%20arbeid-yellow)
![License](https://img.shields.io/badge/Lisens-MIT-blue)
![Dataanalyse](https://img.shields.io/badge/Formål-Dataanalyse%20og%20Datavask-lightgrey)

---

## 📘 Innholdsfortegnelse
1. [Om prosjektet](#om-prosjektet)  
2. [Biblioteker og begrunnelse](#biblioteker-og-begrunnelse)  
3. [Sikkerhet og personvern](#sikkerhet-og-personvern)  
4. [Installasjon og oppsett](#installasjon-og-oppsett)

---

## 📖 Om prosjektet
Dette prosjektet fokuserer på å hente ut relevante data, fjerne unødvendig rot og eliminere dupliserte bookinger for å levere et rent og konsist datasett.  

Python-skriptet leser en CSV-fil, filtrerer ut ønsket informasjon og fjerner dupliserte bookinger. Deretter genereres en ny, renset CSV-fil og et diagram som visualiserer de bearbeidede dataene.

---

## ⚙️ Biblioteker og begrunnelse
| Bibliotek | Formål |
|------------|--------|
| **pandas** | Leser, rensker og lagrer CSV-data med kraftige DataFrames. |
| **matplotlib.pyplot** | Lager diagrammer for å visualisere resultatene. |
| **numpy** | Utfører effektive numeriske og vektoriserte operasjoner som støtter dataanalysen. |
| **dotenv** | Laster miljøvariabler fra en `.env`-fil, slik at sensitive opplysninger holdes utenfor koden. |
| **os** | Håndterer fil- og mappestier, samt tilgang til miljøvariabler på en plattformuavhengig måte. |

---

## 🔒 Sikkerhet og personvern
Skriptet behandler ingen personopplysninger.  
All databehandling skjer lokalt på maskinen, uten at data sendes eller lagres eksternt.

---

## 🧰 Installasjon og oppsett

### 📋 Forutsetninger
For å kjøre skriptet trenger du følgende:
- VS Code (eller annen kodeeditor)  
- Python **3.13.0** eller nyere  
- Pandas – `pip install pandas`  
- Matplotlib – `pip install matplotlib`  
- NumPy – `pip install numpy`  
- Python Dotenv – `pip install python-dotenv`  
- `os`-modulen er en del av standardbiblioteket og krever ingen installasjon

---

### 💾 Kloning av repoet
Klon prosjektet til din lokale maskin med Git:
```bash
git clone https://github.com/SondreHaugom/Datavask-og-analyse-av-bookingdata.git
