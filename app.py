import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIMPEL", page_icon="🧭", layout="centered")

# ---------- HEADER ----------
st.title("🧭 SIMPEL – Cek Bantuan Sosial yang Mungkin Anda Dapat")
st.markdown("Jawab 7 pertanyaan singkat di bawah ini. **Data Anda tidak disimpan.**")

# ---------- PROGRAM DETAILS ----------
program_info = {
    "PKH": {
        "nama": "Program Keluarga Harapan (PKH)",
        "deskripsi": "Bantuan tunai bersyarat untuk keluarga dengan ibu hamil, anak usia sekolah, lansia, atau disabilitas.",
        "dokumen": "KTP, KK, surat keterangan tidak mampu dari RT/RW, buku nikah (jika ada), rapor anak (untuk komponen pendidikan).",
        "tempat": "Dinas Sosial Kabupaten/Kota atau pendamping PKH di kelurahan."
    },
    "BPNT": {
        "nama": "Bantuan Pangan Non‑Tunai (BPNT)",
        "deskripsi": "Bantuan pangan senilai Rp200.000/bulan untuk membeli beras, telur, dan kebutuhan pokok di e‑warong.",
        "dokumen": "KTP, KK, surat keterangan tidak mampu dari RT/RW.",
        "tempat": "Kelurahan/desa (terdaftar di DTKS) atau koordinator BPNT setempat."
    },
    "KIP": {
        "nama": "Kartu Indonesia Pintar (KIP)",
        "deskripsi": "Bantuan biaya pendidikan untuk siswa SD, SMP, SMA/sederajat dari keluarga kurang mampu.",
        "dokumen": "KTP orang tua, KK, surat keterangan tidak mampu, rapor, surat keterangan dari sekolah.",
        "tempat": "Sekolah (operator dapodik) atau Dinas Pendidikan setempat."
    },
    "BPJS_PBI": {
        "nama": "BPJS Kesehatan PBI (Penerima Bantuan Iuran)",
        "deskripsi": "Jaminan kesehatan gratis untuk masyarakat miskin dan tidak mampu, iuran dibayar pemerintah.",
        "dokumen": "KTP, KK, surat keterangan tidak mampu dari kelurahan.",
        "tempat": "Kelurahan atau kantor BPJS Kesehatan terdekat."
    }
}

# ---------- DUMMY PREDICTOR (will be replaced by model later) ----------
def dummy_predict(pendapatan, jumlah_anggota, anak_sekolah, anak_balita, lansia, disabilitas, dinding_rumah):
    """
    Simulates the AI model by returning a list of eligible programs
    and a fake confidence score based on very simple rules.
    This will be replaced with model.predict() on Day 3-4.
    """
    eligible = []
    confidences = {}
    
    # Rule for PKH: low income + (school child / toddler / elderly / disabled)
    if pendapatan in ["< Rp500.000", "Rp500.000 – Rp1.000.000"]:
        if anak_sekolah == "Ya" or anak_balita == "Ya" or lansia == "Ya" or disabilitas == "Ya":
            eligible.append("PKH")
            confidences["PKH"] = 0.82
    
    # Rule for BPNT: very low income, family size >=3, house not fully brick
    if pendapatan in ["< Rp500.000", "Rp500.000 – Rp1.000.000"] and jumlah_anggota in ["3", "4", "5 atau lebih"] and dinding_rumah != "Tembok":
        eligible.append("BPNT")
        confidences["BPNT"] = 0.78
    
    # Rule for KIP: low income + school child
    if pendapatan in ["< Rp500.000", "Rp500.000 – Rp1.000.000"] and anak_sekolah == "Ya":
        eligible.append("KIP")
        confidences["KIP"] = 0.91
    
    # Rule for BPJS PBI: very low income or poor house condition
    if pendapatan == "< Rp500.000" or dinding_rumah in ["Papan/kayu", "Bambu/lainnya"]:
        eligible.append("BPJS_PBI")
        confidences["BPJS_PBI"] = 0.85
    
    return eligible, confidences

# ---------- QUESTIONNAIRE ----------
pendapatan = st.selectbox(
    "1. Rata‑rata pendapatan keluarga per bulan?",
    ["< Rp500.000", "Rp500.000 – Rp1.000.000", "Rp1.000.000 – Rp2.000.000", "> Rp2.000.000"]
)

jumlah_anggota = st.selectbox(
    "2. Jumlah anggota keluarga (termasuk Anda)?",
    ["1", "2", "3", "4", "5 atau lebih"]
)

anak_sekolah = st.radio(
    "3. Apakah ada anak usia sekolah (7–18 tahun) di keluarga?",
    ["Ya", "Tidak"]
)

anak_balita = st.radio(
    "4. Apakah ada anak balita (0–6 tahun) atau ibu hamil?",
    ["Ya", "Tidak"]
)

lansia = st.radio(
    "5. Apakah ada anggota keluarga lanjut usia (≥60 tahun)?",
    ["Ya", "Tidak"]
)

disabilitas = st.radio(
    "6. Apakah ada anggota keluarga dengan disabilitas berat?",
    ["Ya", "Tidak"]
)

dinding_rumah = st.selectbox(
    "7. Jenis dinding terluas rumah Anda?",
    ["Tembok", "Semi permanen (setengah tembok)", "Papan/kayu", "Bambu/lainnya"]
)

# ---------- BUTTON & RESULTS ----------
if st.button("🔍 Cek Bantuan yang Mungkin Saya Dapat", type="primary"):
    # Call dummy predictor
    program_list, confidences = dummy_predict(
        pendapatan, jumlah_anggota, anak_sekolah,
        anak_balita, lansia, disabilitas, dinding_rumah
    )
    
    st.markdown("---")
    st.subheader("📋 Hasil Pemeriksaan")
    
    if not program_list:
        st.warning(
            "Berdasarkan data yang Anda masukkan, saat ini tidak terdeteksi program yang sesuai. "
            "Namun, ini hanya simulasi. Silakan kunjungi kelurahan untuk informasi lebih lanjut."
        )
    else:
        st.success(
            f"Berdasarkan informasi Anda, Anda **mungkin** memenuhi syarat untuk "
            f"{len(program_list)} program berikut."
        )
        
        for prog in program_list:
            info = program_info[prog]
            conf = confidences.get(prog, 0.5)
            
            with st.expander(f"✅ {info['nama']} – Tingkat kecocokan: {conf:.0%}"):
                st.markdown(f"**Mengapa?** Pola kondisi Anda cocok dengan kriteria program ini (simulasi).")
                st.markdown(f"**Deskripsi:** {info['deskripsi']}")
                st.markdown("**Dokumen yang harus disiapkan:**")
                # Convert comma list to bullet points
                docs = info['dokumen'].split(', ')
                for doc in docs:
                    st.markdown(f"- {doc}")
                st.markdown(f"**Ke mana harus pergi:** {info['tempat']}")
    
    # ---------- DISCLAIMER (always visible) ----------
    st.markdown("---")
    st.warning(
        "⚠️ **Peringatan Penting:** Hasil ini **bukan keputusan resmi** dan hanya bersifat simulasi. "
        "Kriteria sebenarnya bisa lebih kompleks dan dapat berubah sewaktu‑waktu. "
        "**Harap verifikasi langsung ke kelurahan atau dinas sosial terdekat.** "
        "Ini adalah alat bantu, bukan penentu akhir."
    )
    
    # ---------- PRINT TIP ----------
    st.info("💡 Tips: Anda bisa mencetak halaman ini (Ctrl+P) untuk dibawa ke kelurahan sebagai panduan awal.")