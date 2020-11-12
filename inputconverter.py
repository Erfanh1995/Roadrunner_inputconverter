#Author: Erfan Hosseini
import glob
import utm

utm_data = [16,'T'] #example: chicago
path = '*.txt'
files = glob.glob(path)
lat_min = 100000000
long_min = 100000000
lat_max = -100000000
long_max = -100000000
for name in files:
    with open(name, 'r') as f1:
        a = f1.readlines()
        for i in range(len(a)):
            line_sequence = a[i].split()
            v = utm.to_latlon(round(float(line_sequence[0])),round(float(line_sequence[1])), utm_data[0],utm_data[1])
            if v[0] < lat_min:
                lat_min = v[0]
            if v[0] > lat_max:
                lat_max = v[0]
            if v[1] < long_min:
                long_min = v[1]
            if v[1] > long_max:
                long_max = v[1]
            a[i] = str(v[0])+","+str(v[1])+","+str(round(float(line_sequence[2])))
            if i != len(a) -1:
                a[i] = str(i + 1)+ "," + a[i] + "\n"
            else:
                a[i] = str(i + 1) + "," + a[i]
    f1.close()
    with open(name, 'w') as f2:
        f2.writelines(a)
        f2.close()

print("lat_min:",lat_min,' ',"long_min:",long_min,'-',"lat_max:",lat_max,' ',"long_max",long_max)
