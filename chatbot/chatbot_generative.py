from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token='5960247905:AAGTxmvwqVx8iLLWeR8duS4mPBhVgyZr1iE')
dp = Dispatcher(bot)

# Welcome
button1 = KeyboardButton('Tanya')
button2 = KeyboardButton('Info')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

# Pertanyaan
button3 = KeyboardButton('Apa itu E-Tilang')
button4 = KeyboardButton('Bagaimana cara membayar denda secara online?')
buttoncek = KeyboardButton('Bagaimana cara mengecek besaran denda di situs web kejaksaan?')
buttonbesar = KeyboardButton('Berapa besar denda E-Tilang?')
buttonbatas = KeyboardButton('Kapan tenggat pembayaran denda?')
buttonpelanggar = KeyboardButton('Bagaimana pemilik kendaraan mengetahui ia telah melanggar?')
buttonsurat = KeyboardButton('Saat menerima surat konfirmasi, apakah pemilik kendaraan sudah ditilang?')
buttonkonfir = KeyboardButton('Bagaimana mengonfirmasi Surat Konfirmasi?')
buttonpemilik = KeyboardButton('Pemilik kendaraan bukan pengemudi kendaraan saat pelanggaran terjadi. Apa yang harus dilakukan?')
buttonjual = KeyboardButton('Apabila kendaraan yang melanggar telah dijual sebelumnya, apa yang harus dilakukan?')
buttonrental = KeyboardButton('Bagaimana jika mobil rental kena tilang?')
buttonalur = KeyboardButton('Bagaimana alur pembayaran kendaraan yang kena tilang elektronik?')
buttongagal = KeyboardButton('Bagaimana jika gagal konfirmasi?')
buttonjenis = KeyboardButton('Apa saja jenis pelanggaran yang terdeteksi E-Tilang?')
buttoncarakerja = KeyboardButton('Bagaimana cara kerja E-Tilang?')
buttontahapan = KeyboardButton('Bagaimana tahapan etilang')
buttoncek = KeyboardButton('Bagaimana cara mengecek E-Tilang secara online?')
buttoncara = KeyboardButton('Cara pembayaran denda E-Tilang?')
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4).add(buttoncek).add(buttonbesar).add(buttonbatas).add(buttonpelanggar).add(buttonsurat).add(buttonkonfir).add(buttonpemilik).add(buttonjual).add(buttonrental).add(buttonalur).add(buttonjenis).add(buttoncarakerja).add(buttontahapan).add(buttoncek).add(buttoncara)

# Bayar
button5 = KeyboardButton('Bank BRI')
button6 = KeyboardButton('ATM BRI')
button7 = KeyboardButton('Mobile Banking BRI')
button8 = KeyboardButton('Internet Banking BRI')
button9 = KeyboardButton('EDC BRI')
button10 = KeyboardButton('Transfer ATM dari bank lain')
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button5).add(button6).add(button7).add(button8).add(button9).add(button10)

# Denda
# button11 = KeyboardButton('Cek Denda')
# button12 = KeyboardButton('Besar Denda')
# keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button11).add(button12)

# Welcome
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
     await message.reply("Hallo! Im E-Bot, Ada yang bisa dibantu??", reply_markup=keyboard1)

# Tanya
@dp.message_handler(commands=['tanya'])
async def tanya(tymessage: types.Message):
     await tymessage.reply("Mau tanya apa nih??", reply_markup=keyboard2)

# Cara Bayar
@dp.message_handler(commands=['carabayar'])
async def tanya(tymessage: types.Message):
     await tymessage.reply("Mau bayar lewat apa??", reply_markup=keyboard3)

# answer welcome
@dp.message_handler()
async def kb_answer(message: types.Message):
     if message.text == 'Tanya':
          await message.answer('Klik /tanya')
     elif message.text == 'Info':
          await message.answer('Klik /info')
     elif message.text == 'Apa itu E-Tilang':
          await message.answer('Tilang elektronik atau e-tilang merupakan upaya pemerintah dalam menegakkan hukum lalu lintas berbasis teknologi informasi. E-tilang merupakan salah satu upaya pemerintah untuk menekan angka pelanggaran peraturan lalu lintas. Hal ini adalah sebuah terobosan dalam merevolusi hukum lalu lintas dari yang sebelumnya konvensional menjadi lebih modern, menggunakan sejenis kamera CCTV yang disebar di berbagai ruas jalan.')
     elif message.text == 'Cara pembayaran denda E-Tilang?':
          await message.answer('Perangkat ETLE ini merekam dan memotret setiap pelanggaran lalu lintas pada lokasi yang dipasang kamera tilang elektronik. Dari hasil rekaman itu, petugas akan mengidentifikasi plat nomor dan data kendaraan menggunakan Electronic Registration & Identification (ERI). Surat konfirmasi akan dikirimkan via Pos ke alamat pemilik kendaraan bermotor untuk konfirmasi atas pelanggaran yang terjadi. Surat konfirmasi adalah dasar untuk penindakan tilang tersebut. Batas konfirmasi setelah menerima surat itu adalah delapan hari. Jika kendaraan yang dimaksud bukan kendaraan milik orang yang dikirimkan surat konfirmasi, maka itu harus diberitahukan. Cara konfirmasi adalah melalui situs web atau datang langsung ke kantor Sub Direktorat Penegakan Hukum. Usai pelanggaran terkonfirmasi, petugas akan menerbitkan tilang. Pembayaran tilang dilakukan via BRI Virtual Account (BRIVA) dengan kode pembayaran untuk pelanggaran yang terverifikasi dalam penegakan hukum.')
     elif message.text == 'Bagaimana cara membayar denda secara online?':
          await message.answer('/carabayar')
     elif message.text == 'Bank BRI':
          await message.answer('Cara bayar e-tilang via kantor Bank BRI -Ambil nomor antrian transaksi teller dan isi slip setoran. -Isi 15 angka Nomor Pembayaran Tilang pada kolom Nomor Rekening dan Nominal titipan denda tilang elektronik pada slip setoran. -Serahkan slip setoran kepada Teller BRI. -Teller BRI akan melakukan validasi transaksi. -Simpan Slip Setoran hasil validasi sebagai bukti bayar denda tilang elektronik yang sah. -Slip setoran diserahkan ke penindak ETLE untuk ditukarkan dengan barang bukti yang disita.')
     elif message.text == 'ATM BRI':
          await message.answer('Cara Bayar denda tilang elektronik via ATM BRI Masukkan Kartu Debit BRI dan PIN Anda. -Pilih menu Transaksi Lain > Pembayaran > Lainnya > BRIVA. -Masukkan 15 angka Nomor Pembayaran Tilang. -Di halaman konfirmasi, pastikan detil denda tilang elektronik sudah sesuai seperti Nomor BRIVA, Nama Pelanggar, dan Jumlah Pembayaran. -Ikuti instruksi untuk menyelesaikan transaksi. -Copy struk ATM sebagai bukti cara bayar e-tilang yang sah dan disimpan. -Struk ATM asli diserahkan ke penindak ETLE untuk ditukarkan dengan barang bukti yang disita.')
     elif message.text == 'Mobile Banking BRI':
          await message.answer('Cara bayar e-tilang via Mobile Banking BRI -Login aplikasi BRI Mobile Pilih Menu Mobile Banking BRI > Pembayaran > BRIVA -Masukkan 15 angka Nomor Pembayaran Tilang -Masukkan nominal pembayaran sesuai jumlah denda tilang elektronik yang harus dibayarkan -Transaksi akan ditolak jika pembayaran tidak sesuai dengan jumlah denda titipan -Masukkan PIN Simpan notifikasi SMS sebagai bukti cara bayar e-tilang -Tunjukkan notifikasi SMS ke penindak ETLE untuk ditukarkan dengan barang bukti yang disita.')
     elif message.text == 'Internet Banking BRI':
          await message.answer('Bayar denda tilang elektronik via Internet Banking BRI -Login pada alamat Internet Banking BRI -Pilih menu Pembayaran Tagihan > Pembayaran > BRIVA -Pada kolom kode bayar, Masukkan 15 angka Nomor Pembayaran Tilang -Di halaman konfirmasi, pastikan detil denda tilang elektronik sudah sesuai seperti Nomor BRIVA, Nama Pelanggar dan Jumlah Pembayaran -Masukkan password dan mToken -Cetak atau simpan struk pembayaran BRIVA sebagai bukti cara bayar e tilang -Tunjukkan bukti bayar denda tilang elektronik ke penindak ETLE untuk ditukarkan dengan barang bukti yang disita.')
     elif message.text == 'EDC BRI':
          await message.answer('Cara bayar e-tilang via EDC BRI -Pilih menu Mini ATM > Pembayaran > BRIVA -Swipe kartu Debit BRI Anda -Masukkan 15 angka Nomor Pembayaran Tilang -Masukkan PIN -Di halaman konfirmasi, pastikan detil pembayaran sudah sesuai seperti Nomor BRIVA, Nama Pelanggar dan Jumlah Pembayaran -Copy dan Simpan struk transaksi sebagai bukti pembayaran -Tunjukkan bukti pembayaran ke penindak ETLE untuk ditukarkan dengan barang bukti yang disita.')
     elif message.text == 'Transfer ATM dari bank lain':
          await message.answer('Bayar denda tilang elektronik via transfer ATM dari bank lain -Masukkan kartu Debit dan PIN Anda -Pilih menu Transaksi Lainnya > Transfer > Ke Rek Bank Lain -Masukkan kode bank BRI (002) kemudian diikuti dengan 15 angka Nomor Pembayaran Tilang -Masukkan nominal denda tilang elektronik -Transaksi akan ditolak jika pembayaran tidak sesuai dengan jumlah denda titipan -Ikuti instruksi untuk menyelesaikan transaksi -Simpan struk transaksi sebagai bukti bayar cara bayar e tilang.')
     elif message.text == 'Bagaimana cara mengecek besaran denda di situs web kejaksaan?':
          await message.answer('Membuka situs web https://tilang.kejaksaan.go.id/ 1. Memasukkan nomor registrasi tilang atau nomor blangko atau nomor berkas tilang, lalu klik Cari 2. Nomor tilang itu tertera di surat penilangan yang diberikan pihak kepolisian 3. Situs web tilang Kejaksaan akan memberikan informasi mengenai tilang daring, kode pembayaran, serta jumlah nominal denda tilang yang harus dibayarkan 4. Membayar tilang daring melalui situs tilang.kejaksaan.go.id')
     elif message.text == 'Berapa besar denda E-Tilang?':
          await message.answer('-Melanggar rambu lalu lintas dan marka jalan denda tilang elektronik Rp 500.000 atau pidana kurungan 2 bulan -Tidak mengenakan sabuk keselamatan denda tilang elektronik sebesar Rp 250.000 atau kurungan penjara 2 bulan -Mengemudi sambil mengoperasikan Smartphone didenda Rp 750.000 atau kurungan penjara 3 bulan -Melanggar batas kecepatan denda e-tilang Rp 500.000 atau kurungan 2 bulan -Menggunakan pelat nomor palsu denda tilang elektronik Rp500.000 atau pidana kurungan 2 bulan -Berkendara melawan arus didenda Rp 500.000 atau kurangan paling lama 2 bulan -Menerobos lampu merah, denda e-tilang Rp 500.000 atau kurungan 2 bulan -Tidak menggunakan helm atau helm yang digunakan tidak sesuai Standar Nasional Indonesia (SNI) denda tilang elektronik Rp 250.000 atau penjara maksimal 1 bulan -Berboncengan lebih dari 3 orang denda e-tilang Rp 250.000 atau kurungan 1 bulan -Tidak menyalakan lampu saat siang hari bagi sepeda motor didenda Rp 100.000 atau dipenjara 15 hari.')
     elif message.text == 'Kapan tenggat pembayaran denda?':
          await message.answer('Batas waktu terakhir untuk pembayaran adalah 15 hari dari tanggal pelanggaran. Jika gagal melakukan ini, maka Surat Tanda Nomor Kendaraan (STNK) Anda akan terblokir')
     elif message.text == 'Bagaimana pemilik kendaraan mengetahui ia telah melanggar?':
          await message.answer('Perangkat secara otomatis menangkap pelanggaran lalu lintas yang dimonitor dan mengirimkan media barang bukti pelanggaran ke Back Office di RTMC Polda Metro Jaya. Kemudian, petugas mengidentifikasi data kendaraan menggunakan Electronic Registration & Identification (ERI) sebagai sumber data kendaraan. Atas informasi itu, petugas pun mengirimkan surat konfirmasi ke alamat pemilik kendaraan selambat-lambatnya tiga hari setelah pelanggaran dilakukan')
     elif message.text == 'Saat menerima surat konfirmasi, apakah pemilik kendaraan sudah ditilang?':
          await message.answer('Belum. Surat Konfirmasi adalah langkah awal dari penindakan di mana pemilik kendaraan wajib konfirmasi tentang kepemilikan kendaraan dan pengemudi kendaraan pada saat terjadinya pelanggaran')
     elif message.text == 'Bagaimana mengonfirmasi Surat Konfirmasi?':
          await message.answer('Pemilik kendaraan diberi waktu selama 8 hari dari terjadinya pelanggaran untuk mengonfirmasi')
     elif message.text == 'Pemilik kendaraan bukan pengemudi kendaraan saat pelanggaran terjadi. Apa yang harus dilakukan?':
          await message.answer('Kendaraan yang dioperasikan di jalan raya, memiliki potensi mencelakakan pengguna jalan raya lainnya, bahkan sampai meninggal dunia. Pemilik kendaraan wajib bertanggung jawab kepada siapa ia meminjamkan kendaraan tersebut')
     elif message.text == 'Bagaimana jika mobil rental kena tilang?':
          await message.answer('harus ada penambahan poin-poin perjanjian saat transaksi menyewakan kendaraan. Penyewa harus bertanggung jawab menyelesaikan sanksi jika terbukti telah melanggar lalu lintas menggunakan kendaraan sewaan. Jangan sampai pengusaha rental mobil dan motor tidak mengetahui jika kendaraan yang disewakan melanggar aturan lalu lintas')
     elif message.text == 'Bagaimana alur pembayaran kendaraan yang kena tilang elektronik?':
          await message.answer('Tahap 1 Perangkat kamera CCTV di ruas jalan secara otomatis menangkap pelanggaran lalu lintas yang dimonitor dan mengirimkan media barang bukti pelanggaran. Tahap 2 Petugas mengidentifikasi data kendaraan menggunakan Electronic Registration and Identification (ERI) sebagai sumber data kendaraan. Tahap 3 Petugas mengirimkan surat konfirmasi pelanggaran ke alamat pemilik kendaraan bermotor untuk permohonan konfirmasi atas pelanggaran yang terjadi. Surat tersebut dikirim lewat pos. Tahap 4 Pemilik Kendaraan melakukan konfirmasi via website sesuai yang tercantum dalam surat tersebut atau datang langsung ke kantor Sub Direktorat Penegakan Hukum. Konfirmasi pelanggaran berlaku selama delapan hari')
     elif message.text == 'Bagaimana jika gagal konfirmasi?':
          await message.answer('Kemungkinan karena pelanggar telah pindah alamat sehingga surat tilang tidak sampai atau kendaraan telah dijual (beralih pemilik). Jika gagal melakukan konfirmasi, Surat Tanda Nomor Kendaraan (STNK) akan diblokir sementara')
     elif message.text == 'Apa saja jenis pelanggaran yang terdeteksi E-Tilang?':
          await message.answer('1. Melanggar rambu lalu lintas dan marka jalan, 2. Tidak mengenakan sabuk keselamatan, 3. Mengemudi sambil mengoperasikan smartphone, 4. Melanggar batas kecepatan, 5. Menggunakan pelat nomor palsu, 6. Berkendara melawan arus -Menerobos lampu merah, 7. Tidak menggunakan helm, 8. Berboncengan lebih dari 3 orang, 9.Tidak menyalakan lampu saat siang hari bagi sepeda motor.')
     elif message.text == 'Bagaimana cara kerja E-Tilang?':
          await message.answer('Kamera tilang elektronik dapat menangkap berbagai pelanggaran lalu lintas yang dilakukan oleh pengguna jalan. Mulai dari pelanggaran ganjil-genap, marka jalan, penggunaan ponsel saat berkendara, dan pelanggaran lainnya. Selain dapat menganalisis berbagai jenis pelanggaran, kamera berbentuk CCTV ini juga mengidentifikasi dan menganalisis jenis kendaraan, bahkan nomor registrasi kendaraan bermotor melalui nomor plat kendaraan yang dijadikan rekaman output dalam bentuk image ataupun video. Jadi, data-data kendaraan yang melanggar dari kamera tersebut akan disajikan kepada petugas kepolisian dan nantinya akan diverifikasi. Selanjutnya, petugas akan mengirimkan surat konfirmasi ke alamat pemilik kendaraan sesuai dengan registrasi kendaraan tersebut. Jadi, para pelanggar di jalan akan mendapatkan surat tilang ke alamat yang tertera pada surat kendaraan.')
     elif message.text == 'Bagaimana tahapan E-Tilang':
          await message.answer('Perangkat ETLE ini merekam dan memotret setiap pelanggaran lalu lintas pada lokasi yang dipasang kamera tilang elektronik. Dari hasil rekaman itu, petugas akan mengidentifikasi plat nomor dan data kendaraan menggunakan Electronic Registration & Identification (ERI). Surat konfirmasi akan dikirimkan via Pos ke alamat pemilik kendaraan bermotor untuk konfirmasi atas pelanggaran yang terjadi. Surat konfirmasi adalah dasar untuk penindakan tilang tersebut. Batas konfirmasi setelah menerima surat itu adalah delapan hari. Jika kendaraan yang dimaksud bukan kendaraan milik orang yang dikirimkan surat konfirmasi, maka itu harus diberitahukan. Cara konfirmasi adalah melalui situs web atau datang langsung ke kantor Sub Direktorat Penegakan Hukum. Usai pelanggaran terkonfirmasi, petugas akan menerbitkan tilang. Pembayaran tilang dilakukan via BRI Virtual Account (BRIVA) dengan kode pembayaran untuk pelanggaran yang terverifikasi dalam penegakan hukum.')
     elif message.text == 'Bagaimana cara mengecek E-Tilang secara online?':
          await message.answer('Pertama, buka browser di ponsel dan ketik link https://etle-pmj.info/id/check-data Kedua, masukkan nomor plat kendaraan, nomor mesin kendaraan, dan nomor rangka kendaraan. Ketiga, klik Cek Data yang nantinya akan muncul informasi terkait waktu, lokasi, dan tipe pelanggaran kendaraan. Setelah terdapat informasi status pelanggaran maka pelanggar diharuskan untuk membayar denda sebesar yang tertera pada email atau SMS pelanggar.')
     else:
          await message.answer(f'Pesan anda untuk /start adalah : {message.text}')

executor.start_polling(dp)
print('bot running')