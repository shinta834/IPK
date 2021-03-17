class students (object):
    def __init__(self):
        self.nim = 0
        self.nama = ''
        self.alamat = ''
        self.asalSekolah = ''
        self.kodeProdi =''
        self.ipkAwal = 0
        self.uts = 0
        self.uas = 0
        self.tm = 0
        self.ips = 0
        self.ipkAkhir = 0
        self.beasiswa = ''
    def enterData (self):
        self.nim = int (input('Nim: '))
        self.nama = input('Nama: ')
        self.alamat = input('Alamat: ')
        self.asalSekolah = input('Asal Sekolah: ')
        self.kodeProdi = input('Kode Prodi: ')
        self.ipkAwal = float(input('IPK Awal: '))
        self.uts = float(input('Nilai UTS: '))
        self.uas = float(input('Nilai UAS: '))
        self.tm = float(input('Nilai TM: '))    
        self.ips = (0.3*self.uts)+(0.3*self.tm)+(0.4*self.uas)
        self.ipkAkhir = (self.ipkAwal + self.ips)/2
        if self.kodeProdi == 'TI' or self.kodeProdi == 'SI':
            if self.ipkAkhir >= 75 and self.ipkAkhir < 85:
                self.beasiswa = '20%'
            else:
                self.beasiswa = '30%'
        else:
            if self.ipkAkhir >= 75 and self.ipkAkhir < 85:
                self.beasiswa = '25%'
            else:
                self.beasiswa = '35%' 
    def printData(self):
        print('-----------------------')
        print('Nim: ', self.nim)
        print('Nama: ',self.nama)
        print('Alamat: ',self.alamat)
        print('Asal Sekolah: ',self.asalSekolah)
        print('Kode Prodi: ',self.kodeProdi)
        print('IPK Awal: ',self.ipkAwal)
        print('Nilai UTS: ',self.uts)
        print('Nilai UAS: ',self.uas)
        print('Nilai TM: ',self.tm)
        print('Nilai IPS: ',self.ips)
        print('IPK Akhir: ',self.ipkAkhir)
        print('Beasiswa: ',self.beasiswa)
        print('-----------------------')


list1 = []
x = int(input('Masukkan jumlah murid: '))
for i in range (x):
    a = students()
    a.enterData()
    list1.append(a)

for i in range (x):
    list1[i].printData()