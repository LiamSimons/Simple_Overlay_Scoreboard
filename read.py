f = open("D:\Files\PycharmProjects\Overlay_first_test\\variables.txt", "r")

variables = []

for line in f:
    line = line.strip('\n')
    line = line.replace(' ', '')
    variables.append(line)

f.close()
