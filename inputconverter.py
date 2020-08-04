#Author: Erfan Hosseini
import glob
import re

path = '/*.txt'
files = glob.glob(path)
x_min = 100000000
y_min = 100000000
x_max = -100000000
y_max = -100000000
for name in files:
    with open(name, 'r') as f1:
        a = f1.readlines()
        for i in range(len(a)):
            line_sequence = a[i].split()
            if float(line_sequence[0]) < x_min:
                x_min = float(line_sequence[0])
            if float(line_sequence[0]) > x_max:
                x_max = float(line_sequence[0])
            if float(line_sequence[1]) < y_min:
                y_min = float(line_sequence[1])
            if float(line_sequence[1]) > y_max:
                y_max = float(line_sequence[1])
            a[i] = re.sub('\s+', ',', a[i])
            a[i] = a[i][:-1]
            if i != len(a) -1:
                a[i] = str(i + 1)+ "," + a[i] + "\n"
            else:
                a[i] = str(i + 1) + "," + a[i]
    f1.close()
    with open(name, 'w') as f2:
        f2.writelines(a)
        f2.close()

print("X_min:",x_min,' ',"Y_min:",y_min,'-',"X_max:",x_max,' ',"Y_max",y_max)