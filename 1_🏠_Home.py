import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(
    page_title="Home",
    page_icon="🏠"
)

#st.title("Maraknya Penipuan Online mengatasnamakan Bank")

#with st.sidebar:
   # selected = option_menu(
       # menu_title=None,
       # options=['Home','Phising Quiz','About Us']
   # )


st.markdown("# Maraknya Penipuan Online Mengatasnamakan Bank")

st.markdown("""
            
            ### Modus Operandi
            Penipu mengirimkan sebuah link ke E-mail ataupun pesan singkat dengan mengatasnamakan Bank dan menawarkan sejumlah hadiah uang.
            Tujuannya adalah untuk mendapatkan akses ke data dan akun pribadi dari korban, seperti mobile banking, e-wallet dan mengambil alih akun-akun tersebut.
            
            ### Metode Penipuan
            Beberapa metode umum yang kerap kali digunakan untuk melancarkan aksi penipuan di dunia maya antara lain phising, pharming, sniffing, money mule, dan social engineering.
            
            ### Phising
            Merupakan metode penipuan paling populer, di mana pelaku mengelabui korban dengan mengirimpakn link ke email atau pesan singkat yang mengarahkan ke situs palsu.
            
            ### Kasus
            Salah satu kasus phising terjadi pada bulan Juni 2022, korban adalah salah satu nasabah Bank BRI dengan nilai kerugian mencapai Rp.1.1 Milyar. 
            Penipu mengirimkan sebuah link melalui aplikasi pesan WhatsApp dan mendorong korban secara halus untuk mengcopy link dan mengisi data-data sesuai petunjuk. 
            Setelah korban selesai mengakses dan mengisi link yang diberikan, pelaku beraksi dan menguras uang milik korban yang ada di rekening. 
            [Baca lebih lanjut](https://nextren.grid.id/read/013320306/ngeri-cuma-klik-link-dari-pesan-wa-rekening-nasabah-bri-terkuras-hingga-rp-11-miliar) 
            
            ### Kasus Phising 2Q 2022 di Indonesia
            """)

data = pd.read_csv('data-phising.csv')
st.sidebar.title('Data Kasus Phising 2Q 2022 di Indonesia')
#st.write(data)
bulan = ["All","Januari","Februari","Maret","April","Mei","Juni"]

select = st.sidebar.selectbox('Bulan:', bulan, key='1')

if select == "All":
    data_filter = data
else:
    data_filter = data[data['Bulan']==select]

st.write(px.bar(data_filter, y='Jumlah_Kasus',x='Bulan'))

st.markdown("""
            [Pelajari Phising lebih lanjut](https://alodiayusuf-print-awesome-1--home-7vhxp1.streamlitapp.com/%EF%B8%8F_Phising_101)
            """)
