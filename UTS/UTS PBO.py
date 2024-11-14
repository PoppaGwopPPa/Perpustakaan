# Class Buku yang menyimpan detail setiap buku
class Buku:
    def __init__(self, id_buku, judul, tersedia, letak):
        self.id = id_buku
        self.judul = judul
        self.tersedia = tersedia
        self.letak = letak

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True
        return f"Buku '{self.judul}' telah dikembalikan."


# Class Perpustakaan untuk menyimpan daftar buku
class Perpustakaan:
    def __init__(self):
        self.books = []

    def lihat_buku(self):
        output = []
        for book in self.books:
            status = 'Ya' if book.tersedia else 'Tidak'
            output.append(f"ID: {book.id}, Judul: {book.judul}, Tersedia: {status}, Letak: {book.letak}")
        return "\n".join(output)

    def pinjam_buku(self, id_buku):
        book = self.cari_buku(id_buku)
        if book and book.pinjam():
            return f"Buku '{book.judul}' berhasil dipinjam."
        elif book:
            return "Buku tersebut sedang dipinjam."
        else:
            return "Buku tidak tersedia atau tidak ditemukan."

    def cari_buku(self, id_buku):
        for book in self.books:
            if book.id == id_buku:
                return book
        return None


# Class Pengguna dengan hak untuk melihat dan meminjam buku
class Pengguna:
    def __init__(self, nama, id_pengguna):
        self.nama = nama
        self.id_pengguna = id_pengguna

    def lihat_buku(self, perpustakaan):
        return perpustakaan.lihat_buku()

    def pinjam_buku(self, perpustakaan):
        try:
            id_buku = int(input("Masukkan ID Buku yang ingin dipinjam: "))
            return perpustakaan.pinjam_buku(id_buku)
        except ValueError:
            return "Input ID Buku harus berupa angka."


# Class Admin yang memiliki hak untuk menambah dan menghapus buku
class Admin(Pengguna):
    def __init__(self, nama, id_pengguna):
        super().__init__(nama, id_pengguna)

    def tambah_buku(self, perpustakaan, buku):
        perpustakaan.books.append(buku)
        return f"Buku '{buku.judul}' berhasil ditambahkan oleh Admin."

    def hapus_buku(self, perpustakaan, id_buku):
        buku_dihapus = [book for book in perpustakaan.books if book.id == id_buku]
        perpustakaan.books = [book for book in perpustakaan.books if book.id != id_buku]
        if buku_dihapus:
            return f"Buku dengan ID {id_buku} berhasil dihapus oleh Admin."
        else:
            return "Buku tidak ditemukan."


# Contoh penggunaan
if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    perpustakaan.books.append(Buku(1, 'Buku Pemrograman Berorientasi Objek', True, 'Rak 1C'))
    perpustakaan.books.append(Buku(2, 'Buku Pemrograman Framework', True, 'Rak 2A'))
    perpustakaan.books.append(Buku(3, 'Buku Deep Learning', True, 'Rak 3A'))
    perpustakaan.books.append(Buku(4, 'Buku Kecerdasan Buatan', True, 'Rak 2B'))

    # Objek
    user = Pengguna('Nabila', 1)
    admin = Admin('Admin', 2)

    # Pengguna melihat buku
    print("Pengguna Melihat Buku:")
    print(user.lihat_buku(perpustakaan))

    # Pengguna memilih untuk meminjam buku
    print("\n" + user.pinjam_buku(perpustakaan))

    # Admin menambah buku
    print("\n" + admin.tambah_buku(perpustakaan, Buku(5, 'Buku Manajemen Jaringan', True, 'Rak 1A')))

    # Buku Ter-Update - Menambah buku
    print("\nBuku Ter-Update (Admin):")
    print(admin.lihat_buku(perpustakaan))

    # Admin menghapus buku
    print("\n" + admin.hapus_buku(perpustakaan, 1))

    # Buku Ter-Update - Menghapus buku
    print("\nBuku Ter-Update (Admin):")
    print(admin.lihat_buku(perpustakaan))

    # Pengguna mencoba meminjam buku lagi
    print("\nPengguna Meminjam Buku Lagi:")
    print(user.pinjam_buku(perpustakaan))
