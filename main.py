catatan = []
mapel_favorit = []

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

def tambah_mapel_favorit():
    print("\n--- Mapel Favorit ---")
    
    # Meminta input mapel favorit
    mapel = input("Masukkan nama mapel favorit: ")
    
    # Cek apakah mapel sudah ada di favorit
    if mapel in mapel_favorit:
        print("✗ Mapel ini sudah ada di favorit Anda!")
        return
    
    # Tambah ke daftar favorit
    mapel_favorit.append(mapel)
    print(f"✓ Mapel '{mapel}' ditambahkan ke favorit!")

def lihat_mapel_favorit():
    print("\n--- Daftar Mapel Favorit ---")
    
    # Cek apakah daftar kosong
    if len(mapel_favorit) == 0:
        print("Belum ada mapel favorit. Tambahkan mapel favorit Anda!")
        return
    
    # Tampilkan daftar favorit
    print("\nMapel favorit Anda:")
    for i, mapel in enumerate(mapel_favorit, 1):
        print(f"  {i}. {mapel}")

def hapus_mapel_favorit():
    print("\n--- Hapus Mapel Favorit ---")
    
    # Cek apakah daftar kosong
    if len(mapel_favorit) == 0:
        print("Belum ada mapel favorit untuk dihapus.")
        return
    
    # Tampilkan pilihan mapel
    print("\nMapel favorit Anda:")
    for i, mapel in enumerate(mapel_favorit, 1):
        print(f"  {i}. {mapel}")
    
    # Minta pengguna memilih mapel yang ingin dihapus
    try:
        pilihan = int(input("\nPilih nomor mapel yang ingin dihapus: "))
        
        if 1 <= pilihan <= len(mapel_favorit):
            mapel_dihapus = mapel_favorit.pop(pilihan - 1)
            print(f"✓ Mapel '{mapel_dihapus}' dihapus dari favorit!")
        else:
            print("✗ Nomor tidak valid!")
    except ValueError:
        print("✗ Masukkan angka yang valid!")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Mapel Favorit")
    print("5. Keluar")

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
        print("\n--- Menu Mapel Favorit ---")
        print("a. Tambah mapel favorit")
        print("b. Lihat mapel favorit")
        print("c. Hapus mapel favorit")
        sub_pilihan = input("Pilih opsi: ")
        
        if sub_pilihan == "a":
            tambah_mapel_favorit()
        elif sub_pilihan == "b":
            lihat_mapel_favorit()
        elif sub_pilihan == "c":
            hapus_mapel_favorit()
        else:
            print("Pilihan tidak valid")
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")