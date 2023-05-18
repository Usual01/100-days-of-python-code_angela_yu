placeholder = "[name]"
with open("mail_merge/names/names.txt") as names_file:
    names = names_file.readlines()
    
with open("mail_merge/letter/starting_letter.txt") as letter:
    leta = letter.read()
    for name in names:
        s_names =name.strip()
        new_letter = leta.replace(placeholder, s_names)
        with open(f"mail_merge/output/letter_for_{s_names}.txt", mode = "w") as written:
            written.write(new_letter)