# Rating
film = int(input("Rating sebuah Film = "))


if (film >= 21):
    print("Khusus DEWASA")

elif (film >= 13):
    print("Khusus Remaja")

elif (film >= 9):
    print("Bimbingan Orang tua")

elif (film < 9):
    print("Semua Usia")
