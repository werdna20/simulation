str = "input()"
out = ""
for i in range(len(str)):
    if str[i] != " ":
        out += "_"
    else:
        out += " "

print(out)
