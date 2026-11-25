# DOKUMENTASI PIPELINE PENELITIAN GNSS-TEC

**Versi:** 0.1  
**Dataset utama:** Halloween Geomagnetic Storm 2003  
**Stasiun GNSS utama:** BAKO  
**Format data:** RINEX Observation 2.10  

---

## 1. Gambaran Umum Penelitian

Penelitian ini berfokus pada pengamatan respons ionosfer ekuator Indonesia
terhadap aktivitas badai geomagnetik menggunakan data Global Navigation
Satellite System (GNSS).

Parameter utama yang dikaji adalah Total Electron Content (TEC), yang
diperoleh melalui pengolahan data observasi GNSS.

Peristiwa badai geomagnetik Halloween 2003 digunakan sebagai salah satu
objek utama penelitian. Data observasi GNSS dari stasiun BAKO digunakan
sebagai dataset utama untuk tahap pengembangan dan validasi pipeline.

Penelitian ini juga direncanakan mencakup perbandingan dengan peristiwa
badai geomagnetik 10–11 Mei 2024, bergantung pada ketersediaan dan
kelayakan data observasi.

## 2. Tujuan Pengembangan Pipeline

Pipeline dikembangkan untuk menghasilkan alur pengolahan data yang
sistematis, terdokumentasi, dan dapat direproduksi.

Tahapan utama yang direncanakan meliputi:

1. Inventarisasi dan pemeriksaan integritas dataset.
2. Pembacaan struktur dan pengembangan parser RINEX.
3. Validasi parser terhadap data mentah dan hasil GeoRinex.
4. Pemeriksaan kualitas observasi GNSS.
5. Deteksi cycle slip dan investigasi anomali fase.
6. Segmentasi arc satelit.
7. Pengolahan Relative STEC.
8. Kalibrasi STEC dan koreksi bias.
9. Konversi STEC menjadi VTEC serta analisis perubahan TEC.
10. Analisis respons TEC terhadap fase badai geomagnetik.
11. Perbandingan respons ionosfer pada peristiwa badai geomagnetik.

Tahapan tersebut merupakan rancangan alur penelitian. Setiap tahap
dilaksanakan setelah tahap sebelumnya memenuhi kriteria pemeriksaan.

## 3. Struktur Direktori Proyek

Struktur direktori utama:

```text
Pipeline_Final/
│
├── data/
│   ├── raw/
│   │   ├── DOY300/
│   │   ├── DOY301/
│   │   ├── DOY302/
│   │   ├── DOY303/
│   │   ├── DOY304/
│   │   ├── DOY305/
│   │   ├── DOY306/
│   │   └── DOY307/
│   │
│   └── external/
│
├── notebooks/
│
├── Output/
│
├── documentations/
│
├── config.py
├── processing_functions.py
└── rinex_parser.py
```

Keterangan:

- `data/raw/` menyimpan data RINEX mentah.
- `data/external/` digunakan untuk menyimpan data pendukung dari sumber eksternal.
- `notebooks/` menyimpan notebook pengolahan dan analisis.
- `Output/` menyimpan hasil pemeriksaan, tabel, dan keluaran pengolahan.
- `documentations/` menyimpan dokumentasi pipeline dan catatan metodologi.
- `config.py`, `processing_functions.py`, dan `rinex_parser.py` merupakan berkas pendukung kode pipeline yang akan digunakan setelah diperiksa dan divalidasi.

## 4. Dataset Halloween Storm 2003

Dataset utama yang diinventarisasi mencakup delapan folder DOY300–DOY307.

| DOY | Tanggal target | Nama berkas |
|---|---|---|
| 300 | 27 Oktober 2003 | bako3000.03o |
| 301 | 28 Oktober 2003 | bako3010.03o |
| 302 | 29 Oktober 2003 | bako3020.03o |
| 303 | 30 Oktober 2003 | bako3030.03o |
| 304 | 31 Oktober 2003 | bako3040.03o |
| 305 | 1 November 2003 | bako3050.03o |
| 306 | 2 November 2003 | bako3060.03o |
| 307 | 3 November 2003 | bako3070.03o |

Seluruh delapan berkas ditemukan dalam direktori data mentah.

### 4.1 Metadata RINEX DOY300

Berdasarkan pemeriksaan header berkas `bako3000.03o`:

- Versi RINEX: 2.10.
- Jenis data: GPS Observation Data.
- Nama stasiun: BAKO.
- Nomor marker: 23101M002.
- Receiver: TRIMBLE 4000SSE.
- Antena: TRM14532.00.
- Jumlah tipe observasi: 6.
- Tipe observasi: L1, L2, C1, P2, P1, dan D1.
- Sistem waktu pada header: GPS.
- Waktu observasi pertama: 27 Oktober 2003 pukul 00:00:30 GPS.

Koordinat stasiun yang tercantum pada header:

- X = -1836967.8873 m
- Y = 6065615.4384 m
- Z = -716260.3127 m

## 5. Hasil Audit Dataset

Pemeriksaan awal dilakukan untuk mengevaluasi kesesuaian identitas berkas,
rentang waktu observasi, keteraturan epoch, dan cakupan data terhadap
grid interval 30 detik.

### 5.1 Audit Identitas Dataset

Hasil pemeriksaan header terhadap delapan berkas:

| Klasifikasi | Jumlah berkas |
|---|---:|
| MATCH | 7 |
| DATE_MISMATCH | 1 |
| Total | 8 |

Temuan penting:

Berkas DOY305 bernama `bako3050.03o` memiliki tanggal observasi pertama
pada 8 November 2003 pukul 00:00:30 GPS, bukan 1 November 2003 seperti
tanggal target folder.

Berkas tersebut diberi status:

`HOLD_IDENTITY_MISMATCH`

Berkas tetap dipertahankan dalam direktori data mentah. Penyebab
ketidaksesuaian tanggal belum dapat dipastikan.

### 5.2 Audit Temporal dan Cakupan Epoch

Pemeriksaan temporal menunjukkan:

- DOY300, DOY301, DOY302, DOY303, DOY306, dan DOY307 memiliki 2878 epoch.
- DOY304 memiliki 2867 epoch.
- DOY305 memiliki 2878 epoch, tetapi tanggal observasinya tidak sesuai
  dengan tanggal target folder.

Untuk DOY300, interval observasi nominal adalah 30 detik.

Hasil pemetaan ke grid 30 detik:

| Parameter | Hasil |
|---|---:|
| Epoch yang diharapkan | 2880 |
| Epoch teramati | 2878 |
| Epoch berhasil dipetakan | 2878 |
| Epoch tidak terpetakan | 0 |
| Epoch duplikat | 0 |
| Epoch hilang | 2 |
| Cakupan grid | 99,930556% |

Dua epoch yang hilang berada pada awal dan akhir rentang observasi:
00:00:00 dan 23:59:30.

Tidak ditemukan gap internal pada grid DOY300.

### 5.3 Klasifikasi Kelayakan Awal

Berdasarkan audit identitas dan temporal:

| Status | DOY | Jumlah |
|---|---|---:|
| ELIGIBLE_FOR_NEXT_STAGE | 300–303, 306–307 | 6 |
| REVIEW_BOUNDARY_COVERAGE | 304 | 1 |
| HOLD_IDENTITY_MISMATCH | 305 | 1 |

**Catatan:** Status ELIGIBLE_FOR_NEXT_STAGE hanya menunjukkan bahwa
berkas lolos kriteria pemeriksaan awal identitas dan cakupan temporal.
Status ini belum menyatakan seluruh observasi GNSS bebas dari anomali
atau telah memenuhi persyaratan pengolahan TEC.

## 6. Rencana dan Struktur Notebook

### Tahap yang telah dikerjakan

**Notebook 00 — Dataset Inventory and Integrity Audit**

Fokus:
- Inventarisasi berkas RINEX.
- Pemeriksaan identitas stasiun dan tanggal observasi.
- Pemeriksaan header.
- Pemeriksaan rentang waktu dan interval epoch.
- Pemeriksaan cakupan grid 30 detik.
- Klasifikasi kelayakan awal dataset.

Keluaran utama:
- `doy300_integrity_audit_summary.csv`
- `dataset_header_identity_audit.csv`
- `dataset_temporal_audit.csv`
- `dataset_grid_coverage_audit.csv`
- `dataset_initial_eligibility.csv`
- `dataset_final_audit_report.csv`
- `dataset_final_audit_report.txt`

### Tahap berikutnya

**Notebook 01 — RINEX Data Ingestion and Parser Development**

Fokus:
- Memahami struktur RINEX 2.10.
- Membaca header dan urutan tipe observasi.
- Mengembangkan parser manual.
- Menangani struktur epoch, daftar satelit, dan continuation records.
- Menghasilkan tabel observasi terstruktur.

**Notebook 02 — RINEX Parser Validation and Data Reconciliation**

Fokus:
- Membandingkan hasil parser manual dengan data mentah.
- Membandingkan hasil parser dengan GeoRinex.
- Memeriksa jumlah satelit dan observasi.
- Memeriksa konsistensi timestamp.
- Menginvestigasi perbedaan hasil parsing, termasuk kasus G02 dan G14.
- Menetapkan kelayakan parser sebagai sumber data resmi pipeline.

Parser belum ditetapkan sebagai parser resmi sebelum proses validasi
pada Notebook 02 selesai.

### Roadmap tahap lanjutan

| Notebook | Nama | Fokus |
|---|---|---|
| 03 | GNSS Observation Quality Assessment | Kualitas dan kelengkapan observasi |
| 04 | Cycle Slip Detection and Anomaly Investigation | Deteksi cycle slip dan investigasi anomali |
| 05 | Satellite Arc Segmentation and Continuity Analysis | Segmentasi dan kontinuitas arc |
| 06 | Relative STEC Processing and Validation | Pengolahan dan validasi Relative STEC |
| 07 | Calibrated STEC Processing and Bias Correction | Kalibrasi STEC dan koreksi bias |
| 08 | VTEC Conversion and Delta TEC Analysis | Konversi VTEC dan analisis perubahan TEC |
| 09 | Geomagnetic Storm Response Analysis | Respons TEC terhadap badai geomagnetik |
| 10 | Comparative Analysis of Geomagnetic Storm Events | Perbandingan antarperistiwa badai |

Notebook 03–10 masih merupakan roadmap dan belum dinyatakan selesai.
Pelaksanaannya bergantung pada hasil validasi tahap sebelumnya serta
ketersediaan data pendukung.

## 7. Catatan Metodologi Penting

Beberapa hal yang harus diperhatikan dalam pengolahan selanjutnya:

1. Waktu pada header RINEX DOY300 dinyatakan dalam GPS Time. Konversi
   ke UTC harus dilakukan secara eksplisit sebelum dibandingkan dengan
   indeks geomagnetik atau data lain yang menggunakan UTC.

2. Struktur observasi RINEX 2.10 harus dibaca berdasarkan jumlah dan
   urutan tipe observasi pada header. Parser tidak boleh mengasumsikan
   bahwa setiap satelit selalu direpresentasikan oleh jumlah baris fisik
   yang sama tanpa memeriksa struktur berkas.

3. Loss-of-Lock Indicator (LLI) perlu diinterpretasikan berdasarkan bit
   penyusunnya. Nilai LLI tidak boleh langsung dianggap sebagai bukti
   tunggal terjadinya cycle slip.

4. Relative STEC yang dihitung secara independen pada setiap arc belum
   dapat diperlakukan sebagai STEC absolut yang kontinu.

5. Perhitungan STEC terkalibrasi memerlukan penanganan ambiguitas fase,
   penggabungan pengamatan fase dan pseudorange, serta koreksi bias yang
   relevan.

6. Konversi STEC menjadi VTEC memerlukan informasi geometri satelit,
   posisi IPP, elevasi satelit, dan fungsi pemetaan yang sesuai.

7. Perbandingan TEC dengan indeks geomagnetik harus menggunakan
   referensi waktu yang konsisten dan mempertimbangkan perbedaan
   resolusi temporal data.

8. Data pendukung seperti navigasi GNSS, orbit presisi, indeks
   geomagnetik, dan data ionosfer harus diperiksa ketersediaannya
   sebelum digunakan dalam tahapan analisis.

## 8. Prinsip Pengembangan Pipeline

Pipeline dikembangkan dengan prinsip:

- Setiap tahap memiliki tujuan dan keluaran yang jelas.
- Pemeriksaan kualitas dilakukan sebelum pengolahan fisik lebih lanjut.
- Hasil pengolahan harus dapat ditelusuri ke data mentah.
- Perubahan kode dan metode harus terdokumentasi.
- Asumsi dan keterbatasan data harus dinyatakan secara eksplisit.
- Tahap berikutnya tidak dilanjutkan sebelum kriteria validasi tahap
  sebelumnya terpenuhi.

## 9. Status Pengembangan

**Versi pipeline:** 0.1

**Status Notebook 00:** Audit awal dataset telah diselesaikan.

**Status Notebook 01:** Belum dimulai.

**Status Notebook 02:** Belum dimulai.

Pekerjaan selanjutnya difokuskan pada pengembangan dan validasi parser
RINEX sebelum melanjutkan ke pemeriksaan kualitas observasi dan
pengolahan TEC.

---

**Dokumen ini merupakan dokumentasi pengembangan pipeline versi 0.1.**
Pembaruan dilakukan mengikuti hasil pemeriksaan, validasi, dan keputusan
metodologi pada tahapan penelitian berikutnya.
