import streamlit as st

st.set_page_config(
    page_title="Titrimetri - LPK",
    page_icon="🧪",
    layout="wide"
)

# ─────────────────────────────────────────
# DATA
# ─────────────────────────────────────────
methods = [
    "Alkalimetri", "Asidimetri", "Permanganometri",
    "Iodometri", "Argentometri", "Kompleksometri"
]

baku_primer = {
    "Alkalimetri":     {"nama": "Asam Oksalat (H₂C₂O₄·2H₂O)", "be": 63.03},
    "Asidimetri":      {"nama": "Boraks (Na₂B₄O₇·10H₂O)",      "be": 190.69},
    "Permanganometri": {"nama": "Asam Oksalat (H₂C₂O₄·2H₂O)",  "be": 63.03},
    "Iodometri":       {"nama": "K₂Cr₂O₇",                      "be": 49.03},
    "Argentometri":    {"nama": "NaCl",                          "be": 58.44},
    "Kompleksometri":  {"nama": "CaCO₃",                         "be": 100.09},
}

# ─────────────────────────────────────────
# FUNGSI PERHITUNGAN
# ─────────────────────────────────────────
def hitung_rpd(h1, h2):
    rata = (h1 + h2) / 2
    if rata == 0:
        return 0.0
    return abs(h1 - h2) / rata * 100

def hitung_standarisasi(mg, v1, v2, be, fp):
    n1 = mg / (v1 * be * fp)
    n2 = mg / (v2 * be * fp)
    return n1, n2

def hitung_standarisasi_edta(mg, v1, v2, bm):
    m1 = mg / (v1 * bm * fp)
    m2 = mg / (v2 * bm * fp)
    return m1, m2

def hitung_kadar(v1, v2, nm, be, fp, s):
    k1 = ((v1 * nm * be * fp) * 1e-3 / s) * 100
    k2 = ((v2 * nm * be * fp) * 1e-3 / s) * 100
    return k1, k2

def hitung_kesadahan(v1, v2, m, bm, fp, s):
    p1 = (v1 * m * bm * fp * 1000) / s
    p2 = (v2 * m * bm * fp * 1000) / s
    return p1, p2

def status_presisi(rpd_val, batas):
    return rpd_val <= batas

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.title("🧪 Web Perhitungan Kadar dan Standarisasi Titrimetri")
st.caption("Laboratorium Kimia Analitik — Politeknik AKA Bogor")
st.divider()

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Pengaturan")
    st.divider()

    metode = st.selectbox("🔬 Pilih Metode", methods)

    bp = baku_primer[metode]
    st.info(f"🧴 **Baku Primer:** {bp['nama']}\n\n**BE/BM = {bp['be']}**")

    st.divider()

    if metode == "Kompleksometri":
        st.markdown("**📖 Rumus Standarisasi**")
        st.latex(r"M = \frac{mg}{V \times BM_{CaCO_3}}")
        st.markdown("**📖 Rumus Kesadahan**")
        st.latex(r"ppm = \frac{V \times M \times BM \times FP \times 1000}{V_{sampel}}")
    else:
        st.markdown("**📖 Rumus Standarisasi**")
        st.latex(r"N = \frac{mg}{V \times BE \times FP}")
        st.markdown("**📖 Rumus Penetapan Kadar**")
        st.latex(r"Kadar = \frac{V \times N \times BE \times FP \times 10^{-3}}{S} \times 100")

    st.divider()
    st.markdown("**📌 Keterangan**")
    st.markdown("""
| Simbol | Keterangan |
|--------|-----------|
| V | Volume titran (mL) |
| N/M | Normalitas / Molaritas |
| BE/BM | Berat Ekuivalen / BM |
| FP | Faktor Pengali |
| S | Massa / Volume Sampel |
| mg | Massa baku primer (mg) |
    """)

# ─────────────────────────────────────────
# BATAS RPD
# ─────────────────────────────────────────
col_rpd, col_info = st.columns([1, 2])
with col_rpd:
    batas_rpd = st.number_input(
        "📏 Batas RPD (%)",
        min_value=0.1, max_value=20.0,
        value=10.0, step=0.5
    )
with col_info:
    st.info(f"Metode aktif: **{metode}** | Baku Primer: **{baku_primer[metode]['nama']}**")

st.divider()

# ─────────────────────────────────────────
# TABS
# ─────────────────────────────────────────
tab1, tab2 = st.tabs(["🧪 Standarisasi", "📊 Penetapan Kadar"])

# ══════════════════════════════════════════
# TAB 1 — STANDARISASI
# ══════════════════════════════════════════
with tab1:
    st.subheader("Input Data Standarisasi")

    be_val = baku_primer[metode]["be"]
    bp_nama = baku_primer[metode]["nama"]

    st.info(f"🧴 Baku Primer: **{bp_nama}** | BE/BM = **{be_val}** (auto-terisi)")

    if metode == "Kompleksometri":
        col1, col2, col3 = st.columns(3)
        with col1:
            v1 = st.number_input("Volume EDTA 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
            v2 = st.number_input("Volume EDTA 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
        with col2:
            mg = st.number_input("Massa CaCO₃ (mg)", min_value=0.0, format="%.4f", key="s_mg")
            bm = st.number_input("BM CaCO₃ (g/mol)", min_value=0.0001,
                                  value=float(be_val), format="%.4f", key="s_bm")
        with col3:
            st.metric("Satuan Hasil", "Molaritas (M)")

        if st.button("🖩 Hitung Standarisasi", use_container_width=True):
            if v1 <= 0 or v2 <= 0 or mg <= 0:
                st.warning("⚠️ Isi semua field dengan nilai > 0!")
            else:
                m1, m2 = hitung_standarisasi_edta(mg, v1, v2, bm)
                rata   = (m1 + m2) / 2
                r      = hitung_rpd(m1, m2)
                presisi = status_presisi(r, batas_rpd)

                st.divider()
                st.subheader("Hasil Perhitungan")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("M EDTA 1", f"{m1:.4f} M")
                c2.metric("M EDTA 2", f"{m2:.4f} M")
                c3.metric("Rata-rata", f"{rata:.4f} M")
                c4.metric("%RPD", f"{r:.2f}%")

                if presisi:
                    st.success(f"✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)")
                else:
                    st.error(f"❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)")

    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            v1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
            v2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
        with col2:
            mg = st.number_input("Massa Baku Primer (mg)", min_value=0.0, format="%.4f", key="s_mg")
            be = st.number_input("BE / BM", min_value=0.0001,
                                  value=float(be_val), format="%.4f", key="s_be")
        with col3:
            fp = st.number_input("Faktor Pengali (FP)", min_value=0.0001,
                                  value=1.0, format="%.4f", key="s_fp")
            st.metric("Satuan Hasil", "Normalitas (N)")

        if st.button("🖩 Hitung Standarisasi", use_container_width=True):
            if v1 <= 0 or v2 <= 0 or mg <= 0:
                st.warning("⚠️ Isi semua field dengan nilai > 0!")
            else:
                n1, n2 = hitung_standarisasi(mg, v1, v2, be, fp)
                rata   = (n1 + n2) / 2
                r      = hitung_rpd(n1, n2)
                presisi = status_presisi(r, batas_rpd)

                st.divider()
                st.subheader("Hasil Perhitungan")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("N Titran 1", f"{n1:.4f} N")
                c2.metric("N Titran 2", f"{n2:.4f} N")
                c3.metric("Rata-rata",  f"{rata:.4f} N")
                c4.metric("%RPD",       f"{r:.2f}%")

                if presisi:
                    st.success(f"✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)")
                else:
                    st.error(f"❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)")

# ══════════════════════════════════════════
# TAB 2 — PENETAPAN KADAR
# ══════════════════════════════════════════
with tab2:
    st.subheader("Input Data Penetapan Kadar")

    be_val  = baku_primer[metode]["be"]
    bp_nama = baku_primer[metode]["nama"]

    if metode == "Kompleksometri":
        st.info(f"🧴 Baku Primer: **{bp_nama}** | BM = **{be_val}** | Hasil: **ppm CaCO₃**")

        col1, col2, col3 = st.columns(3)
        with col1:
            pv1 = st.number_input("Volume EDTA 1 / V1 (mL)", min_value=0.0, format="%.4f", key="k_v1")
            pv2 = st.number_input("Volume EDTA 2 / V2 (mL)", min_value=0.0, format="%.4f", key="k_v2")
        with col2:
            nm  = st.number_input("Molaritas EDTA (M)", min_value=0.0, format="%.4f", key="k_nm")
            pbe = st.number_input("BM CaCO₃ (g/mol)", min_value=0.0001,
                                   value=float(be_val), format="%.4f", key="k_be")
        with col3:
            pfp = st.number_input("Faktor Pengali (FP)", min_value=0.0001,
                                   value=1.0, format="%.4f", key="k_fp")
            s   = st.number_input("Volume Sampel (mL)", min_value=0.0001,
                                   value=1.0, format="%.4f", key="k_s")

        if st.button("🖩 Hitung Kesadahan", use_container_width=True):
            if pv1 <= 0 or pv2 <= 0 or nm <= 0:
                st.warning("⚠️ Isi semua field dengan nilai > 0!")
            else:
                h1, h2 = hitung_kesadahan(pv1, pv2, nm, pbe, pfp, s)
                rata   = (h1 + h2) / 2
                r      = hitung_rpd(h1, h2)
                presisi = status_presisi(r, batas_rpd)

                st.divider()
                st.subheader("Hasil Perhitungan")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Kesadahan 1", f"{h1:.2f} ppm")
                c2.metric("Kesadahan 2", f"{h2:.2f} ppm")
                c3.metric("Rata-rata",   f"{rata:.2f} ppm")
                c4.metric("%RPD",        f"{r:.2f}%")

                if presisi:
                    st.success(f"✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)")
                else:
                    st.error(f"❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)")

    else:
        st.info(f"🧴 Baku Primer: **{bp_nama}** | BE/BM = **{be_val}** | Hasil: **% b/v**")

        col1, col2, col3 = st.columns(3)
        with col1:
            pv1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="k_v1")
            pv2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="k_v2")
        with col2:
            nm  = st.number_input("Normalitas / Molaritas (N/M)", min_value=0.0, format="%.4f", key="k_nm")
            pbe = st.number_input("BE / BM Analit", min_value=0.0001,
                                   value=float(be_val), format="%.4f", key="k_be")
        with col3:
            pfp = st.number_input("Faktor Pengali (FP)", min_value=0.0001,
                                   value=1.0, format="%.4f", key="k_fp")
            s   = st.number_input("Massa / Volume Sampel (S)", min_value=0.0001,
                                   value=1.0, format="%.4f", key="k_s")

        if st.button("🖩 Hitung Kadar", use_container_width=True):
            if pv1 <= 0 or pv2 <= 0 or nm <= 0:
                st.warning("⚠️ Isi semua field dengan nilai > 0!")
            else:
                h1, h2 = hitung_kadar(pv1, pv2, nm, pbe, pfp, s)
                rata   = (h1 + h2) / 2
                r      = hitung_rpd(h1, h2)
                presisi = status_presisi(r, batas_rpd)

                st.divider()
                st.subheader("Hasil Perhitungan")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Kadar 1",   f"{h1:.4f} %")
                c2.metric("Kadar 2",   f"{h2:.4f} %")
                c3.metric("Rata-rata", f"{rata:.4f} %")
                c4.metric("%RPD",      f"{r:.2f}%")

                if presisi:
                    st.success(f"✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)")
                else:
                    st.error(f"❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)")

st.divider()
st.caption("© 2026 Web Perhitungan Titrimetri | Laboratorium Kimia Analitik — Politeknik AKA Bogor")
