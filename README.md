# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Nadhia Shafira

Kelas : TI.24.A.5

NIM : 312410498

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang diinputkan 
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang di temukan.

## Flowchart Program 
![foto](https://github.com/NadhiaShafira/Flowchart-/blob/0f0f9582875c1568c89e0ddeffebc3b3af5ec342/IMG_20241016_072809_1.jpg)

```python
largest = float('-inf')  # Menginisialisasi Largest dengan -∞

while True:
    print("Enter 0 to stop")
    n = float(input("Input a number: "))  # Meminta input dari pengguna

    if n == 0:
        break  # Keluar dari loop jika input adalah 0

    if n > largest:
        largest = n  # Update nilai Largest jika n lebih besar

if largest == float('-inf'):
    print("No numbers were entered.")
else:
    print("The largest number is:", largest)

```
## penjelasan kode program 

```python
maxBilangan = float('-inf')  # -∞
count = 0
```
N = int(input("Masukkan jumlah bilangan: "))

Bagian ini meminta pengguna untuk memasukkan jumlah bilangan yang akan dimasukkan (dalam bentuk bilangan bulat). Fungsi `input()` mengambil input dari pengguna, lalu `int()` mengubahnya menjadi tipe data integer.

```python
`max_num = 0`

Di sini, variabel `max_num` diinisialisasi dengan nilai 0. Variabel ini akan digunakan untuk menyimpan bilangan terbesar yang ditemukan dalam proses loop.
```
for i in range(1, N+1):
    num = int(input(f"Masukkan bilangan ke-{i}: "))

Bagian ini adalah loop `for` yang berjalan sebanyak `N` kali, mulai dari 1 hingga N. Pada setiap iterasi, pengguna diminta untuk memasukkan bilangan melalui `input()`. Setiap bilangan yang dimasukkan dikonversi menjadi tipe integer dan disimpan dalam variabel `num`.

```python
if num > max_num:
    max_num = num

Pada setiap iterasi, bilangan yang dimasukkan `(num)` akan dibandingkan dengan `max_num`. Jika `num` lebih besar dari `max_num`, maka `max_num` akan diperbarui dengan nilai `num`. Hal ini memastikan bahwa `max_num` selalu menyimpan bilangan terbesar yang ditemukan sejauh ini.
```
 print("Bilangan terbesar adalah:", max_num)

Setelah loop selesai, program akan mencetak nilai dari `max_num`, yaitu bilangan terbesar yang ditemukan dari seluruh input.
## hasil kode program 
![foto](https://github.com/NadhiaShafira/Flowchart-/blob/0f0f9582875c1568c89e0ddeffebc3b3af5ec342/IMG-20241021-WA0011.jpg)
