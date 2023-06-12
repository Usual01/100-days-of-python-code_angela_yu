PLACEHOLDER = "[name]"

with open("./input/names/names.txt") as names_file:
    names = names_file.readlines()
    

with open("./input/letter/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        s_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, s_name)
        with open(f"./output/letter_for_{s_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)