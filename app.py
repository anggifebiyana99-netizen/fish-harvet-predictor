import streamlit as st

st.set_page_config(
	page_title="Fish Harvest Predictor",
	page_icon="🐟",
	layout="wide"
)

st.title("🐟 Fish Harvest Predictor")
st.subheader("Sistem Prediksi Hasil Panen Ikan")

st.write("Masukkan data budidaya ikan untuk menghitung estimasi panen.")

jenis_ikan = st.selectbox(
	"Jenis Ikan",
	["Lele", "Nila", "Gurame", "Bandeng", "Patin"]
)

jumlah_ikan = st.number_input(
	"Jumlah ikan",
	min_value=1,
	value=1000
)

berat_sekarang = st.number_input(
	"Berat rata-rata ikan saat ini (gram)",
	min_value=1.0,
	value=100.0
)

target_berat = st.number_input(
	"Target berat panen per ikan (gram)",
	min_value=1.0,
	value=500.0
)

tingkat_hidup = st.number_input(
	"Perkiraan tingkat kelangsungan hidup (%)",
	min_value=0.0,
	max_value=100.0,
	value=90.0
)

if st.button("HITUNG ESTIMASI PANEN"):
	ikan_hidup = jumlah_ikan * tingkat_hidup / 100
	total_panen = ikan_hidup * target_berat / 1000

	st.success("Perhitungan berhasil!")
	st.metric("Jenis Ikan", jenis_ikan)
	st.metric("Estimasi ikan hidup", f"{ikan_hidup:,.0f} ekor")
	st.metric("Estimasi hasil panen", f"{total_panen:,.2f} kg")

	if berat_sekarang >= target_berat:
		st.info("Ikan sudah mencapai target berat panen.")
	else:
		st.warning("Ikan belum mencapai target berat panen.")
