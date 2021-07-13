# importing libraries, modules etc...

from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.optimize as opt
from scipy.optimize import brentq
from scipy.optimize import root
from numpy import log as ln
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca.colormap
from collections import defaultdict

# importing constants from relative scientific literature

T_fumes = 423
gravity_acceleration = 9.81
fumes_velocity = 15.3
karman_constant = 0.4
vegetative_roughness = 1.3

x_deg = 0
y_deg = 0

x_min = 0
y_min = 0

x_sec = 0
y_sec = 0


# importing constants and list for the model
I = 0
climatic_scenario = 1
building_list = []
climatic_scenario_list = []
meteorological_conditions_list = []
C_natural_gas_list = []
C_heating_oil_list = []
distance_x_list = []
std_dev_z_list = []
std_dev_y_list = []
distance_y_list = []
lat_list_right = []
lon_list_right = []
lat_list_left = []
lon_list_left = []
CO2_natural_gas_list = []
CO_natural_gas_list = []
NOx_natural_gas_list = []
VOC_natural_gas_list = []
SOx_natural_gas_list = []
PM_natural_gas_list = []
CO2_heating_oil_list = []
CO_heating_oil_list = []
NOx_heating_oil_list = []
VOC_heating_oil_list = []
SOx_heating_oil_list = []
PM_heating_oil_list = []

# selection of meteorological conditions

meteorological_conditions = 'b'

# selection of climatic scenario for analysis

climatic_scenario == 8

# selection of wind angle

fi = 30
omega = 90 - fi



if climatic_scenario == 1:
    T_air = 2
    wind_velocity = 1.5
elif climatic_scenario == 2:
    T_air = 2
    wind_velocity = 2.5
elif climatic_scenario == 3:
    T_air = 2
    wind_velocity = 3.5
elif climatic_scenario == 4:
    T_air = 2
    wind_velocity = 5.5
elif climatic_scenario == 5:
    T_air = 2
    wind_velocity = 15
elif climatic_scenario == 6:
    T_air = 2
    wind_velocity = 20
elif climatic_scenario == 7:
    T_air = 5
    wind_velocity = 1.5
elif climatic_scenario == 8:
    T_air = 5
    wind_velocity = 2.5
elif climatic_scenario == 9:
    T_air = 5
    wind_velocity = 3.5
elif climatic_scenario == 10:
    T_air = 5
    wind_velocity = 5.5
elif climatic_scenario == 11:
    T_air = 5
    wind_velocity = 15
elif climatic_scenario == 12:
    T_air = 5
    wind_velocity = 20
elif climatic_scenario == 13:
    T_air = 8
    wind_velocity = 1.5
elif climatic_scenario == 14:
    T_air = 8
    wind_velocity = 2.5
elif climatic_scenario == 15:
    T_air = 8
    wind_velocity = 3.5
elif climatic_scenario == 16:
    T_air = 8
    wind_velocity = 5.5
elif climatic_scenario == 17:
    T_air = 8
    wind_velocity = 15
elif climatic_scenario == 18:
    T_air = 8
    wind_velocity = 20
elif climatic_scenario == 19:
    T_air = 11
    wind_velocity = 1.5
elif climatic_scenario == 20:
    T_air = 11
    wind_velocity = 2.5
elif climatic_scenario == 21:
    T_air = 11
    wind_velocity = 3.5
elif climatic_scenario == 22:
    T_air = 11
    wind_velocity = 5.5
elif climatic_scenario == 23:
    T_air = 11
    wind_velocity = 15
elif climatic_scenario == 24:
    T_air = 11
    wind_velocity = 20
elif climatic_scenario == 25:
    T_air = 14
    wind_velocity = 1.5
elif climatic_scenario == 26:
    T_air = 14
    wind_velocity = 2.5
elif climatic_scenario == 27:
    T_air = 14
    wind_velocity = 3.5
elif climatic_scenario == 28:
    T_air = 14
    wind_velocity = 5.5
elif climatic_scenario == 29:
    T_air = 14
    wind_velocity = 15
elif climatic_scenario == 30:
    T_air = 14
    wind_velocity = 20



# Choise of building to be analysed


for building in range(1,10):
    if building == 1:
        chimney_length = 3.85
        chimney_width = 2.05
        h_chimney = 41.9
        Q_natural_gas = 1102.82
        Q_heating_oil = 1570.54
        lat_start = 40.630625
        lon_start = 22.956482
        distance_max = 418.4865485
    elif building == 2:
        chimney_length = 2.5
        chimney_width = 1.9
        h_chimney = 18.45
        Q_natural_gas = 41.72
        Q_heating_oil = 59.42
        lat_start = 40.628345
        lon_start = 22.958944
        distance_max = 319.7281116
    elif building == 3:
        chimney_length = 1.42
        chimney_width = 0.8
        h_chimney = 27.79
        Q_natural_gas = 105.65
        Q_heating_oil = 150.46
        lat_start = 40.627284
        lon_start = 22.960023
        distance_max = 265.455499
    elif building == 4:
        chimney_length = 0.415
        chimney_width = 0.405
        h_chimney = 47.25
        Q_natural_gas = 117.08
        Q_heating_oil = 166.74
        lat_start = 40.627459
        lon_start = 22.961568
        distance_max = 371.6373852
    elif building == 5:
        chimney_length = 2.84
        chimney_width = 1.6
        h_chimney = 27.68
        Q_natural_gas = 463.27
        Q_heating_oil = 659.74
        lat_start = 40.630723
        lon_start = 22.955131
        distance_max = 333.5177008
    elif building == 6:
        chimney_length = 0.6
        chimney_width = 0.45
        h_chimney = 21.68
        Q_natural_gas = 43.93
        Q_heating_oil = 62.56
        lat_start = 40.628093
        lon_start = 22.960745
        distance_max = 368.765376
    elif building == 7:
        chimney_length = 0.37
        chimney_width = 0.35
        h_chimney = 18.45
        Q_natural_gas = 257.34
        Q_heating_oil = 366.48
        lat_start = 40.626889
        lon_start = 22.961327
        distance_max = 419.4285975
    elif building == 8:
        chimney_length = 1.7
        chimney_width = 0.8
        h_chimney = 16.63
        Q_natural_gas = 36.85
        Q_heating_oil = 52.48
        lat_start = 40.627071
        lon_start = 22.963486
        distance_max = 208.2021911
    elif building == 9:
        chimney_length = 2.9
        chimney_width = 2.1
        h_chimney = 15.1
        Q_natural_gas = 55.28
        Q_heating_oil = 78.72
        lat_start = 40.625715
        lon_start = 22.961027
        distance_max = 336.4133407
    chimney_surface_area = chimney_length * chimney_width
    chimney_perimeter = chimney_length + chimney_width
    diametros_kaminadas = 4 * (chimney_surface_area / chimney_perimeter)

    # conversion of Celsius degrees to Kelvin degrees

    T_air_K = 273 + T_air
    dT = T_fumes - T_air_K

    # calculation of coefficient F

    F = (gravity_acceleration * fumes_velocity * (diametros_kaminadas ** 2) * (T_fumes - T_air_K)) / (
            4 * T_air_K)

    # calculation of plume lift and total height

    if F < 55:
        dh = (21.425 * (F ** 0.75)) / wind_velocity
    elif F > 55:
        dh = (38.71 * (F ** 0.6)) / wind_velocity

    H = dh + h_chimney


    # choice of atmospheric stability

    if meteorological_conditions == 'a' or meteorological_conditions == '2' and wind_velocity < 2:
        atmospheric_stability = "A"
    elif meteorological_conditions == 'c' and wind_velocity < 2:
        atmospheric_stability = "B"
    elif meteorological_conditions == 'a' and wind_velocity > 2 or wind_velocity < 3:
        atmospheric_stability = "A"
    elif meteorological_conditions == 'b' and wind_velocity > 2 or wind_velocity < 3:
        atmospheric_stability = "B"
    elif meteorological_conditions == 'c' and wind_velocity > 2 or wind_velocity < 3:
        atmospheric_stability = "C"
    elif meteorological_conditions == 'a' or meteorological_conditions == 'b' and wind_velocity > 3 or wind_velocity < 5:
        atmospheric_stability = "B"
    elif meteorological_conditions == 'c' and wind_velocity > 3 or wind_velocity < 5:
        atmospheric_stability = "C"
    elif meteorological_conditions == 'a' or meteorological_conditions == 'b' and wind_velocity > 5 or wind_velocity < 6:
        atmospheric_stability = "C"
    elif meteorological_conditions == 'c' and wind_velocity > 5 or wind_velocity < 6:
        atmospheric_stability = "D"
    elif meteorological_conditions == 'a' and wind_velocity >= 6:
        atmospheric_stability = "C"
    elif meteorological_conditions == 'b' and wind_velocity >= 6:
        atmospheric_stability = "D"
    elif meteorological_conditions == 'c' and wind_velocity >= 6:
        atmospheric_stability = "C"
    elif meteorological_conditions == 'd':
        atmospheric_stability = "D"


    # calculation of coefficients k

    if atmospheric_stability == 'A':
        k_1 = 0.25
        k_2 = 927
        k_3 = 0.189
        k_4 = 0.102
        k_5 = -1.918
    elif atmospheric_stability == 'B':
        k_1 = 0.202
        k_2 = 370
        k_3 = 0.162
        k_4 = 0.0962
        k_5 = -0.101
    elif atmospheric_stability == 'C':
        k_1 = 0.134
        k_2 = 283
        k_3 = 0.134
        k_4 = 0.0722
        k_5 = 0.102
    elif atmospheric_stability == 'D':
        k_1 = 0.0787
        k_2 = 707
        k_3 = 0.135
        k_4 = 0.0475
        k_5 = 0.465


    # velocity correction

    friction_velocity = (karman_constant * wind_velocity) / (ln(10 / vegetative_roughness))
    wind_velocity_corrected = (friction_velocity / karman_constant) * (ln(H / vegetative_roughness))

    range = 20 * distance_max
    step = 10
    distance_x = 10

    # calculation of maximum concentrations

    while distance_x < range:
        # calculation of coefficient a,b,c,d and theta
        if atmospheric_stability == 'A':
            c = 24.167
            d = 2.5334
            if distance_x < 100.0:
                a = 122.8
                b = 0.9447
            elif distance_x > 100.0 and distance_x < 150.0:
                a = 158.08
                b = 1.0542
            elif distance_x > 150.0 and distance_x < 200.0:
                a = 170.22
                b = 1.0932
            elif distance_x > 200.0 and distance_x < 250.0:
                a = 179.52
                b = 1.1262
            elif distance_x > 260.0 and distance_x < 300.0:
                a = 217.41
                b = 1.2644
            elif distance_x > 300.0 and distance_x < 400.0:
                a = 258.89
                b = 1.4094
            elif distance_x > 400.0 and distance_x < 500.0:
                a = 346.75
                b = 1.72830
            elif distance_x > 500.0 and distance_x < 3110.0:
                a = 453.85
                b = 2.11660
            elif distance_x > 3110.0:
                std_dev_z = 5000
        elif atmospheric_stability == 'B':
            c = 18.333
            d = 1.8096
            if distance_x < 200.0:
                a = 90.673
                b = 0.93198
            elif distance_x > 200.0 and distance_x < 400.0:
                a = 98.483
                b = 0.98332
            elif distance_x > 400.0:
                a = 109.3
                b = 1.0971
        elif atmospheric_stability == 'C':
            a = 61.141
            b = 0.91465
            c = 12.5
            d = 1.0857
        elif atmospheric_stability == 'D':
            c = 8.333
            d = 0.72382
            if distance_x < 300.0:
                a = 34.459
                b = 0.86974
            elif distance_x > 300.0 and distance_x < 1000.0:
                a = 32.093
                b = 0.81066
            elif distance_x > 1010.0 and distance_x < 3000.0:
                a = 32.093
                b = 0.64403
            elif distance_x > 3000.0 and distance_x < 10000.0:
                a = 33.504
                b = 0.60486
            elif distance_x > 10000.0 and distance_x < 30000.0:
                a = 36.65
                b = 0.56589
            elif distance_x > 30000:
                a = 44.053
                b = 0.51179

        theta = 0.017453293 * (c - (d * (ln(distance_x / 1000))))
        std_dev_y = 465.11628 * (distance_x / 1000) * math.tan(theta)
        std_dev_z = ((k_4 * distance_x) / ((1 + (distance_x / k_2)) ** k_5))
        distance_y = 0
        distance_z = 0

        for k in range(1, 9):

            factor_1 = Q_natural_gas / (math.pi * wind_velocity_corrected * std_dev_y * std_dev_z)
            factor_2 = math.exp(-((distance_y ** 2) / (2 * (std_dev_y ** 2))))
            factor_3 = math.exp(-(H ** 2) / (2 * (std_dev_z ** 2)))
            factor_4 = Q_heating_oil / (math.pi * wind_velocity_corrected * std_dev_y * std_dev_z)

            C_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000

            CO2_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000
            CO_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000*5.3*(10**(-4))
            NOx_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000*7.13*(10**(-4))
            VOC_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000*3.57*(10**(-5))
            SOx_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000*5.35*(10**(-5))
            PM_natural_gas = 1.7 * factor_1 * factor_2 * factor_3 * 1000000*1.6*(10**(-5))

            C_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000

            CO2_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000
            CO_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000*0.00176
            NOx_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000*0.01273
            VOC_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000*8.92*(10**(-4))
            SOx_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000*6.5*(10**(-4))
            PM_heating_oil = 1.7 * factor_4 * factor_2 * factor_3 * 1000000*8.11*(10**(-4))

            # calculation of sine and cosine

            tan_fi = round((math.tan(math.radians(fi))), 3)
            sin_omega = round((math.sin(math.radians(omega))), 3)
            cos_omega = round((math.cos(math.radians(omega))), 3)

            # calculation of the distance from the starting point and its conversion into degrees, minutes, seconds

            y_min = round((((distance_x * tan_fi * 0.000540679)) / 60), 6)
            x_min = round(((distance_x * 0.0006835083) / 60), 6)

            # coordinates added to the original coordinates

            lat_0 = round((y_deg + y_min + y_sec), 6)
            lon_0 = round((x_deg + x_min + x_sec), 6)

            # intermediate points

            lat_intermediate = round((lat_start - lat_0), 6)
            lon_intermediate = round((lon_start + lon_0), 6)

            # calculation of the distance from the intermediate point and its conversion into degrees, minutes, seconds

            y_dev_min = round((((distance_y * sin_omega * 0.000540679)) / 60), 6)
            x_dev_min = round(((distance_y * cos_omega * 0.0006835083) / 60), 6)

            # coordinates added to the intermediate coordinates

            lat_0_dev = round((y_deg + y_dev_min + y_sec), 6)
            lon_0_dev = round((x_deg + x_dev_min + x_sec), 6)

            # endpoints calculation

            lat_tel_right = round((lat_intermediate + lat_0_dev), 6)
            lon_tel_right = round((lon_intermediate + lon_0_dev ), 6)

            lat_tel_left = round((lat_intermediate - lat_0_dev), 6)
            lon_tel_left = round((lon_intermediate - lon_0_dev), 6)


            C_natural_gas_list.append(C_natural_gas)
            C_heating_oil_list.append(C_heating_oil)
            distance_x_list.append(distance_x)
            distance_y_list.append(distance_y)
            lat_list_right.append(lat_tel_right)
            lon_list_right.append(lon_tel_right)
            lat_list_left.append(lat_tel_left)
            lon_list_left.append(lon_tel_left)
            building_list.append(building)
            climatic_scenario_list.append(climatic_scenario)
            meteorological_conditions_list.append(meteorological_conditions)
            CO2_natural_gas_list.append(CO2_natural_gas)
            CO_natural_gas_list.append(CO_natural_gas)
            NOx_natural_gas_list.append(NOx_natural_gas)
            VOC_natural_gas_list.append(VOC_natural_gas)
            SOx_natural_gas_list.append(SOx_natural_gas)
            PM_natural_gas_list.append(PM_natural_gas)
            CO2_heating_oil_list.append(CO2_heating_oil)
            CO_heating_oil_list.append(CO_heating_oil)
            NOx_heating_oil_list.append(NOx_heating_oil)
            VOC_heating_oil_list.append(VOC_heating_oil)
            SOx_heating_oil_list.append(SOx_heating_oil)
            PM_heating_oil_list.append(PM_heating_oil)

            df_results_1 = pd.DataFrame({'Latitude': lat_list_right,
                                       'Longtitude': lon_list_right,
                                       'C_natural_gas': C_natural_gas_list,
                                       'C_heating_oil': C_heating_oil_list,
                                       'Distance from source (m)': distance_x_list,
                                       'Distance from central axis (m)': distance_y_list,
                                       'Building': building_list,
                                       'Climatic scenario': climatic_scenario_list,
                                       'Meteorological conditions': meteorological_conditions_list,
                                       'CO2_natural_gas': CO2_natural_gas_list,
                                       'CO_natural_gas': CO_natural_gas_list,
                                       'NOx_natural_gas': NOx_natural_gas_list,
                                       'VOC_natural_gas': VOC_natural_gas_list,
                                       'SOx_natural_gas': SOx_natural_gas_list,
                                       'PM_natural_gas': PM_natural_gas_list,
                                       'CO2_heating_oil': CO2_heating_oil_list,
                                       'CO_heating_oil': CO_heating_oil_list,
                                       'NOx_heating_oil': NOx_heating_oil_list,
                                       'VOC_heating_oil': VOC_heating_oil_list,
                                       'SOx_heating_oil': SOx_heating_oil_list,
                                       'PM_heating_oil': PM_heating_oil_list})

            df_results_2 = pd.DataFrame({'Latitude': lat_list_left,
                                         'Longtitude': lon_list_left,
                                         'C_natural_gas': C_natural_gas_list,
                                         'C_heating_oil': C_heating_oil_list,
                                         'Distance from source (m)': distance_x_list,
                                         'Distance from central axis (m)': distance_y_list,
                                         'Building': building_list,
                                         'Climatic scenario': climatic_scenario_list,
                                         'Meteorological conditions': meteorological_conditions_list,
                                         'CO2_natural_gas': CO2_natural_gas_list,
                                         'CO_natural_gas': CO_natural_gas_list,
                                         'NOx_natural_gas': NOx_natural_gas_list,
                                         'VOC_natural_gas': VOC_natural_gas_list,
                                         'SOx_natural_gas': SOx_natural_gas_list,
                                         'PM_natural_gas': PM_natural_gas_list,
                                         'CO2_heating_oil': CO2_heating_oil_list,
                                         'CO_heating_oil': CO_heating_oil_list,
                                         'NOx_heating_oil': NOx_heating_oil_list,
                                         'VOC_heating_oil': VOC_heating_oil_list,
                                         'SOx_heating_oil': SOx_heating_oil_list,
                                         'PM_heating_oil': PM_heating_oil_list})

            df_results = df_results_1.append(df_results_2)

            distance_y += std_dev_y*0.5

        distance_x += 10

        print(building,((distance_x/range)*100),'%')

df_results.to_excel(%file_directory%)

print('Sensitivity analysis was completed and pollution data was stored in excel file')

