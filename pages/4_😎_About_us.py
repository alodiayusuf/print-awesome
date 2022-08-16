import requests
import streamlit as st 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About Us", page_icon="😎")
st.header("Print(awesome)")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----Link Animation----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_h6ykqbyg.json")

st_lottie(lottie_coding, height=200, key="hello")



with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Siti Agrippina Alodia Yusuf")
		st.write("##")
		st.markdown(
			"""
			<p align="justify">Hello, nama saya Siti Agrippina Alodia Yusuf. Kalian bisa memanggil saya Alodia atau Al.
			Disini saya bertugas untuk membuat website menggunakan Streamlit. Untuk bisa berkenalan lebih jauh
			bisa berkunjung ke sosmed saya di bawah ini:</p align="justify"> 
			<p>ig: alodiayusuf</p> 
			<p>twitter: dheiromancy</p> 
			<p>email: alodiaysf@gmail.com</p>
			""", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----Link Animation----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_cw2hhqpz.json")

with right_column:
	st_lottie(lottie_coding, key="hai")


with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Rizki Nur Wulandari")
		st.write("##")
		st.markdown(
			"""
			<p align="justify">Hai, nama ku Rizki Nur Wulandari. Biasa dipanggil Kiki.
			Disini aku bertugas sama seperti Kak Al, yaitu membuat website menggunakan Streamlit. Untuk berkenalan lebih jauh
			bisa berkunjung ke sosial media ku:</p align="justify"> 
			<p>ig: rizki_nw7</p> 
			<p>email: rizkinurwulandari20@gmail.com</p>
			""", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----Link Animation----
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_dv3etasb.json")

with right_column:
	st_lottie(lottie_coding, key="Helo")


with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Nabilah Argyanti")
		st.write("##")
		st.markdown(
			"""
			<p align="justify">Hello, nama ku Nabilah Argyanti. Bisa dipanggil Nabila atau Bila.
			Disini aku bertugas untuk membuat konten dengan tema Phishing. Untuk bisa berkenalan lebih jauh dengan
			bisa main ke sosmed ku:</p align="justify"> 
			<p>ig: nargyanti</p> 
			<p>twitter: nargyanti</p> 
			<p>email: nargyanti@gmail.com</p>
			""", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----Link Animation----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_twbpyk8b.json")


with right_column:
	st_lottie(lottie_coding, key="halo")
