#import csv
#with open("weather.csv") as data_file:
#    data = csv.reader(data_file)
#    temp = []
#    for x in data:
#        if x[1] != "temp":
#            temp.append(x[1])
#    print(temp)

'''import pandas
data = pandas.read_csv("weather.csv")
print(data)
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
print(data["temp"].max())
print(data["temp"].mean())
print(data[data.temp == data.temp.max()])
data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data_csv")'''

import pandas
data_read = pandas.read_csv("Squirrel_Data.csv")
grey_count = len(data_read[data_read["Primary Fur Color"] == "Gray"])
red_count = len(data_read[data_read["Primary Fur Color"] == "Cinnamon"])
black_count = len(data_read[data_read["Primary Fur Color"] == "Black"])
print(grey_count)
print(red_count)
print(black_count)
data_dict = {
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[2473,392,103]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("SquirrelCount.csv")