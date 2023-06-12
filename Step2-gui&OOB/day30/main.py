#filenotfound
try:
    like = open ("miracle_alx.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    like = open("miracle_alx.txt", "w")
    like.write("you need to make money")
except KeyError as error_message:
    print(f"The {error_message} doesnot exist")
else:
    content = like.read()
    print(content)
finally:
    like.close()
    print("file was closed")