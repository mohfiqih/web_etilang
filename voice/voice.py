# import speech_recognition as srec
# from gtts import gTTS
# import os
# from playsound import playsound

# def perintah():
#     mendengar = srec.Recognizer()
#     with srec.Microphone() as source:
#         print('Mendengarkan....')
#         suara = mendengar.listen(source,phrase_time_limit=5)
#         try: 
#             print('Diterima...')
#             dengar = mendengar.recognize_google(suara, language='id-ID')
#             print(dengar)
#         except: 
#             pass
#         return dengar

# def etilang(self):
#     teks = (self)
#     bahasa = 'id'
#     namafile = 'voice/pertanyaan/apaetilang.mp3'
#     jawaban = 'voice/jawaban/etilang.mp3'
#     def reading():
#         suara = gTTS(text=teks, lang=bahasa, slow=False)
#         suara.save(namafile)
#      #    play = playsound(jawaban)
#         os.system(f'start {jawaban}')
#     reading()

# def maaf(self):
#     teks = (self)
#     bahasa = 'id'
#     namafile = 'voice/pertanyaan/maafsalah.mp3'
#     jawaban = 'voice/jawaban/maaf.mp3'
#     def reading():
#         suara = gTTS(text=teks, lang=bahasa, slow=False)
#         suara.save(namafile)
#      #    play = playsound(jawaban)
#         os.system(f'start {jawaban}')
#     reading()

# def run_michelle():
#     Layanan = perintah()
#     etilang(Layanan)
#     # maaf(Layanan)

# run_michelle()