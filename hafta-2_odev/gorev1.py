
import pandas as pd

try:
    df = pd.read_csv("train.csv")
except FileNotFoundError:
    print("train.csv dosyası bulunamadı!")
    exit()

print("Veri setinin ilk 5 satırı:")
print(df.head())

# Veri seti hakkında genel bilgi
print("\nVeri seti hakkında genel bilgi:")
print(df.info())

# Eksik verileri kontrol etme
print("\nEksik veri sayısı:")
print(df.isnull().sum())

# Eksik verileri doldurma
# 'Age' sütunundaki eksik değerleri medyan ile dolduruyoruz
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)
# 'Embarked' sütunundaki eksik değerleri en sık görülen değerle dolduruyoruz
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
# 'Cabin' sütunundaki eksik değerleri 'Unknown' ile dolduruyoruz
if 'Cabin' in df.columns:
    df['Cabin'].fillna('Unknown', inplace=True)

# Yeni bir sütun ekleme
# 'FamilySize' sütunu, 'SibSp' ve 'Parch' sütunlarının toplamı + 1 olarak hesaplanır
if 'SibSp' in df.columns and 'Parch' in df.columns:
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Kategorik verileri sayısal değerlere dönüştürme
# 'Sex' sütununu 0 (erkek) ve 1 (kadın) olarak kodluyoruz
if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    if df['Sex'].isnull().any():
        print("Uyarı: 'Sex' sütununda beklenmeyen değerler var!")

# 'Embarked' sütununu sayısal değerlere dönüştürme
if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
    if df['Embarked'].isnull().any():
        print("Uyarı: 'Embarked' sütununda beklenmeyen değerler var!")

# Veri setinin güncellenmiş halini görüntüleme
print("\nGüncellenmiş veri setinin ilk 5 satırı:")
print(df.head())

print("\nGüncellenmiş veri tipleri:")
print(df.info())

# Veri setini yeni bir CSV dosyasına kaydetme
df.to_csv("train_titanic.csv", index=False)
print("\nManipüle edilmiş veri seti 'manipulated_titanic.csv' olarak kaydedildi.")