import matplotlib.pyplot as plt
import numpy as np

# Nastavení vysoké kvality pro prezentaci
plt.rcParams['savefig.dpi'] = 400

# 1. DATA: Japonský státní rozpočet (Initial Budget Proposal FY2026)
# Zdroj: Ministry of Finance Japan (MOF) - 01.pdf (Ippan kaikei sainyū saishutsu gaisan)
labels = [
    'Sociální zabezpečení\n(hlavně výdaje na seniory)',
    'Obsluha státního dluhu\n(Rostoucí úroky)',
    'Regionální dotace',
    'Národní obrana',
    'Veřejné práce',
    'Vzdělávání a věda',
    'Ostatní / Rezervy\n(Prostor pro reformy)'
]

# Hodnoty v % (přesně podle návrhu na 122,3 bilionů JPY z 01.pdf)
sizes = [31.9, 25.6, 17.1, 7.2, 5.1, 4.8, 8.3]

# Barevná paleta: Economist/FT styl
# Červená a fialová značí největší strukturální brzdy
colors = [
    '#e63946',  # Sytě červená (Sociální systém)
    '#7b2cbf',  # Fialová (Dluh)
    '#f4a261',  # Oranžová (Regiony)
    '#457b9d',  # Modrá (Obrana)
    '#2a9d8f',  # Zelená (Veřejné práce)
    '#1d3557',  # Tmavě modrá (Vzdělání)
    '#adb5bd'   # Šedá (Vše ostatní - zbylý prostor)
]

# 2. VIZUALIZACE
fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Donut chart s vysunutím mandatorních výdajů
explode = (0.05, 0.05, 0.05, 0, 0, 0, 0)

wedges, texts, autotexts = ax.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85,
    textprops=dict(color='#343a40', fontsize=11, fontweight='bold')
)

# Čitelnost vnitřních čísel
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

# Vytvoření moderního donut efektu
centre_circle = plt.Circle((0, 0), 0.70, fc='#f8f9fa')
fig.gca().add_artist(centre_circle)

# Centrální text - pointa fiskální nepružnosti (upraveno na 75 % a přidána celková částka)
plt.text(0, 0, 'ROZPOČET\nFY2026\n(122,3 bil. JPY)\n\nFixní zátěž:\n~ 75 %', 
         ha='center', va='center', fontsize=15, fontweight='900', color='#e63946')

# 3. TITULKY A ZDROJ
plt.title('Rozložení vládních výdajů Japonska (pro FY2026)', 
          fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

plt.figtext(0.125, 0.05, 'Zdroj: Ministry of Finance Japan, Initial Budget Proposal FY2026 (Ippan kaikei sainjú saišucu gaisan).', 
            fontsize=9, color='#6c757d', fontstyle='italic')

plt.tight_layout()

# Uložení
plt.savefig('japonsko_rozpocet_2026_profi.png', dpi=400, bbox_inches='tight')
print("Aktualizovaný graf rozpočtu pro rok 2026 úspěšně uložen.")

plt.show()