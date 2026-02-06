catatan = []

def tambah_catatan():
    print("\n--- Tambah Catatan Belajar ---")
    
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik: ")
    durasi = int(input("Masukkan durasi belajar (menit): "))
    
    # Membuat dictionary untuk satu catatan
    data_catatan = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    # Menyimpan data ke dalam list catatan
    catatan.append(data_catatan)
    print("✓ Catatan berhasil ditambahkan!")

def lihat_catatan():
    print("\n--- Lihat Catatan Belajar ---")
    
    # Cek apakah data kosong
    if len(catatan) == 0:
        print("Belum ada catatan belajar. Mulai tambahkan catatan Anda!")
        return
    
    # Tampilkan semua catatan dengan format rapi
    print("\n" + "="*60)
    for i, data in enumerate(catatan, 1):
        print(f"\nCatatan No. {i}")
        print(f"  Mapel  : {data['mapel']}")
        print(f"  Topik  : {data['topik']}")
        print(f"  Durasi : {data['durasi']} menit")
    print("\n" + "="*60)

def total_waktu():
    print("\n--- Total Waktu Belajar ---")
    
    # Cek apakah data kosong
    if len(catatan) == 0:
        print("Belum ada catatan belajar. Mulai tambahkan catatan Anda!")
        return
    
    # Hitung total durasi dari semua catatan
    total = sum(data['durasi'] for data in catatan)
    
    # Konversi ke jam dan menit
    jam = total // 60
    menit = total % 60
    
    # Tampilkan hasil dengan rapi
    print(f"\nTotal waktu belajar Anda: {total} menit")
    print(f"Setara dengan: {jam} jam {menit} menit")
    print(f"✓ Terus semangat belajar!")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")