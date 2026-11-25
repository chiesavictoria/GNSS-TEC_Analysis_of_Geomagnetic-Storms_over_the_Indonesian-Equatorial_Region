# PIPELINE PENELITIAN GNSS-TEC
## Pipeline_Final_v0.1

**Topik penelitian:** Analisis Respons Temporal dan Time Lag GNSS TEC Terhadap Gangguan Geomagnetik pada Halloween Storm 2003 dan Badai Geomagnetik Mei 2004 di Indonesia

**Fokus tahap awal:** Pengolahan dan validasi data GNSS RINEX stasiun BAKO pada Halloween Geomagnetic Storm 2003.

---

## 1. Tujuan Pipeline

Pipeline ini disusun untuk membangun alur pengolahan data GNSS yang sistematis, reproducible, dan dapat divalidasi pada setiap tahap.

Tahap awal difokuskan pada pemeriksaan integritas data RINEX, pengembangan parser, dan validasi hasil pembacaan data sebelum dilakukan pemrosesan observasi GNSS lebih lanjut.

## 2. Struktur Direktori

```text
Pipeline_Final_v0.1/
│
├── notebooks/
│
├── data/
│   ├── raw/
│   └── external/
│
├── output/
│
└── documentation/
    └── README_Pipeline_v0.1.md
```

### Fungsi Direktori

| Direktori | Fungsi |
|---|---|
| notebooks | Notebook pengolahan dan analisis |
| data/raw | Data RINEX mentah |
| data/external | Data pendukung dari sumber eksternal |
| output | Hasil pengolahan, tabel, dan laporan validasi |
| documentation | Dokumentasi metodologi dan perkembangan pipeline |

Data mentah dipertahankan tanpa perubahan langsung. Seluruh hasil pengolahan disimpan secara terpisah di direktori output.

## 3. Arsitektur Pipeline v0.1

### Tahap A — Data Ingestion dan Validasi Parser

**00. Dataset Inventory and Integrity Audit**

Tujuan:
- Menginventarisasi data RINEX.
- Memeriksa nama file, stasiun, dan tanggal observasi.
- Memeriksa metadata header.
- Memeriksa epoch pertama dan terakhir.
- Mengidentifikasi ketidaksesuaian atau masalah integritas data.

Output:
- Dataset inventory.
- Integrity audit report.

**01. RINEX Data Ingestion and Parser Development**

Tujuan:
- Membaca struktur header RINEX.
- Mengidentifikasi tipe dan urutan observasi.
- Mengembangkan parser manual sesuai struktur RINEX 2.10.
- Menangani struktur epoch dan continuation records.
- Menghasilkan tabel observasi terstruktur.

Output:
- Manual-parser observation table.
- Parser metadata.

**02. RINEX Parser Validation and Data Reconciliation**

Tujuan:
- Membandingkan hasil parser manual dengan struktur data RINEX mentah.
- Membandingkan hasil parser manual dengan GeoRinex.
- Memeriksa kesesuaian timestamp, satelit, dan nilai observasi.
- Menginvestigasi ketidaksesuaian hasil parsing.

Output:
- Parser validation report.
- Validated observation table.

Keputusan sumber data:
- RINEX mentah menjadi acuan utama.
- Parser manual menjadi sumber tabel observasi resmi setelah validasi berhasil.
- GeoRinex digunakan sebagai pembanding independen.

### Tahap B — Quality Assessment dan Relative STEC

**03. GNSS Observation Quality Assessment**

Fokus:
- Ketersediaan observasi setiap epoch dan satelit.
- Kelengkapan L1 dan L2.
- Missing values dan NaN.
- Signal Strength Indicator (SSI).

Tahap ini tidak melakukan kombinasi fase.

**04. Cycle Slip Detection and Anomaly Investigation**

Fokus:
- Geometry-Free combination.
- Interpretasi Loss of Lock Indicator (LLI).
- Pemeriksaan pseudorange.
- Investigasi anomali satelit.

**05. Satellite Arc Segmentation and Continuity Analysis**

Fokus:
- Identifikasi arc observasi.
- Segmentasi berdasarkan kontinuitas data.
- Pemeriksaan durasi dan kualitas arc.

**06. Relative STEC Processing and Validation**

Fokus:
- Pengolahan kombinasi fase L1 dan L2.
- Perhitungan relative STEC.
- Validasi konsistensi hasil perhitungan.
- Pemeriksaan keterbatasan ambiguitas fase.

### Tahap C — Pengolahan TEC dan Analisis Badai Geomagnetik

**07. Calibrated STEC Processing and Bias Correction**

Fokus:
- Kalibrasi STEC.
- Koreksi bias yang diperlukan.
- Evaluasi kelayakan hasil STEC untuk konversi VTEC.

**08. VTEC Conversion and Delta TEC Analysis**

Fokus:
- Perhitungan posisi satelit dan IPP.
- Mapping function.
- Konversi STEC menjadi VTEC.
- Perhitungan perubahan TEC (ΔTEC).

**09. Geomagnetic Storm Response Analysis**

Fokus:
- Analisis respons TEC terhadap fase badai geomagnetik.
- Penyelarasan waktu dengan indeks SYM-H.
- Evaluasi respons dan kemungkinan time lag.

**10. Comparative Analysis of Geomagnetic Storm Events**

Fokus:
- Perbandingan respons ionosfer pada Halloween Storm 2003 dan badai geomagnetik Mei 2024.
- Evaluasi perbedaan karakteristik respons TEC.

Ketersediaan data dan kelayakan metodologi harus diverifikasi sebelum tahap ini dilaksanakan.

## 4. Prinsip Pengembangan

1. Setiap notebook memiliki tujuan dan ruang lingkup yang jelas.
2. Setiap notebook memiliki input dan output yang terdokumentasi.
3. Notebook berikutnya membaca hasil yang telah disimpan dari tahap sebelumnya.
4. Validasi dilakukan sebelum hasil digunakan pada tahap lanjutan.
5. Fungsi yang digunakan bersama akan ditempatkan dalam modul Python setelah definisinya stabil.
6. Tidak melakukan interpretasi ilmiah melebihi dukungan data dan hasil validasi.
7. Perubahan metodologi dan struktur pipeline dicatat beserta alasan perubahannya.

## 5. Status Pengembangan

| Notebook | Status |
|---|---|
| 00 — Dataset Inventory and Integrity Audit | Belum dikerjakan |
| 01 — RINEX Data Ingestion and Parser Development | Belum dikerjakan |
| 02 — RINEX Parser Validation and Data Reconciliation | Belum dikerjakan |
| 03–06 | Roadmap |
| 07–10 | Roadmap |

Pengerjaan saat ini diprioritaskan pada Notebook 00–02. Notebook selanjutnya baru dikembangkan setelah tahap validasi sebelumnya memenuhi kriteria yang ditetapkan.

## 6. Catatan Versi

**Versi:** v0.1

Arsitektur ini merupakan rancangan awal dan belum bersifat final. Penyesuaian dapat dilakukan berdasarkan hasil pemeriksaan data, evaluasi metodologi, dan diskusi bersama pembimbing.

Setiap perubahan harus memiliki alasan teknis atau ilmiah yang jelas.
