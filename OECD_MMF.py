import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(1990, 1, 1)
end = datetime.datetime(2023, 12, 31)

print("connecting to FRED...")

try:
    df_dluh = web.DataReader('GGGDTAJPA188N', 'fred', start, end)
    
    # RGDPNAJPA666NRUG = real GDP
    df_hdp = web.DataReader('RGDPNAJPA666NRUG', 'fred', start, end)

    df_hdp['HDP_Index'] = (df_hdp['RGDPNAJPA666NRUG'] / df_hdp['RGDPNAJPA666NRUG'].iloc[0]) * 100

    plt.style.use('seaborn-v0_8-darkgrid')

    plt.figure(figsize=(10, 6))
    plt.plot(df_dluh.index, df_dluh['GGGDTAJPA188N'], color='purple', linewidth=2.5)
    plt.fill_between(df_dluh.index, df_dluh['GGGDTAJPA188N'], 0, color='purple', alpha=0.2)

    plt.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.7)
    plt.axhline(200, color='black', linestyle='--', linewidth=1, alpha=0.7)

    plt.title('Vývoj státního dluhu Japonska (% HDP) - Zdroj dat: FRED', fontsize=14, fontweight='bold')
    plt.xlabel('Rok', fontsize=12)
    plt.ylabel('Státní dluh (% HDP)', fontsize=12)
    plt.tight_layout()
    plt.savefig('japonsko_statni_dluh_live.png', dpi=300)
    print("saved as 'japonsko_statni_dluh_live.png'")

    plt.figure(figsize=(10, 6))
    plt.plot(df_hdp.index, df_hdp['HDP_Index'], color='forestgreen', linewidth=2.5)
    
    plt.title('Vývoj reálného HDP Japonska (Index 1990 = 100) - Zdroj dat: FRED', fontsize=14, fontweight='bold')
    plt.xlabel('Rok', fontsize=12)
    plt.ylabel('Reálné HDP (Index)', fontsize=12)
    plt.tight_layout()
    plt.savefig('japonsko_hdp_live.png', dpi=300)
    print("saved as'japonsko_hdp_live.png'")

    plt.show()

except Exception as e:
    print(f"error: {e}")