a = input("entree")

print(a)

print(int(a))

relance = {
    "d1" : 0,
    "d2" : 0
}

relance["d{}".format(a)] = 1
print(relance)