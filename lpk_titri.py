import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Perhitungan Titrimetri",
    page_icon="🧪",
    layout="wide"
)

# =====================================
# HEADER
# =====================================
st.title("🧪 Web Perhitungan Titrimetri")
st.subheader("Standarisasi & Penetapan Kadar")

# =====================================
# GAMBAR TITRASI
# =====================================
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/92/Titration_setup.svg",
    caption="Praktik Titrasi"
)

# =====================================
# ICON ALAT LAB
# =====================================
st.header("Peralatan Titrasi")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("### ⚗️")
    st.write("Buret")

with col2:
    st.markdown("### 🧪")
    st.write("Erlenmeyer")

with col3:
    st.markdown("### 🧫")
    st.write("Pipet Volumetrik")

with col4:
    st.markdown("### 🧴")
    st.write("Bulb")

with col5:
    st.markdown("### ⚱️")
    st.write("Labu Takar")

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:
    st.header("Menu")

    jenis = st.selectbox(
        "Pilih Jenis Perhitungan",
        ["Standarisasi", "Penetapan Kadar"]
    )

    metode = st.selectbox(
        "Pilih Metode",
        [
            "Alkalimetri",
            "Asidimetri",
            "Permanganometri",
            "Iodometri",
            "Argentometri",
            "Kompleksometri"
        ]
    )

# =====================================
# INFORMASI METODE
# =====================================
st.header("Informasi Metode")

if jenis == "Standarisasi":
    if metode == "Alkalimetri":
        st.info("Baku Primer : Asam Oksalat")
    elif metode == "Asidimetri":
        st.info("Baku Primer : Boraks")
    elif metode == "Permanganometri":
        st.info("Baku Primer : Asam Oksalat")
    elif metode == "Iodometri":
        st.info("Baku Primer : K2Cr2O7")
    elif metode == "Argentometri":
        st.info("Baku Primer : NaCl")
    elif metode == "Kompleksometri":
        st.info("Baku Primer : CaCO3")

else:
    if metode == "Alkalimetri":
        st.info("Penetapan kadar CH3COOH dalam cuka")
    elif metode == "Asidimetri":
        st.info("Penetapan kadar Na2CO3 & NaOH (Warder)")
    elif metode == "Permanganometri":
        st.info("Penetapan kadar Fe")
    elif metode == "Iodometri":
        st.info("Penetapan kadar Cl")
    elif metode == "Argentometri":
        st.info("Penetapan kadar Cl")
    elif metode == "Kompleksometri":
        st.info("Kesadahan air (CaCO3 ppm)")

# =====================================
# FORM INPUT
# =====================================
st.header("Input Data")

# Input sama
V1 = st.number_input("Volume Titran 1 (mL)", min_value=0.0)
V2 = st.number_input("Volume Titran 2 (mL)", min_value=0.0)
BE = st.number_input("BE / BM", min_value=0.0)
FP = st.number_input("Faktor Pengali", min_value=0.0, value=1.0)

# Form dinamis
if jenis == "Standarisasi":
    mg = st.number_input("mg Baku Primer", min_value=0.0)

else:
    N = st.number_input("Normalitas / Molaritas", min_value=0.0)
    S = st.number_input("Massa / Volume Sampel", min_value=0.0)

# =====================================
# TOMBOL HITUNG
# =====================================
if st.button("Hitung"):

    # validasi dasar
    if V1 == 0 or V2 == 0 or BE == 0 or FP == 0:
        st.error("Data tidak boleh 0")

    else:

        # =====================================
        # STANDARISASI
        # N = mg / (V × BE × FP)
        # =====================================
        if jenis == "Standarisasi":

            hasil1 = mg / (V1 * BE * FP)
            hasil2 = mg / (V2 * BE * FP)

            rata = (hasil1 + hasil2) / 2
            rpd = abs(hasil1 - hasil2) / rata * 100

            st.header("Hasil Standarisasi")
            st.success(f"N1 = {hasil1:.4f}")
            st.success(f"N2 = {hasil2:.4f}")
            st.write(f"Rata-rata Normalitas = {rata:.4f}")
            st.write(f"%RPD = {rpd:.2f}%")

        # =====================================
        # PENETAPAN KADAR
        # Kadar = (V × N × BE × FP × 10^-3 ×100)/S
        # =====================================
        else:

            if S == 0:
                st.error("Sampel tidak boleh 0")

            else:
                hasil1 = (V1 * N * BE * FP * (10**-3) * 100) / S
                hasil2 = (V2 * N * BE * FP * (10**-3) * 100) / S

                rata = (hasil1 + hasil2) / 2
                rpd = abs(hasil1 - hasil2) / rata * 100

                st.header("Hasil Penetapan Kadar")
                st.success(f"Kadar 1 = {hasil1:.2f}%")
                st.success(f"Kadar 2 = {hasil2:.2f}%")
                st.write(f"Rata-rata Kadar = {rata:.2f}%")
                st.write(f"%RPD = {rpd:.2f}%")

        # =====================================
        # VALIDASI RPD
        # =====================================
        if "rpd" in locals():
            if rpd <= 10:
                st.success("✅ Presisi Memenuhi Syarat (RPD ≤ 10%)")
            else:
                st.error("❌ Presisi Tidak Memenuhi (RPD > 10%)")
