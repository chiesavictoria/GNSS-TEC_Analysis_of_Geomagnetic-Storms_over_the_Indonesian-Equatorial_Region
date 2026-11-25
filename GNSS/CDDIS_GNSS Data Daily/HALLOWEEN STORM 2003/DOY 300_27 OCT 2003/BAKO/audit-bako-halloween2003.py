
from pathlib import Path
from datetime import datetime
import pandas as pd
import georinex as gr
import numpy as np

# ============================================================
# AUDIT DATA GNSS BAKO - HALLOWEEN STORM 2003
# Periode target: DOY 300-307 (27 Oktober-3 November 2003)
# Sumber data: CDDIS
# ============================================================

ROOT = Path(
    r"C:\SKRIPSI AKHIR\ALL DATA\GNSS\CDDIS_GNSS Data Daily"
) / "HALLOWEEN STORM 2003"

DOY_INFO = {
    300: "2003-10-27",
    301: "2003-10-28",
    302: "2003-10-29",
    303: "2003-10-30",
    304: "2003-10-31",
    305: "2003-11-01",
    306: "2003-11-02",
    307: "2003-11-03",
}

OUTPUT = ROOT / "hasil_audit_bako"
OUTPUT.mkdir(exist_ok=True)

print("=" * 70)
print("AUDIT AWAL DATA GNSS BAKO")
print("Periode: 27 Oktober - 3 November 2003")
print("=" * 70)

# ------------------------------------------------------------
# 1. INVENTARISASI FILE RINEX BAKO
# ------------------------------------------------------------

inventaris = []

for doy, tanggal_target in DOY_INFO.items():
    nama_file = f"bako{doy}0.03o"

    kandidat = list(ROOT.rglob(nama_file))

    if kandidat:
        for file_rinex in kandidat:
            inventaris.append({
                "DOY_target": doy,
                "tanggal_target": tanggal_target,
                "nama_file": file_rinex.name,
                "ukuran_MB": round(
                    file_rinex.stat().st_size / (1024 ** 2), 3
                ),
                "lokasi_file": str(file_rinex.relative_to(ROOT)),
                "status": "Ditemukan",
            })
    else:
        inventaris.append({
            "DOY_target": doy,
            "tanggal_target": tanggal_target,
            "nama_file": nama_file,
            "ukuran_MB": np.nan,
            "lokasi_file": "",
            "status": "Tidak ditemukan",
        })

df_inventaris = pd.DataFrame(inventaris)

print("\n[1] INVENTARISASI FILE")
print(df_inventaris.to_string(index=False))

# Simpan hasil inventarisasi
df_inventaris.to_csv(
    OUTPUT / "01_inventaris_bako.csv",
    index=False
)

print("\nHasil inventarisasi disimpan di:")
print(OUTPUT / "01_inventaris_bako.csv")

