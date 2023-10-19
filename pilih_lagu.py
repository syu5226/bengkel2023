#!/usr/bin/env python

def main():
    print("PILIH NAMA LAGU")

    lagu = [
        "warisan",
        "tanggal 31",
        "saya anak malaysia",
        "inilah barisan kita",
        "negaraku"
        ]

    x = (lagu)
    print("1.warisan")
    print("2.tanggal 31")
    print("3.saya anak malaysia")
    print("4.inilah barisan kita")
    print("5.negaraku")
    
    guess = None

    while x != guess:

        guess = str(input("Pilih lagu patriotik yang dinyanyikan oleh Sudirman : "))
        
        if guess == "warisan":
            print("Betul")
            break
        else:
            print("Salah")

main()