## It sould be mentioned that the following part of code should be run in Jupyter Notebook, as the heatmaps produced cannot be created in other Python editors ##




# heatmaps for separate buildings 

hmap = folium.Map(location=[40.607421, 22.957578], zoom_start=13)
path = 'file_directory_of_spreadsheet_file'

for_map = pd.read_excel(path)

print(
    'Buildings to choose:\nManagement Βuilding = 1\nArchitecture = 2\nΒuilding D = 3\nFaculty of Education = 4\nFaculty of Theology = 5\nHydraulics Building = 6\n
    Building E13 = 7\nUniversity Gym = 8\nUniversity Student Club = 9')
    
building = int(input("Βuilding selection (1-9): "))

print('Fuel selection:\nNaatural Gas = 1\nHeating Oil = 2')
fuel = int(input("Fuel selection (1-2): "))

if fuel == 1:
    fuel = str('ng')
else:
    fuel = str('ho')

print('Pollutant selection:\nCO2 = 1\nCO = 2\nNOx = 3\nVOC = 4\nSOx = 5\nPM = 6')
pollutant = int(input("Pollutant selection (1-6): "))


if pollutant == 1:
    pollutant = str('C_')
elif pollutant == 2:
    pollutant = str('CO_')
elif pollutant == 3:
    pollutant = str('NOx_')
elif pollutant == 4:
    pollutant = str('VOC_')
elif pollutant == 5:
    pollutant = str('SOx_')
elif pollutant == 6:
    pollutant = str('PM_')
else:
    pollutant = str('error')

column = str(pollutant + fuel)

print(column)

max_amount = float(for_map['CO2_ho'].max())
print(max_amount)

for_map = for_map[(for_map['Building'] == Building)]

hm_wide = HeatMap( list(zip(for_map.Latitude.values, for_map.Longtitude.values, for_map[column].values)),
                   min_opacity=0.3,
                   max_val=max_amount,
                   radius=17, blur=8,
                   max_zoom=1,
                 )

steps=40
colormap = branca.colormap.linear.YlOrRd_09.scale(0, max_amount).to_step(steps)
gradient_map=defaultdict(dict)

for i in range(steps):
    gradient_map[1/steps*i] = colormap.rgb_hex_str(1/steps*i)
colormap.add_to(hmap)

hmap.add_child(hm_wide)


# heatmaps for all buildings (gas oil NOxes)


hmap = folium.Map(location=[40.607421, 22.957578], zoom_start=13)
path = 'file_directory_of_spreadsheet_file'

for_map = pd.read_excel(path)


print('Fuel choice:\nNatural Gas = 1\nHeating oil = 2')
fuel = int(input("Fuel selection (1-2): "))

if fuel == 1:
    fuel = str('ng')
else:
    fuel = str('ho')

print('Pollutant selection:\nCO2 = 1\nCO = 2\nNOx = 3\nVOC = 4\nSOx = 5\nPM = 6')
pollutant = int(input("Pollutant selection (1-6): "))


if pollutant == 1:
    pollutant = str('C_')
elif pollutant == 2:
    pollutant = str('CO_')
elif pollutant == 3:
    pollutant = str('NOx_')
elif pollutant == 4:
    pollutant = str('VOC_')
elif pollutant == 5:
    pollutant = str('SOx_')
elif pollutant == 6:
    pollutant = str('PM_')
else:
    pollutant = str('error')

column = str(pollutant + fuel)

print(column)

max_amount = float(for_map['NOx_ho'].max())
print(max_amount)

hm_wide = HeatMap( list(zip(for_map.Latitude.values, for_map.Longtitude.values, for_map[column].values)),
                   min_opacity=0.2,
                   max_val=max_amount,
                   radius=17, blur=10,
                   max_zoom=1,
                 )


steps=20
colormap = branca.colormap.linear.YlOrRd_09.scale(0, for_map[column].max()).to_step(steps)
gradient_map=defaultdict(dict)

hmap.add_child(hm_wide)

for i in range(steps):
    gradient_map[1/steps*i] = colormap.rgb_hex_str(1/steps*i)
colormap.add_to(hmap)

hmap.add_child(hm_wide)


# points of maxes in map

hmap = folium.Map(location=[40.607421, 22.957578], zoom_start=13)
path = 'file_directory_of_spreadsheet_file'

for_map = pd.read_excel(path)

df_max = pd.DataFrame()
df_building = pd.DataFrame()

for building in range(1,10):
    df_building = for_map[(for_map['Building'] == building)]
    df_building = df_building[df_building.NOx_fa == df_building.NOx_fa.max()]
    df_max = df_max.append(df_building)
    
df_max = df_max.drop_duplicates('Building')
locations = df_max[['Latitude', 'Longtitude']]
locationlist = locations.values.tolist()

hmap = folium.Map(location=[40.607421, 22.957578], zoom_start=13)

for point in range(0, 9):
    folium.Marker(locationlist[point]).add_to(hmap)
    
hmap


# plot for concentration - distance from point source, for each building

path = 'file_directory_of_spreadsheet_file'
for_map = pd.read_excel(path)

df_building = pd.DataFrame()
building = int((input('Buildings to choose:\nManagement Βuilding = 1\nArchitecture = 2\nΒuilding D = 3\nFaculty of Education = 4\nFaculty of Theology = 5\n
Hydraulics Building = 6\nBuilding E13 = 7\nUniversity Gym = 8\nUniversity Student Club = 9')))

for_map = for_map[(for_map['Buiding'] == building)]
df_building = for_map[(for_map['Distance_y(m)'] == 0)]
df_building = df_building.drop_duplicates('Distance_x (m)')

print('Ρύποι προς επιλογή:\nCO2 = 1\nCO = 2\nNOx = 3\nVOC = 4\nSOx = 5\nPM = 6')
pollutant = int(input("Pollutant selection (1-6): "))

if pollutant == 1:
    pollutant = str('CO2_')
elif pollutant == 2:
    pollutant = str('CO_')
elif pollutant == 3:
    pollutant = str('NOx_')
elif pollutant == 4:
    pollutant = str('VOC_')
elif pollutant == 5:
    pollutant = str('SOx_')
elif pollutant == 6:
    pollutant = str('PM_')
else:
    pollutant = str('error')

column_ng = str(pollutant + 'ng')
column_ho = str(pollutant + 'ho')

line_C_ng = []
line_C_ho = []
line_dist = []
line_C_ng = df_building[column_ng].tolist()
line_C_ho = df_building[column_ho].tolist() 
line_dist = df_building['Distance_x (m)'].tolist()

plt.plot(line_dist, line_C_ng, color='b')
plt.plot(line_dist, line_C_ho, color='r', alpha=0.5)

plt.xlabel('Distance from source point axis (m)')
plt.ylabel('Concentration μg/m^3')
plt.title("Concentration comparison")
plt.legend(["Natural Gas","Gas Oil"])
plt.show()



