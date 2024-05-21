from tabulate import tabulate 
import numpy as np  

print("+30", 'Welcome', '+30')

def f(x, p, q, r, s):
    return p*x**3 + q*x**2 + r*x + s

def regula_falsi(p, q, r, s, a, b, tol=1e-6, max_iter=100):
 
    if f(a, p, q, r, s) * f(b, p, q, r, s) >= 0:
        print("\n+----------------------------+")
        print("!!!Nilai fungsi pada kedua ujung interval memiliki tanda yang sama,\n!!!silahkan input ulang Nilai A dan B.!!!\n")
        print("+----------------------------+\n")
        print("Masih tidak mungkin menemukan akar dalam interval yang diberikan.")
        return None, []

    iterasi_data = []  

    for iterasi in range(max_iter):
        c = b - (f(b, p, q, r, s) * (b - a)) / (f(b, p, q, r, s) - f(a, p, q, r, s))
        fc = f(c, p, q, r, s)  # menghitung f(c) dengan menggunakan f(x)
        iterasi_data.append([iterasi, a, b, c, fc])  # Menyimpan nilai iterasi saat ini

        if abs(fc) < tol:
            # kondisi konvergensi untuk menghentikan iterasi.
            print(f"\nKonvergensi diperoleh setelah {iterasi} iterasi.\n")
            return (c, iterasi_data)  # Mengembalikan nilai akhir dari aproksimasi akar

        elif f(a, p, q, r, s) * fc < 0:
            b = c  # Jika nilai fungsi c sama dengan nol, maka interval berikutnya adalah [a, c]
        else:
            a = c  # Jika nilai fungsi c sama dengan nol, maka interval berikutnya adalah [c, b]

    print("\nTidak menemukan akar dalam iterasi yang diberikan!!!!.\n")
    return None, iterasi_data

# Input koefisien f(x)
p = float(input("Masukkan nilai p: "))
q = float(input("Masukkan nilai q: "))
r = float(input("Masukkan nilai r: "))
s = float(input("Masukkan nilai s: "))

# Input interval A dan B
a = float(input("Masukkan nilai titik a (Interval): "))
b = float(input("Masukkan nilai titik b (Interval): "))

hasil, iterasi_data = regula_falsi(p, q, r, s, a, b) 

if hasil is not None:  
    table_data = [["Iterasi", "a", "b", "c", "f(c)"]]
    for data in iterasi_data:
        table_data.append([data[0], data[1], data[2], data[3], data[4]]) 

    # Menampilkan tabel data iterasi dengan format yang diperlukan untuk tabulate.
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    # Menampilkan hasil akar
    print(f"\nNilai aproksimasi akar: {hasil}\n")
else:
    print("\nTidak menemukan akar dalam iterasi yang diberikan!!!!.\n")
