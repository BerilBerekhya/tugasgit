import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# 1
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# 2
print("DataFrame setelah diberikan peningkatan gaji 5%:")
print(df)

print("\nRingkasan perubahan:")
perubahan = df['Gaji'] - data['Gaji']
print(perubahan)

# 3
df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)

# 4
print("\nDataFrame setelah peningkatan gaji tambahan untuk usia di atas 30 tahun:")
print(df)

# Ringkasan hasil:
print("\nRingkasan hasil:")
perubahan_total = df['Gaji'] - data['Gaji']
print(perubahan_total)

print('')
