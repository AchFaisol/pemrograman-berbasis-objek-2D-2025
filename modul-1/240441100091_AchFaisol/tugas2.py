class Mahasiswa:
    def __init__(self,nama,nim,prodi,alamat):
        self.nama = nama
        self.nim = nim 
        self.prodi = prodi
        self.alamat = alamat
    def info_mahasiswa(self):
        return f"nama saya {self.nama} dengan NIM {self.nim} dari prodi {self.prodi} dan saya dari {self.alamat}"
mhs1 = Mahasiswa(input("Masukkan nama mahasiswa 1:"),
                 input("masukkan nim mahasiswa 1:"),
                 input("masukkan prodi mahasiswa 1:"),
                 input("masukkan alamat mahasiswa 1:"))
print(mhs1.info_mahasiswa())
mhs2 = Mahasiswa(input("Masukkan nama mahasiswa 2:"),
                 input("masukkan nim mahasiswa 2:"),
                 input("masukkan prodi mahasiswa 2:"),
                 input("masukkan alamat mahasiswa 1:"))
print(mhs2.info_mahasiswa())
mhs3 = Mahasiswa(input("Masukkan nama mahasiswa 3:"),
                 input("masukkan nim mahasiswa 3:"),
                 input("masukkan prodi mahasiswa 3:"),
                 input("masukkan alamat mahasiswa 1:"))
print(mhs3.info_mahasiswa())
