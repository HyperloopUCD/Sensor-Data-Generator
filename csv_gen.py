import csv

###CONTROLS
#Units Unknown
dist_laser_sense = ['C_Las0, C_Las1']

###SPEED SENSING MODULE
#Units Unknown
dist_lidar_sense = ['SX_Las0, SX_Las1']

###BRAKING###
#Tenths of A Degree Celsius: XX.X
pressure_brake_sense = ['B_Pres0','B_Pres1','B_Pres2','B_Pres3','B_Pres4','B_Pres5','B_Pres6','B_Pres7','B_Pres8','B_Pres9']
#Tenths of A Degree Celsius: XX.X
thermo_brake_sense = ['B_Tem0, B_Tem1'];

###PROPULSION###
#PSIG (Gauge Pressure, relative to atmospheric pressure, i.e. 0 PSIG = standard atmospheric)
pressure_sense = ['P_Pres0','P_Pres1','P_Pres2','P_Pres3','P_Pres4', 'P_Pres5', 'P_Pres6']
#Tenths of A Degree Celsius: XX.X
prop_pressure_sense = ['P_Tem0','P_Tem1','P_Tem2','P_Tem3','P_Tem4','P_Tem5','P_Tem6','P_Tem7','P_Tem8']

all_sensors = [dist_laser_sense, dist_lidar_sense, pressure_brake_sense, thermo_brake_sense, pressure_sense, prop_pressure_sense]

#Flatten list of lists 
all_sensors = [sensor for sensor_list in all_sensors for sensor in sensor_list]

#Generate arrays of data


with open('out.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',
		quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['sens_1', '2000', '1000'])