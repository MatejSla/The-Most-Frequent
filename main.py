zoznam = ["b", "b", "c", "a", "b", "a"]
def most_frequent(data: list[str]) -> str:
    numero = 0
    najcastejsie = ""
    for i in zoznam:
        if zoznam.count(i) > numero:
            numero = zoznam.count(i)
            najcastejsie = i
    return najcastejsie
print(most_frequent(zoznam))
