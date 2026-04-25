print("Welcome to the code messager,\nWhere you can enter codes and I will decode it, or you enter a message and I will turn it into a code.")
code_word = input("Enter your coded message: ")
Word_shift_num = int(input("Enter your shift amount: "))
print("The message is: ")
for i in range(len(code_word)):
    char = code_word[i]
    Word_shift_num = Word_shift_num%26
    shifted_code = (chr((ord(char)) + (Word_shift_num)))
    print(shifted_code, end = "")