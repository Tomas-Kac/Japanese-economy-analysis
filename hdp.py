import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import numpy as np

plt.rcParams['savefig.dpi'] = 400

start = datetime.datetime(1950, 1, 1)
end = datetime.datetime(2023, 12, 31)

print("downloading from FRED...")

try:
    df = web.DataReader('RGDPNAJPA666NRUG', 'fred', start, end)
    col_name = 'RGDPNAJPA666NRUG'

    val_1991 = df[df.index.year == 1991].iloc[0][col_name]
    df['HDP_Index'] = (df[col_name] / val_1991) * 100

    bubble_burst_date = datetime.datetime(1991, 1, 1)
    df_zazrak = df[df.index <= bubble_burst_date]
    df_stagnace = df[df.index >= bubble_burst_date]

    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    ax.plot(df_zazrak.index, df_zazrak['HDP_Index'], color='#2a9d8f', linewidth=4, label='Hospodářský zázrak (1950–1991)')
    ax.fill_between(df_zazrak.index, df_zazrak['HDP_Index'], alpha=0.15, color='#2a9d8f')

    ax.plot(df_stagnace.index, df_stagnace['HDP_Index'], color='#e63946', linewidth=4, label='Ztracená desetiletí (1991–2023)')
    ax.fill_between(df_stagnace.index, df_stagnace['HDP_Index'], alpha=0.15, color='#e63946')

    ax.axhline(100, color='#adb5bd', linestyle='-', linewidth=1.5, alpha=0.6, zorder=1)

    ax.axvline(bubble_burst_date, color='#495057', linestyle='--', linewidth=2, zorder=2)
    ax.scatter([bubble_burst_date], [100], color='#343a40', s=100, zorder=5, edgecolor='white', lw=2)

    bbox_zlom = dict(boxstyle="round,pad=0.5", fc="#f8f9fa", ec="#343a40", lw=1.5, alpha=0.95)
    ax.text(datetime.datetime(1984, 1, 1), 101, 
            'Prasknutí bubliny', 
            fontsize=11, fontweight='bold', color='#343a40', bbox=bbox_zlom, ha='center')

    ax.grid(axis='y', color='white', linestyle='-', linewidth=2)
    ax.grid(axis='x', color='white', linestyle='-', linewidth=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#adb5bd')

    ax.set_ylim(0, 150)
    ax.set_xlim(datetime.datetime(1948, 1, 1), datetime.datetime(2025, 1, 1))

    plt.title('Reálné HDP. Index (Rok prasknutí bubliny 1991 = 100%).', 
              fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

    ax.legend(loc='lower right', fontsize=11, frameon=True, facecolor='white', edgecolor='#adb5bd')

    plt.tight_layout()

    plt.savefig('japonsko_hdp_historie_profi.png', dpi=400, bbox_inches='tight')
    print("saved as'japonsko_hdp_historie_profi.png'")
    
    plt.show()

except Exception as e:
    print(f"error: {e}")