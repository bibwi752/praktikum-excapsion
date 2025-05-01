#print(var)
#print(1/0)

#try:
#    dict = {'a' : 1, 'b': 2}
 #   print(dict['c'])
#except KeyError:
 #   print("Kunci yang anda coba akses tidak ada dalam dictionary")



 #try:
  #  jumlah = 5 + "10"
#except TypeError:
 #   print("Terjadi TypeError, pastikan Anda menjumlahkan dua angka.")


#try:
 #  hasil = 10 / 0
#except ZeroDivisionError:
  # print("Anda mencoba membagi dengan nol. Ini tidak dapat dilakukan.")




#try:
 #   file = open('file_tidak_ada.txt')
#except FileNotFoundError:
 #  print("File tidak ditemukan. Pastikan Anda memasukkan path yang benar.")





 # mengimpor modul sys untuk exit()
#import sys
#
#def main():
 #   # membuat judul program
  #  print("PROGRAM PEMBAGIAN BILANGAN")

    # meminta user memasukkan bilangan
   # a = float(input("Masukkan a: "))
    #b = float(input("Masukkan b: "))

    # mendefinisikan blok try ... except
    #try:
     #   hasil = a / b
    #except ZeroDivisionError:
     #   print("ERROR: Nilai b tidak boleh nol")
      #  sys.exit(1)  # menghentikan exit

    # menampilkan hasil
    #print("\na : ", a)
    #print("b : ", b)
    #print("a / b = ", hasil)

#if __name__ == "__main__":
 #   main()




def main():
 #   membuat judul program
    print("PROGRAM PEMBAGIAN BILANGAN")

    # meminta user memasukkan bilangan
    a = float(input("Masukkan a: "))
    b = float(input("Masukkan b: "))

    # mendefinisikan blok try ... except
   try:
     hasil = a / b
    except ZeroDivisionError:
        print("nERROR: Nilai b tidak boleh nol")

     menampilkan hasil
    print("\na =", a)
    print("b =", b)
    print("a / b =", hasil)

    # kode dibawah ini akan menimbulkan kesalahan dengan tipe NameError

if __name__ == "__main__":
    main()

  







#def main():
 #   # membuat judul program
  #  print("PROGRAM PEMBAGIAN BILANGAN")
#
 #   # meminta user memasukkan bilangan
  #  a = float(input("Masukkan a: "))
   # b = float(input("Masukkan b: "))
#
  # mendefinisikan blok try ... except
  #  try:
    #    hasil = a / b
    e#xcept ZeroDivisionError:
      #  print("ERROR: Nilai b tidak boleh nol")
   # else:
    #    print('a =', a)
     #   print('b =', b)
      #  print('a / b =', hasil)

#if __name__ == "__main__":
 #   main()