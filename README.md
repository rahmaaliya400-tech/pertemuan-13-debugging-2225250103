# Pertemuan 13 - Debugging dan Testing

Nama: Rahma Aliya  
NIM: 2225250103  
Kelas: 3F

## Kasus

Praktikum ini membahas debugging dan testing pada program Python. Pengujian dilakukan pada program penentuan kelulusan, pembacaan data nilai dari file, perhitungan rata-rata, serta latihan tracing dan debugging.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC01 | Nilai 80 | Lulus | Belum dicatat | Perlu verifikasi |
| TC02 | Nilai 60 | Tidak lulus | Belum dicatat | Perlu verifikasi |
| TC03 | Nilai 40 | Tidak lulus | Belum dicatat | Perlu verifikasi |
| TC04 | File `nilai.txt` berisi `80 90 70` | Data nilai terbaca dengan benar | File tidak ditemukan | Berhasil setelah perbaikan path |
| TC05 | Data nilai 80, 90, 70 | Rata-rata 80.0 | Hasil awal perlu diverifikasi | Berhasil setelah perbaikan perhitungan |

## Bug Report

**Bug 1: File tidak ditemukan**

- **Gejala:** Program menampilkan pesan `File tidak ditemukan`.
- **Lokasi:** Program yang membaca file `nilai.txt`.
- **Akar penyebab:** Path file yang digunakan program tidak sesuai dengan lokasi file data.
- **Perbaikan:** Menyesuaikan path menjadi `kasus/nilai.txt`.
- **Hasil:** Program berhasil membaca data `[80, 90, 70]`.

**Bug 2: Perhitungan rata-rata tidak tepat**

- **Gejala:** Program menghasilkan rata-rata yang tidak sesuai dengan data.
- **Lokasi:** Fungsi `rata_rata()` pada latihan debugging.
- **Akar penyebab:** Program membagi total nilai dengan angka tetap 5, padahal data yang digunakan berjumlah 3.
- **Perbaikan:** Mengganti pembagi dengan `len(data)`.
- **Hasil:** Rata-rata nilai 80, 90, dan 70 menjadi 80.0.

## Retest

Setelah perbaikan dilakukan, program dijalankan kembali melalui terminal VS Code.

1. Program pembacaan file berhasil menampilkan `Data nilai: [80, 90, 70]`.
2. Program penentuan kelulusan menampilkan hasil sesuai aturan pada kode, yaitu nilai lebih dari 60 dinyatakan lulus.
3. Fungsi rata-rata menghasilkan nilai `80.0` untuk data `[80, 90, 70]`.
4. Program latihan dan praktik dijalankan kembali untuk memeriksa hasilnya.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal pada folder utama proyek:

```bash
python praktik/praktik_4_debugging.py
```

Contoh menjalankan program lain:

```bash
python kasus/kasus_01_batas_kelulusan.py
python kasus/kasus_02_rata_rata.py
python kasus/kasus_03_file_nilai.py
python latihan/01_trace_loop.py
python latihan/02_trace_fungsi.py
python latihan/03_test_case.py
python latihan/04_debug_breakpoint.py
```

## Refleksi

Teknik debugging yang paling membantu adalah memeriksa pesan kesalahan dan menelusuri kode secara bertahap. Teknik ini membantu menemukan penyebab masalah, seperti path file yang tidak sesuai dan pembagi yang salah dalam perhitungan rata-rata. Setelah kode diperbaiki, program dijalankan kembali untuk memastikan hasilnya sesuai dengan yang diharapkan.
