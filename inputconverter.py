#Author: Erfan Hosseini
import glob
import os
from pyproj import Transformer

epsg = input("EPSG code of the projection:")
inProj = 'epsg:'+epsg
outProj = 'epsg:4326'
transformer = Transformer.from_crs(inProj, outProj)

pathname = input("Please insert the global path to the folder (end with '/'):") #pathname here
path = pathname + '*.txt'
files = glob.glob(path)
lat_min = 100000000
long_min = 100000000
lat_max = -100000000
long_max = -100000000
try:
	os.mkdir(os.path.join(pathname,'new'))
except FileExistsError:
	print("Rewriting files")

for name in files:
	with open(name, 'r') as f1:
		a = f1.readlines()
		for i in range(len(a)):
			line_sequence = a[i].split()
			long, lat = transformer.transform(float(line_sequence[0]),float(line_sequence[1]))
			v = (lat,long)
			if v[0] < lat_min:
				lat_min = v[0]
				lat_min_long = v[1]
			if v[0] > lat_max:
				lat_max = v[0]
				lat_max_long = v[1]
			if v[1] < long_min:
				long_min = v[1]
				long_min_lat = v[0]
			if v[1] > long_max:
				long_max = v[1]
				long_max_lat = v[0]
			a[i] = str(v[0])+","+str(v[1])+","+str(round(float(line_sequence[2])))
			if i != len(a) -1:
				a[i] = str(i + 1)+ "," + a[i] + "\n"
			else:
				a[i] = str(i + 1) + "," + a[i]
	f1.close()
	with open(pathname+'new/'+name.split('/')[-1], 'w') as f2:
		f2.writelines(a)
		f2.close()

print("lat_min:",lat_min,' ',"long_min:",long_min,'-',"lat_max:",lat_max,' ',"long_max",long_max)
print("------------------------------------------------------------")
print(lat_min,lat_min_long,"&",lat_max,lat_max_long,"&",long_min,long_min_lat,"&",long_max,long_max_lat)
