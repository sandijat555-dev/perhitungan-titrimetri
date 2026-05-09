import streamlit as st

# ===================================
# KONFIGURASI HALAMAN
# ===================================
st.set_page_config(
    page_title="Perhitungan Titrimetri",
    page_icon="🧪",
    layout="centered"
)

# ===================================
# JUDUL
# ===================================
st.title("🧪 Perhitungan Titrimetri")
st.write("Website Standarisasi dan Penetapan Kadar")

# ===================================
# SIDEBAR
# ===================================
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
            "Iodimetri",
            "Argentometri",
            "Kompleksometri"
        ]
    )

# ===================================
# INFORMASI METODE
# ===================================
st.header("Informasi Metode")

if jenis == "Standarisasi":

    if metode == "Alkalimetri":
        st.info("Baku Primer : Asam Oksalat")
        parameter = "Normalitas"

    elif metode == "Asidimetri":
        st.info("Baku Primer : Boraks")
        parameter = "Normalitas"

    elif metode == "Permanganometri":
        st.info("Baku Primer : Asam Oksalat")
        parameter = "Normalitas"

    elif metode == "Iodimetri":
        st.info("Baku Primer : K2Cr2O7")
        parameter = "Normalitas"

    elif metode == "Argentometri":
        st.info("Baku Primer : NaCl")
        parameter = "Normalitas"

    elif metode == "Kompleksometri":
        st.info("Baku Primer : CaCO3")
        parameter = "Molaritas"

else:

    if metode == "Alkalimetri":
        st.info("Kadar CH3COOH dalam cuka")

    elif metode == "Asidimetri":
        st.info("Kadar Na2CO3 dan NaOH metode Warder")

    elif metode == "Permanganometri":
        st.info("Kadar Fe")

    elif metode == "Iodimetri":
        st.info("Kadar Cl")

    elif metode == "Argentometri":
        st.info("Kadar Cl")

    elif metode == "Kompleksometri":
        st.info("Kesadahan air (CaCO3 dalam ppm)")

# ===================================
# INPUT DATA DUPLO
# ===================================
st.header("Input Data")

col1, col2 = st.columns(2)

# ===================================
# PERCOBAAN 1
# ===================================
with col1:

    st.subheader("Percobaan 1")

    V1 = st.number_input(
        "Volume Titran 1 (mL)",
        min_value=0.0,
        key="V1"
    )

    N1 = st.number_input(
        "Normalitas/Molaritas 1",
        min_value=0.0,
        key="N1"
    )

    BE1 = st.number_input(
        "BE/BM 1",
        min_value=0.0,
        key="BE1"
    )

    FP1 = st.number_input(
        "Faktor Pengali 1",
        min_value=1.0,
        value=1.0,
        key="FP1"
    )

    S1 = st.number_input(
        "Massa/Volume Sampel 1",
        min_value=0.0,
        key="S1"
    )

# ===================================
# PERCOBAAN 2
# ===================================
with col2:

    st.subheader("Percobaan 2")

    V2 = st.number_input(
        "Volume Titran 2 (mL)",
        min_value=0.0,
        key="V2"
    )

    N2 = st.number_input(
        "Normalitas/Molaritas 2",
        min_value=0.0,
        key="N2"
    )

    BE2 = st.number_input(
        "BE/BM 2",
        min_value=0.0,
        key="BE2"
    )

    FP2 = st.number_input(
        "Faktor Pengali 2",
        min_value=1.0,
        value=1.0,
        key="FP2"
    )

    S2 = st.number_input(
        "Massa/Volume Sampel 2",
        min_value=0.0,
        key="S2"
    )

# ===================================
# TOMBOL HITUNG
# ===================================
if st.button("Hitung"):

    # MENCEGAH PEMBAGIAN NOL
    if S1 == 0 or S2 == 0:
        st.error("Volume/Massa sampel tidak boleh 0")

    else:

        # ===================================
        # PENETAPAN KADAR
        # ===================================
        if jenis == "Penetapan Kadar":

            hasil1 = (
                V1 * N1 * BE1 * FP1 *
                (10**-3) * 100
            ) / S1

            hasil2 = (
                V2 * N2 * BE2 * FP2 *
                (10**-3) * 100
            ) / S2

            rata = (hasil1 + hasil2) / 2

            rpd = abs(hasil1 - hasil2) / rata * 100

            st.header("Hasil Perhitungan")

            st.success(f"Kadar 1 = {hasil1:.2f} %")
            st.success(f"Kadar 2 = {hasil2:.2f} %")

            st.write(f"Rata-rata = {rata:.2f} %")
            st.write(f"%RPD = {rpd:.2f} %")

        # ===================================
        # STANDARISASI
        # ===================================
        else:

            hasil1 = (
                S1 / (V1 * BE1 * FP1)
            ) * 1000

            hasil2 = (
                S2 / (V2 * BE2 * FP2)
            ) * 1000

            rata = (hasil1 + hasil2) / 2

            rpd = abs(hasil1 - hasil2) / rata * 100

            st.header("Hasil Standarisasi")

            st.success(f"Hasil 1 = {hasil1:.4f}")
            st.success(f"Hasil 2 = {hasil2:.4f}")

            st.write(f"Rata-rata = {rata:.4f}")
            st.write(f"%RPD = {rpd:.2f} %")

        # ===================================
        # VALIDASI RPD
        # ===================================
        if rpd <= 10:
            st.success("Presisi Memenuhi Syarat")

        else:
            st.error("Presisi Tidak Memenuhi")
