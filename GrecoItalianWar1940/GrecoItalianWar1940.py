import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.PlateCarree()})

ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND, facecolor='gold')

ax.set_extent([19, 21.8, 37, 41.2])

cities = {
    "Agioi Saranta": (20.0069, 39.8747),
    "Argyrokastro": (20.1379, 40.0797),
    "Avlonas": (19.4845, 40.4651),
    "Berati": (19.9507, 40.7048),
    "Corfu": (19.9185, 39.6244),
    "Delvino": (20.0954, 39.9480),
    "Elbasan": (20.0832, 41.1110),
    "Erseka": (20.6796, 40.3376),
    "Himara": (19.7463, 40.1020),
    "Igoumenitsa": (20.2647, 39.5060),
    "Ioannina": (20.8509, 39.6632),
    "Kalpaki": (20.6254, 39.8861),
    "Kastoria": (21.2684, 40.5190),
    "Kleisoura": (20.1913, 40.3138),
    "Konitsa": (20.7524, 40.0479),
    "Korytsa": (20.7796, 40.6156),
    "Metsovo": (21.1822, 39.7701),
    "Pogradec": (20.6554, 40.9014),
    "Premeti": (20.3519, 40.2358),
    "Samarina": (21.0184, 40.1062),
    "Vovousa ": (21.0490, 39.9370)
}

greek_counterattacks = {
    "Morava-Ivan": (20.8287, 40.5979),
    "Peak 731": (20.0874, 40.4379),
    "Trempesina": (20.1163, 40.3497),
}

italian_attacks = {
    "Elaia-Kalamas": (20.3282, 39.5804),
    "Pindos": (20.9252, 40.0888)
}

for city, (lon, lat) in cities.items():
    ax.plot(lon, lat, 'ro', markersize=3, transform=ccrs.PlateCarree())

for counterattack, (lon, lat) in greek_counterattacks.items():
    ax.plot(lon, lat, 'bs', markersize=2, transform=ccrs.PlateCarree())

for attack, (lon, lat) in italian_attacks.items():
    ax.plot(lon, lat, 'bs', markersize=2, transform=ccrs.PlateCarree())

plt.title('Greco-Italian War (1940-1941)', fontsize=15)

plt.savefig('Greco-Italian War (1940-1941).png', dpi=300, bbox_inches='tight')
plt.show()