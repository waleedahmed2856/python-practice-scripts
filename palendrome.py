word = input("Enter the word")

save_word = ""

for chr in word:

    save_word = chr + save_word
if word == save_word:print(f"The word is palendrome: {save_word}")

else:print(f"Not palendrome:{save_word}")

