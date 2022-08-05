import requests
import streamlit as st 
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

st.set_page_config(page_title="Phising 101", page_icon="⚙️")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#----Link Animation----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zdtukd5q.json")

st_lottie(lottie_coding, height=300, key="cyber")

st.markdown("# Phishing 101")

st.markdown("""
            ### Apa itu Phishing?
            <p align="justify">
            Phishing adalah salah satu kejahatan dunia maya dimana korban dihubungi melalui email, pesan teks, ataupun telefon oleh seseorang yang menyamar 
            sebagai lembaga yang sah untuk memikat korban sehingga memberikan data sensitifnya seperti informasi pribadi, 
            rekening bank, detail kartu kredit, bahkan password akun milik korban. 
            Informasi tersebut kemudian digunakan untuk mengakses akun-akun penting yang dapat mengakibatkan pencurian identitas hingga kerugian material.</p align="justify"> 
            
            <p align="justify">Phishing itu sendiri? Istilah Phishing sendiri berasal dari kata “Fishing” yang artinya “Memancing”.
            Dimana kemudian dijabarkan sebagai memancing korban untuk terperangkap dalam jebakan sehingga korban memberikan informasi-informasi penting.</p align="justify">
            
           <p align="justify"> Serangan Phishing menjadi lebih canggih dan sering secara transparan menunjuk korban yang ditargetkan, dimana korban mengijinkan penyerangnya 
            untuk mengamati semuanya sementara korban menavigasikan situsnya, lalu kemudian mentransfer beberapa hal yang bersifat rahasia kepada penyerangnya.
            Selama tahun 2020, Phishing adalah serangan yang paling sering dilakukan oleh para penjahat dunia maya, devisi Internet Crime Complaint Center
            milik FBI melaporkan dua kali lipat lebih banyak insiden Phishing dari pada tipe kejahatan dunia maya lainnya. </p align="justify">
            
            ### Tipe-tipe Phising
            Ada beberapa tipe serangan Phishing antara lain: 
            
            * Email Phising
            
              <p align="justify"> Phishing disampaikan dengan spam email, dan tidak dipersonalisasi atau ditargetkan kepada individu atau perusahaan secara spesifik – 
              istilah ini disebut dengan Phishing “masal”. Konten Phishing masal sangat bervariasi tergantung dari tujuan penyerang – 
              umumnya menirukan pelayanan bank atau keuangan, penyedia email dan produktivitas cloud, dan juga pelayanan streaming. Email Phising dibagi
              menjadi tiga macam, yaitu:</p align="justify">
              
            """, unsafe_allow_html=True)
components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div id="accordion">
            <div class="card">
                <div class="card-header" id="headingOne">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                    Spear Phising
                    </button>
                </h5>
                </div>
                <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Spear Phishing adalah sebuah serangan yang melibatkan penyerang secara langsung menargetkan organisasi tertentu atau seseorang dengan
                    mencoba mencuri login credential mereka. 
                    <p align="justify">Pada dasarnya serangan ini menciptakan dan mengirim sebuah email kepada seseorang untuk membuat 
                    orang itu berpikir bahwa email itu legal. Target eksekutif dari tipe Spear Phising adalah mereka yang bekerja di departemen 
                    keuangan yang mempunyai akses pelayanan dan keuangan perusahaan.
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingTwo">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Whaling dan CEO Fraud
                    </button>
                </h5>
                </div>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Whaling mengarahkan untuk melakukan penyerangan Phising yang secara khusus diarahkan kepada senior executive atau para petinggi perusahaan. 
                    CEO Fraud merupakan kebalikan dari Whaling. Penyerang biasanya membuat email palsu yang katanya berasal dari CEO atau 
                    petinggi perusahaan dengan tujuan membuat karyawan disuatu organisasi melakukan sebuah tindakan tertentu, biasanya mengarahkan untuk 
                    mentransfer uang ke rekening luar negeri.
                </div>
                </div>
            </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingThree">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                    Clone Phising
                    </button>
                </h5>
                </div>
                <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Clone Phishing adalah sejenis serangan dimana peretas menyalin email yang sah dari suatu organisasi yang terpercaya dan membuat tampilannya hampir
                    identik dengan yang asli. Lampiran atau tautan dalam email diganti dengan versi yang berbahaya dan kemudian dikirim dari alamat email yang dipalsukan 
                    sehingga nampak seperti pengirim sebenarnya. Biasanya tipe ini meretas pihak ketiga sebelum kemudian diubah dan dikirimkan kepada target.
                </div>
                </div>
            </div>
            </div>
            """,
            height=380,
)
st.markdown("""
                   
            * Voice Phising
            
              <p align="justify">
              Voice Phishing atau Vishing adalah salah satu tipe yang beraksi dengan menggunakan telefon (biasanya dari alat IP telefon) 
              untuk melakukan penyerangan Phishing. Penyerang biasanya memanggil nomor dalam jumlah besar dan memainkan rekamanan otomatis –
              terkadang menggunakan synthesizer text-to-speech – yang membuat klaim palsu tentang aktivitas penipuan pada rekening bank atau 
              kartu kredit korban. Nomor telepon yang menelpon akan dipalsukan untuk menunjukkan nomor asli bank atau instansi yang ditiru. 
              Korban kemudian diarahkan untuk memanggil nomor telepon yang telah dikendalikan oleh penyerang, yang kemudian meminta korban 
              memasukkan informasi sensitive untuk “menyelesaikan” penipuan yang tengah terjadi.
            
            * SMS Phising

              <p align="justify">
              SMS Phishing atau smishing secara konseptual mirip dengan email Phishing, dimana perbedaannya penyerang menggunakan pesan teks ponsel 
              untuk mengirim “umpan”. Serangan smishing biasanya mengundang korban untuk mengklik tautan, menghubungi nomor telepon, atau menghubungi 
              alamat email yang telah dikirim pelaku melalui pesan SMS. Korban kemudian diarahkan untuk memberikan informasi pribadi yang nantinya 
              akan digunakan pelaku untuk melakukan aksi kejahatannya.</p align="justify"> 
            
            * Website Spoofing
            
              <p align="justify">
              Dengan Website Spoofing, seorang peretas membuat website palsu yang telihat seperti yang asli. Kemudian ketika target atau pengguna menggunakan 
              website tersebut dan masuk kedalamnya, informasi dari terget atau pengguna akan didapatkan dan dikumpulkan oleh peretas.
            
            * Search Engine Phising
              
              <p align="justify">
              Sebuah Search Engine Phishing menyerang dengan melibatkan seorang peretas untuk membuat produk palsu yang terlihat atraktif. Ketika informasi 
              muncul tiba-tiba di mesin pencarian, target akan diminta untuk memasukkan informs sensitive sebelum melakukan pembayaran yang kemudian diarahkan kepada peretas. 
            
            ### Kerugian Akibat Phising
            <p align="justify">
            Kerugian paling utama akibat Phishing adalah kerugian finansial. Banyak perusahaan ataupun perorangan yang kehilangan sejumlah uang mereka akibat kejahatan ini. 
            Kebanyakan tujuan dari tindak kejahatan ini adalah mengambil uang target. Dan kerugian selanjutnya adalah tersebarnya informasi pribadi korban 
            yang dapat disalah gunakan dan dijual ke darkweb.
            
            ### Cara-Cara untuk menghadapi dan menghindari kejahatan Phising
            Ada 10 cara yang dapat digunakan untuk menghadapi dan menghindar dari kejahatan Phising, antara lain:            
            """, unsafe_allow_html=True)
components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div id="accordion">
            <div class="card">
                <div class="card-header" id="headingSatu">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseSatu" aria-expanded="false" aria-controls="collapseSatu">
                    Tetap Mendapat Informasi tentang Phishing
                    </button>
                </h5>
                </div>
                <div id="collapseSatu" class="collapse" aria-labelledby="headingSatu" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Penipuan Phishing baru sedang dikembangkan setiap saat. Tanpa mendapatkan informasi terbaru tentang Phishing, 
                    kita mungkin secara tidak sengaja dapat menjadi salah satu korbannya. Tetap memperhatikan berita dan perkembangan tentang mereka. 
                    Dengan mendapatkan informasi sedini mungkin dapat membuat kita terhindar dari kejahatan Phishing ini. 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingDua">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseDua" aria-expanded="false" aria-controls="collapseDua">
                    Berfikir sebelum Mengklik
                    </button>
                </h5>
                </div>
                <div id="collapseDua" class="collapse" aria-labelledby="headingDua" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Tidak masalah untuk mengklik link pada situs yang terpercaya. Mengklik sebuah link yang muncul dari email random dan pesan instan, 
                    bagaimanapun bukan tindakan yang tepat. Pertimpangan link yang tidak kamu yakini sebelumnya. Apakah link tersebut akan mengarahkan 
                    ke tujuan yang tepat? 
                    <p align="justify">Sebuah Phishing email mengklaim dari perusahaan legal dan ketika kita klik link menuju website terlihat website 
                    yang begitu mirip dengan aslinya. Kebanyakan email Phishing dimulai dengan kalimat “Dear Customer” jadi kita perlu waspada ketika 
                    menerima email seperti ini. Ketika ragu-ragu, pergi langsung untuk mencari informasi dari pada mengklik link yang berpotensi bahaya. 
                </div>
                </div>
            </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingTiga">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTiga" aria-expanded="false" aria-controls="collapseTiga">
                    Install Toolbar Anti-Phishing 
                    </button>
                </h5>
                </div>
                <div id="collapseTiga" class="collapse" aria-labelledby="headingTiga" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Kebanyak browser internet yang terkenal dilengkapi dengan toolbars Anti-Phishing. Kebanyakan toolbar secara cepat memeriksa situs yang kamu kunjungi 
                    dan membandingkan dengan list situs Phishing yang terlah diketahui. Ketika kamu secara tidak sengaja menemukan sebuah situs berbahaya, 
                    toolbar tersebut akan memperingatkan. Ini hanya salah satu lapisan dari melindungi dari serangan Phishing, dan ini semua gratis. 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingEmpat">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseEmpat" aria-expanded="false" aria-controls="collapseEmpat">
                    Memeriksa Keamanan Situs 
                    </button>
                </h5>
                </div>
                <div id="collapseEmpat" class="collapse" aria-labelledby="headingEmpat" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Sebuah hal biasa untuk sedikit khawatir mengenai sensitifitas penyediaan informasi terkait keuangan secara online. 
                    Selama kita menggunakan website yang terjamin, bagaimanapun kita tidak akan terkena beberapa masalah. 
                    Sebelum memasukkan beberapa informasi, periksa URL dari website tersebut diawali dengan “http” dan terdapat icon 
                    yang terkunci dan dekat dengan bar alamat. Periksa sertifikat keamanan situs dengan teliti. Jika kamu mendapatkan 
                    pesan yang menyatakan website tertentu yang mungkin mengandung file berbahaya, jangan buka website tersebut.
                     
                    <p align="justify">Jangan pernah download file dari email atau website yang berbahaya. Meskipun mesin pencarian menunjukkan link 
                    yang mungkin mengarahkan pengguna kepada halaman web Phishing yang mana terdapat banyak produk dengan harga murah. 
                    Jika pengguna melakukan pembayaran pada website tersebut, detail dari kartu kredit akan dapat diakses oleh para peretas. 
 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingLima">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseLima" aria-expanded="false" aria-controls="collapseLima">
                    Periksa Akun Online Secara Berkala
                    </button>
                </h5>
                </div>
                <div id="collapseLima" class="collapse" aria-labelledby="headingLima" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Jika kamu tidak mengunjungi akun online untuk sementara, seseorang mungkin dapat mengisinya. Meskipun kamu secara teknik tidak membutuhkannya, 
                    periksa terus setiap akun secara berkala. Ubah password secara berkala juga. Untuk mencegah penyerangan Phishing akun bank dan scam kartu kredit, 
                    kamu harus memeriksa secara berkala. Periksa juga secara berkala akun keuanganmu dan periksa setiap pemasukkan secara hati-hati untuk 
                    meneliti transaksi janggal yang telah dibuat tanpa diketahui. 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingEnam">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseEnam" aria-expanded="false" aria-controls="collapseEnam">
                    Pastikan Browser Up to Date 
                    </button>
                </h5>
                </div>
                <div id="collapseEnam" class="collapse" aria-labelledby="headingEnam" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Bagian keamaan selalu tersedia untuk browser populer setiap saat. Mereka merilis respon keamanan untuk jalan keluar 
                    dari tindakan Phishing dan beberapa peretasan yang tidak dapat terhindarkan. Jika kamu tipikal yang mengacuhkan pesan 
                    tentang update browsermu, berhenti melakukan hal itu. Pertama kali sebuah update tersedia, download dan segara install. 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingTujuh">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTujuh" aria-expanded="false" aria-controls="collapseTujuh">
                    Menggunakan Firewalls 
                    </button>
                </h5>
                </div>
                <div id="collapseTujuh" class="collapse" aria-labelledby="headingTujuh" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Peran Firewalls yang tinggi sebagai penyangga antara kamu, komputer mu, dan pengacau dari luar. Kamu harus menggunakan dua macam yang berbeda: 
                    sebuah firewalls untuk desktop dan sebuah firewalls untuk jaringan. Opsi pertama adalah tipe software, dan opsi kedua adalah tipe hardware. 
                    Ketika kamu menggunakan bersama, mereka secara drastis mengurangi serangan dari peretas dan penjahat Phishing yang menerobos komputer dan juga jaringanmu. 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingTuDelapan">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTuDelapan" aria-expanded="false" aria-controls="collapseTuDelapan">
                    Waspada terhadap Pop-Up 
                    </button>
                </h5>
                </div>
                <div id="collapseTuDelapan" class="collapse" aria-labelledby="headingTuDelapan" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Pop-up Windows sering menyamar sebagai sebuah website legal yang kompeten. Semuanya seringkali adalah percobaan dari Phishing. 
                    Banyak browser populer yang memberi ijin untuk melarang sebuah pop-up, kamu juga dapat mengijinkan mereka. Jika satu pesan masuk 
                    dan menerobos, jangan klik pada tombol batal, tombol itu akan mengarahkanmu kepada situs Phishing, lebih baik klik “x” kecil yang terdapat di sudut bawah window. 
                </div>
                </div>
            </div>
            <div class="card">
                <div class="card-header" id="headingSembilan">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseSembilan" aria-expanded="false" aria-controls="collapseSembilan">
                    Jangan Pernah Memberikan Informasi Pribadi 
                    </button>
                </h5>
                </div>
                <div id="collapseSembilan" class="collapse" aria-labelledby="headingSembilan" data-parent="#accordion">
                <div class="card-body">
                    <p align="justify">Sebagai peraturan umum, kamu jangan pernah memberikan informasi pribadi atau informasi keuangan yang sensitive pada internet. 
                    Peraturan ini semua menilik balik pada Online Amerika, ketika pengguna seringkali diperingati tentang penipuan Phishing. 
                    Ketika ragu, pergi ke halaman utama dari website perusahaan dan tanyakan, dapatkan nomor mereka dan segera hubungi mereka. 
                    Kebanyakan email Phishing akan mengarahkan mu kehalaman dimana diminta untuk memasukkan informasi keuangan atau informasi pribadi. 
                    
                    <p align="justify">Sebagai pengguna internet tidak seharusnya dengan percaya masuk dalam link yang dikirim melalui email. 
                    Jangan pernah mengirim email dengan informasi yang sensitive kepada setiap orang. Selalu periksa alamat website. Sebuah website resmi dimulai dengan “http”. 
                </div>
                </div>
            </div>
             <div class="card">
                <div class="card-header" id="headingSepuluh">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseSepuluh" aria-expanded="false" aria-controls="collapseSepuluh">
                    Gunakan Software Antivirus
                    </button>
                </h5>
                </div>
                <div id="collapseSepuluh" class="collapse" aria-labelledby="headingSepuluh" data-parent="#accordion">
                <div class="card-body">
                   <p align="justify">Ada banyak alasan untuk menggunakan software antivirus. Tanda special yang masuk ke dalam software antivirus akan dikawal melawan teknologi bebas hama. 
                   Hanya untuk membuat software mu tetap up to date. Definisi barunya adalah menambah semua waktu karena penipuan terbaru juga menambahkan semua waktu. 
                   Anti-spyware dan firewall diatur untuk melindungi serangan phishing dan membuat pengguna untuk terus memperbarui program secara berkala. 
                   
                  <p align="justify"> Firewall melindungi serangan akses dari file berbahaya dengan memblok serangan. Software antivirus memeriksa setiap file dari internet yang masuk ke dalam komputer.
                   Ini membantu untuk mengurangi kerusakan pada sistem. Kamu tidak harus takut terhadap penipuan Phishing. Dengan tetap memprediksi dan waspada, 
                   kamu harus menikmati internet dengan bebas dan tanpa rasa takut. 
                </div>
                </div>
            </div>
            </div>
            """,
            height=1000,
)
