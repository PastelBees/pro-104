import csv
from collections import Counter

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

new_data=[]

for i in range(len(data)):
    n_num = data[i][2]
    new_data.append(float(n_num))

dl = len(new_data)


def findingMean():

    sum = 0

    for x in new_data:
        sum += x

    mean = sum/dl

    print("The average weight of an 18 year old is " + str(mean), "pounds.")

findingMean()


def findingMedian():

    new_data.sort()

    if dl%2 == 0:
        m1 = float(new_data[dl//2])
        m2 = float(new_data[dl//2 - 1])
        median = (m1 + m2)/2

    else:
        median = new_data[dl//2]
        print(dl)

    print("The median is " + str(median), "pounds.")

findingMedian()


def findingMode():

    data = Counter(new_data)

    mdfr = {"75-85":0,
            "85-95":0,
            "95-105":0,
            "105-115":0,
            "115-125":0,
            "125-135":0,
            "135-145":0,
            "145-155":0,
            "155-165":0,
            "165-175":0,
            }
                      
    for height, occurence in data.items():
        if 75 < float(height) < 85:
            mdfr["75-85"] += occurence
        elif 85 < float(height) < 95:
            mdfr["85-95"] += occurence
        elif 95 < float(height) < 105:
            mdfr["95-105"] += occurence
        elif 105 < float(height) < 115:
            mdfr["105-115"] += occurence
        elif 115 < float(height) < 125:
            mdfr["115-125"] += occurence
        elif 125 < float(height) < 135:
            mdfr["125-135"] += occurence
        elif 135 < float(height) < 145:
            mdfr["135-145"] += occurence
        elif 145 < float(height) < 155:
            mdfr["145-155"] += occurence
        elif 155 < float(height) < 165:
            mdfr["155-165"] += occurence
        elif 165 < float(height) < 175:
            mdfr["165-175"] += occurence
     

    mode_range, mode_occurence = 0, 0

    for range, occurence in mdfr.items():

        if occurence > mode_occurence:

            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

    mode = float((mode_range[0] + mode_range[1]) / 2)

    print(f"The mode is {mode:2f} pounds.")

findingMode()