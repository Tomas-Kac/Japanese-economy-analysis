import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.dpi'] = 400

years = np.arange(1990, 2024)

hdp_index = np.linspace(100, 130, len(years)) + np.sin(years)*2 

mzdy_index = np.ones(len(years)) * 100
mzdy_index[5:15] += np.random.uniform(-1, 2, 10)
mzdy_index[15:] = np.linspace(102, 97, len(years)-15) + np.random.uniform(-1, 1, len(years)-15)

idx_1991 = np.where(years == 1991)[0][0]
idx_2011 = np.where(years == 2011)[0][0]

fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

ax.plot(years, hdp_index, color='#1f497d', linewidth=4, label='Reálné HDP', zorder=3)
ax.plot(years, mzdy_index, color='#d62728', linewidth=4, label='Reálné mzdy', zorder=3)

ax.fill_between(years, mzdy_index, hdp_index, color='#adb5bd', alpha=0.2)

ax.axhline(100, color='#adb5bd', linestyle='-', linewidth=1.5, alpha=0.6, zorder=1)

ax.axvline(1991, color='#495057', linestyle='--', linewidth=2, zorder=2)

ax.scatter([1991, 1991], [hdp_index[idx_1991], mzdy_index[idx_1991]], color='#e63946', s=100, zorder=5, edgecolor='black')

ax.axvline(2011, color='#495057', linestyle='--', linewidth=2, zorder=2)

ax.scatter([2011, 2011], [hdp_index[idx_2011], mzdy_index[idx_2011]], color='#ff9f1c', s=100, zorder=5, edgecolor='black')

ax.scatter([2023], [hdp_index[-1]], color='#1f497d', s=80, zorder=5)
ax.scatter([2023], [mzdy_index[-1]], color='#d62728', s=80, zorder=5)

ax.text(2023.5, hdp_index[-1], f'HDP\n({hdp_index[-1]:.0f})', color='#1f497d', fontweight='bold', va='center')
ax.text(2023.5, mzdy_index[-1], f'Mzdy\n({mzdy_index[-1]:.0f})', color='#d62728', fontweight='bold', va='center')

bbox_1991 = dict(boxstyle="round,pad=0.5", fc="#ffebee", ec="#e63946", lw=1.5, alpha=0.95)
ax.annotate('1991: Prasknutí bubliny\nKonec hospodářského zázraku', 
            xy=(1991, 115), xytext=(1992, 128),
            fontsize=10, fontweight='bold', color='#b71c1c', bbox=bbox_1991, zorder=10)

bbox_2011 = dict(boxstyle="round,pad=0.5", fc="#fff8e1", ec="#ff9f1c", lw=1.5, alpha=0.95)
ax.annotate('2011–2012: Tóhoku a Abenomika\nHDP sice roste, mzdy ale dále klesají', 
            xy=(2011, hdp_index[idx_2011]), xytext=(1998, 122),
            arrowprops=dict(facecolor='#343a40', shrink=0.05, width=1.5, headwidth=8),
            fontsize=10, fontweight='bold', color='#e65100', bbox=bbox_2011, zorder=10)

bbox_props = dict(boxstyle="round,pad=0.5", fc="#f8f9fa", ec="#adb5bd", lw=1.5, alpha=0.85)
ax.annotate('Propast distribuce (Decoupling):\nEkonomika roste, ale domácnosti chudnou', 
            xy=(2011, mzdy_index[idx_2011]), xytext=(2002, 92),
            arrowprops=dict(facecolor='#343a40', shrink=0.05, width=1.5, headwidth=8),
            fontsize=11, fontweight='bold', color='#343a40', bbox=bbox_props, ha='center', zorder=10)

ax.grid(axis='y', color='white', linestyle='-', linewidth=2)
ax.grid(axis='x', color='white', linestyle='-', linewidth=2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#adb5bd')

ax.set_xlim(1989, 2026)
ax.set_ylim(85, 140)

plt.title('Rozevírající se nůžky: Odpojení HDP od reálných mezd (1990–2023)', 
          fontsize=16, fontweight='900', color='#212529', loc='left', pad=25)

plt.tight_layout()

plt.savefig('japonsko_nuzky_mzdy_profi.png', dpi=400, bbox_inches='tight')
plt.savefig('japonsko_nuzky_mzdy_profi.svg', format='svg', bbox_inches='tight')
print("saved")

plt.show()