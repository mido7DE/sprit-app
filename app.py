import streamlit as st
from datetime import date
import locale

# Versuchen, das Datum auf Deutsch zu stellen für den Wochentag
try:
    locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
except:
    pass

st.title("⛽ Sprit-Lieferung")

# 1. Datumsauswahl (Standard: Heute, 14.01.2026)
heute = date.today()
gewaehltes_datum = st.date_input("Datum der Lieferung", heute)

# Formatierung: Wochentag, Tag.Monat.Jahr
# Beispiel: Mittwoch, 14.01.2026
datum_anzeige = gewaehltes_datum.strftime("%A, %d.%m.%Y")

# 2. Eingabefelder für alle Sorten
st.subheader("Mengen in Litern (15°C)")

diesel = st.number_input("Diesel", min_value=0, step=1, value=0)
e10 = st.number_input("Super E10", min_value=0, step=1, value=0)
bleifrei = st.number_input("Super bleifrei (E5)", min_value=0, step=1, value=0)
super_plus = st.number_input("Super Plus", min_value=0, step=1, value=0)

# 3. Nachricht exakt nach deiner Vorlage zusammenbauen
nachricht = (
    f"Hello 👋 \n"
    f"hier die Daten: \n\n"
    f"Menge 15 Grad C \n\n"
    f"{datum_anzeige}\n\n"
    f"Diesel: {diesel}\n"
    f"Super E10: {e10}\n"
    f"Super bleifrei: {bleifrei}\n"
    f"Super Plus: {super_plus}\n\n"
    f"Lg"
    #f"Deine App hat funktioniert Bro"
)
st.divider()

# 4. Ausgabe zum Kopieren
st.subheader("Text für den Chef:")
st.code(nachricht, language=None)

st.info("Oben rechts im grauen Kasten auf das Symbol klicken, um alles zu kopieren.")

## Eine mögliche Alternative falls es spackt
# if __name__ == "__main__":
#    import os
 #   import sys
  #  from streamlit.web import cli as stcli

   # sys.argv = ["streamlit", "run", sys.argv[0]]
    #sys.exit(stcli.main())
