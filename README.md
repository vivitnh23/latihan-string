# latihan-string
# Vivit nurul hidayah
# 312410110
# TI.24.A1
# Mata Kuliah : Bahasa Pemrograman 
# Dosen Pengampu : Bapak Agung Nugroho, S.Kom.,M.Kom

# Latihan 1 
# Input Program 
```python
txt = 'Hello World'

# Ambil karakter terakhir
print("Karakter terakhir:", txt[-1])
```
# Output Program 
````
 "c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/Ambil karakter terakhir.py"
Karakter terakhir: d
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````
# Input Program 
```python
txt = 'Hello World'

# Ganti karakter H dengan karakter J
print("Ganti H dengan J:", txt.replace("H", "J"))
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/ganti karakter.py"
Ganti H dengan J: Jello World
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````
# Input Program 
```python
txt = 'Hello World'

# Hilangkan spasi pada text tersebut (HelloWorld)
print("Tanpa spasi:", txt.replace(" ", ""))
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/hilang spasi.py"
Tanpa spasi: HelloWorld
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````
# Input Program 
```python
txt = 'Hello World'

# Hilangkan spasi pada text tersebut (HelloWorld)
print("Tanpa spasi:", txt.replace(" ", ""))
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/hilang spasi.py"
Tanpa spasi: HelloWorld
PS C:\Users\hp\Documents\Lab praktikum\Latihan String> 
````
# Input Program 
```python
txt = 'Hello World'

# Ambil karakter index ke-2 sampai index ke-4 (llo)
print("Karakter index 2-4:", txt[2:5])
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/index ke2.py"
Karakter index 2-4: llo
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````
# Input Program 
```python
txt = 'Hello World'

# Hitung jumlah karakternya
print("Jumlah karakter:", len(txt))
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/menghitung karakter.py"
Jumlah karakter: 11
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````
# Input Program 
```python
txt = 'Hello World'

# Ubah text menjadi huruf kecil
print("Huruf kecil:", txt.lower())
```
# Output Program 
````
 "c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/ubah menjadi hrf kecil.py"
Huruf kecil: hello world
PS C:\Users\hp\Documents\Lab praktikum\Latihan String> 
````
# Input Program 
```python
txt = 'Hello World'

# Ubah text menjadi huruf besar
print("Huruf besar:", txt.upper())
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/latihan 1/ubah menjadi huruf besar.py"
Huruf besar: HELLO WORLD
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````

# Latihan 2
# Input Program 
```python
umur = 22
txt = 'Hello, nama saya vivit nurul hidayah, dan umur saya adalah {} tahun'
print(txt.format(umur))
```
# Output Program 
````
"c:/Users/hp/Documents/Lab praktikum/Latihan String/Latihan 2/latihan.py"
Hello, nama saya vivit nurul hidayah, dan umur saya adalah 22 tahun
PS C:\Users\hp\Documents\Lab praktikum\Latihan String>
````

# Latihan 3 (Studi Kasus)
# Input Program 
```python
def validasi_input(nama, nomor_telepon, email):
    #Validasi nama (hanya huruf)
    if not nama.isalpha():
        return "Nama lengkap harus hanya berisi huruf."

    #Validasi nomor telepon (hanya angka)
    if not nomor_telepon.isdigit():
        return "Nomor telepon harus hanya berisi angka."

    #Validasi email (mengandung karakter @ dan .)
    if "@" not in email or "." not in email:
        return "Email harus mengandung karakter '@' dan '.'."

    #Jika semua validasi lolos
    return "Data pendaftaran valid."


#Contoh penggunaan
nama = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

hasil = validasi_input(nama, nomor_telepon, email)
print(hasil)
```
# Output Program 
````
