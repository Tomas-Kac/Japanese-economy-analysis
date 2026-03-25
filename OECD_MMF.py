import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

# 1. Nastavení časového období (od prasknutí bubliny po současnost)
start = datetime.datetime(1990, 1, 1)
end = datetime.datetime(2023, 12, 31)

print("Připojuji se k databázi FRED...")

try:
    # 2. Živé stažení dat z databáze FRED
    # Kód GGGDTAJPA188N = Hrubý státní dluh Japonska (% HDP)
    df_dluh = web.DataReader('GGGDTAJPA188N', 'fred', start, end)
    
    # Kód RGDPNAJPA666NRUG = Reálné HDP v národních cenách
    df_hdp = web.DataReader('RGDPNAJPA666NRUG', 'fred', start, end)

    # 3. Zpracování dat pro grafy
    # Přepočet HDP na index (Rok 1990 = 100) pro lepší viditelnost stagnace
    df_hdp['HDP_Index'] = (df_hdp['RGDPNAJPA666NRUG'] / df_hdp['RGDPNAJPA666NRUG'].iloc[0]) * 100

    plt.style.use('seaborn-v0_8-darkgrid')

    # --- GRAF 1: Raketový růst státního dluhu ---
    plt.figure(figsize=(10, 6))
    plt.plot(df_dluh.index, df_dluh['GGGDTAJPA188N'], color='purple', linewidth=2.5)
    plt.fill_between(df_dluh.index, df_dluh['GGGDTAJPA188N'], 0, color='purple', alpha=0.2)

    # Vyznačení kritických milníků
    plt.axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.7)
    plt.axhline(200, color='black', linestyle='--', linewidth=1, alpha=0.7)

    plt.title('Vývoj státního dluhu Japonska (% HDP) - Zdroj dat: FRED', fontsize=14, fontweight='bold')
    plt.xlabel('Rok', fontsize=12)
    plt.ylabel('Státní dluh (% HDP)', fontsize=12)
    plt.tight_layout()
    plt.savefig('japonsko_statni_dluh_live.png', dpi=300)
    print("Graf 1 (Státní dluh) úspěšně uložen jako 'japonsko_statni_dluh_live.png'")

    # --- GRAF 2: Stagnace reálného HDP (Ztracené dekády) ---
    plt.figure(figsize=(10, 6))
    plt.plot(df_hdp.index, df_hdp['HDP_Index'], color='forestgreen', linewidth=2.5)
    
    plt.title('Vývoj reálného HDP Japonska (Index 1990 = 100) - Zdroj dat: FRED', fontsize=14, fontweight='bold')
    plt.xlabel('Rok', fontsize=12)
    plt.ylabel('Reálné HDP (Index)', fontsize=12)
    plt.tight_layout()
    plt.savefig('japonsko_hdp_live.png', dpi=300)
    print("Graf 2 (Reálné HDP) úspěšně uložen jako 'japonsko_hdp_live.png'")

    plt.show()

except Exception as e:
    print(f"Došlo k chybě při stahování nebo zpracování dat: {e}")