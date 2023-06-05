"""
You are goig to write a program that will mark a spot with an X
"""

row1 = [":)", ":()", ":("]
row2 = [":)", ":()", ":("]
row3 = [":)", ":()", ":("]
mapi = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("where do you want to hide the treasure")
vertical = int(position[0])
horizontal = int(position[1])
mapi[vertical- 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
#hint vertical = mapi[1][1]
