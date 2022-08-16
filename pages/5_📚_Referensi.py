import requests
import streamlit as st 
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About Us", page_icon="📚")
st.header("Referensi")

with st.container():
	left_column, right_column = st.columns(2)
	with left_column:
		st.write("https://en.wikipedia.org/wiki/Phishing")
		st.write("https://www.fortinet.com/resources/cyberglossary/types-of-phishing-attacks")
		st.write("https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams https://www.phishing.org/10-ways-to-avoid-phishing-scams")
		st.write("https://www.ncsc.gov.uk/collection/small-business-guide/avoiding-phishing-attacks")
		st.write("https://www.phishing.org/what-is-phishing")
		st.write("https://nextren.grid.id/read/013320306/ngeri-cuma-klik-link-dari-pesan-wa-rekening-nasabah-bri-terkuras-hingga-rp-11-miliar")
		st.write("https://internasional.kontan.co.id/news/terkait-penipuan-phising-ocbc-ganti-rugi-kerugian-nasabah-secara-penuh")
		st.write("https://databoks.katadata.co.id/datapublish/2022/06/08/idadx-ada-3180-laporan-phishing-pada-kuartal-i-2022")
		st.write("https://www.inilah.com/pandi-catat-5-579-insiden-serangan-phising-terjadi-di-kuartal-kedua-2022")
		

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----Link Animation----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1a8dx7zj.json")

with right_column:
	st_lottie(lottie_coding, key="refence")
