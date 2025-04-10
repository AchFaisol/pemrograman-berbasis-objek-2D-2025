class kucing:
    def __init__(self,jenis,nama,ras):
        self.jenis = jenis
        self.nama = nama
        self.ras = ras
    def makan(self):
        print(f"{self.jenis} sedang makan")
    def info(self):
        print(f"{self.jenis} dengan nama {self.nama} dan dari ras {self.ras}")

class Anjing:
    def __init__(self,jenis,nama,ras):
        self.jenis = jenis
        self.nama = nama
        self.ras = ras
    def tidur(self):
        print(f"{self.jenis} sedang tidur")
    def info(self):
        print(f"{self.jenis} dengan nama {self.nama} dan dari ras {self.ras}")

class kuda:
    def __init__(self,jenis,nama,ras):
        self.jenis = jenis
        self.nama = nama
        self.ras = ras
    def berlari(self):
        print(f"{self.jenis} sedang berlari")
    def info(self):
        print(f"{self.jenis} dengan nama {self.nama} dan dari ras {self.ras}")

kucing_list = [
    kucing("Kucing", "budi", "Persia"),
    kucing("Kucing", "anto", "Maine Coon"),
    kucing("Kucing", "yanto", "Ragdoll")
]
anjing_list = [
    Anjing("Anjing", "rocky", "Bulldog"),
    Anjing("Anjing","yocky","Bulldog"),
    Anjing("Anjing","yonko","Poodle")
]
kuda_list = [
    kuda("Kuda", "kudus", "Arabian"),
    kuda("kuda","phoenix","Thoroughbred"),
    kuda("kuda","titan","Percheron")
]
for kucing in kucing_list:
    kucing.info()
    kucing.makan()
    print("-----------------------------------------------------")
for anjing in anjing_list:
    anjing.info()
    anjing.tidur()
    print("-----------------------------------------------------")
for kuda in kuda_list:
    kuda.info()
    kuda.berlari()
    print("-----------------------------------------------------")


