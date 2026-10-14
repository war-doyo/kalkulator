
rumus = {}

def hitung(teks, variabel=None):
    if variabel is None:
        variabel = {}

    izin = {
        "__builtins__": {},
    }

    izin.update(variabel)

    return eval(teks, izin, {})


def biasa():
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        return angka1 + angka2
    elif operator == "-":
        return angka1 - angka2
    elif operator == "*":
        return angka1 * angka2
    elif operator == "/":
        return angka1 / angka2
    else:
        print("Operator tidak valid.")
    return


def nambah_rumus():
    nama = input("Nama rumus: ").strip()

    if not nama:
        print("Nama tidak boleh kosong.")
        return

    if nama in rumus:
        print("Nama sudah ada. Gunakan edit untuk mengubahnya.")
        return

    ekspresi = input("Masukkan rumus matematika: ").strip()

    if not ekspresi:
        print("Rumus tidak boleh kosong.")
        return

    rumus[nama] = ekspresi
    print("Rumus", nama, "berhasil disimpan.")


def hapus_rumus():
    nama = input("Nama rumus yang ingin dihapus: ").strip()

    if nama in rumus:
        del rumus[nama]
        print("Rumus", nama, "berhasil dihapus.")
    else:
        print("Rumus tidak ditemukan.")


def edit_rumus():
    nama = input("Nama rumus yang ingin diedit: ").strip()

    if nama not in rumus:
        print("Rumus tidak ditemukan.")
        return

    print("Rumus lama:", rumus[nama])
    baru = input("Masukkan rumus baru: ").strip()

    if baru:
        rumus[nama] = baru
        print("Rumus berhasil diperbarui.")
    else:
        print("Perubahan dibatalkan.")


def tampilkan_rumus():
    if not rumus:
        print("Belum ada rumus tersimpan.")
        return

    print("\nDaftar rumus:")
    for nama, ekspresi in rumus.items():
        print(nama, "=", ekspresi)


def gunakan_rumus(nama):
    ekspresi = rumus[nama]

    print("Rumus:", ekspresi)
    print("Ketik 'kembali' untuk keluar dari mode rumus.")

    while True:
        try:
            nilai = input("Nilai variabel (masukan variabel sesuai rumus): ")

            if nilai.lower() == "kembali":
                break

            variabel = {}

            if nilai.strip():
                for bagian in nilai.split(","):
                    kunci, angka = bagian.split("=")
                    variabel[kunci.strip()] = float(angka.strip())

            hasil = hitung(ekspresi, variabel)
            print("Hasil:", hasil)

        except Exception:
            print("Input atau rumus tidak valid.")




while True:
    print("=== KALKULATOR ===")
    print("Ketik 1 untuk mode biasa.")
    print("Ketik 2 untuk membuat rumus.")
    print("Ketik 3 untuk menghapus rumus.")
    print("Ketik 4 untuk mengedit rumus.")
    print("Ketik 5 untuk melihat rumus.")
    print("Ketik 6 untuk menghentikan program.")
    mode = input("\nMode / perintah: ").strip()

    if mode == "6":
        print("Program dihentikan.")
        break

    elif mode == "2":
        nambah_rumus()

    elif mode == "3":
        hapus_rumus()

    elif mode == "4":
        edit_rumus()

    elif mode == "5":
        tampilkan_rumus()

    elif mode == "1":
        print("Hasil:", biasa())

    elif mode in rumus:
        gunakan_rumus(mode)

    
