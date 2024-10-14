# Header
print('___________________________________________')
print('_____SELAMAT DATANG DI INFORSA BILYARD_____')
print('___________________________________________')

import random
meja = random.randint(1, 5)
harga_per_jam = 30000

# Fungsi login untuk user
def login():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == "Riza" and password == "beelcuk":
            print("Login Berhasil")
            return username
        else:
            print("Login Gagal")

# Fungsi login untuk admin
def admin_login():
    while True:
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")
        if username == "Adminbl" and password == "beelcuk":
            print("Login Admin Berhasil")
            return True
        else:
            print("Login Gagal")

# Fungsi untuk menghitung biaya pemesanan
def hitung_biaya(durasi):
    diskon = 5000 if durasi >= 2 else 0
    total_biaya = (durasi * harga_per_jam) - diskon
    if diskon > 0:
        print(f"Anda mendapat diskon Rp{diskon}.")
    return total_biaya

# Fungsi menu admin
def admin_menu():
    global harga_per_jam  # Agar bisa mengubah variabel harga_per_jam
    while True:
        print("\n====== MENU ADMIN ======")
        print("1. Lihat status meja")
        print("2. Ubah harga per jam")
        print("3. Logout Admin")

        pilihan_admin = int(input("Masukkan pilihan: "))

        if pilihan_admin == 1:
            print(f"Meja yang tersedia: Meja {meja}")
        elif pilihan_admin == 2:
            harga_per_jam = int(input("Masukkan harga baru per jam: "))
            print(f"Harga per jam berhasil diubah menjadi Rp{harga_per_jam}.")
        elif pilihan_admin == 3:
            print("Logout Admin berhasil.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Fungsi menu utama
def main():
    while True:
        print("\n====== MENU ======")
        print("1. Login User")
        print("2. Login Admin")
        print("3. Exit")
        
        pilihan = int(input("Masukkan pilihan: "))
        
        if pilihan == 1:
            # Login user
            username = login()
            if username:
                while True:
                    print("\n1. Booking meja")
                    print("2. Logout")
                    pilihan_user = int(input("Masukkan pilihan: "))
                    if pilihan_user == 1:
                        durasi = float(input("Masukkan durasi pemesanan (dalam jam): "))
                        total_biaya = hitung_biaya(durasi)
                        print(f"Silahkan bermain di meja {meja}.")
                        print(f"Total biaya yang harus dibayar: Rp{total_biaya}")
                    elif pilihan_user == 2:
                        print("Logout berhasil. Terima kasih!")
                        break
                    else:
                        print("Pilihan tidak valid")
        
        elif pilihan == 2:
            # Login admin
            if admin_login():
                admin_menu()
        
        elif pilihan == 3:
            print("Terima kasih telah menggunakan layanan kami.")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
