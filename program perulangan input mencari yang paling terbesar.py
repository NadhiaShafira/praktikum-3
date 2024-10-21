# Meminta input jumlah N bilangan
N = int(input("Masukkan jumlah bilangan: "))

# Inisialisasi variabel max dengan 0
max_num = 0

# Loop untuk meminta input N bilangan
for i in range(1, N+1):
    num = int(input(f"Masukkan bilangan ke-{i}: "))
    
    # Memeriksa apakah bilangan ini lebih besar dari max_num
    if num > max_num:
        max_num = num

# Menampilkan bilangan terbesar
print("Bilangan terbesar adalah:", max_num)
