# retunerar str, måste läggas i en variabel eftersom vi använder return
def displayName(name: str) -> str:
    return f"Hello {name}"


# Print retunerar none, så kalla på det utan att lägga det i en variabel och sen printa (endast function namnet)
def printName(name: str) -> None:
    print(f"Hello, I am printing my name: {name}")
