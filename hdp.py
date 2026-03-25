import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Nastavení globální kvality pro ukládání přes ikonu
plt.rcParams['savefig.dpi'] = 400

# 1. Stažení a příprava dat z FRED
start = datetime.datetime(1950, 1, 1)
end = datetime.datetime(2023, 12, 31)

print("Stahuji data o reálném HDP Japonska z FRED...")

try:
    # FRED kód: RGDPNAJPA666NRUG (Real Gross Domestic Product for Japan)
    df = web.DataReader('RGDPNAJPA666NRUG', 'fred', start, end)
    col_name = 'RGDPNAJPA666NRUG'
    
    # Pro dokonalou čitelnost převedeme HDP na Index (Rok 1991 = 100)
    # Tím se to metodologicky sjednotí s grafem "nůžek"
    val_1991 = df[df.index.year == 1991].iloc[0][col_name]
    df['HDP_Index'] = (df[col_name] / val_1991) * 100

    # Rozdělení dat na dvě éry pro barevné odlišení
    bubble_burst_date = datetime.datetime(1991, 1, 1)
    df_zazrak = df[df.index <= bubble_burst_date]
    df_stagnace = df[df.index >= bubble_burst_date] # Mírný překryv kvůli spojení křivky

    # 2. VIZUÁLNÍ STYLING (The Economist / Financial Times styl)
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    # Éra 1: Hospodářský zázrak (Zelená)
    ax.plot(df_zazrak.index, df_zazrak['HDP_Index'], color='#2a9d8f', linewidth=4, label='Hospodářský zázrak (1950–1991)')
    ax.fill_between(df_zazrak.index, df_zazrak['HDP_Index'], alpha=0.15, color='#2a9d8f')

    # Éra 2: Ztracená desetiletí (Červená)
    ax.plot(df_stagnace.index, df_stagnace['HDP_Index'], color='#e63946', linewidth=4, label='Ztracená desetiletí (1991–2023)')
    ax.fill_between(df_stagnace.index, df_stagnace['HDP_Index'], alpha=0.15, color='#e63946')

    # 3. ZVÝRAZNĚNÉ MILNÍKY
    # Horizontální referenční linka maxima před krizí (Index 100)
    ax.axhline(100, color='#adb5bd', linestyle='-', linewidth=1.5, alpha=0.6, zorder=1)
    
    # Vertikální zlom (Prasknutí bubliny 1990)
    ax.axvline(bubble_burst_date, color='#495057', linestyle='--', linewidth=2, zorder=2)
    ax.scatter([bubble_burst_date], [100], color='#343a40', s=100, zorder=5, edgecolor='white', lw=2)

    # 4. POKROČILÉ ANOTACE
    # Anotace: Hospodářský zázrak
    # Anotace: Zlom 1991
    bbox_zlom = dict(boxstyle="round,pad=0.5", fc="#f8f9fa", ec="#343a40", lw=1.5, alpha=0.95)
    ax.text(datetime.datetime(1984, 1, 1), 101, 
            'Prasknutí bubliny', 
            fontsize=11, fontweight='bold', color='#343a40', bbox=bbox_zlom, ha='center')


    # 5. ČIŠTĚNÍ DESIGNU
    ax.grid(axis='y', color='white', linestyle='-', linewidth=2)
    ax.grid(axis='x', color='white', linestyle='-', linewidth=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#adb5bd')

    # Limity os
    ax.set_ylim(0, 150)
    ax.set_xlim(datetime.datetime(1948, 1, 1), datetime.datetime(2025, 1, 1))

    # Titulky
    plt.title('Reálné HDP. Index (Rok prasknutí bubliny 1991 = 100%).', 
              fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

    # Legenda
    ax.legend(loc='lower right', fontsize=11, frameon=True, facecolor='white', edgecolor='#adb5bd')

    plt.tight_layout()
    
    # Uložení ve špičkové kvalitě
    plt.savefig('japonsko_hdp_historie_profi.png', dpi=400, bbox_inches='tight')
    print("Graf HDP úspěšně uložen jako 'japonsko_hdp_historie_profi.png'")
    
    plt.show()

except Exception as e:
    print(f"Došlo k chybě při stahování dat: {e}. Zkontrolujte prosím připojení k internetu nebo dostupnost API FRED.")