try:
    with open('sample.txt','r') as file1:
        l = file1.readlines()
        print("Reading file content")
        for i in range(len(l)):
            print(f"Line {i+1}: {l[i]}")
except:
    print('Error: The file "sample.txt" was not found.')
