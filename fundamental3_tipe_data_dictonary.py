"""
Tipe data dictionary sekedar menghubungkan antara KEY dan value
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'ayah': 'father', 'ibu': 'mother', 'istri': 'wife'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData yang dikirimkan dari server gojek, untuk memberikan info driver disekitar kita')
data_from_gojek = {
    'date': '2020-06-25',
    'driver_list': [
        {'name': 'Eko', 'distance': 10},
        {'name': 'Dwi', 'distance': 30},
        {'name': 'Tri', 'distance': 100},
        {'name': 'Catur', 'distance': 1000}
    ]
}

print(data_from_gojek)
print(f"\nDriver disekitar ini {data_from_gojek['driver_list']}")
print(f"Driver #1 adalah {data_from_gojek['driver_list'][0]}")
print(f"Driver #4 adalah {data_from_gojek['driver_list'][3]}")

print(f"\n Driver terdekat berjarak {data_from_gojek['driver_list'][0]['distance']} Meter")
