# Latihan 3
# Studi Kasus 
# Deskripsi Program memvalidasi input data pendaftaran dari pengguna
Program ini adalah sebuah alat sederhana untuk memvalidasi input data pendaftaran dari pengguna. Input yang divalidasi meliputi:
- Nama Lengkap: Harus hanya berisi huruf tanpa angka atau karakter khusus.
- Nomor Telepon: Harus hanya terdiri dari angka tanpa huruf atau simbol.
- Email: Harus mengandung karakter @ dan . untuk memenuhi format dasar email yang valid.

Program memberikan umpan balik langsung kepada pengguna jika ada kesalahan dalam format input, sehingga pengguna dapat memperbaiki 
data yang dimasukkan sebelum melanjutkan.

# Input Program 
```python
def validasi_input(nama, nomor_telepon, email):
    # Validasi nama (hanya huruf)
    if not nama.isalpha():
        return "Nama lengkap harus hanya berisi huruf."

    # Validasi nomor telepon (hanya angka)
    if not nomor_telepon.isdigit():
        return "Nomor telepon harus hanya berisi angka."

    # Validasi email (mengandung karakter @ dan .)
    if "@" not in email or "." not in email:
        return "Email harus mengandung karakter '@' dan '.'."

    # Jika semua validasi lolos
    return "Data pendaftaran valid."


# Contoh penggunaan
nama = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

hasil = validasi_input(nama, nomor_telepon, email)
print(hasil)
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 3/studi kasus.py"
Masukkan nama lengkap: vivit nurul
Masukkan nomor telepon: 08812320511
Masukkan email: vivitnh@gmail.com
Nama lengkap harus hanya berisi huruf.
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>

Masukkan nama lengkap: VIVIT            
Masukkan nomor telepon: 08812320511      
Masukkan email: vivitnh@gmail.com  
Data pendaftaran valid.
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````
# Cara Kerja Program 
1. Meminta Input dari Pengguna:
- Program meminta pengguna untuk memasukkan nama lengkap, nomor telepon, dan email melalui input keyboard.
Melakukan Validasi:

    - Nama Lengkap: Diperiksa apakah hanya berisi huruf menggunakan metode .isalpha(). Jika terdapat angka atau karakter selain
      huruf, program akan memberikan pesan kesalahan.
    - Nomor Telepon: Diperiksa apakah hanya terdiri dari angka menggunakan metode .isdigit(). Jika terdapat huruf atau simbol lain,
      program akan memberikan pesan kesalahan.
    - Email: Diperiksa apakah mengandung karakter @ dan . menggunakan operator in. Jika salah satu atau kedua karakter tidak ditemukan,
      program akan memberikan pesan kesalahan.
2. Menampilkan Hasil Validasi:
- Jika semua validasi lolos, program mencetak pesan bahwa data pendaftaran valid.
Jika ada kesalahan, program akan mencetak pesan yang sesuai dengan kesalahan tersebut, misalnya:
    - "Nama lengkap harus hanya berisi huruf."
    - "Nomor telepon harus hanya berisi angka."
    - "Email harus mengandung karakter '@' dan '.'."
    - Selesai:
3. Pengguna dapat memperbaiki input jika terdapat kesalahan dan menjalankan ulang program untuk memeriksa kembali.
