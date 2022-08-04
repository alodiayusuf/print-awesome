import streamlit as st 
from PIL import Image

st.set_page_config(page_title="Phising Quiz", page_icon="❓")

st.header('Seberapa Beresiko Kamu Terkena Phising?')
st.subheader('Ikuti tes berikut ini dan cari tahu resiko kamu!')

satu = st.radio('Apakah kamu menggunakan password yang sama pada akun-akun yang berbeda?',('Iya','Tidak'))
dua = st.radio('Apakah kamu sering mengarahkan mouse ke tautan asing yang dikirimkan?', ('Iya','Tidak'))
tiga = st.radio('Apakah kamu pernah membuka lampiran email dari pengirim asing?',('Iya','Tidak'))
empat = st.radio('Apakah kamu membalas email yang terlihat mencurigakan?',('Iya','Tidak'))
lima = st.radio('Apakah kamu menggunakan antii-virus sebagai proteksi utama pada saat berselancar di internet?',('Iya','Tidak'))
enam = st.radio('Apakah kamu membuka lampiran email yang tidak kamu harapkan?',('Iya','Tidak'))
tujuh = st.radio('Apakah kamu mengirimkan uang ke temanmu yang ditipu di luar negeri?',('Iya','Tidak'))
delapan = st.radio('Apakah kamu membalas email yang mengatakan bahwa kamu menang undian?',('Iya','Tidak'))
sembilan = st.radio('Apakah kamu rajin update medsos dan menjawab pertanyaan-pertanyaan personal?',('Iya','Tidak'))
sepuluh = st.radio('Apakah kamu melakukan instalasi saat ada update terbaru yang tersedia?',('Iya','Tidak'))

nilai1 = 0
if st.button('Lihat Hasil'):
    
    if satu == 'Iya':
        nilai1 = nilai1
    else:
        nilai1 = nilai1+1

    if dua =='Iya':
        nilai2 = nilai1 + 1
    else:
        nilai2 = nilai1

    if tiga == 'Iya':
        nilai3 = nilai2-1
    else:
        nilai3 = nilai2+1
    
    if empat == 'Iya':
        nilai4 = nilai3-1
    else:
        nilai4 = nilai3+1
    
    if lima =='Iya':
        nilai5= nilai4-1
    else:
        nilai5=nilai4+1
    
    if enam=='Iya':
        nilai6= nilai5-1
    else:
        nilai6=nilai5+1
    
    if tujuh == 'Iya':
        nilai7 = nilai6-1
    else:
        nilai7 = nilai6+1
    
    if delapan == 'Iya':
        nilai8 = nilai7-1
    else:
        nilai8 = nilai7+1
    
    if sembilan == 'Iya':
        nilai9 =  nilai8-1
    else:
        nilai9=nilai8+1
    
    if sepuluh =='Iya':
        nilai10 = nilai9+1
    else:
        nilai10 = nilai9-1
        
    
    nilaiakhir = nilai10
    if nilaiakhir >0 and nilaiakhir < 3:
        image = Image.open('1.png')
        st.image(image,width=360)
        st.error(f'Skor Kamu {nilaiakhir}/10')
        st.snow()
    elif nilaiakhir >=3 and nilaiakhir < 5:
        image = Image.open('2.png')
        st.image(image,width=360)
        st.warning(f'Skor Kamu {nilaiakhir}/10')
    elif nilaiakhir >=5 and nilaiakhir<7:
        image = Image.open('3.png')
        st.image(image,width=360)
        st.warning(f'Skor Kamu {nilaiakhir}/10')
    elif nilaiakhir>=7:
        image = Image.open('4.png')
        st.image(image,width=360)
        st.success(f'Skor Kamu {nilaiakhir}/10')
        st.balloons()
    else:
        st.error('Kami speechless, nilai kamu parah banget!')
 