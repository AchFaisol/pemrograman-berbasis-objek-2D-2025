class Karyawan:
    def __init__(self,nama,gaji,departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class Tetap(Karyawan):
    def __init__(self, nama, gaji, departemen,tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: Rp.{self.gaji}")
        print(f"Departemen: {self.departemen}")
        print(f"Tunjangan: Rp.{self.tunjangan}")

class Harian(Karyawan):
    def __init__(self, nama, gaji, departemen,jam):
        super().__init__(nama, gaji, departemen)
        self.jam = jam
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: Rp.{self.gaji}")
        print(f"Departemen: {self.departemen}")
        print(f"Jam kerja: {self.jam}")

class Manajemen:
    def __init__(self):
        self.karyawan_list = []

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

    def info_semua_karyawan(self):
        for karyawan in self.karyawan_list:
            karyawan.info()
            print("---------------------------")

manajemen = Manajemen()

while True:
    print("\n== Pilih Karyawan ==")
    print("1. Karyawan Tetap")
    print("2. Karyawan Harian")
    pilih = input("Pilih tipe karyawan (1/2): ")

    if pilih == "1":
        nama = input("Nama: ")
        while True:
            gaji = input("Gaji: ")
            if gaji.isdigit():
                gaji = float(gaji)
                break
            else:
                print("masukkan angka")
        departemen = input("Departemen: ")
        while True:
            tunjangan = input("Tunjangan: ")
            if tunjangan.isdigit():
                tunjangan = float(tunjangan)
                break
            else:
                print("masukkan angka")
        karyawan = Tetap(nama, gaji, departemen, tunjangan)
        manajemen.tambah_karyawan(karyawan)

    elif pilih == "2":
        nama = input("Nama: ")
        while True:
            gaji = input("Gaji: ")
            if gaji.isdigit():
                gaji = float(gaji)
                break
            else:
                print("masukkan angka")
        departemen = input("Departemen: ")
        while True:
            jam = input("Jam: ")
            if jam.isdigit():
                jam = float(jam)
                break
            else:
                print("masukkan angka")
        karyawan = Harian(nama, gaji, departemen, jam)
        manajemen.tambah_karyawan(karyawan)

    else:
        print("Masukkan sesuai pilihan!")
    while True:
        lanjut = input("Tambah karyawan lagi? (ya/tidak): ")
        if lanjut.lower() == "ya":
            break
        elif lanjut.lower() == "tidak":
            print("\n== Daftar Semua Karyawan ==")
            manajemen.info_semua_karyawan()
            exit()
        else:
            print("jawaban tidak valid")
