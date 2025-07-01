with open("output.txt",'w') as file:
    text = input("Enter text to write the file: ")
    w = file.write(text)
    print("Data successfully written to output.txt.")
with open("output.txt",'a') as file:
    text = input("Enter additional text to append: ")
    w1 = file.write(text)
    print("Data successfully appended.")
with open("output.txt", 'r') as f:
    r = f.read()
    print(r)