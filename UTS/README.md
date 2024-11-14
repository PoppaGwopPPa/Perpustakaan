Sistem Manajemen Perpustakaan
Proyek ini adalah sistem manajemen perpustakaan sederhana yang dibuat menggunakan Python, dengan fitur untuk melihat, meminjam, menambah, dan menghapus buku. Terdapat dua jenis pengguna: Pengguna dan Admin. Pengguna dapat melihat daftar buku dan meminjam buku, sedangkan Admin dapat menambah dan menghapus buku.

Struktur Kelas
Buku: Kelas yang menyimpan detail setiap buku di perpustakaan.
Perpustakaan: Kelas yang berfungsi sebagai tempat menyimpan daftar buku dan mengelola peminjaman.
Pengguna: Kelas yang memiliki hak untuk melihat daftar buku dan meminjam buku.
Admin: Subkelas dari Pengguna yang memiliki hak tambahan untuk menambah dan menghapus buku dari perpustakaan.
Fitur
Melihat Daftar Buku: Semua pengguna dapat melihat daftar buku yang tersedia, termasuk informasi ID, judul, status ketersediaan, dan letak buku.
Meminjam Buku: Pengguna dapat meminjam buku dengan memasukkan ID buku yang ingin dipinjam.
Mengembalikan Buku: Kembali otomatis saat status peminjaman berubah.
Menambah Buku: Admin dapat menambahkan buku baru ke perpustakaan.
Menghapus Buku: Admin dapat menghapus buku dari perpustakaan berdasarkan ID buku.
Cara Menggunakan
Clone atau unduh proyek ini ke komputer Anda.

Buka terminal atau command prompt dan navigasikan ke folder proyek.

Jalankan program dengan perintah:

bash
Salin kode
python nama_file.py
Program ini akan:

Menampilkan daftar buku di perpustakaan.
Meminta input dari pengguna untuk meminjam buku.
Menampilkan hasil peminjaman, penambahan buku oleh Admin, dan daftar buku yang diperbarui setelah perubahan.
