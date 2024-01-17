import pandas as pd

a = [1, 7, 2]
# show data as a table form (row ,column)
myvar = pd.Series(a)

print(myvar)
print(myvar[0])

calories = {"day1":50,"day2":40,"day3":30,"day4":20}
data = pd.Series(calories,["day1","day2"])
print(data)

print(pd.Series(calories))


data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data,index = ["Day1", "Day2", "Day3"])

print(df)
print(df.loc["Day1"])
print(df.info())


csv_data = pd.read_csv('annualdata.csv')
# print(csv_data.to_string())  to print entire data
print(csv_data)
print(pd.options.display.max_rows)


data_json = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

json_data = pd.DataFrame(data_json)
print(json_data)
