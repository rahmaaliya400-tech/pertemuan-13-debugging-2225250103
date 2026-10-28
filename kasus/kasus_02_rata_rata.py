
nama_file = "kasus/nilai.txt"

try:
    with open(nama_file, "r") as file:
        isi = file.read().strip()

    if isi == "":
        print("File kosong")
    else:
        nilai = [int(x) for x in isi.split()]
        print("Data nilai:", nilai)

except FileNotFoundError:
    print("File tidak ditemukan")
except ValueError:
    print("Data nilai tidak valid")
