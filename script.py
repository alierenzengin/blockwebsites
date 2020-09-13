
print("Coded by turkScript")
print("This script blocks websites for Windows")
print("Make sure you are running with administrator authority")
print("Type website address (without http and www)" )
blockedSite = input()
print("blocked site = "+ blockedSite)
blockerIp = "127.0.0.1 "
newData = blockerIp + blockededSite
print("Adding data to hosts file")

filePath = "C://Windows//System32//drivers//etc//hosts"
f = open(filePath, "a")
with open (filePath , "a") as f:
    f.write("\n\n\n\n\n\n\n\n\n\n\n\n"+ newData)

print("Task completed successfuly")
print("Press any key to close the program")
input()














    