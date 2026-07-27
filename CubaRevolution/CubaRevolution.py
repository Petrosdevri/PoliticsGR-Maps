import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.PlateCarree()})

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black')

ax.set_extent([-86, -73, 18, 25])

cities = {
    "Alegría de Pío": (19.8753, -77.5239),
    "Havana": (23.1366, -82.3588),
    "Santa Clara": (22.3731, 38.5251),
    "Santiago de Cuba": (20.0216, -75.8294),
    "Sierra Maestra": (19.9894, -76.8358),
    "Yaguajay ": (20.9850, 39.1600)
}

for city, (lon, lat) in cities.items():
    ax.plot(lon, lat, 'bs', markersize=5, transform=ccrs.PlateCarree())

plt.title('Cuban Revolution (1953-1959)', fontsize=15)

plt.savefig('Cuban Revolution (1953-1959).png', dpi=300, bbox_inches='tight')
plt.show()