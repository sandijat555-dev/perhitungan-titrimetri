import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Perhitungan Titrimetri",
    page_icon="🧪",
    layout="centered"
)

# =====================================
# JUDUL
# =====================================
st.title("🧪 Perhitungan Titrimetri")
st.write("Standarisasi dan Penetapan Kadar")

# =====================================
# GAMBAR HEADER
# =====================================
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/92/Titration_setup.svg",
    caption="Praktik Titrasi"
)

# =====================================
# GAMBAR ALAT LAB
# =====================================
st.header("Peralatan Titrasi")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2933/2933821.png",
        caption="Buret",
        width=120
    )

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2965/2965567.png",
        caption="Erlenmeyer",
        width=120
    )

with col3:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2784/2784487.png",
        caption="Pipet Volumetrik",
        width=120
    )

col4, col5 = st.columns(2)

with col4:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/619/619103.png",
        caption="Labu Takar",
        width=120
    )

with col5:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/706/706797.png",
        caption="Bulb",
        width=120
    )

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
            "Iodimetri",
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

    elif metode == "Iodimetri":
        st.info("Baku Primer : K2Cr2O7")

    elif metode == "Argentometri":
        st.info("Baku Primer : NaCl")

    elif metode == "Kompleksometri":
        st.info("Baku Primer : CaCO3")

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

# =====================================
# INPUT DATA
# =====================================
st.header("Input Data")

V1 = st.number_input(
    "Volume Titran 1 (mL)",
    min_value=0.0
)

V2 = st.number_input(
    "Volume Titran 2 (mL)",
    min_value=0.0
)

N = st.number_input(
    "Normalitas/Molaritas",
    min_value=0.0
)

BE = st.number_input(
    "BE/BM",
    min_value=0.0
)

FP = st.number_input(
    "Faktor Pengali",
    min_value=1.0,
    value=1.0
)

S = st.number_input(
    "Volume/Massa Sampel",
    min_value=0.0
)

# =====================================
# TOMBOL HITUNG
# =====================================
if st.button("Hitung"):

    if S == 0:
        st.error("Volume/Massa sampel tidak boleh 0")

    else:

        # =====================================
        # PENETAPAN KADAR
        # =====================================
        if jenis == "Penetapan Kadar":

            hasil1 = (
                V1 * N * BE * FP *
                (10**-3) * 100
            ) / S

            hasil2 = (
                V2 * N * BE * FP *
                (10**-3) * 100
            ) / S

            rata = (hasil1 + hasil2) / 2

            rpd = abs(hasil1 - hasil2) / rata * 100

            st.header("Hasil Perhitungan")

            st.success(f"Kadar 1 = {hasil1:.2f} %")
            st.success(f"Kadar 2 = {hasil2:.2f} %")

            st.write(f"Rata-rata = {rata:.2f} %")
            st.write(f"%RPD = {rpd:.2f} %")

        # =====================================
        # STANDARISASI
        # =====================================
        else:

            hasil1 = (
                S / (V1 * BE * FP)
            ) * 1000

            hasil2 = (
                S / (V2 * BE * FP)
            ) * 1000

            rata = (hasil1 + hasil2) / 2

            rpd = abs(hasil1 - hasil2) / rata * 100

            st.header("Hasil Standarisasi")

            st.success(f"Hasil 1 = {hasil1:.4f}")
            st.success(f"Hasil 2 = {hasil2:.4f}")

            st.write(f"Rata-rata = {rata:.4f}")
            st.write(f"%RPD = {rpd:.2f} %")

        # =====================================
        # VALIDASI RPD
        # =====================================
        if rpd <= 10:
            st.success("✅ Presisi Memenuhi Syarat")

        else:
            st.error("❌ Presisi Tidak Memenuhi")
