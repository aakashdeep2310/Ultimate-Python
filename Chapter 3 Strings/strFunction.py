# name = "Aakash"

# print(len(name))

# a = name.endswith("sh")
# print(a)
# b = name.startswith("Aa")
# print(b)

name = "aakash"
print(name.capitalize()) # only first letter will be capital
name1 = "          aakash"
print(name1.strip())
print(name1.lstrip())
name2 = "aakash              "
print(name2.rstrip())


print(name.find("h"))
print(name.index("h"))
print(name.replace("aakash", "Aakash"))
name1 = "Abhinav"
print(name1.startswith("Abhi"))
print(name1.endswith("nav"))

print(name1.split("i"))
print(name1.rsplit("n", maxsplit=4))
