import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.dpi'] = 400

labels = [
    'Sociální zabezpečení\n(hlavně výdaje na seniory)',
    'Obsluha státního dluhu\n(Rostoucí úroky)',
    'Regionální dotace',
    'Národní obrana',
    'Veřejné práce',
    'Vzdělávání a věda',
    'Ostatní / Rezervy\n(Prostor pro reformy)'
]

sizes = [31.9, 25.6, 17.1, 7.2, 5.1, 4.8, 8.3]

colors = [
    '#e63946',
    '#7b2cbf',
    '#f4a261', 
    '#457b9d', 
    '#2a9d8f',  
    '#1d3557',  
    '#adb5bd'   
]

fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

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

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

centre_circle = plt.Circle((0, 0), 0.70, fc='#f8f9fa')
fig.gca().add_artist(centre_circle)

plt.text(0, 0, 'ROZPOČET\nFY2026\n(122,3 bil. JPY)\n\nFixní zátěž:\n~ 75 %', 
         ha='center', va='center', fontsize=15, fontweight='900', color='#e63946')

plt.title('Rozložení vládních výdajů Japonska (pro FY2026)', 
          fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

plt.figtext(0.125, 0.05, 'Zdroj: Ministry of Finance Japan, Initial Budget Proposal FY2026 (Ippan kaikei sainjú saišucu gaisan).', 
            fontsize=9, color='#6c757d', fontstyle='italic')

plt.tight_layout()

plt.savefig('japonsko_rozpocet_2026_profi.png', dpi=400, bbox_inches='tight')

plt.show()