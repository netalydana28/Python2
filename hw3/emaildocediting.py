with open("emails.txt", "r+") as doc:
    emails = doc.read().split()
    for i in range(len(emails)):
        ans = "name"+ str(i)+ " " + "<"+ emails[i] + ">"
        doc.write(ans + "\n")