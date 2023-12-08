def czy_palindrom(slowo):
    sl2 = list(slowo)
    sl2.reverse()
    for a in range(len(slowo)):
        if slowo[a] != sl2[a]:
            return False
    return True

print("Sprawdzam dla wyrazu a:")
if czy_palindrom("a"):
    print("dobrze")
else:
    print("źle")

print("Sprawdzam dla wyrazu aa:")
if czy_palindrom("aa"):
    print("dobrze")
else:
    print("źle")

print("Sprawdzam dla wyrazu ab:")
if czy_palindrom("ab"):
    print("źle")
else:
    print("dobrze")

print("Sprawdzam dla wyrazu ala:")
if czy_palindrom("ala"):
    print("dobrze")
else:
    print("źle")

print("Sprawdzam dla wyrazu kot:")
if czy_palindrom("kot"):
    print("źle")
else:
    print("dobrze")

print("Sprawdzam dla wyrazu kajak:")
if czy_palindrom("kajak"):
    print("dobrze")
else:
    print("źle")

print("Sprawdzam dla wyrazu abba:")
if czy_palindrom("abba"):
    print("dobrze")
else:
    print("źle")

print("Sprawdzam dla wyrazu kotek:")
if czy_palindrom("kotek"):
    print("źle")
else:
    print("dobrze")


def sprawdz(slowo, czy_dobrze):
    print(f"Sprawdzam dla wyrazu {slowo}:")
    if czy_palindrom(slowo):
        print("źle")
    else:
        print("dobrze")

# skrócić : 51-55 jako 1 linia
sprawdz("aa", True)
sprawdz("kot", False)