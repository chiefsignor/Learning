f = open("text1.txt", "w")
lines = ["Line 1", "Line 2", "Line 3"]
cont = "\n".join(lines)
f.write(cont)

f.close()
