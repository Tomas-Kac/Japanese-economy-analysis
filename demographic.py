import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data (Zdroj: World Bank / Statista) - reprezentativní pro Japonsko
years = np.array([1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023])
pop_mil = np.array([93.2, 98.3, 103.7, 111.6, 116.8, 120.8, 123.5, 125.4, 126.8, 127.8, 128.1, 127.1, 125.7, 123.9])
aging_rate = np.array([5.7, 6.3, 7.1, 7.9, 9.1, 10.3, 12.1, 14.6, 17.4, 20.2, 23.0, 26.6, 28.9, 29.8])

# 1. VIZUÁLNÍ STYLING (The Economist style)
plt.rcParams['savefig.dpi'] = 400
fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
ax1.set_facecolor('#f8f9fa')

# Primární osa: Populace (Modrá)
color_pop = '#1f497d'
ax1.plot(years, pop_mil, color=color_pop, linewidth=4, label='Celková populace (miliony)', zorder=3)
ax1.fill_between(years, pop_mil, alpha=0.1, color=color_pop)
ax1.set_ylabel('Populace (miliony)', color=color_pop, fontweight='bold', fontsize=11)
ax1.tick_params(axis='y', labelcolor=color_pop)

# Sekundární osa: Podíl 65+ (Červená)
ax2 = ax1.twinx()
color_aging = '#e63946'
ax2.plot(years, aging_rate, color=color_aging, linewidth=4, label='Podíl populace 65+ (%)', linestyle='--', zorder=3)
ax2.set_ylabel('Podíl populace 65+ (%)', color=color_aging, fontweight='bold', fontsize=11)
ax2.tick_params(axis='y', labelcolor=color_aging)

# 2. ANOTACE - Bod zlomu (Peak population ~2010)
peak_idx = np.argmax(pop_mil)
peak_year = years[peak_idx]
peak_val = pop_mil[peak_idx]
ax1.scatter([peak_year], [peak_val], color=color_pop, s=120, zorder=5, edgecolor='white')

bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="#adb5bd", lw=1.5, alpha=0.95)
ax1.annotate(f'Vrchol populace: {peak_val:.1f} mil.\n(rok {peak_year})', 
             xy=(peak_year, peak_val), xytext=(peak_year-23, peak_val-25),
             arrowprops=dict(facecolor='#343a40', shrink=0.05, width=1.5, headwidth=8),
             fontsize=10, fontweight='bold', color='#343a40', bbox=bbox_props)

# 3. ČIŠTĚNÍ DESIGNU
ax1.grid(axis='y', color='white', linestyle='-', linewidth=2)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_color('#adb5bd')

# Titulky
plt.title('Demografie: Úbytek a stárnutí populace (1960–2023)', 
          fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

# Legenda
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center left', fontsize=10, frameon=True, facecolor='white', edgecolor='#adb5bd')

plt.tight_layout()
plt.savefig('japonsko_demografie_profi.png', dpi=400, bbox_inches='tight')
plt.show()