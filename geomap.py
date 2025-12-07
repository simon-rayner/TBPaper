import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets

# Load the built-in world map dataset from GeoPandas



# Print the list
print("Available built-in datasets in GeoPandas:")
#world = gpd.read_file(gpd.datasets.get_path(geodatasets.get_path('geoda airbnb')))
url = "http://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
dfc = gpd.read_file(url)



# Example: Create dummy data to plot
import pandas as pd

data = {'country': ['France', 'Germany', 'Italy', 'Spain'],
        'value': [100, 150, 80, 120]}
df = pd.DataFrame(data)

# Merge your data with the world GeoDataFrame
#world_with_data = world.merge(df, left_on='name', right_on='country', how='left')
world_with_data = dfc.merge(df, left_on='name', right_on='country', how='left')

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
#world_with_data.plot(column='value', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
dfc.plot(column='value', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('World Map with Data')
ax.set_axis_off()  # Remove axes for a cleaner map
plt.show()


#  pip install folium
import folium

m = folium.Map(location=[0, 0], zoom_start=2)  # Centered at [0,0] with zoom level 2
# Example: Add markers for specific locations
folium.Marker(
    location=[48.8566, 2.3522],  # Paris coordinates
    popup="Paris"
).add_to(m)

# Example: Create a choropleth map (requires GeoJSON data and your values)
# folium.Choropleth(
#     geo_data=world_geojson, # Path to GeoJSON file or dictionary
#     name='choropleth',
#     data=df,
#     columns=['country', 'value'],
#     key_on='feature.properties.name', # Key in GeoJSON to match with 'country'
#     fill_color='YlGnBu',
#     legend_name='Your Data Values'
# ).add_to(m)
m.save("world_map_with_data.html")

