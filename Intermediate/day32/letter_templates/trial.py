
# with open("brthdays.csv") as data:
#     formatted_data = []
#     for entry in data:
#         formatted_entry = ", ".join(str(e) for e in entry)
#         print(formatted_entry)
#         formatted_data.append(formatted_entry)

# result = "\n".join(formatted_data)

# print(result)

# with open("brthdays.csv") as data_file:
#     lines = data_file.readlines()

# formatted_data = []
# for line in lines:
#     formatted_entry = ", ".join(line.strip().split(','))
#     formatted_data.append(formatted_entry)

# result = "\n".join(formatted_data)
# print(result)
################################### TO CONVERT TO CSV##################
with open("tetet.csv") as data_file:
    lines = data_file.readlines()
a = []
for line in lines:
    b = ", ".join(line.strip().split(','))
    c = b.replace("\t", ",")
    a.append(c)
result = "\n".join(a)
print(result)
