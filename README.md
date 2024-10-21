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

## hasil kode program 
![foto](https://github.com/NadhiaShafira/Flowchart-/blob/0f0f9582875c1568c89e0ddeffebc3b3af5ec342/IMG-20241021-WA0011.jpg)
