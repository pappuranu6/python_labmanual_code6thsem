with open("a.txt") as f1, open("b.txt","w") as f2:
    f2.write(f1.read())
print("File copied")
