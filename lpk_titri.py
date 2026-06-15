import streamlit as st

<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Titrimetri — Politeknik AKA Bogor</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,sans-serif;background:#f4f6f8;color:#2d3a4a;min-height:100vh}
:root{
  --mint:#d4f5f0;--mint2:#a8e8e0;--mint3:#6dd4ca;--mint-dark:#0a6b5e;--mint-med:#1a9a8a;
  --lav:#e8e4f8;--lav2:#c9bff0;--lav-dark:#3c3489;
  --peach:#fde8d8;--peach2:#f9c9a8;--peach-dark:#7a3000;
  --sky:#dbeffe;--sky2:#aed6f8;--sky-dark:#0c447c;
  --rose:#fde4ec;--rose2:#f9b8cc;--rose-dark:#72243e;
  --lemon:#fef9d4;--lemon2:#fce97a;--lemon-dark:#633806;
  --text:#2d3a4a;--text-mid:#5a6a7a;--text-soft:#8a9bab;
  --border:#d8e8e4;--white:#ffffff;
}

.wrapper{max-width:980px;margin:0 auto;padding:20px 16px}

.nav{display:flex;gap:4px;border-bottom:2px solid var(--mint2);margin-bottom:20px;flex-wrap:wrap}
.nav-btn{padding:10px 20px;font-size:14px;font-weight:600;color:var(--text-mid);cursor:pointer;
  border-radius:8px 8px 0 0;border:1px solid transparent;border-bottom:none;
  background:none;transition:all .15s}
.nav-btn.active{background:var(--mint);color:var(--mint-dark);border-color:var(--mint2);
  border-bottom:2px solid var(--mint);margin-bottom:-2px}
.nav-btn:hover:not(.active){background:var(--mint);opacity:.7;color:var(--mint-dark)}

.page{display:none}.page.active{display:block}

.hero{
  background:linear-gradient(135deg,#c8f0eb 0%,#b8e8f5 40%,#d4dcf8 80%,#f0d4f0 100%);
  border-radius:18px;padding:36px 20px 30px;text-align:center;
  margin-bottom:28px;border:1px solid var(--mint2);position:relative;overflow:hidden
}
.hero::before{content:'';position:absolute;inset:0;
  background:repeating-linear-gradient(45deg,transparent,transparent 18px,rgba(255,255,255,0.07) 18px,rgba(255,255,255,0.07) 36px)}
.hero-badge{display:inline-block;background:rgba(255,255,255,0.55);border:1px solid rgba(255,255,255,0.8);
  border-radius:20px;padding:4px 16px;font-size:11px;color:var(--text);font-weight:700;
  letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;position:relative;z-index:1}
.hero h1{color:var(--text);font-size:26px;font-weight:700;position:relative;z-index:1;line-height:1.45;margin-bottom:6px}
.hero h1 .orange{color:#b86000}
.hero h1 .teal{color:#0a6b5e}
.hero-line{width:44px;height:3px;background:rgba(255,255,255,0.7);border-radius:2px;margin:12px auto 12px}
.hero-sub{color:var(--text-mid);font-size:13px;position:relative;z-index:1;letter-spacing:.3px}

.section-title{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:700;
  color:var(--text);border-bottom:2px solid var(--mint2);padding-bottom:10px;margin-bottom:18px}

.desc-card{background:var(--mint);border-left:4px solid var(--mint3);border-radius:0 12px 12px 0;
  padding:16px 18px;margin-bottom:20px}
.desc-card p{font-size:13.5px;color:var(--mint-dark);line-height:1.8}

.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:24px}
.feature-card{background:var(--white);border:1px solid var(--border);
  border-radius:12px;padding:16px 12px;text-align:center}
.feature-icon{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;margin:0 auto 12px;font-size:20px}
.feature-card h4{font-size:13px;font-weight:700;color:var(--text);margin-bottom:5px}
.feature-card p{font-size:11.5px;color:var(--text-soft);line-height:1.5}

.howto-list{display:flex;flex-direction:column;gap:12px;margin-bottom:24px}
.step{display:flex;gap:14px;align-items:flex-start}
.step-num{width:30px;height:30px;border-radius:50%;background:var(--mint);border:2px solid var(--mint3);
  display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;
  color:var(--mint-dark);flex-shrink:0;margin-top:1px}
.step-text{font-size:13.5px;color:var(--text-mid);line-height:1.7;padding-top:4px}
.step-text b{font-weight:700;color:var(--text)}

.rumus-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:24px}
.rumus-box{background:var(--lemon);border-radius:12px;padding:14px;border:1px solid var(--lemon2)}
.rumus-label{font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--lemon-dark);margin-bottom:8px}
.rumus-formula{background:rgba(255,255,255,0.7);border-radius:6px;padding:9px 10px;
  font-family:Georgia,serif;font-size:13px;color:var(--text);text-align:center;line-height:1.8;margin-bottom:6px}
.rumus-note{font-size:11px;color:#7a6800;line-height:1.5}

.kreator-header{background:var(--lav);border-radius:12px;padding:14px 18px;
  margin-bottom:16px;display:flex;align-items:center;gap:14px}
.kreator-header-text h3{font-size:14px;font-weight:700;color:var(--lav-dark)}
.kreator-header-text p{font-size:12px;color:#534ab7;margin-top:2px}

.member-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:18px}
.member-card{background:var(--white);border:1px solid var(--border);
  border-radius:12px;padding:16px 14px;display:flex;align-items:center;gap:14px}
.avatar{width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:15px;font-weight:700;flex-shrink:0}
.member-name{font-size:13.5px;font-weight:700;color:var(--text);margin-bottom:3px}
.member-nim{font-size:11.5px;color:var(--text-soft)}

.inst-card{background:var(--peach);border-radius:12px;padding:14px 18px;
  display:flex;align-items:center;gap:14px;border:1px solid var(--peach2);margin-bottom:28px}
.inst-icon{font-size:28px}
.inst-card p{font-size:14px;color:var(--peach-dark);font-weight:700}
.inst-card span{font-size:12px;color:#a05030;display:block;margin-top:3px}

.cta-btn{background:var(--mint-dark);color:white;border:none;border-radius:10px;
  padding:13px 28px;font-size:14px;font-weight:700;cursor:pointer;margin-top:8px;
  letter-spacing:.5px;transition:background .15s;display:inline-block}
.cta-btn:hover{background:var(--mint-med)}

/* ---- KALKULATOR ---- */
.calc-layout{display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap}
.sidebar{width:250px;min-width:210px;flex-shrink:0}
.main-panel{flex:1;min-width:280px}

.card{background:var(--white);border:1px solid var(--border);border-radius:12px;padding:16px;margin-bottom:14px}
.card-title{font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;
  color:var(--text-soft);margin-bottom:10px}

.info-pill{background:var(--mint);border-left:4px solid var(--mint3);
  border-radius:0 8px 8px 0;padding:10px 13px;font-size:12px;color:var(--mint-dark);
  margin-top:10px;line-height:1.6}

.formula-card{background:var(--lemon);border-radius:10px;padding:13px;border:1px solid var(--lemon2)}
.formula-title{font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--lemon-dark);margin-bottom:6px}
.formula-box{background:rgba(255,255,255,0.7);border-radius:6px;padding:8px 10px;
  font-family:Georgia,serif;font-size:12px;color:var(--text);text-align:center;line-height:1.7;margin-bottom:6px}

.ket-card{background:var(--lav);border-radius:10px;padding:12px}
.ket-grid{display:grid;grid-template-columns:48px 1fr;gap:5px 0;align-items:center;font-size:12px}
.ket-key{color:var(--mint-dark);font-weight:700;font-size:13px}
.ket-val{color:var(--text-mid)}

label{display:block;font-size:12px;font-weight:600;color:var(--text-mid);margin-bottom:5px;margin-top:12px}
label:first-of-type{margin-top:0}
input[type=number],select{
  width:100%;padding:9px 11px;font-size:13px;
  border:1px solid var(--border);border-radius:8px;
  background:var(--white);color:var(--text);outline:none;transition:border .15s;
}
input[type=number]:focus,select:focus{border-color:var(--mint-med);box-shadow:0 0 0 3px rgba(26,154,138,.1)}

.tabs{display:flex;gap:4px;border-bottom:2px solid var(--mint2);margin-bottom:16px}
.tab{padding:9px 18px;font-size:13px;font-weight:600;color:var(--text-mid);cursor:pointer;
  border-radius:8px 8px 0 0;border:1px solid transparent;border-bottom:none;
  transition:all .15s;background:none}
.tab.active{background:var(--mint);color:var(--mint-dark);border-color:var(--mint2);
  border-bottom:2px solid var(--mint);margin-bottom:-2px}
.tab:hover:not(.active){background:var(--mint);color:var(--mint-dark);opacity:.7}

.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 16px}
@media(max-width:500px){.form-grid{grid-template-columns:1fr}}

.btn{background:var(--mint-dark);color:white;border:none;border-radius:10px;
  padding:12px 20px;font-size:14px;font-weight:700;cursor:pointer;margin-top:18px;
  width:100%;letter-spacing:.5px;transition:background .15s}
.btn:hover{background:var(--mint-med)}

.result-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:14px 0}
@media(max-width:480px){.result-grid{grid-template-columns:1fr 1fr}}
.result-item{background:var(--sky);border:1px solid var(--sky2);border-radius:10px;
  padding:13px 8px;text-align:center}
.rc-label{font-size:10px;font-weight:700;color:var(--text-soft);text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px}
.rc-val{font-size:20px;font-weight:700;color:var(--text)}
.rc-unit{font-size:10px;color:var(--text-soft);margin-top:3px}

.status-ok{background:var(--mint);color:#066b4e;border:1px solid var(--mint3);
  border-radius:8px;padding:12px 16px;text-align:center;font-weight:700;font-size:13.5px}
.status-err{background:var(--rose);color:#a02040;border:1px solid var(--rose2);
  border-radius:8px;padding:12px 16px;text-align:center;font-weight:700;font-size:13.5px}

.sec-header{display:flex;align-items:center;gap:8px;padding-bottom:10px;
  border-bottom:2px solid var(--mint2);margin-bottom:16px}
.sec-header h3{color:var(--text);font-weight:700;font-size:14px;margin:0}

.rpd-row{display:flex;align-items:center;gap:12px;margin-bottom:18px;flex-wrap:wrap}
.rpd-row label{margin:0;font-size:13px;font-weight:600;color:var(--text-mid)}
.rpd-row input{width:100px;margin-top:0}

.footer{text-align:center;color:var(--text-soft);font-size:12px;padding:18px;
  border-top:1px solid var(--border);margin-top:20px}

@media(max-width:640px){
  .sidebar{width:100%}
  .main-panel{width:100%}
  .calc-layout{flex-direction:column}
  .hero h1{font-size:20px}
  .member-grid{grid-template-columns:1fr}
  .feature-grid{grid-template-columns:1fr 1fr}
}
</style>
</head>
<body>
<div class="wrapper">

  <nav class="nav">
    <button class="nav-btn active" onclick="showPage('beranda',this)">🏠 Beranda</button>
    <button class="nav-btn" onclick="showPage('kalkulator',this)">🧮 Kalkulator</button>
  </nav>

  <!-- ========== BERANDA ========== -->
  <div id="page-beranda" class="page active">

    <div class="hero">
      <div class="hero-badge">⚗️ Laboratorium Kimia Analitik</div>
      <h1>Web Perhitungan<br><span class="orange">Kadar dan Standarisasi</span><br><span class="teal">✦ Titrimetri ✦</span></h1>
      <div class="hero-line"></div>
      <div class="hero-sub">Standarisasi &nbsp;·&nbsp; Penetapan Kadar &nbsp;·&nbsp; RPD Otomatis &nbsp;·&nbsp; 6 Metode</div>
    </div>

    <div class="section-title">📋 Tentang Aplikasi Ini</div>
    <div class="desc-card">
      <p>Web Titrimetri adalah aplikasi kalkulator berbasis web yang dirancang untuk membantu mahasiswa dan praktisi kimia analitik dalam menghitung <b>standarisasi larutan titran</b> dan <b>penetapan kadar analit</b> secara akurat dan efisien. Aplikasi ini mendukung enam metode titrimetri yang umum digunakan di laboratorium, dilengkapi dengan perhitungan <b>%RPD (Relative Percent Difference)</b> otomatis untuk mengevaluasi presisi hasil duplo.</p>
    </div>

    <div class="section-title">⚗️ Metode yang Didukung</div>
    <div class="feature-grid">
      <div class="feature-card">
        <div class="feature-icon" style="background:#d4f5f0;color:#0a6b5e">🔵</div>
        <h4>Alkalimetri</h4>
        <p>Baku primer: Asam Oksalat · BE 63,03</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:#dbeffe;color:#0c447c">🔷</div>
        <h4>Asidimetri</h4>
        <p>Baku primer: Boraks · BE 190,69</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:#fde8d8;color:#7a3000">🟠</div>
        <h4>Permanganometri</h4>
        <p>Baku primer: Asam Oksalat · BE 63,03</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:#fef9d4;color:#633806">🟡</div>
        <h4>Iodometri</h4>
        <p>Baku primer: K₂Cr₂O₇ · BE 49,03</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:#fde4ec;color:#72243e">🔴</div>
        <h4>Argentometri</h4>
        <p>Baku primer: NaCl · BE 58,44</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:#e8e4f8;color:#3c3489">🟣</div>
        <h4>Kompleksometri</h4>
        <p>Baku primer: CaCO₃ · BM 100,09</p>
      </div>
    </div>

    <div class="section-title">📌 Cara Menggunakan</div>
    <div class="howto-list">
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-text"><b>Pilih metode titrimetri</b> yang sesuai dengan percobaan pada menu dropdown di sidebar kalkulator.</div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-text"><b>Atur batas RPD (%)</b> yang diinginkan sebagai batas keberterimaan presisi duplo (default: 10%).</div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-text">Pada tab <b>Standarisasi</b>, masukkan volume titran (V1, V2), massa baku primer, BE/BM, dan faktor pengali (FP).</div>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <div class="step-text">Pada tab <b>Penetapan Kadar</b>, masukkan volume titran, nilai N/M dari standarisasi, BE analit, FP, dan massa/volume sampel.</div>
      </div>
      <div class="step">
        <div class="step-num">5</div>
        <div class="step-text">Klik tombol <b>Hitung</b> — hasil N/M, kadar, rata-rata, dan %RPD beserta status presisi ditampilkan otomatis.</div>
      </div>
    </div>

    <div class="section-title">📐 Rumus yang Digunakan</div>
    <div class="rumus-grid">
      <div class="rumus-box">
        <div class="rumus-label">Standarisasi (Normalitas)</div>
        <div class="rumus-formula">N = mg / (V × BE × FP)</div>
        <div class="rumus-note">Untuk alkalimetri, asidimetri, permanganometri, iodometri, argentometri</div>
      </div>
      <div class="rumus-box">
        <div class="rumus-label">Penetapan Kadar</div>
        <div class="rumus-formula">Kadar = (V × N × BE × FP × 10⁻³ / S) × 100%</div>
        <div class="rumus-note">Hasil dalam % b/v. S = massa atau volume sampel</div>
      </div>
      <div class="rumus-box">
        <div class="rumus-label">Standarisasi EDTA (Molaritas)</div>
        <div class="rumus-formula">M = mg / (V × BM CaCO₃)</div>
        <div class="rumus-note">Khusus kompleksometri — standarisasi berbasis molaritas</div>
      </div>
      <div class="rumus-box">
        <div class="rumus-label">Penetapan Kesadahan</div>
        <div class="rumus-formula">ppm = (V × M × BM × FP × 1000) / V sampel</div>
        <div class="rumus-note">Hasil dalam ppm CaCO₃ — khusus kompleksometri</div>
      </div>
      <div class="rumus-box">
        <div class="rumus-label">%RPD (Relative Percent Difference)</div>
        <div class="rumus-formula">%RPD = |H₁ − H₂| / rata-rata × 100%</div>
        <div class="rumus-note">Evaluasi presisi duplo. Hasil ≤ batas RPD = presisi diterima</div>
      </div>
    </div>

    <div style="text-align:center;margin-bottom:32px">
      <button class="cta-btn" onclick="showPage('kalkulator',document.querySelectorAll('.nav-btn')[1])">
        🧮 Mulai Hitung Sekarang
      </button>
    </div>

    <div class="section-title">👥 Identitas Kreator</div>
    <div class="kreator-header">
      <span style="font-size:28px">🎓</span>
      <div class="kreator-header-text">
        <h3>Kelompok Mahasiswa — Kelas ANKIM 1D</h3>
        <p>Mata Kuliah Kimia Analitik · Tahun Akademik 2025/2026</p>
      </div>
    </div>

    <div class="member-grid">
      <div class="member-card">
        <div class="avatar" style="background:#d4f5f0;color:#085041">DA</div>
        <div>
          <div class="member-name">Dzulia Azhahra</div>
          <div class="member-nim">NIM 2560617 · ANKIM 1D</div>
        </div>
      </div>
      <div class="member-card">
        <div class="avatar" style="background:#dbeffe;color:#0c447c">MS</div>
        <div>
          <div class="member-name">Muhammad Sahwal Sandijat</div>
          <div class="member-nim">NIM 2560689 · ANKIM 1D</div>
        </div>
      </div>
      <div class="member-card">
        <div class="avatar" style="background:#e8e4f8;color:#3c3489">NH</div>
        <div>
          <div class="member-name">Nuhara Hanami</div>
          <div class="member-nim">NIM 2560731 · ANKIM 1D</div>
        </div>
      </div>
      <div class="member-card">
        <div class="avatar" style="background:#fde4ec;color:#72243e">RA</div>
        <div>
          <div class="member-name">Rita Aryani</div>
          <div class="member-nim">NIM 2560761 · ANKIM 1D</div>
        </div>
      </div>
    </div>

    <div class="inst-card">
      <span class="inst-icon">🏛️</span>
      <div>
        <p>Politeknik AKA Bogor</p>
        <span>Program Studi Analis Kimia · Kelas ANKIM 1D</span>
      </div>
    </div>

  </div>

  <!-- ========== KALKULATOR ========== -->
  <div id="page-kalkulator" class="page">
    <div class="calc-layout">

      <aside class="sidebar">
        <div class="card">
          <div class="card-title">🔬 Pilih Metode</div>
          <select id="metode" onchange="updateMethod()">
            <option>Alkalimetri</option>
            <option>Asidimetri</option>
            <option>Permanganometri</option>
            <option>Iodometri</option>
            <option>Argentometri</option>
            <option>Kompleksometri</option>
          </select>
          <div class="info-pill" id="bp-info"></div>
        </div>

        <div class="card">
          <div class="card-title">📖 Rumus</div>
          <div class="formula-card">
            <div class="formula-title">Standarisasi</div>
            <div class="formula-box" id="f-std"></div>
            <div class="formula-title" style="margin-top:10px">Penetapan Kadar</div>
            <div class="formula-box" id="f-kad"></div>
          </div>
        </div>

        <div class="card">
          <div class="card-title">📌 Keterangan</div>
          <div class="ket-card">
            <div class="ket-grid">
              <span class="ket-key">V</span><span class="ket-val">= Volume titran (mL)</span>
              <span class="ket-key">N/M</span><span class="ket-val">= Normalitas / Molaritas</span>
              <span class="ket-key">BE/BM</span><span class="ket-val">= Berat Ekuivalen / BM</span>
              <span class="ket-key">FP</span><span class="ket-val">= Faktor Pengali</span>
              <span class="ket-key">S</span><span class="ket-val">= Massa / Volume Sampel</span>
              <span class="ket-key">mg</span><span class="ket-val">= Massa baku primer (mg)</span>
            </div>
          </div>
        </div>
      </aside>

      <main class="main-panel">
        <div class="rpd-row">
          <label>📏 Batas RPD (%)</label>
          <input type="number" id="batas-rpd" value="10" min="0.1" max="20" step="0.5" style="width:100px;margin-top:0">
        </div>

        <div class="tabs">
          <button class="tab active" id="tab-std-btn" onclick="switchTab('std')">🧪 Standarisasi</button>
          <button class="tab" id="tab-kad-btn" onclick="switchTab('kad')">📊 Penetapan Kadar</button>
        </div>

        <!-- TAB STANDARISASI -->
        <div id="panel-std">
          <div class="sec-header"><span style="font-size:18px">🧪</span><h3 id="std-title">Input Data — Standarisasi</h3></div>
          <div class="info-pill" id="bp-info2" style="margin-bottom:14px"></div>
          <div class="form-grid">
            <div>
              <label>Volume Titran 1 / V1 (mL)</label>
              <input type="number" id="s-v1" min="0" step="0.0001">
              <label>Volume Titran 2 / V2 (mL)</label>
              <input type="number" id="s-v2" min="0" step="0.0001">
            </div>
            <div>
              <label>Massa Baku Primer (mg)</label>
              <input type="number" id="s-mg" min="0" step="0.0001">
              <label id="lbl-be">BE / BM Baku Primer</label>
              <input type="number" id="s-be" min="0.0001" step="0.0001">
            </div>
            <div>
              <label>Faktor Pengali (FP)</label>
              <input type="number" id="s-fp" min="0.0001" step="0.0001" value="1">
            </div>
          </div>
          <button class="btn" onclick="hitungStd()">🖩 Hitung Standarisasi</button>
          <div id="result-std" style="margin-top:16px"></div>
        </div>

        <!-- TAB PENETAPAN KADAR -->
        <div id="panel-kad" style="display:none">
          <div class="sec-header"><span style="font-size:18px">📊</span><h3>Input Data — Penetapan Kadar</h3></div>
          <div class="info-pill" id="bp-info3" style="margin-bottom:14px"></div>
          <div class="form-grid">
            <div>
              <label id="lbl-kv1">Volume Titran 1 / V1 (mL)</label>
              <input type="number" id="k-v1" min="0" step="0.0001">
              <label>Volume Titran 2 / V2 (mL)</label>
              <input type="number" id="k-v2" min="0" step="0.0001">
            </div>
            <div>
              <label id="lbl-knm">Normalitas / Molaritas (N/M)</label>
              <input type="number" id="k-nm" min="0" step="0.0001">
              <label id="lbl-kbe">BE / BM Analit</label>
              <input type="number" id="k-be" min="0.0001" step="0.0001" value="1">
            </div>
            <div>
              <label>Faktor Pengali (FP)</label>
              <input type="number" id="k-fp" min="0.0001" step="0.0001" value="1">
              <label id="lbl-ks">Massa / Volume Sampel (S)</label>
              <input type="number" id="k-s" min="0.0001" step="0.0001" value="1">
            </div>
          </div>
          <button class="btn" id="btn-kad" onclick="hitungKad()">🖩 Hitung Kadar</button>
          <div id="result-kad" style="margin-top:16px"></div>
        </div>
      </main>

    </div>
  </div>

  <div class="footer">
    © 2026 Web Perhitungan Titrimetri &nbsp;|&nbsp; ANKIM 1D &nbsp;|&nbsp; Politeknik AKA Bogor
  </div>

</div>

<script>
const DATA={
  Alkalimetri:{nama:"Asam Oksalat (H₂C₂O₄·2H₂O)",be:63.03,mode:"N"},
  Asidimetri:{nama:"Boraks (Na₂B₄O₇·10H₂O)",be:190.69,mode:"N"},
  Permanganometri:{nama:"Asam Oksalat (H₂C₂O₄·2H₂O)",be:63.03,mode:"N"},
  Iodometri:{nama:"K₂Cr₂O₇",be:49.03,mode:"N"},
  Argentometri:{nama:"NaCl",be:58.44,mode:"N"},
  Kompleksometri:{nama:"CaCO₃",be:100.09,mode:"M"},
};

function showPage(id,btn){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  btn.classList.add('active');
}

function switchTab(t){
  const isStd=t==='std';
  document.getElementById('panel-std').style.display=isStd?'block':'none';
  document.getElementById('panel-kad').style.display=isStd?'none':'block';
  document.getElementById('tab-std-btn').classList.toggle('active',isStd);
  document.getElementById('tab-kad-btn').classList.toggle('active',!isStd);
}

function getMetode(){return document.getElementById('metode').value}
function getBatas(){return parseFloat(document.getElementById('batas-rpd').value)||10}
function rpd(a,b){let avg=(a+b)/2;return avg===0?0:Math.abs(a-b)/avg*100}

function updateMethod(){
  const m=getMetode(),d=DATA[m],isK=m==='Kompleksometri';
  const infoHtml=`<b>${d.nama}</b> &nbsp;|&nbsp; ${isK?'BM':'BE/BM'} = <b>${d.be}</b>`;
  ['bp-info','bp-info2'].forEach(id=>document.getElementById(id).innerHTML=infoHtml);
  document.getElementById('bp-info3').innerHTML=isK
    ?`<b>${d.nama}</b> &nbsp;|&nbsp; BM = <b>${d.be}</b> &nbsp;·&nbsp; Hasil: <b>ppm CaCO₃</b>`
    :infoHtml;
  document.getElementById('s-be').value=d.be;
  document.getElementById('lbl-be').textContent=isK?'BM CaCO₃ (g/mol)':'BE / BM Baku Primer';
  document.getElementById('std-title').textContent=isK
    ?'Input Data — Standarisasi EDTA (Molaritas)':'Input Data — Standarisasi';
  if(isK){
    document.getElementById('f-std').textContent='M = mg / (V × BM CaCO₃)';
    document.getElementById('f-kad').textContent='ppm = (V × M × BM × FP × 1000) / V sampel';
    document.getElementById('lbl-kv1').textContent='Volume EDTA 1 / V1 (mL)';
    document.getElementById('lbl-knm').textContent='Molaritas EDTA (M)';
    document.getElementById('lbl-kbe').textContent='BM CaCO₃ (g/mol)';
    document.getElementById('lbl-ks').textContent='Volume Sampel (mL)';
    document.getElementById('btn-kad').textContent='🖩 Hitung Kesadahan';
    document.getElementById('k-be').value=d.be;
  } else {
    document.getElementById('f-std').textContent='N = mg / (V × BE × FP)';
    document.getElementById('f-kad').textContent='Kadar = (V × N × BE × FP × 10⁻³ / S) × 100%';
    document.getElementById('lbl-kv1').textContent='Volume Titran 1 / V1 (mL)';
    document.getElementById('lbl-knm').textContent='Normalitas / Molaritas (N/M)';
    document.getElementById('lbl-kbe').textContent='BE / BM Analit';
    document.getElementById('lbl-ks').textContent='Massa / Volume Sampel (S)';
    document.getElementById('btn-kad').textContent='🖩 Hitung Kadar';
    document.getElementById('k-be').value=1;
  }
  document.getElementById('result-std').innerHTML='';
  document.getElementById('result-kad').innerHTML='';
}

function resultHtml(items,ok,msg){
  const cards=items.map(i=>`
    <div class="result-item">
      <div class="rc-label">${i.label}</div>
      <div class="rc-val">${i.val}</div>
      <div class="rc-unit">${i.unit}</div>
    </div>`).join('');
  const status=ok
    ?`<div class="status-ok">✅ PRESISI — ${msg}</div>`
    :`<div class="status-err">❌ TIDAK PRESISI — ${msg}</div>`;
  return `<div class="result-grid">${cards}</div>${status}`;
}

function hitungStd(){
  const m=getMetode(),isK=m==='Kompleksometri';
  const v1=parseFloat(document.getElementById('s-v1').value);
  const v2=parseFloat(document.getElementById('s-v2').value);
  const mg=parseFloat(document.getElementById('s-mg').value);
  const be=parseFloat(document.getElementById('s-be').value);
  const fp=parseFloat(document.getElementById('s-fp').value)||1;
  if(!v1||!v2||!mg||v1<=0||v2<=0||mg<=0){
    document.getElementById('result-std').innerHTML=
      `<div class="status-err">⚠️ Harap isi semua field dengan nilai yang valid!</div>`;
    return;
  }
  let r1,r2,unit;
  if(isK){r1=mg/(v1*be);r2=mg/(v2*be);unit='M';}
  else{r1=mg/(v1*be*fp);r2=mg/(v2*be*fp);unit='N';}
  const avg=(r1+r2)/2,rpdVal=rpd(r1,r2),batas=getBatas(),ok=rpdVal<=batas;
  const items=[
    {label:isK?'M EDTA 1':'N Titran 1',val:r1.toFixed(4),unit},
    {label:isK?'M EDTA 2':'N Titran 2',val:r2.toFixed(4),unit},
    {label:'Rata-rata',val:avg.toFixed(4),unit},
    {label:'%RPD',val:rpdVal.toFixed(2),unit:'%'}
  ];
  document.getElementById('result-std').innerHTML=
    resultHtml(items,ok,`%RPD = ${rpdVal.toFixed(2)}% (${ok?'≤':'>'} ${batas}%)`);
}

function hitungKad(){
  const m=getMetode(),isK=m==='Kompleksometri';
  const v1=parseFloat(document.getElementById('k-v1').value);
  const v2=parseFloat(document.getElementById('k-v2').value);
  const nm=parseFloat(document.getElementById('k-nm').value);
  const be=parseFloat(document.getElementById('k-be').value);
  const fp=parseFloat(document.getElementById('k-fp').value)||1;
  const s=parseFloat(document.getElementById('k-s').value)||1;
  if(!v1||!v2||!nm||v1<=0||v2<=0||nm<=0){
    document.getElementById('result-kad').innerHTML=
      `<div class="status-err">⚠️ Harap isi semua field dengan nilai yang valid!</div>`;
    return;
  }
  let h1,h2,unit,lbl1,lbl2,decs=4;
  if(isK){h1=(v1*nm*be*fp*1000)/s;h2=(v2*nm*be*fp*1000)/s;unit='ppm CaCO₃';lbl1='Kesadahan 1';lbl2='Kesadahan 2';decs=2;}
  else{h1=((v1*nm*be*fp)*1e-3/s)*100;h2=((v2*nm*be*fp)*1e-3/s)*100;unit='% b/v';lbl1='Kadar 1';lbl2='Kadar 2';}
  const avg=(h1+h2)/2,rpdVal=rpd(h1,h2),batas=getBatas(),ok=rpdVal<=batas;
  const items=[
    {label:lbl1,val:h1.toFixed(decs),unit},
    {label:lbl2,val:h2.toFixed(decs),unit},
    {label:'Rata-rata',val:avg.toFixed(decs),unit},
    {label:'%RPD',val:rpdVal.toFixed(2),unit:'%'}
  ];
  document.getElementById('result-kad').innerHTML=
    resultHtml(items,ok,`%RPD = ${rpdVal.toFixed(2)}% (${ok?'≤':'>'} ${batas}%)`);
}

updateMethod();
</script>
</body>
</html>

""", unsafe_allow_html=True)
