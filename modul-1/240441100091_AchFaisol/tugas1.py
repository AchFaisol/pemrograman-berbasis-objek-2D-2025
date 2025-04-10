class Manusia:
    def __init__(self,nama,umur,alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    def berjalan(self):
        print(f"{self.nama} sedang berjalan")
    def berlari(self):
        print(f"{self.nama} sedang berlari")
mns1 = Manusia("budi",17,"bandung")
mns1.ortu = "bujang"
print(f"nama:{mns1.nama}, umur:{mns1.umur}, alamat:{mns1.alamat}")
mns1.berjalan()
mns2 = Manusia("yanto",18,"surabaya")
print(f"nama:{mns2.nama}, umur:{mns2.umur}, alamat:{mns2.alamat}")
mns2.berlari()
mns3 = Manusia("edi",19,"malang")
print(f"nama:{mns3.nama}, umur:{mns3.umur}, alamat{mns3.alamat}")
mns3.berjalan()
mns4 = Manusia("bintang",17,"malang")
print(f"nama:{mns4.nama}, umur:{mns4.umur}, alamat{mns4.alamat}")
mns4.berjalan()
mns5 = Manusia("bagus",18,"surabaya")
print(f"nama:{mns5.nama}, umur:{mns5.umur}, alamat{mns5.alamat}")
mns5.berlari()
