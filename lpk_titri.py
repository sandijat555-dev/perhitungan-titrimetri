 import streamlit as st

st.set_page_config(page_title="Web Titrimetri", layout="wide", page_icon="🧪")

# ---------- STYLE ----------
st.markdown("""
<style>
/* General */
.main { background-color: #f4f6f8; }
[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #d4e6e3; }

/* Hero Banner */
.hero {
    background: linear-gradient(135deg, #a8e6df 0%, #7dcecb 40%, #5bb8c4 70%, #3fa0b5 100%);
    padding: 36px 20px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}
.hero h1 {
    color: #1a2e44;
    font-size: 1.9rem;
    font-weight: 900;
    margin: 0 0 4px 0;
    line-height: 1.3;
}
.hero .sub1 { color: #f5a623; font-size: 1.9rem; font-weight: 900; margin: 0; }
.hero .sub2 { color: #076b5e; font-size: 1.9rem; font-weight: 900; margin: 0; }
.hero p { color: #1a2e44; opacity: 0.7; margin-top: 8px; font-size: 0.9rem; }
.hero-icons { font-size: 2rem; opacity: 0.3; letter-spacing: 12px; margin-bottom: 8px; }

/* Cards */
.info-card {
    background: #e0f4f1;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 12px;
    font-size: 0.82rem;
    color: #076b5e;
    border-left: 4px solid #0e8a7a;
}
.rumus-card {
    background: #fff6e5;
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 12px;
}
.rumus-title {
    color: #f5a623;
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}
.rumus-formula {
    background: white;
    border-radius: 6px;
    padding: 8px 10px;
    font-family: Georgia, serif;
    font-size: 0.82rem;
    color: #1a2e44;
    text-align: center;
    line-height: 1.6;
    margin-bottom: 4px;
}
.ket-card {
    background: #f4f6f8;
    border-radius: 10px;
    padding: 12px 14px;
    font-size: 0.8rem;
}

/* Section Header */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 10px;
    border-bottom: 2px solid #e0f4f1;
    margin-bottom: 16px;
}
.section-header h3 {
    color: #1a2e44;
    font-weight: 800;
    font-size: 1rem;
    margin: 0;
}

/* Sub title */
.sub-title {
    color: #0e8a7a;
    font-size: 0.78rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

/* Result box */
.result-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 14px;
}
.result-item {
    background: #f0faf8;
    border: 1.5px solid #d4e6e3;
    border-radius: 10px;
    padding: 14px 10px;
    text-align: center;
}
.result-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: #7a8fa6;
    margin-bottom: 6px;
}
.result-value {
    font-size: 1.1rem;
    font-weight: 800;
    color: #1a2e44;
}
.result-unit {
    font-size: 0.68rem;
    color: #7a8fa6;
    margin-top: 2px;
}

/* Status */
.status-presisi {
    background: #e8f8f0;
    color: #27ae60;
    border: 1.5px solid #27ae60;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
    font-weight: 700;
    font-size: 0.9rem;
}
.status-gagal {
    background: #fdecea;
    color: #e74c3c;
    border: 1.5px solid #e74c3c;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
    font-weight: 700;
    font-size: 0.9rem;
}

/* Hitung button */
div.stButton > button {
    background: #0e8a7a !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    padding: 14px !important;
    width: 100% !important;
    letter-spacing: 1px !important;
    transition: background 0.2s !important;
}
div.stButton > button:hover {
    background: #076b5e !important;
}

/* Sidebar labels */
.sidebar-label {
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #7a8fa6;
    margin-bottom: 6px;
    margin-top: 14px;
}

/* Footer */
.footer {
    text-align: center;
    color: #7a8fa6;
    font-size: 0.78rem;
    padding: 16px;
    border-top: 1px solid #d4e6e3;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
methods = ["Alkalimetri", "Asidimetri", "Permanganometri", "Iodometri", "Argentometri", "Kompleksometri"]

baku_primer = {
    "Alkalimetri": "Asam Oksalat (H₂C₂O₄·2H₂O) / Asam Benzoat",
    "Asidimetri": "Na₂CO₃ / Boraks (Na₂B₄O₇·10H₂O)",
    "Permanganometri": "As₂O₃ / Asam Oksalat",
    "Iodometri": "K₂Cr₂O₇ / As₂O₃",
    "Argentometri": "NaCl / KCl (Metode Mohr/Volhard)",
    "Kompleksometri": "CaCO₃ / ZnO",
}

def rpd(h1, h2):
    avg = (h1 + h2) / 2
    return 0 if avg == 0 else abs(h1 - h2) / avg * 100

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="hero-icons">🧪 ⚗️ 🔬</div>
    <h1>Web Perhitungan</h1>
    <p class="sub1">Kadar dan Standarisasi</p>
    <p class="sub2">✦ Titrimetri ✦</p>
    <p>Standarisasi • Penetapan Kadar • RPD Otomatis • 6 Metode Titrimetri</p>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-label">Pilih Metode</div>', unsafe_allow_html=True)
    metode = st.selectbox("", methods, label_visibility="collapsed")

    st.markdown(f"""
    <div class="info-card">
        <strong>ℹ️ Baku Primer:</strong><br>{baku_primer[metode]}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="rumus-card">
        <div class="rumus-title">📖 Standarisasi</div>
        <div class="rumus-formula">N = mg / (V × BE × FP)</div>
        <div class="rumus-title" style="margin-top:10px">📖 Penetapan Kadar</div>
        <div class="rumus-formula">Kadar = (V × N × BE × FP × 10⁻³ / S) × 100</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ket-card">
        <strong>📌 Keterangan</strong><br><br>
        <span style="color:#0e8a7a;font-weight:700">V</span> = Volume titran (mL)<br>
        <span style="color:#0e8a7a;font-weight:700">N</span> = Normalitas / Molaritas<br>
        <span style="color:#0e8a7a;font-weight:700">BE</span> = Berat Ekuivalen / BM<br>
        <span style="color:#0e8a7a;font-weight:700">FP</span> = Faktor Pengali<br>
        <span style="color:#0e8a7a;font-weight:700">S</span> = Massa / Volume Sampel<br>
        <span style="color:#0e8a7a;font-weight:700">mg</span> = Massa baku primer (mg)
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label" style="margin-top:16px">Info Presisi</div>', unsafe_allow_html=True)
    batas_rpd = st.number_input("Batas RPD (%)", min_value=0.1, max_value=20.0, value=10.0, step=0.5)

# ---------- TABS ----------
tab1, tab2 = st.tabs(["🧪 Standarisasi", "📊 Penetapan Kadar"])

# ===== TAB 1 : STANDARISASI =====
with tab1:
    st.markdown("""
    <div class="section-header">
        <span style="font-size:20px">🧪</span>
        <h3>INPUT DATA — Standarisasi</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        v1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
        v2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
    with col2:
        mg = st.number_input("Massa Baku Primer (mg)", min_value=0.0, format="%.4f", key="s_mg")
        be = st.number_input("BE / BM Baku Primer", min_value=0.0001, value=1.0, format="%.4f", key="s_be")
    with col3:
        fp = st.number_input("Faktor Pengali (FP)", min_value=0.0001, value=1.0, format="%.4f", key="s_fp")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🖩 HITUNG STANDARISASI"):
        if v1 <= 0 or v2 <= 0 or mg <= 0:
            st.warning("⚠️ Harap isi semua field dengan nilai yang valid!")
        else:
            n1 = mg / (v1 * be * fp)
            n2 = mg / (v2 * be * fp)
            avg = (n1 + n2) / 2
            hasil_rpd = rpd(n1, n2)

            st.markdown("""
            <div class="section-header" style="margin-top:20px">
                <span style="font-size:20px">📊</span>
                <h3>HASIL PERHITUNGAN</h3>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="result-grid">
                <div class="result-item">
                    <div class="result-label">N Titran 1</div>
                    <div class="result-value">{n1:.4f}</div>
                    <div class="result-unit">N</div>
                </div>
                <div class="result-item">
                    <div class="result-label">N Titran 2</div>
                    <div class="result-value">{n2:.4f}</div>
                    <div class="result-unit">N</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Rata-rata</div>
                    <div class="result-value">{avg:.4f}</div>
                    <div class="result-unit">N</div>
                </div>
                <div class="result-item">
                    <div class="result-label">%RPD</div>
                    <div class="result-value">{hasil_rpd:.2f}</div>
                    <div class="result-unit">%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if hasil_rpd <= batas_rpd:
                st.markdown(f'<div class="status-presisi">✅ PRESISI — %RPD = {hasil_rpd:.2f}% (≤ {batas_rpd}%)</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="status-gagal">❌ TIDAK PRESISI — %RPD = {hasil_rpd:.2f}% (> {batas_rpd}%)</div>', unsafe_allow_html=True)

# ===== TAB 2 : PENETAPAN KADAR =====
with tab2:
    st.markdown("""
    <div class="section-header">
        <span style="font-size:20px">📊</span>
        <h3>INPUT DATA — Penetapan Kadar</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        pv1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="k_v1")
        pv2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="k_v2")
    with col2:
        normalitas = st.number_input("Normalitas / Molaritas (N/M)", min_value=0.0, format="%.4f", key="k_nm")
        pbe = st.number_input("BE / BM Analit", min_value=0.0001, value=1.0, format="%.4f", key="k_be")
    with col3:
        pfp = st.number_input("Faktor Pengali (FP)", min_value=0.0001, value=1.0, format="%.4f", key="k_fp")
        sampel = st.number_input("Massa / Volume Sampel (S)", min_value=0.0001, value=1.0, format="%.4f", key="k_s")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🖩 HITUNG KADAR"):
        if pv1 <= 0 or pv2 <= 0 or normalitas <= 0:
            st.warning("⚠️ Harap isi semua field dengan nilai yang valid!")
        else:
            if metode == "Kompleksometri":
                h1 = (pv1 * normalitas * pbe * 1000) / sampel
                h2 = (pv2 * normalitas * pbe * 1000) / sampel
                unit = "ppm"
            else:
                h1 = ((pv1 * normalitas * pbe * pfp) * 1e-3 / sampel) * 100
                h2 = ((pv2 * normalitas * pbe * pfp) * 1e-3 / sampel) * 100
                unit = "% b/v"

            avg = (h1 + h2) / 2
            hasil_rpd = rpd(h1, h2)

            st.markdown("""
            <div class="section-header" style="margin-top:20px">
                <span style="font-size:20px">📊</span>
                <h3>HASIL PERHITUNGAN</h3>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="result-grid">
                <div class="result-item">
                    <div class="result-label">Kadar 1</div>
                    <div class="result-value">{h1:.4f}</div>
                    <div class="result-unit">{unit}</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Kadar 2</div>
                    <div class="result-value">{h2:.4f}</div>
                    <div class="result-unit">{unit}</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Rata-rata</div>
                    <div class="result-value">{avg:.4f}</div>
                    <div class="result-unit">{unit}</div>
                </div>
                <div class="result-item">
                    <div class="result-label">%RPD</div>
                    <div class="result-value">{hasil_rpd:.2f}</div>
                    <div class="result-unit">%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if hasil_rpd <= batas_rpd:
                st.markdown(f'<div class="status-presisi">✅ PRESISI — %RPD = {hasil_rpd:.2f}% (≤ {batas_rpd}%)</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="status-gagal">❌ TIDAK PRESISI — %RPD = {hasil_rpd:.2f}% (> {batas_rpd}%)</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    © 2024 Web Perhitungan Titrimetri | Dibuat untuk Laboratorium Kimia Analitik — Politeknik AKA Bogor
</div>
""", unsafe_allow_html=True)
