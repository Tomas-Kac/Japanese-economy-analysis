import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

# Endpoint API Světové banky pro Japonsko
url = "http://api.worldbank.org/v2/country/JP/indicator/{}?format=json&per_page=100"

# Slovník požadovaných indikátorů
indicators = {
    'Inflace_CPI_pct': 'FP.CPI.TOTL.ZG',
}

data_frames = []

try:
    print("Stahuji data z World Bank API...")
    for name, ind_code in indicators.items():
        res = requests.get(url.format(ind_code)).json()
        if len(res) > 1:
            records = res[1]
            df = pd.DataFrame(records)
            df = df[['date', 'value']].rename(columns={'value': name, 'date': 'Rok'})
            df['Rok'] = df['Rok'].astype(int)
            data_frames.append(df)

    # Sloučení a filtrace
    if data_frames:
        df_merged = data_frames[0]
        df_merged = df_merged.sort_values('Rok').reset_index(drop=True)
        # Oříznutí na roky 1990 - současnost
        df_merged = df_merged[df_merged['Rok'] >= 1990]

        # ================== VIZUÁLNÍ STYLING ==================
        plt.rcParams['savefig.dpi'] = 400
        fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
        ax.set_facecolor('#f8f9fa')

        roky = df_merged['Rok'].values
        inflace = df_merged['Inflace_CPI_pct'].values

        # Nulová hranice (hranice deflace)
        ax.axhline(0, color='#495057', linestyle='-', linewidth=2, zorder=1)

        # Sloupce (Modrá = inflace, Červená = deflace) a křivka
        colors = ['#d62728' if val < 0 else '#1f497d' for val in inflace]
        ax.bar(roky, inflace, color=colors, width=0.7, zorder=3, alpha=0.85)
        ax.plot(roky, inflace, color='#343a40', linewidth=1.5, zorder=4, marker='o', markersize=4)

        # Milníky
        rok_last = roky[-1]
        
        # 1991 (Poslední záchvěvy staré inflace)
        idx_1991 = np.where(roky == 1991)[0]
        if len(idx_1991) > 0:
            val_1991 = inflace[idx_1991[0]]
            ax.scatter([1991], [val_1991], color='#1f497d', s=100, zorder=5, edgecolor='black')
            bbox_1991 = dict(boxstyle="round,pad=0.5", fc="#f8f9fa", ec="#495057", lw=1.5, alpha=0.95)
            ax.annotate('1991: Poslední záchvěvy inflace', 
                        xy=(1991, val_1991), xytext=(1993, max(inflace)*0.9),
                        arrowprops=dict(facecolor='#343a40', shrink=0.05, width=1.5, headwidth=8),
                        fontsize=10, fontweight='bold', color='#343a40', bbox=bbox_1991, zorder=10)

        # 2013 (Abenomika a cíl Japonské centrální banky)
        idx_2013 = np.where(roky == 2013)[0] 
        if len(idx_2013) > 0:
            val_2013 = inflace[idx_2013[0]]
            ax.scatter([2013], [val_2013], color='#ff9f1c', s=100, zorder=5, edgecolor='black')
            bbox_2013 = dict(boxstyle="round,pad=0.5", fc="#fff8e1", ec="#ff9f1c", lw=1.5, alpha=0.95)
            ax.annotate('2013: Inflační cíl na 2 %', 
                        xy=(2013, val_2013), xytext=(2005, 2),
                        arrowprops=dict(facecolor='#343a40', shrink=0.05, width=1.5, headwidth=8),
                        fontsize=10, fontweight='bold', color='#e65100', bbox=bbox_2013, zorder=10)

        # Vysvětlivka k červeným číslům (deflaci)
        bbox_deflace = dict(boxstyle="round,pad=0.5", fc="#ffebee", ec="#d62728", lw=1.5, alpha=0.95)
        ax.text(2005.5, -1.2, 'Období deflace', 
                fontsize=11, fontweight='bold', color='#b71c1c', bbox=bbox_deflace, ha='center', zorder=10)

        # Čištění designu
        ax.grid(axis='y', color='white', linestyle='-', linewidth=2, zorder=0)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('#adb5bd')

        # Úprava popisků osy Y (%)
        yticks = ax.get_yticks()
        ax.set_yticklabels([f'{tick:.1f} %' for tick in yticks], color='#495057', fontweight='bold')

        # Omezení os
        ax.set_xlim(1989, rok_last + 2)
        ax.set_ylim(min(inflace) - 0.5, max(inflace) + 1.5)
        
        plt.title(f'Vývoj japonské inflace (1990–{rok_last})', 
                  fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

        plt.tight_layout()
        plt.savefig('japonsko_inflace_profi.png', dpi=400, bbox_inches='tight')
        plt.savefig('japonsko_inflace_profi.svg', format='svg', bbox_inches='tight')
        print("Graf inflace úspěšně uložen!")
        
except Exception as e:
    print(f"Chyba při stahování: {e}")