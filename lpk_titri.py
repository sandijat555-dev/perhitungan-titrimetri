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

# HDPE bottle icon SVG
hdpe_icon = (
    '{hdpe_icon}'
)

# Baku primer: nama dan nilai BE/BM
baku_primer = {
    "Alkalimetri":     {"nama": "Asam Oksalat (H₂C₂O₄·2H₂O)", "be": 63.03},
    "Asidimetri":      {"nama": "Boraks (Na₂B₄O₇·10H₂O)",      "be": 190.69},
    "Permanganometri": {"nama": "Asam Oksalat (H₂C₂O₄·2H₂O)",  "be": 63.03},
    "Iodometri":       {"nama": "K₂Cr₂O₇",                      "be": 49.03},
    "Argentometri":    {"nama": "NaCl",                          "be": 58.44},
    "Kompleksometri":  {"nama": "CaCO₃",                         "be": 100.09},
}

def rpd(h1, h2):
    avg = (h1 + h2) / 2
    return 0 if avg == 0 else abs(h1 - h2) / avg * 100

# ---------- HERO ----------
import streamlit.components.v1 as components
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: transparent; }
  .hero {
    background: linear-gradient(135deg, #b2ece8 0%, #80d8d4 30%, #4dc4c8 60%, #2aa8bb 100%);
    border-radius: 18px;
    display: flex;
    align-items: center;
    min-height: 185px;
    box-shadow: 0 6px 24px rgba(14,138,122,0.18);
    overflow: hidden;
    position: relative;
    font-family: Georgia, serif;
  }
  .hero::before {
    content: '';
    position: absolute; inset: 0;
    background: repeating-linear-gradient(45deg, transparent, transparent 20px, rgba(255,255,255,0.04) 20px, rgba(255,255,255,0.04) 40px);
  }
  .side {
    width: 130px; min-width: 100px;
    display: flex; align-items: center; justify-content: center;
    gap: 10px; padding: 16px 10px;
    z-index: 2; opacity: 0.75;
  }
  .center {
    flex: 1; text-align: center; padding: 24px 10px; z-index: 2;
  }
  .badge {
    display: inline-block;
    background: rgba(255,255,255,0.3);
    border: 1.5px solid rgba(255,255,255,0.6);
    border-radius: 20px; padding: 3px 16px;
    font-size: 11px; color: #1a2e44; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    margin-bottom: 10px; font-family: sans-serif;
  }
  h1 { color: #1a2e44; font-size: 28px; font-weight: 900; margin: 0; }
  .orange { color: #c96f00; font-size: 28px; font-weight: 900; margin: 2px 0; }
  .teal   { color: #054e44; font-size: 28px; font-weight: 900; margin: 2px 0; }
  .line { width: 50px; height: 3px; background: rgba(255,255,255,0.65); border-radius: 2px; margin: 10px auto 8px; }
  .sub { color: #1a2e44; opacity: 0.6; font-size: 12px; font-family: sans-serif; }
</style>
</head>
<body>
<div class="hero">

  <div class="side">
    <svg width="52" height="130" viewBox="0 0 52 130">
      <rect x="4" y="118" width="36" height="7" rx="3" fill="white" fill-opacity="0.6"/>
      <rect x="8" y="18" width="5" height="103" rx="2" fill="white" fill-opacity="0.5"/>
      <rect x="8" y="26" width="18" height="4" rx="2" fill="white" fill-opacity="0.55"/>
      <rect x="22" y="8" width="10" height="5" rx="2" fill="white" fill-opacity="0.8"/>
      <rect x="24" y="13" width="6" height="58" rx="2" fill="white" fill-opacity="0.65"/>
      <rect x="25" y="14" width="4" height="30" rx="1" fill="#38bdf8" fill-opacity="0.55"/>
      <rect x="20" y="56" width="14" height="5" rx="2" fill="#065f52" fill-opacity="0.8"/>
      <rect x="32" y="57" width="9" height="3" rx="1.5" fill="#054e44" fill-opacity="0.85"/>
      <path d="M26 71 L24 86 L26 93 L28 93 L30 86 L28 71 Z" fill="white" fill-opacity="0.6"/>
      <ellipse cx="27" cy="98" rx="2.5" ry="3.5" fill="#38bdf8" fill-opacity="0.8"/>
    </svg>
    <svg width="30" height="105" viewBox="0 0 30 105">
      <ellipse cx="15" cy="17" rx="10" ry="13" fill="white" fill-opacity="0.5"/>
      <rect x="12" y="28" width="6" height="50" rx="2" fill="white" fill-opacity="0.55"/>
      <rect x="13" y="35" width="4" height="28" rx="1" fill="#0ea5e9" fill-opacity="0.45"/>
      <path d="M13 78 L12 88 L14.5 97 L15.5 97 L18 88 L17 78 Z" fill="white" fill-opacity="0.55"/>
    </svg>
  </div>

  <div class="center">
    <div class="badge">⚗️ Laboratorium Kimia Analitik</div>
    <h1>Web Perhitungan</h1>
    <p class="orange">Kadar dan Standarisasi</p>
    <p class="teal">✦ Titrimetri ✦</p>
    <div class="line"></div>
    <p class="sub">Standarisasi &nbsp;•&nbsp; Penetapan Kadar &nbsp;•&nbsp; RPD Otomatis &nbsp;•&nbsp; 6 Metode</p>
  </div>

  <div class="side">
    <svg width="70" height="105" viewBox="0 0 70 105">
      <rect x="27" y="2" width="16" height="5" rx="2.5" fill="white" fill-opacity="0.7"/>
      <rect x="30" y="7" width="10" height="22" rx="2" fill="white" fill-opacity="0.6"/>
      <path d="M30 29 L6 74 Q4 86 35 86 Q66 86 64 74 L40 29 Z" fill="white" fill-opacity="0.35"/>
      <path d="M32 48 L10 74 Q9 83 35 83 Q61 83 60 74 L38 48 Z" fill="#f9a8d4" fill-opacity="0.55"/>
      <line x1="22" y1="62" x2="28" y2="62" stroke="white" stroke-opacity="0.5" stroke-width="1.5"/>
      <line x1="19" y1="72" x2="26" y2="72" stroke="white" stroke-opacity="0.5" stroke-width="1.5"/>
    </svg>
    <svg width="48" height="100" viewBox="0 0 48 100">
      <rect x="17" y="1" width="14" height="7" rx="3" fill="white" fill-opacity="0.65"/>
      <rect x="20" y="8" width="8" height="26" rx="2" fill="white" fill-opacity="0.55"/>
      <ellipse cx="24" cy="68" rx="21" ry="22" fill="white" fill-opacity="0.3"/>
      <path d="M5 74 Q4 90 24 91 Q44 90 43 74 Z" fill="#6ee7b7" fill-opacity="0.5"/>
      <line x1="15" y1="48" x2="22" y2="48" stroke="white" stroke-opacity="0.55" stroke-width="1.5"/>
      <rect x="21" y="30" width="6" height="8" rx="1" fill="#6ee7b7" fill-opacity="0.4"/>
    </svg>
  </div>

</div>
</body>
</html>
""", height=220, scrolling=False)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-label">Pilih Metode</div>', unsafe_allow_html=True)
    metode = st.selectbox("", methods, label_visibility="collapsed")

    st.markdown(f'<div class="info-card">{hdpe_icon}<b>{baku_primer[metode]["nama"]}</b> &nbsp;|&nbsp; BE/BM = <b>{baku_primer[metode]["be"]}</b></div>', unsafe_allow_html=True)

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

# ---------- BATAS RPD ----------
col_rpd, _ = st.columns([1, 3])
with col_rpd:
    batas_rpd = st.number_input("📏 Batas RPD (%)", min_value=0.1, max_value=20.0, value=10.0, step=0.5)

# ---------- TABS ----------
tab1, tab2 = st.tabs(["🧪 Standarisasi", "📊 Penetapan Kadar"])

# ===== TAB 1 : STANDARISASI =====
with tab1:
    st.markdown('<div class="sec-header"><span style="font-size:18px">🧪</span><h3>INPUT DATA — Standarisasi</h3></div>', unsafe_allow_html=True)

    if metode == "Kompleksometri":
        # Standarisasi EDTA berbasis Molaritas

        _be_val = baku_primer[metode]["be"]
        _bp_nama = baku_primer[metode]["nama"]
        st.markdown(f'<div class="info-card" style="margin-bottom:12px">{hdpe_icon}<b>{_bp_nama}</b> &nbsp;|&nbsp; BM = <b>{_be_val}</b></div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            v1 = st.number_input("Volume EDTA 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
            v2 = st.number_input("Volume EDTA 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
        with c2:
            mg = st.number_input("Massa CaCO₃ (mg)", min_value=0.0, format="%.4f", key="s_mg")
            bm = st.number_input("BM CaCO₃ (g/mol)", min_value=0.0001, value=float(_be_val), format="%.4f", key="s_be")
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
        _be_val = baku_primer[metode]["be"]
        _bp_nama = baku_primer[metode]["nama"]
        st.markdown(f'<div class="info-card" style="margin-bottom:12px">{hdpe_icon}<b>{_bp_nama}</b> &nbsp;|&nbsp; BE/BM = <b>{_be_val}</b></div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            v1 = st.number_input("Volume Titran 1 / V1 (mL)", min_value=0.0, format="%.4f", key="s_v1")
            v2 = st.number_input("Volume Titran 2 / V2 (mL)", min_value=0.0, format="%.4f", key="s_v2")
        with c2:
            mg = st.number_input("Massa Baku Primer (mg)", min_value=0.0, format="%.4f", key="s_mg")
            be = st.number_input("BE / BM Baku Primer", min_value=0.0001, value=float(_be_val), format="%.4f", key="s_be")
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
        _bm_val = baku_primer[metode]["be"]
        _bp_nama = baku_primer[metode]["nama"]
        st.markdown(f'<div class="info-card" style="margin-bottom:12px">{hdpe_icon}<b>{_bp_nama}</b> &nbsp;|&nbsp; BM = <b>{_bm_val}</b> | Hasil: <b>ppm CaCO₃</b></div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            pv1 = st.number_input("Volume EDTA 1 / V1 (mL)", min_value=0.0, format="%.4f", key="k_v1")
            pv2 = st.number_input("Volume EDTA 2 / V2 (mL)", min_value=0.0, format="%.4f", key="k_v2")
        with c2:
            nm  = st.number_input("Molaritas EDTA (M)", min_value=0.0, format="%.4f", key="k_nm")
            pbe = st.number_input("BM CaCO₃ (g/mol)", min_value=0.0001, value=float(_bm_val), format="%.4f", key="k_be")
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
