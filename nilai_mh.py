banyak = int(input("Banyak siswa (5-10): "))

if banyak < 5:
    print("Terlalu sedikit, minimal 5 siswa")
elif banyak > 10:
    print("Terlalu banyak, maksimal 10 siswa")
else:
    jumlah_nilai = 0
    for no in range(1, banyak + 1):
        print("Input nilai siswa", no)
        n = int(input("Nilai: "))
        jumlah_nilai += n
    print("Total nilai:", jumlah_nilai)
    print("Rata-rata nilai:", jumlah_nilai / banyak)