import pandas
data = pandas.read_csv("squirrel.csv")
grays = len(data[data["Primary Fur Color"] == "Gray"])
reds = len(data[data["Primary Fur Color"] == "Cinnamon"])
blacks = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grays", "reds", "blacks"],
    "count":[grays, reds, blacks]

}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")