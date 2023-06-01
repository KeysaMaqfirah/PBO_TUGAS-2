print("============= TUGAS_2 PBO =============")
print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>")

# Membuat Kelas Mahasiswa.
class Mahasiswa:

# Konstruktor __init__ berfungsi untuk menginisialisasi 
# objek mahasiswa dengan atribut seperti Nama dan NIM.
    def __init__(self, Nama, NIM):
        self.Nama = Nama
        self.NIM = NIM

# Tampilkan_Info digunakan untuk mencetak informasi Nama dan NIM mahasiswa.
    def Tampilkan_Info(self):
        print("Nama:", self.Nama)
        print("NIM:", self.NIM)

"""
Kode program implementasi kelas Mahasiswa padaKode class Mahasiswa: menunjukkan bahwa kita sedang membuat sebuah kelas dengan nama "Mahasiswa".
Metode konstruktor def _init_(self, Nama, NIM, Jurusan): adalah metode khusus yang akan dieksekusi 
secara otomatis saat objek mahasiswa dibuat. Metode ini menerima empat parameter: self, Nama, NIM, dan Jurusan. 
Parameter self merujuk pada objek yang sedang dibuat, sedangkan Nama, NIM, dan Jurusan adalah atribut-atribut 
yang akan diinisialisasi dengan nilai yang diberikan saat pembuatan objek.
Pada baris berikutnya, self.Nama = Nama, self.NIM = NIM, dan self.Jurusan = Jurusan digunakan 
untuk menginisialisasi atribut-atribut Nama, NIM, dan Jurusan pada objek yang sedang dibuat 
dengan nilai yang diberikan saat pembuatan objek.
Metode Tampilkan_Info(self): digunakan untuk mencetak informasi Nama, NIM, dan Jurusan Mahasiswa. 
Pada bagian print, self.Nama akan mencetak nilai atribut nama pada objek yang memanggil metode ini,
self.NIM akan mencetak nilai atribut nim, dan self.jurusan.NamaJurusan akan mencetak nilai atribut NamaJurusan 
dari objek jurusan yang merupakan atribut dari objek Mahasiswa.
"""


# Membuat Kelas Jurusan.
class Jurusan:

# Konstruktor __init__ berfungsi untuk menginisialisasi objek jurusan dengan atribut nama_jurusan.
# Daftar_Mahasiswa merupakan list untuk menyimpan objek mahasiswa yang terdaftar dalam jurusan.
    def __init__(self, Nama_Jurusan):
        self.Nama_Jurusan = Nama_Jurusan
        self.Daftar_Mahasiswa = []

# Tambah_Mahasiswa berfungsi untuk menambahkan objek mahasiswa ke dalam daftar mahasiswa pada jurusan.
    def Tambah_Mahasiswa(self, Mahasiswa):
        self.Daftar_Mahasiswa.append(Mahasiswa)

# Tampilkan_Daftar_Mahasiswa digunakan untuk mencetak daftar mahasiswa yang terdaftar dalam jurusan, 
# Termasuk Nama dan NIM masing-masing mahasiswa.
    def Tampilkan_Daftar_Mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.Nama_Jurusan)
        for Mahasiswa in self.Daftar_Mahasiswa:
            print("~ Nama :", Mahasiswa.Nama)
            print("  NIM  :", Mahasiswa.NIM)


"""
Kode program di atas adalah implementasi kelas Jurusan pada Kode class Jurusan: menunjukkan bahwa kita sedang membuat sebuah 
kelas dengan nama "Jurusan".Konstruktor def __init__(self, Nama_Jurusan): adalah metode khusus yang akan dieksekusi 
secara otomatis saat objek jurusan dibuat. Metode ini menerima dua parameter: self dan Nama_Jurusan.
Parameter self merujuk pada objek yang sedang dibuat, sedangkan Nama_Jurusan adalah atribut yang akan diinisialisasi
dengan nilai yang diberikan saat pembuatan objek.
Pada baris berikutnya, self.Nama_Jurusan = Nama_Jurusan digunakan untuk menginisialisasi atribut Nama_Jurusan 
pada objek yang sedang dibuat dengan nilai yang diberikan saat pembuatan objek.
Atribut Daftar_Mahasiswa adalah sebuah list yang digunakan untuk menyimpan objek mahasiswa yang terdaftar dalam jurusan. 
Atribut ini diinisialisasi sebagai list kosong pada konstruktor dengan self.Daftar_Mahasiswa = [].
Metode Tambah_Mahasiswa(self, Mahasiswa): digunakan untuk menambahkan objek mahasiswa ke dalam daftar mahasiswa pada jurusan.
Metode ini menerima dua parameter: self dan Mahasiswa. Parameter self merujuk pada objek yang memanggil metode ini, 
sedangkan Mahasiswa adalah objek mahasiswa yang akan ditambahkan ke daftar mahasiswa.
Metode Tampilkan_Daftar_Mahasiswa(self): digunakan untuk mencetak daftar mahasiswa yang terdaftar dalam jurusan. 
Metode ini akan mencetak informasi nama dan NIM dari setiap mahasiswa yang ada dalam daftar mahasiswa menggunakan 
pernyataan print dan perulangan for.

"""


# Membuat Kelas Universitas. 
class Universitas:

# Konstruktor __init__ digunakan untuk menginisialisasi objek universitas dengan atribut Nama_Universitas
# Atribut daftar_jurusan merupakan list untuk menyimpan objek jurusan yang terdapat dalam Universitas
    def __init__(self, Nama_Universitas):
        self.Nama_Universitas = Nama_Universitas
        self.Daftar_Jurusan = []

# Tambah_Jurusan berfungsi untuk menambahkan objek jurusan ke dalam daftar jurusan pada Universitas
    def Tambah_Jurusan(self, Jurusan):
        self.Daftar_Jurusan.append(Jurusan)

# Tampilkan_Daftar_Jurusan berfungsi untuk mencetak daftar jurusan yang
# terdapat dalam Universitas, termasuk Nama jurusannya
    def Tampilkan_Daftar_Jurusan(self):
        print("Daftar Jurusan di Universitas", self.Nama_Universitas)
        for Jurusan in self.Daftar_Jurusan:
            print("~ Nama Jurusan :", Jurusan.Nama_Jurusan)

"""
Kode program di atas adalah implementasi kelas Universitas pada Kode class Universitas: menunjukkan bahwa kita sedang membuat 
sebuah kelas dengan nama "Universitas".Konstruktor def __init__(self, Nama_Universitas): adalah metode khusus yang 
akan dieksekusi secara otomatis saat objek universitas dibuat.Metode ini menerima dua parameter: self dan Nama_Universitas. 
Parameter self merujuk pada objek yang sedang dibuat, sedangkan Nama_Universitas adalah atribut yang akan 
diinisialisasi dengan nilai yang diberikan saat pembuatan objek.Pada baris berikutnya, self.Nama_Universitas = Nama_Universitas digunakan 
untuk menginisialisasi atribut Nama_Universitas pada objek yang sedang dibuat dengan nilai yang diberikan saat pembuatan objek.
Atribut Daftar_Jurusan adalah sebuah list yang digunakan untuk menyimpan objek jurusan yang terdapat dalam universitas. 
Atribut ini diinisialisasi sebagai list kosong pada konstruktor dengan self.Daftar_Jurusan = [].
Metode Tambah_Jurusan(self, Jurusan): digunakan untuk menambahkan objek jurusan ke dalam daftar jurusan pada universitas.
Metode ini menerima dua parameter: self dan Jurusan. Parameter self merujuk pada objek yang memanggil metode ini, 
sedangkan Jurusan adalah objek jurusan yang akan ditambahkan ke daftar jurusan.
Metode Tampilkan_Daftar_Jurusan(self): digunakan untuk mencetak daftar jurusan yang terdapat dalam universitas.
Metode ini akan mencetak informasi nama jurusan dari setiap jurusan yang ada dalam daftar jurusan menggunakan pernyataan print dan perulangan for.

"""


# Membuat objek Universitas dengan nama "XYZ University"
Universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan "Teknik Informatika" dan daftar mahasiswa
Jurusan_Teknik_Informatika = Jurusan("Teknik Informatika")
Mahasiswa_1 = Mahasiswa("Keysa Maqfirah", "G1A022012")
Jurusan_Teknik_Informatika.Tambah_Mahasiswa(Mahasiswa_1)

# Membuat objek Jurusan "Hukum" dan daftar mahasiswa
Jurusan_Hukum = Jurusan("Hukum")
Mahasiswa_3 = Mahasiswa("Suci Rusmiarni", "B1A002013")
Mahasiswa_4 = Mahasiswa("Nurlaila", "B1A021020")
Mahasiswa_5 = Mahasiswa("Sofia Anata", "B1A022078")
Jurusan_Hukum.Tambah_Mahasiswa(Mahasiswa_3)
Jurusan_Hukum.Tambah_Mahasiswa(Mahasiswa_4)
Jurusan_Hukum.Tambah_Mahasiswa(Mahasiswa_5)

"""
Kode program di atas merupakan  kelas-kelas yang telah didefinisikan sebelumnya (Universitas, Jurusan, dan Mahasiswa) 
untuk membuat objek-objek dan mengisi data ke dalamnya. pada baris pertama, Universitas_xyz = Universitas("XYZ University") 
membuat objek universitas baru dengan nama "XYZ University" menggunakan kelas Universitas yang telah didefinisikan sebelumnya. 
Objek ini disimpan dalam variabel Universitas_xyz.Pada baris selanjutnya, Jurusan_Teknik_Informatika = Jurusan("Teknik Informatika") 
membuat objek jurusan barudengan nama "Teknik Informatika" menggunakan kelas Jurusan. Objek ini disimpan dalam variabel Jurusan_Teknik_Informatika.
Kemudian, Mahasiswa_1 = Mahasiswa("Keysa Maqfirah", "G1A022012") membuat objek mahasiswa baru dengan nama "Keysa Maqfirah" 
dan NIM "G1A022012" menggunakan kelas Mahasiswa. Objek ini disimpan dalam variabel Mahasiswa_1.

selanjutnya, Jurusan_Teknik_Informatika.Tambah_Mahasiswa(Mahasiswa_1) memanggil metode Tambah_Mahasiswa() 
pada objek Jurusan_Teknik_Informatika untuk menambahkan objek Mahasiswa_1 ke dalam daftar mahasiswa pada jurusan tersebut.
Pada baris berikutnya, Jurusan_Hukum = Jurusan("Hukum") membuat objek jurusan baru dengan nama "Hukum" menggunakan kelas Jurusan. 
Objek ini disimpan dalam variabel Jurusan_Hukum.Kemudian, Mahasiswa_3 = Mahasiswa("Suci Rusmiarni", "B1A002013"), 
Mahasiswa_4 = Mahasiswa("Nurlaila", "B1A021020"), dan Mahasiswa_5 = Mahasiswa("Sofia Anata", "B1A022078") 
masing-masing membuat objek mahasiswa baru dengan nama dan NIM 
yang sesuai menggunakan kelas Mahasiswa. Objek-objek ini disimpan dalam variabel Mahasiswa_3, Mahasiswa_4, dan Mahasiswa_5.

Selanjutnya, Jurusan_Hukum.Tambah_Mahasiswa(Mahasiswa_3), Jurusan_Hukum.Tambah_Mahasiswa(Mahasiswa_4), 
dan Jurusan_Hukum.Tambah_Mahasiswa(Mahasiswa_5) memanggil metode Tambah_Mahasiswa() pada objek Jurusan_Hukum untuk 
menambahkan objek mahasiswa yang sesuai ke dalam daftar mahasiswa pada jurusan tersebut.

"""


# Membuat objek Jurusan "Manajemen" dan daftar mahasiswa
Jurusan_Manajemen = Jurusan("Manajemen")
Mahasiswa_5 = Mahasiswa("Bintang Gustiady", "C1B022130")
Mahasiswa_6 = Mahasiswa("Delma Triani", "C1B022130")
Jurusan_Manajemen.Tambah_Mahasiswa(Mahasiswa_5)
Jurusan_Manajemen.Tambah_Mahasiswa(Mahasiswa_6)

# Membuat objek Jurusan "Kedokteran" dan daftar mahasiswa
Jurusan_Kedokteran = Jurusan("Kedokteran")
Mahasiswa_5 = Mahasiswa("Andini Junisca","H1A022004")
Mahasiswa_6 = Mahasiswa("Firbari Afza","H1A022053")
Mahasiswa_7 = Mahasiswa("Dea Rizki Ananda","H1A022058")
Jurusan_Kedokteran.Tambah_Mahasiswa(Mahasiswa_5)
Jurusan_Kedokteran.Tambah_Mahasiswa(Mahasiswa_6)
Jurusan_Kedokteran.Tambah_Mahasiswa(Mahasiswa_7)


# Menambahkan jurusan ke dalam Universitas
Universitas_xyz.Tambah_Jurusan(Jurusan_Teknik_Informatika)
Universitas_xyz.Tambah_Jurusan(Jurusan_Hukum)
Universitas_xyz.Tambah_Jurusan(Jurusan_Manajemen)
Universitas_xyz.Tambah_Jurusan(Jurusan_Kedokteran)


"""
Kode program di atas melanjutkan  kelas-kelas yang telah didefinisikan sebelumnya (Jurusan dan Mahasiswa) untuk membuat
objek-objek dan mengisi data ke dalamnya. Jurusan_Manajemen = Jurusan("Manajemen") membuat objek jurusan baru dengan nama 
"Manajemen" menggunakan kelas Jurusan. Objek ini disimpan dalam variabel Jurusan_Manajemen.Mahasiswa_5 = Mahasiswa("Bintang Gustiady", "C1B022130")
dan Mahasiswa_6 = Mahasiswa("Delma Triani", "C1B022130") masing-masing membuat objek mahasiswa baru dengan nama dan NIM yang sesuai 
menggunakan kelas Mahasiswa. Objek-objek ini disimpan dalam variabel Mahasiswa_5 dan Mahasiswa_6.
Jurusan_Manajemen.Tambah_Mahasiswa(Mahasiswa_5) dan Jurusan_Manajemen.Tambah_Mahasiswa(Mahasiswa_6) memanggil
metode Tambah_Mahasiswa() pada objek Jurusan_Manajemen untuk menambahkan objek mahasiswa yang sesuai ke dalam daftar 
mahasiswa pada jurusan tersebut. 

selanjutnya, Jurusan_Kedokteran = Jurusan("Kedokteran") membuat objek jurusan baru dengan nama "Kedokteran" 
menggunakan kelas Jurusan. Objek ini disimpan dalam variabel Jurusan_Kedokteran.Kemudian, Mahasiswa_5 = Mahasiswa("Andini Junisca","H1A022004"), Mahasiswa_6 = Mahasiswa("Firbari Afza","H1A022053"), 
dan Mahasiswa_7 = Mahasiswa("Dea Rizki Ananda","H1A022058") masing-masing membuat objek mahasiswa baru dengan nama dan
NIM yang sesuai menggunakan kelas Mahasiswa. Objek-objek ini disimpan dalam variabel Mahasiswa_5, Mahasiswa_6, dan Mahasiswa_7.

Selanjutnya, Jurusan_Kedokteran.Tambah_Mahasiswa(Mahasiswa_5), Jurusan_Kedokteran.Tambah_Mahasiswa(Mahasiswa_6), 
dan Jurusan_Kedokteran.Tambah_Mahasiswa(Mahasiswa_7) memanggil metode Tambah_Mahasiswa() pada objek Jurusan_Kedokteran 
untuk menambahkan objek mahasiswa yang sesuai ke dalam daftar mahasiswa pada jurusan tersebut.
Pada bagian terakhir, Universitas_xyz.Tambah_Jurusan(Jurusan_Teknik_Informatika), Universitas_xyz.Tambah_Jurusan(Jurusan_Hukum), 
Universitas_xyz.Tambah_Jurusan(Jurusan_Manajemen), dan Universitas_xyz.Tambah_Jurusan(Jurusan_Kedokteran) memanggil metode 
Tambah_Jurusan() pada objek Universitas_xyz untuk menambahkan objek jurusan yang sesuai ke dalam daftar jurusan pada universitas tersebut.

"""


# Menampilkan daftar jurusan di Universitas
Universitas_xyz.Tampilkan_Daftar_Jurusan()
print("===============================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Informatika"
Jurusan_Teknik_Informatika.Tampilkan_Daftar_Mahasiswa()
print("===============================================")

# Menampilkan daftar mahasiswa di Jurusan "Hukum"
Jurusan_Hukum.Tampilkan_Daftar_Mahasiswa()
print("===============================================")

# Menampilkan daftar mahasiswa di Jurusan "Manajemen"
Jurusan_Manajemen.Tampilkan_Daftar_Mahasiswa()
print("===============================================")

# Menampilkan daftar mahasiswa di Jurusan "Kedokteran"
Jurusan_Kedokteran.Tampilkan_Daftar_Mahasiswa()
print("===============================================")

# Penjelasan kode di atas #
# ======================= #

#Kode tersebut menunjukkan penggunaan beberapa fungsi dan objek terkait dengan jurusan di sebuah universitas (Universitas_xyz). 
#Universitas_xyz.Tampilkan_Daftar_Jurusan(): Memanggil metode Tampilkan_Daftar_Jurusan() dari objek Universitas_xyz. 
#Fungsi ini akan menampilkan daftar jurusan yang tersedia di Universitas_xyz.
 
#Jurusan_Teknik_Informatika.Tampilkan_Daftar_Mahasiswa(): Memanggil metode Tampilkan_Daftar_Mahasiswa() dari objek Jurusan_Teknik_Informatika.
#Fungsi ini akan menampilkan daftar mahasiswa yang terdaftar di jurusan "Teknik Informatika". 

#Jurusan_Hukum.Tampilkan_Daftar_Mahasiswa(): Memanggil metode Tampilkan_Daftar_Mahasiswa() dari objek Jurusan_Hukum.
#Fungsi ini akan menampilkan daftar mahasiswa yang terdaftar di jurusan "Hukum".

#Jurusan_Manajemen.Tampilkan_Daftar_Mahasiswa(): Memanggil metode Tampilkan_Daftar_Mahasiswa() dari objek Jurusan_Manajemen. 
#Fungsi ini akan menampilkan daftar mahasiswa yang terdaftar di jurusan "Manajemen". 

#Jurusan_Kedokteran.Tampilkan_Daftar_Mahasiswa(): Memanggil metode Tampilkan_Daftar_Mahasiswa() dari objek Jurusan_Kedokteran.
#Fungsi ini akan menampilkan daftar mahasiswa yang terdaftar di jurusan "Kedokteran". 


