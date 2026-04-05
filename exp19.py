with open("log.txt","a") as f:
    msg=input("Enter log: ")
    f.write(msg+"\n")
print("Log saved")
