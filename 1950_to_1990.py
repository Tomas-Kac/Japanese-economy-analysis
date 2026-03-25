import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(1950, 1, 1)
end = datetime.datetime(2023, 12, 31)


try:

    df_hdp = web.DataReader('RGDPNAJPA666NRUG', 'fred', start, end)

    df_hdp['HDP_Index'] = (df_hdp['RGDPNAJPA666NRUG'] / df_hdp['RGDPNAJPA666NRUG'].iloc[0]) * 100

    val_1950 = df_hdp[df_hdp.index.year == 1950]['HDP_Index'].values[0]
    val_1991 = df_hdp[df_hdp.index.year == 1991]['HDP_Index'].values[0]
    val_2023 = df_hdp[df_hdp.index.year == 2023]['HDP_Index'].values[0]

    cagr_zazrak = ((val_1991 / val_1950) ** (1 / 41) - 1) * 100
    cagr_stagnace = ((val_2023 / val_1991) ** (1 / 32) - 1) * 100

    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    ax.plot(df_hdp.index, df_hdp['HDP_Index'], color='#1f497d', linewidth=4, label='Reálné HDP')
    ax.fill_between(df_hdp.index, df_hdp['HDP_Index'], alpha=0.15, color='#1f497d')

    ax.axvspan(datetime.datetime(1950, 1, 1), datetime.datetime(1991, 1, 1), color='#2ca02c', alpha=0.08)
    ax.axvspan(datetime.datetime(1991, 1, 1), datetime.datetime(2023, 12, 31), color='#d62728', alpha=0.08)

    ax.axvline(datetime.datetime(1991, 1, 1), color='#495057', linestyle='--', linewidth=2)
    ax.scatter([datetime.datetime(1991, 1, 1)], [val_1991], color='#e63946', s=120, zorder=5, edgecolor='black')

    ax.scatter([datetime.datetime(2023, 1, 1)], [val_2023], color='#1f497d', s=80, zorder=5)

    bbox_props_green = dict(boxstyle="round,pad=0.6", fc="#e8f5e9", ec="#2ca02c", lw=1.5, alpha=0.95)
    ax.text(datetime.datetime(1960, 1, 1), 800, 
            f'Hospodářský zázrak\n(cca 1950–1991)\nPrůměrný roční růst: +{cagr_zazrak:.1f} %', 
            fontsize=11, fontweight='bold', color='#1b5e20', bbox=bbox_props_green, ha='center')

    bbox_props_red = dict(boxstyle="round,pad=0.6", fc="#ffebee", ec="#d62728", lw=1.5, alpha=0.95)
    ax.text(datetime.datetime(2007, 1, 1), 800, 
            f'Ztracená desetiletí\n(cca 1991–2023)\nPrůměrný roční růst: +{cagr_stagnace:.1f} %', 
            fontsize=11, fontweight='bold', color='#b71c1c', bbox=bbox_props_red, ha='center')

    ax.annotate('Prasknutí bubliny\n(začátek stagnace)', 
                xy=(datetime.datetime(1991, 1, 1), val_1991), 
                xytext=(datetime.datetime(1960, 1, 1), val_1991 + 100),
                arrowprops=dict(facecolor='#343a40', shrink=0.05, width=1.5, headwidth=8),
                fontsize=12, fontweight='bold', color='#343a40')

    ax.grid(axis='y', color='white', linestyle='-', linewidth=2)
    ax.grid(axis='x', color='white', linestyle='-', linewidth=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#adb5bd')

    plt.title('Reálné HDP přepočtené na index (Rok 1950 = 100)', 
              fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

    plt.tight_layout()
    
    plt.savefig('japonsko_hdp_profi.png', dpi=400, bbox_inches='tight')
    print("saved as'japonsko_hdp_profi.png'")
    
    plt.show()

except Exception as e:
    print(f"error: {e}")