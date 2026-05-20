import streamlit as st

st.set_page_config(page_title="Web Titrimetri", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.main {background-color:#f7fcfc;}
.hero {
    background: linear-gradient(135deg,#0ea5a4,#38bdf8);
    padding: 35px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}
.result-box{
    padding:15px;
    border-radius:12px;
    background:#ecfeff;
    border:1px solid #a5f3fc;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Web Perhitungan Kadar dan Standarisasi Titrimetri</h1>
<p>Responsive • Duplo • RPD otomatis • Metode titrimetri</p>
</div>
""", unsafe_allow_html=True)

methods = [
    "Alkalimetri", "Asidimetri", "Permanganometri",
    "Iodometri", "Argentometri", "Kompleksometri"
]

with st.sidebar:
    st.header("Pengaturan")
    metode = st.selectbox("Pilih Metode", methods)
    st.info("RPD Lulus jika ≤ 10%")

def rpd(h1, h2):
    avg = (h1 + h2) / 2
    return 0 if avg == 0 else abs(h1 - h2) / avg * 100

tab1, tab2 = st.tabs(["Standarisasi", "Penetapan Kadar"])

# ---------- TAB 1 ----------
with tab1:
    st.subheader("Standarisasi")
    c1, c2 = st.columns(2)

    with c1:
        v1 = st.number_input("V1 (mL)", min_value=0.0)
        v2 = st.number_input("V2 (mL)", min_value=0.0)
        mg = st.number_input("mg baku primer", min_value=0.0)

    with c2:
        be = st.number_input("BE / BM", min_value=0.0001, value=1.0)
        fp = st.number_input("Faktor Pengali (FP)", min_value=0.0001, value=1.0)

    if st.button("Hitung Standarisasi"):
        n1 = mg / (v1 * be * fp) if v1 else 0
        n2 = mg / (v2 * be * fp) if v2 else 0
        avg = (n1 + n2) / 2
        hasil_rpd = rpd(n1, n2)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.write(f"**N1:** {n1:.4f}")
        st.write(f"**N2:** {n2:.4f}")
        st.write(f"**Rata-rata N/M:** {avg:.4f}")
        st.write(f"**RPD:** {hasil_rpd:.2f}%")
        st.success("LULUS") if hasil_rpd <= 10 else st.error("TIDAK LULUS")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- TAB 2 ----------
with tab2:
    st.subheader("Penetapan Kadar")
    c1, c2 = st.columns(2)

    with c1:
        pv1 = st.number_input("V1 Kadar (mL)", min_value=0.0)
        pv2 = st.number_input("V2 Kadar (mL)", min_value=0.0)
        normalitas = st.number_input("N / M", min_value=0.0)

    with c2:
        pbe = st.number_input("BE/BM Kadar", min_value=0.0001, value=1.0)
        pfp = st.number_input("FP Kadar", min_value=0.0001, value=1.0)
        sampel = st.number_input("Massa / Volume Sampel", min_value=0.0001, value=1.0)

    if st.button("Hitung Kadar"):
        if metode == "Kompleksometri":
            h1 = (pv1 * normalitas * pbe * 1000) / sampel
            h2 = (pv2 * normalitas * pbe * 1000) / sampel
            unit = "ppm"
        else:
            h1 = ((pv1 * normalitas * pbe * pfp) / sampel) * 100
            h2 = ((pv2 * normalitas * pbe * pfp) / sampel) * 100
            unit = "% b/v"

        avg = (h1 + h2) / 2
        hasil_rpd = rpd(h1, h2)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.write(f"**Kadar 1:** {h1:.4f} {unit}")
        st.write(f"**Kadar 2:** {h2:.4f} {unit}")
        st.write(f"**Rata-rata:** {avg:.4f} {unit}")
        st.write(f"**RPD:** {hasil_rpd:.2f}%")
        st.success("LULUS") if hasil_rpd <= 10 else st.error("TIDAK LULUS")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Titrimetri Web • Streamlit")
