def main():
    print("PROGRAM PEMBAGIAN BILANGAN")
    try:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        hasil = a / b
    except(ZeroDivisionError, ValueError, KeyboardInterrupt):
        print("\nERROR: anda telah melakukan kesalahan pada input")
    
    else:
        print("nilai a: ", a)
        print("nilai b: ", b)
        print("hasil dari a/b adalah ", hasil)

if __name__ == "__main__":
    main()