# IN THIS WE WILL TRY TO CREATE TO-DO LIST BY USING LIST AND TUPLE.

tasks=[]
tasks.append(("PYTHON HOWEWORK","COMPLETED."))
tasks.append(("DSA HOMEWORK","PENDING."))
tasks.append(("BEE HOMEWORK","PENDING."))

tasks[1]=("DSA HOMEWORK","COMPLETED.")
print(tasks)

del tasks[0]
print(tasks)

#tasks.sort()
#print(tasks)

print(sorted(tasks))

tasks.remove(("BEE HOMEWORK","PENDING."))
print(tasks)