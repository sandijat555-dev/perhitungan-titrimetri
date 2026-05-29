import streamlit as st

st.set_page_config(page_title="Web Titrimetri", layout="wide", page_icon="🧪")

st.markdown("""
<style>
.main { background-color: #f4f6f8; }
[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #d4e6e3; }

.hero {
    background: linear-gradient(135deg, #b2ece8 0%, #80d8d4 30%, #4dc4c8 60%, #2aa8bb 100%);
    border-radius: 18px; margin-bottom: 24px; position: relative;
    overflow: hidden; display: flex; align-items: center;
    min-height: 180px; box-shadow: 0 6px 24px rgba(14,138,122,0.18);
}
.hero::before {
    content: ''; position: absolute; inset: 0;
    background: repeating-linear-gradient(45deg, transparent, transparent 20px,
        rgba(255,255,255,0.04) 20px, rgba(255,255,255,0.04) 40px);
}
.hero-side {
    width: 120px; min-width: 90px; display: flex; flex-direction: column;
    justify-content: center; align-items: center; gap: 8px;
    padding: 20px 10px; opacity: 0.5; z-index: 2;
}
.hero-side span { font-size: 2rem; display: block; }
.hero-side span:nth-child(2) { font-size: 1.5rem; }
.hero-side span:nth-child(3) { font-size: 1.8rem; }
.hero-center {
    flex: 1; padding: 28px 10px; position: relative; z-index: 2; text-align: center;
}
.hero-badge {
    background: rgba(255,255,255,0.3); border: 1.5px solid rgba(255,255,255,0.55);
    border-radius: 20px; padding: 3px 16px; font-size: 0.68rem; color: #1a2e44;
    font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
    margin-bottom: 10px; display: inline-block;
}
.hero h1 { color:#1a2e44; font-size:1.8rem; font-weight:900; margin:0; line-height:1.25; font-family:Georgia,serif; }
.hero .orange { color:#c96f00; font-size:1.8rem; font-weight:900; font-family:Georgia,serif; }
.hero .teal   { color:#054e44; font-size:1.8rem; font-weight:900; font-family:Georgia,serif; }
.hero-line { width:50px; height:3px; background:rgba(255,255,255,0.65); border-radius:2px; margin:10px auto 8px; }
.hero-sub { color:#1a2e44; opacity:0.6; font-size:0.75rem; letter-spacing:0.5px; }

.sidebar-label { font-size:0.68rem; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:#7a8fa6; margin-bottom:5px; margin-top:12px; }
.info-card { background:#e0f4f1; border-radius:10px; padding:11px 13px; margin-bottom:10px; font-size:0.8rem; color:#076b5e; border-left:4px solid #0e8a7a; }
.rumus-card { background:#fff6e5; border-radius:10px; padding:13px; margin-bottom:10px; }
.rumus-title { color:#f5a623; font-size:0.68rem; font-weight:800; text-transform:uppercase; letter-spacing:1px; margin-bottom:5px; }
.rumus-formula { background:white; border-radius:6px; padding:7px 10px; font-family:Georgia,serif; font-size:0.78rem; color:#1a2e44; text-align:center; line-height:1.6; margin-bottom:4px; }
.ket-card { background:#f4f6f8; border-radius:10px; padding:11px 13px; }
.sec-header { display:flex; align-items:center; gap:8px; padding-bottom:10px; border-bottom:2px solid #e0f4f1; margin-bottom:16px; }
.sec-header h3 { color:#1a2e44; font-weight:800; font-size:1rem; margin:0; }

.result-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:14px; }
.result-item { background:#f0faf8; border:1.5px solid #d4e6e3; border-radius:10px; padding:13px 8px; text-align:center; }
.rc-label { font-size:0.7rem; font-weight:700; color:#7a8fa6; margin-bottom:5px; }
.rc-val   { font-size:1.1rem; font-weight:800; color:#1a2e44; }
.rc-unit  { font-size:0.65rem; color:#7a8fa6; margin-top:2px; }

.status-ok  { background:#e8f8f0; color:#27ae60; border:1.5px solid #27ae60; border-radius:8px; padding:12px 16px; text-align:center; font-weight:700; font-size:.88rem; }
.status-err { background:#fdecea; color:#e74c3c; border:1.5px solid #e74c3c; border-radius:8px; padding:12px 16px; text-align:center; font-weight:700; font-size:.88rem; }

div.stButton > button {
    background:#0e8a7a !important; color:white !important; border:none !important;
    border-radius:10px !important; font-weight:800 !important; font-size:1rem !important;
    padding:14px !important; width:100% !important; letter-spacing:1px !important;
}
div.stButton > button:hover { background:#076b5e !important; }
.footer { text-align:center; color:#7a8fa6; font-size:.75rem; padding:16px; border-top:1px solid #d4e6e3; margin-top:20px; }
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
methods = ["Alkalimetri","Asidimetri","Permanganometri","Iodometri","Argentometri","Kompleksometri"]

baku_primer = {
    "Alkalimetri":      "Asam Oksalat (H₂C₂O₄·2H₂O) / Asam Benzoat",
    "Asidimetri":       "Na₂CO₃ / Boraks (Na₂B₄O₇·10H₂O)",
    "Permanganometri":  "As₂O₃ / Asam Oksalat",
    "Iodometri":        "K₂Cr₂O₇ / As₂O₃",
    "Argentometri":     "NaCl / KCl (Metode Mohr / Volhard)",
    "Kompleksometri":   "CaCO₃ (BM = 100,09 g/mol)",
}

def rpd(h1, h2):
    avg = (h1 + h2) / 2
    return 0 if avg == 0 else abs(h1 - h2) / avg * 100

# ---------- HERO ----------
st.markdown("""
<div class="hero">

    
    <div class="hero-side">

        
        <svg width="72" height="130" viewBox="0 0 72 130" fill="none" xmlns="http://www.w3.org/2000/svg">
            
            <rect x="8" y="120" width="40" height="7" rx="3" fill="white" fill-opacity="0.55"/>
            
            <rect x="14" y="20" width="5" height="103" rx="2" fill="white" fill-opacity="0.45"/>
            
            <rect x="14" y="28" width="18" height="4" rx="2" fill="white" fill-opacity="0.5"/>
            
            <rect x="29" y="10" width="10" height="5" rx="2" fill="white" fill-opacity="0.75"/>
            <rect x="31" y="15" width="6" height="58" rx="2" fill="white" fill-opacity="0.6"/>
            
            <rect x="32" y="16" width="4" height="35" rx="1" fill="#38bdf8" fill-opacity="0.5"/>
            
            <rect x="27" y="58" width="14" height="5" rx="2" fill="#065f52" fill-opacity="0.75"/>
            <rect x="39" y="59" width="9" height="3" rx="1.5" fill="#054e44" fill-opacity="0.8"/>
            
            <path d="M33 73 L31 88 L33 95 L35 95 L37 88 L35 73 Z" fill="white" fill-opacity="0.55"/>
            
            <ellipse cx="34" cy="100" rx="2.5" ry="3.5" fill="#38bdf8" fill-opacity="0.7"/>
        </svg>

        
        <svg width="28" height="110" viewBox="0 0 28 110" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-left:-10px; margin-top:10px">
            
            <ellipse cx="14" cy="18" rx="10" ry="14" fill="white" fill-opacity="0.45"/>
            
            <rect x="11" y="30" width="6" height="55" rx="2" fill="white" fill-opacity="0.5"/>
            
            <rect x="12" y="38" width="4" height="30" rx="1" fill="#0ea5e9" fill-opacity="0.4"/>
            
            <path d="M12 85 L11 95 L13.5 103 L14.5 103 L17 95 L16 85 Z" fill="white" fill-opacity="0.5"/>
        </svg>

    </div>

    
    <div class="hero-center">
        <div class="hero-badge">⚗️ Laboratorium Kimia Analitik</div>
        <h1>Web Perhitungan</h1>
        <p class="orange">Kadar dan Standarisasi</p>
        <p class="teal">✦ Titrimetri ✦</p>
        <div class="hero-line"></div>
        <p class="hero-sub">Standarisasi &nbsp;•&nbsp; Penetapan Kadar &nbsp;•&nbsp; RPD Otomatis &nbsp;•&nbsp; 6 Metode</p>
    </div>

    
    <div class="hero-side">

        
        <svg width="80" height="110" viewBox="0 0 80 110" fill="none" xmlns="http://www.w3.org/2000/svg">
            
            <rect x="30" y="4" width="20" height="5" rx="2.5" fill="white" fill-opacity="0.65"/>
            <rect x="33" y="9" width="14" height="22" rx="2" fill="white" fill-opacity="0.55"/>
            
            <path d="M33 31 L8 78 Q5 90 40 90 Q75 90 72 78 L47 31 Z" fill="white" fill-opacity="0.3"/>
            
            <path d="M34 50 L12 78 Q10 87 40 87 Q70 87 68 78 L46 50 Z" fill="#f9a8d4" fill-opacity="0.5"/>
            
            <path d="M33 31 L30 45 L35 48 L38 32 Z" fill="white" fill-opacity="0.2"/>
            
            <ellipse cx="40" cy="88" rx="28" ry="5" fill="white" fill-opacity="0.15"/>
            
            <line x1="25" y1="65" x2="30" y2="65" stroke="white" stroke-opacity="0.4" stroke-width="1.5"/>
            <line x1="22" y1="74" x2="28" y2="74" stroke="white" stroke-opacity="0.4" stroke-width="1.5"/>
        </svg>

        
        <svg width="55" height="100" viewBox="0 0 55 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-top:6px">
            
            <rect x="21" y="1" width="13" height="7" rx="3" fill="white" fill-opacity="0.6"/>
            
            <rect x="23" y="8" width="9" height="28" rx="2" fill="white" fill-opacity="0.5"/>
            
            <ellipse cx="27.5" cy="72" rx="24" ry="24" fill="white" fill-opacity="0.28"/>
            
            <path d="M6 78 Q5 94 27.5 95 Q50 94 49 78 Z" fill="#6ee7b7" fill-opacity="0.45"/>
            
            <line x1="18" y1="50" x2="25" y2="50" stroke="white" stroke-opacity="0.5" stroke-width="1.5"/>
            
            <rect x="24" y="32" width="7" height="8" rx="1" fill="#6ee7b7" fill-opacity="0.35"/>
        </svg>

    </div>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-label">Pilih Metode</div>', unsafe_allow_html=True)
    metode = st.selectbox("", methods, label_visibility="collapsed")

    st.markdown(f'<div class="info-card"><strong>ℹ️ Baku Primer:</strong><br>{baku_primer[metode]}</div>', unsafe_allow_html=True)

    # Rumus dinamis berdasarkan metode
    if metode == "Kompleksometri":
        st.markdown("""
        <div class="rumus-card">
            <div class="rumus-title">📖 Standarisasi (Molaritas)</div>
            <div class="rumus-formula">M = mg / (V × BM CaCO₃)</div>
            <div class="rumus-title" style="margin-top:10px">📖 Penetapan Kesadahan</div>
            <div class="rumus-formula">ppm = (V EDTA × M EDTA × BM CaCO₃ × FP × 1000) / V sampel</div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="rumus-card">
            <div class="rumus-title">📖 Standarisasi</div>
            <div class="rumus-formula">N = mg / (V × BE × FP)</div>
            <div class="rumus-title" style="margin-top:10px">📖 Penetapan Kadar</div>
            <div class="rumus-formula">Kadar = (V × N × BE × FP × 10⁻³ / S) × 100</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="ket-card">
        <strong>📌 Keterangan</strong><br><br>
        <span style="color:#0e8a7a;font-weight:700">V</span> = Volume titran (mL)<br>
        <span style="color:#0e8a7a;font-weight:700">N/M</span> = Normalitas / Molaritas<br>
        <span style="color:#0e8a7a;font-weight:700">BE/BM</span> = Berat Ekuivalen / BM<br>
        <span style="color:#0e8a7a;font-weight:700">FP</span> = Faktor Pengali<br>
        <span style="color:#0e8a7a;font-weight:700">S</span> = Massa / Volume Sampel<br>
        <span style="color:#0e8a7a;font-weight:700">mg</span> = Massa baku primer (mg)
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label" style="margin-top:16px">Batas RPD (%)</div>', unsafe_allow_html=True)
    batas_rpd = st.number_input("", min_value=0.1, max_value=20.0, value=10.0, step=0.5, label_visibility="collapsed")

# ---------- TABS ----------
tab1, tab2 = st.tabs(["🧪 Standarisasi", "📊 Penetapan Kadar"])

# ===== TAB 1 : STANDARISASI =====
with tab1:
    st.markdown('<div class="sec-header"><span style="font-size:18px">🧪</span><h3>INPUT DATA — Standarisasi</h3></div>', unsafe_allow_html=True)

    if metode == "Kompleksometri":
        # Standarisasi EDTA berbasis Molaritas
        st.info("ℹ️ Kompleksometri: Standarisasi menggunakan **Molaritas (M)** dengan baku primer **CaCO₃**")
        c1, c2, c3 = st.columns(3)
        with c1:
            v1 = st.number_input("Volume EDTA 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
            v2 = st.number_input("Volume EDTA 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
        with c2:
            mg = st.number_input("Massa CaCO₃ (mg)", min_value=0.0, format="%.4f", key="s_mg")
            bm = st.number_input("BM CaCO₃ (g/mol)", min_value=0.0001, value=100.09, format="%.4f", key="s_be")
        with c3:
            st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🖩  HITUNG STANDARISASI"):
            if v1 <= 0 or v2 <= 0 or mg <= 0:
                st.warning("⚠️ Harap isi semua field dengan nilai yang valid!")
            else:
                # M = mg / (V_mL * BM) → mmol/mL = M
                m1 = mg / (v1 * bm)
                m2 = mg / (v2 * bm)
                avg = (m1 + m2) / 2
                r   = rpd(m1, m2)

                st.markdown('<div class="sec-header" style="margin-top:20px"><span style="font-size:18px">📊</span><h3>HASIL PERHITUNGAN</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="result-grid">
                    <div class="result-item"><div class="rc-label">M EDTA 1</div><div class="rc-val">{m1:.4f}</div><div class="rc-unit">M</div></div>
                    <div class="result-item"><div class="rc-label">M EDTA 2</div><div class="rc-val">{m2:.4f}</div><div class="rc-unit">M</div></div>
                    <div class="result-item"><div class="rc-label">Rata-rata</div><div class="rc-val">{avg:.4f}</div><div class="rc-unit">M</div></div>
                    <div class="result-item"><div class="rc-label">%RPD</div><div class="rc-val">{r:.2f}</div><div class="rc-unit">%</div></div>
                </div>""", unsafe_allow_html=True)
                if r <= batas_rpd:
                    st.markdown(f'<div class="status-ok">✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-err">❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)</div>', unsafe_allow_html=True)
    else:
        # Standarisasi normal (Normalitas)
        c1, c2, c3 = st.columns(3)
        with c1:
            v1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
            v2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
        with c2:
            mg = st.number_input("Massa Baku Primer (mg)", min_value=0.0, format="%.4f", key="s_mg")
            be = st.number_input("BE / BM Baku Primer", min_value=0.0001, value=1.0, format="%.4f", key="s_be")
        with c3:
            fp = st.number_input("Faktor Pengali (FP)", min_value=0.0001, value=1.0, format="%.4f", key="s_fp")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🖩  HITUNG STANDARISASI"):
            if v1 <= 0 or v2 <= 0 or mg <= 0:
                st.warning("⚠️ Harap isi semua field dengan nilai yang valid!")
            else:
                n1  = mg / (v1 * be * fp)
                n2  = mg / (v2 * be * fp)
                avg = (n1 + n2) / 2
                r   = rpd(n1, n2)

                st.markdown('<div class="sec-header" style="margin-top:20px"><span style="font-size:18px">📊</span><h3>HASIL PERHITUNGAN</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="result-grid">
                    <div class="result-item"><div class="rc-label">N Titran 1</div><div class="rc-val">{n1:.4f}</div><div class="rc-unit">N</div></div>
                    <div class="result-item"><div class="rc-label">N Titran 2</div><div class="rc-val">{n2:.4f}</div><div class="rc-unit">N</div></div>
                    <div class="result-item"><div class="rc-label">Rata-rata</div><div class="rc-val">{avg:.4f}</div><div class="rc-unit">N</div></div>
                    <div class="result-item"><div class="rc-label">%RPD</div><div class="rc-val">{r:.2f}</div><div class="rc-unit">%</div></div>
                </div>""", unsafe_allow_html=True)
                if r <= batas_rpd:
                    st.markdown(f'<div class="status-ok">✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-err">❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)</div>', unsafe_allow_html=True)

# ===== TAB 2 : PENETAPAN KADAR =====
with tab2:
    st.markdown('<div class="sec-header"><span style="font-size:18px">📊</span><h3>INPUT DATA — Penetapan Kadar</h3></div>', unsafe_allow_html=True)

    if metode == "Kompleksometri":
        st.info("ℹ️ Kompleksometri: Penetapan **Kesadahan** — hasil dalam **ppm CaCO₃**")
        c1, c2, c3 = st.columns(3)
        with c1:
            pv1 = st.number_input("Volume EDTA 1 / V1 (mL)", min_value=0.0, format="%.4f", key="k_v1")
            pv2 = st.number_input("Volume EDTA 2 / V2 (mL)", min_value=0.0, format="%.4f", key="k_v2")
        with c2:
            nm  = st.number_input("Molaritas EDTA (M)", min_value=0.0, format="%.4f", key="k_nm")
            pbe = st.number_input("BM CaCO₃ (g/mol)", min_value=0.0001, value=100.09, format="%.4f", key="k_be")
        with c3:
            pfp = st.number_input("Faktor Pengali (FP)", min_value=0.0001, value=1.0, format="%.4f", key="k_fp")
            s   = st.number_input("Volume Sampel / V sampel (mL)", min_value=0.0001, value=1.0, format="%.4f", key="k_s")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🖩  HITUNG KESADAHAN"):
            if pv1 <= 0 or pv2 <= 0 or nm <= 0:
                st.warning("⚠️ Harap isi semua field dengan nilai yang valid!")
            else:
                h1  = (pv1 * nm * pbe * pfp * 1000) / s
                h2  = (pv2 * nm * pbe * pfp * 1000) / s
                avg = (h1 + h2) / 2
                r   = rpd(h1, h2)

                st.markdown('<div class="sec-header" style="margin-top:20px"><span style="font-size:18px">📊</span><h3>HASIL PERHITUNGAN</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="result-grid">
                    <div class="result-item"><div class="rc-label">Kesadahan 1</div><div class="rc-val">{h1:.2f}</div><div class="rc-unit">ppm CaCO₃</div></div>
                    <div class="result-item"><div class="rc-label">Kesadahan 2</div><div class="rc-val">{h2:.2f}</div><div class="rc-unit">ppm CaCO₃</div></div>
                    <div class="result-item"><div class="rc-label">Rata-rata</div><div class="rc-val">{avg:.2f}</div><div class="rc-unit">ppm CaCO₃</div></div>
                    <div class="result-item"><div class="rc-label">%RPD</div><div class="rc-val">{r:.2f}</div><div class="rc-unit">%</div></div>
                </div>""", unsafe_allow_html=True)
                if r <= batas_rpd:
                    st.markdown(f'<div class="status-ok">✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-err">❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)</div>', unsafe_allow_html=True)
    else:
        c1, c2, c3 = st.columns(3)
        with c1:
            pv1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="k_v1")
            pv2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="k_v2")
        with c2:
            nm  = st.number_input("Normalitas / Molaritas (N/M)", min_value=0.0, format="%.4f", key="k_nm")
            pbe = st.number_input("BE / BM Analit", min_value=0.0001, value=1.0, format="%.4f", key="k_be")
        with c3:
            pfp = st.number_input("Faktor Pengali (FP)", min_value=0.0001, value=1.0, format="%.4f", key="k_fp")
            s   = st.number_input("Massa / Volume Sampel (S)", min_value=0.0001, value=1.0, format="%.4f", key="k_s")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🖩  HITUNG KADAR"):
            if pv1 <= 0 or pv2 <= 0 or nm <= 0:
                st.warning("⚠️ Harap isi semua field dengan nilai yang valid!")
            else:
                h1  = ((pv1 * nm * pbe * pfp) * 1e-3 / s) * 100
                h2  = ((pv2 * nm * pbe * pfp) * 1e-3 / s) * 100
                avg = (h1 + h2) / 2
                r   = rpd(h1, h2)

                st.markdown('<div class="sec-header" style="margin-top:20px"><span style="font-size:18px">📊</span><h3>HASIL PERHITUNGAN</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="result-grid">
                    <div class="result-item"><div class="rc-label">Kadar 1</div><div class="rc-val">{h1:.4f}</div><div class="rc-unit">% b/v</div></div>
                    <div class="result-item"><div class="rc-label">Kadar 2</div><div class="rc-val">{h2:.4f}</div><div class="rc-unit">% b/v</div></div>
                    <div class="result-item"><div class="rc-label">Rata-rata</div><div class="rc-val">{avg:.4f}</div><div class="rc-unit">% b/v</div></div>
                    <div class="result-item"><div class="rc-label">%RPD</div><div class="rc-val">{r:.2f}</div><div class="rc-unit">%</div></div>
                </div>""", unsafe_allow_html=True)
                if r <= batas_rpd:
                    st.markdown(f'<div class="status-ok">✅ PRESISI — %RPD = {r:.2f}% (≤ {batas_rpd}%)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-err">❌ TIDAK PRESISI — %RPD = {r:.2f}% (> {batas_rpd}%)</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    © 2024 Web Perhitungan Titrimetri | Dibuat untuk Laboratorium Kimia Analitik — Politeknik AKA Bogor
</div>
""", unsafe_allow_html=True)
