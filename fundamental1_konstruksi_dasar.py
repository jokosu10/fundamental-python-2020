# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Prosedural Eksekusi Berurutan
print('Hello World!')
print('by Joko Susilo')
print('Tanggal 24 Juni 2020')
print('-' * 10)

# PERCABANGAN dengan eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus saja ya !')
else:
    print('jalan lainnya ya')
print('-' * 10)

# PERULANGAN
jumlah_anak = 4

for index_anak in range(0, jumlah_anak):
    print(f'Halo anak ke # {index_anak + 1}')
print('-' * 10)

item = ['kopi', 'nasi', 'teh', 'jeruk']

for isi in item:
    print(isi)
print('-' * 10)

warna = {'Merah', 'Biru', 'Kuning', 'Biru'}
for i in warna:
    print(i)
print('-' * 10)

sentence = 'jokosu10'
count_character = len(sentence)
for huruf in sentence:
    print(huruf)
print(count_character)
