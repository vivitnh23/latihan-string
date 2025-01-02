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