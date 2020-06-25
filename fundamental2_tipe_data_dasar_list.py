print('\nTipe data skalar => tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)
print('-' * 10)

print('\nTipe ada array/list/daftar')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Five')
print(anak)
print('-' * 10)

for i in anak:
    print(f'Hai {i}')

print('-' * 10)
print(f'Hai {anak[1]}')
print('-' * 10)

for index_anak in range(0, len(anak)):
    print(f'{index_anak + 1} Hai {anak[index_anak]}')
