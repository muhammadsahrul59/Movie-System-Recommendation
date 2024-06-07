# -*- coding: utf-8 -*-
"""submission_sistem_rekomendasi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y6ow1eqUOeNMETBfqBdqMxZnUUVozl7E

# **Proyek Sistem Rekomendasi Movie**

Nama     : Muhammad Sahrul

email    : m.sahrul59@gmail.com

github   : https://github.com/muhammadsahrul59

linkedin : https://www.linkedin.com/in/sahrul59

# **Project Overview**

Sistem rekomendasi adalah suatu system yang digunakan oleh para user / *customer* /pelanggan untuk mendapatkan produk yang diinginkan. Ide awal dari sistem rekomendasi sendiri adalah untuk menggunakan beberapa sumber informasi, tujuan utama dari sistem rekomendasi adalah untuk meningkatkan penjualan produk.Beberapa platform yang menyuguhkan film, seperti *Vidio*, *Netflix*, *WeTV*, *Viu*, *Disney+*, *Amazon Prime*, *HBO*, dan lainnya menerapkan sistem rekomendasi yang sama.

Proyek ini penting untuk diselesaikan karena sistem rekomendasi dapat memberikan nilai tambah yang signifikan bagi pengguna dan penyedia layanan. Bagi pengguna, sistem rekomendasi memungkinkan mereka menemukan konten yang sesuai dengan preferensi mereka tanpa perlu mencari secara manual, sehingga meningkatkan kepuasan dan pengalaman menonton. Bagi penyedia layanan, sistem rekomendasi dapat meningkatkan keterlibatan pengguna dan loyalitas pelanggan, yang pada akhirnya dapat meningkatkan pendapatan. Selain itu, dengan persaingan yang semakin ketat di industri streaming, memiliki sistem rekomendasi yang efektif dapat menjadi keunggulan kompetitif bisnis.

Mengembangkan sistem rekomendasi yang akurat dan relevan juga membantu dalam memahami tren dan perilaku pelanggan, yang dapat digunakan untuk strategi pemasaran yang lebih efektif dan pengembangan konten yang lebih tepat sasaran. Oleh karena itu, menyelesaikan proyek ini tidak hanya memberikan manfaat langsung kepada pengguna dan penyedia layanan, tetapi juga mendukung pertumbuhan dan inovasi dalam industri hiburan secara keseluruhan.

Referensi dari proyek ini adalah sebagai berikut:
1. *Movie Recommendation System Using Collaborative Filtering* [1]
2. *Movie Recommender System Using Content-based and Collaborative Filtering* [2]

## **Business Understanding**

### **Problem Statements**

Bagaimana cara merekomendasikan *movie* yang disukai pengguna lain dapat direkomendasikan kepada pengguna lainnya?

### **Goals**
Dapat membuat sistem rekomendasi yang akurat berdasarkan *ratings* dan aktivitas pengguna pada masa lalu.

### **Solution statements**
Solusi pembuatan model yang dilakukan adalah dengan menerapkan 2 algoritma *machine learning*, terbatas pada ***Content Based Filtering*** dan ***Collaborative Filtering***. Diterapkannya 2 algoritma tersebut sama-sama bertujuan untuk memberikan rekomendasi mengenai film kepada pengguna. Algoritma *content based filtering* akan merekomendasikan film kepada pengguna berdasarkan aktivitas film pengguna di masa lalu. Sedangkan, algoritma *collaborative filtering* akan merekomendasikan pengguna berdasarkan rating yang paling tinggi.

- ***Collaborative-filtering*** : Algoritma *Collaborative Filtering* menggunakan pendekatan model dari tingkah laku pengguna sebelumnya seperti kunjungan pengguna pada suatu alamat tayangan atau memberikan rating terhadap beberapa *item* pilihan pengguna dan juga yang dilakukan oleh pengguna lain yang nantinya *item* tersebut akan dijadikan acuan untuk memberikan prediksi terhadap pengguna lain atau pengguna yang berkaitan.

- ***Content-based filtering*** : Algoritma *Content Based Filtering* melakukan pedekatan melalui pendekatan diskrit sesuai dengan item yang memiliki kedekatan dalam tipikal *item*, pendekatan ini melakukan pengambilan data dari suatu item yang memiliki karakterisitik yang berdekatan.

# **Data Understanding**

Data atau dataset yang digunakan pada proyek machine learning ini adalah data ***Movie Recommendation Data*** yang didapat dari situs *kaggle* [3].

Variabel-variabel pada *movie recommendation data* adalah sebagai berikut :

1. *links* : merupakan daftar tautan movie.
2. *movies* : merupakan daftar *movie* yang tersedia
3. *ratings* : merupakan daftar penilaian yang diberikan pengguna terhadap *movie*.
4. *tags* : merupakan daftar kata kunci dari *movie* tersebut

Menginstal *library* *Kaggle* yang diperlukan untuk mengunduh dataset dari *Kaggle*
"""

!pip install -q kaggle
from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle

"""Mengunduh dataset dari *Kaggle* menggunakan API token yang telah diunggah dan disimpan di '*kaggle.json*'"""

!kaggle datasets download -d rohan4050/movie-recommendation-data

"""Lakukan unzip file dengan menerapkan kode berikut."""

!unzip /content/movie-recommendation-data.zip

"""Selanjutnya, baca data-data di atas dengan menggunakan fungsi pandas.read_csv. Implementasikan kode berikut."""

import pandas as pd

movies_df = pd.read_csv('/content/ml-latest-small/movies.csv')
ratings_df = pd.read_csv('/content/ml-latest-small/ratings.csv')
links_df = pd.read_csv('/content/ml-latest-small/links.csv')
tags_df = pd.read_csv('/content/ml-latest-small/tags.csv')


print('Jumlah data movie: ', len(movies_df.movieId.unique()))
print('Jumlah data tags movie: ', len(tags_df.movieId.unique()))
print('Jumlah data link movie : ', len(links_df.movieId.unique()))
print('Jumlah data ratings dari pengguna : ', len(ratings_df.userId.unique()))
print('Jumlah data ratings dari movie : ', len(ratings_df.movieId.unique()))

"""# **Explanatory Data Analysis**

## **Univariate Data Analysis**

### **Movies Variable**

Eksplorasi variabel *movies*, yaitu daftar *movie* yang mana terdapat informasi mengenai *movieId*, *title*, dan *genres* dari *movie*.
"""

movies_df

"""`info()` digunakan untuk mengetahui informasi terkait tipe data dan *non-null* data pada *dataset movies*."""

movies_df.info()

"""`isna()` dilakukan untuk mengetahui apakah ada *missing value* pada *dataset movies*."""

movies_df.isna().sum()

movies_df.shape

"""*Dataset movies* memiliki banyak data **10,329** ***sample*** dengan **3 fitur**"""

print('Banyak data: ', len(movies_df.movieId.unique()))
print('Judul movies yang ada: ', movies_df.title.unique())

"""### **Links Variable**

Eksplorasi variabel *links*, yaitu daftar *link movie*.

`info()` digunakan untuk mengetahui informasi terkait tipe data dan *non-null* data pada *dataset links*.
"""

links_df.info()

"""### **Ratings Variable**

Eksplorasi variabel *ratings* data yang akan digunakan pada model yaitu data *rating* (data pengguna).
"""

ratings_df

"""`info()` digunakan untuk mengetahui informasi terkait tipe data dan *non-null* data pada *dataset ratings*."""

ratings_df.info()

"""`describe()` digunakan untuk mengetahui informasi terkait *mean*, *std*, *min*, *quartil*, dan *max*.

Dari tabel yang didapatkan, dapat diketahui bahwa dataset rating, memiliki minimum rating 0.5 dan maksimum rating 5 yang dapat diberikan oleh pengguna.
"""

ratings_df.describe()

print('Jumlah userID: ', len(ratings_df.userId.unique()))
print('Jumlah placeID: ', len(ratings_df.movieId.unique()))
print('Jumlah data rating: ', len(ratings_df))

"""`isna()` dilakukan untuk mengetahui apakah ada *missing value* pada *dataset ratings*."""

ratings_df.isna().sum()

"""# **Data Preprocessing**

## **Menggabungkan Movie**

Menggunakan *library numpy* dan fungsi *concatenate()* untuk menggabungkan beberapa *file*. Setelah itu menggunakan movieId yang unik sebagai acuan dalam penggabungan.
"""

import numpy as np

# Menggabungkan seluruh item_id pada kategori Movie
movie_all = np.concatenate((movies_df.movieId.unique(),
                            ratings_df.movieId.unique(),
                            links_df.movieId.unique(),
                            tags_df.movieId.unique()))

movie_all = np.sort(np.unique(movie_all))

print('Jumlah seluruh data movie berdasarkan movieId: ', len(movie_all))

"""## **Menghubungkan Seluruh User**

Terapkan cara yang sama pada kategori *variabel User*. Dengan fungsi `concatenate()` dari *library numpy*, gabungkan seluruh data pada kategori *variabel User*.
"""

# Menggabungkan seluruh userID
user_all = np.concatenate((ratings_df.userId.unique(),
                           tags_df.userId.unique()))

# Menghapus data yang sama kemudian mengurutkannya
user_all = np.sort(np.unique(user_all))

print('Jumlah seluruh user: ', len(user_all))

"""## **Mengetahui Jumlah Rating**

Menggabungkan ***links_df***, ***movies_df***, ***ratings_df***, dan ***tags_df*** ke dalam *dataframe movie_info*. Serta menggabungkan *dataframe ratings* dengan *movie_info* berdasarkan nilai *movieId*
"""

# Menggabungkan file rating, dan movies ke dalam dataframe movie_info
movie_info = pd.concat([movies_df, ratings_df, tags_df, links_df])

# Menggabungkan dataframe rating dengan movie_info berdasarkan nilai item_id
movie = pd.merge(ratings_df, movie_info , on='movieId', how='left')
movie

"""Hasil jumlah *rating* diatas terdapat banyak sekali *missing value* maka selanjutnya lakukan cek missing value."""

movie.isnull().sum()

"""Terdapat banyak missing value pada sebagian besar fitur. Hanya fitur userID_x, movieId, rating_x, dan timestamp_x saja yang memiliki 0 missing value. Selanjutnya, menggabungkan rating berdasarkan movieId"""

movie.groupby('movieId').sum()

"""## **Menggabungkan Data dengan Fitur Nama Movie**

Pertama, definisikan variabel *all_movie_rate* dengan variabel *rating_df* yang telah kita ketahui sebelumnya.
"""

# Definisikan dataframe rating ke dalam variabel all_movie_rate
all_movie_rate = ratings_df
all_movie_rate

"""Selanjutnya, untuk mengetahui nama *movie* dengan *movieId* tertentu, gabungkan data *movies_df* yang berisikan *movieId*, *title*, dan *genres* berdasarkan *movieId* dan assign ke variabel *all_movie_name* dengan fungsi merge dari *library pandas*."""

# Menggabungkan all_movie_name dengan dataframe geo berdasarkan movieId
all_movie_name = pd.merge(all_movie_rate, movies_df[['movieId','title','genres']], on='movieId', how='left')

# Print dataframe all_movie_name
all_movie_name

"""Menggabungkan *variabel* *all_movie_name* yang diperoleh dari tahapan sebelumnya dengan fitur *movieId* dan *tag*."""

# Menggabungkan dataframe genres dengan all_movie_name dan memasukkannya ke dalam variabel all_movie
all_movie = pd.merge(all_movie_name, tags_df[['movieId','tag']], on='movieId', how='left')

# Print dataframe all_movie
all_movie

"""# **Data Preparation**

## **Menangani Missing Value**

Setelah proses penggabungan. Mengecek datanya apakah ada *missing value* atau tidak.
"""

# Mengecek missing value pada dataframe all_movie
all_movie.isnull().sum()

"""Terdapat 52549 *missing value* pada fitur *tag*, kemudian menghapus *missing value* dengan fungsi `dropna()`"""

# Membersihkan missing value dengan fungsi dropna()
all_movie_clean = all_movie.dropna()
all_movie_clean

"""Setelah menghapus missing value, maka data yang sebelumnya memiliki 285762 baris sekarang memiliki 233213 baris. Cek kembali missing value pada variabel all_movie_clean"""

# Mengecek kembali missing value pada variabel all_movie_clean
all_movie_clean.isnull().sum()

"""## **Menyamakan Movie berdasarkan movieId**

Mengurutkan *movie* berdasarkan *movieId* kemudian memasukkannya ke dalam variabel *fix_movie*
"""

# Mengurutkan movie berdasarkan movieId kemudian memasukkannya ke dalam variabel fix_movie
fix_movie = all_movie_clean.sort_values('movieId', ascending=True)
fix_movie

"""Mengetahui berapa jumlah fix_movie."""

# Mengecek berapa jumlah fix_movie
len(fix_movie.movieId.unique())

"""Membuat variabel *preparation* yang berisi *dataframe fix_movie* kemudian mengurutkan berdasarkan *movieId*."""

# Membuat variabel preparation yang berisi dataframe fix_movie kemudian mengurutkan berdasarkan movieId
preparation = fix_movie
preparation.sort_values('movieId')

"""Selanjutnya, gunakan data unik untuk dimasukkan ke dalam proses pemodelan. serta hapus data *duplicate* dengan fungsi `drop_duplicates()` berdasarkan *movieId*."""

# Membuang data duplikat pada variabel preparation
preparation = preparation.drop_duplicates('movieId')
preparation

"""Kemudian, melakukan konversi data series menjadi *list*. Dalam hal ini, menggunakan fungsi `tolist()` dari *library numpy*.


"""

# Mengonversi data series ‘movieId’ menjadi dalam bentuk list
movie_id = preparation['movieId'].tolist()

# Mengonversi data series ‘title’ menjadi dalam bentuk list
movie_name = preparation['title'].tolist()

# Mengonversi data series ‘genres’ menjadi dalam bentuk list
movie_genre = preparation['genres'].tolist()

print(len(movie_id))
print(len(movie_name))
print(len(movie_genre))

"""Membuat *dictionary* untuk menentukan pasangan *key-value* pada data *movie_id*, *movie_name*, dan *movie_genre* yang telah disiapkan sebelumnya."""

# Membuat dictionary untuk data ‘movie_id’, ‘movie_name’, dan ‘movie_genre’
movie_new = pd.DataFrame({
    'id': movie_id,
    'movie_name': movie_name,
    'genre': movie_genre
})

movie_new

"""# **Model Development dengan Content Based Filtering**

Mengecek data dan *assign dataframe* dari tahap sebelumnya ke dalam variabel data, sebagai berikut:
"""

data = movie_new
data.sample(5)

"""## **TF-IDF Vectorizer**

Teknik *TF-IDF Vectorizer* dapat digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kategori *movie*. Pada proyek ini, menggunakan fungsi `tfidfvectorizer()` dari *library sklearn*
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data cuisine
tf.fit(data['genre'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

"""Selanjutnya, lakukan fit dan transformasi ke dalam bentuk matriks."""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['genre'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""*Matriks* berukuran (1554, 24). Nilai 1554 merupakan ukuran data dan 24 merupakan matrik kategori *genre*.

Untuk menghasilkan *vektor tf-idf* dalam bentuk *matriks*, menggunakan fungsi `todense()`.
"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""Selanjutnya, *matriks tf-idf* untuk beberapa nama *movie* dan *genre*."""

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan genre
# Baris diisi dengan nama movie

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.movie_name
).sample(22, axis=1).sample(10, axis=0)

"""## **Cosine Similarity**

***Cosine Similarity*** menghitung derajat kesamaan (*similarity degree*) antar movie dengan teknik *cosine similarity*.
"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Membuat dataframe dari variabel *cosine_sim_df* dengan baris dan kolom berupa nama *movie*, serta melihat kesamaan *matrix* dari setiap *movie*."""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama movie
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['movie_name'], columns=data['movie_name'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap movie
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""## **Mendapatkan Rekomendasi**

Membuat fungsi *movie_recommendations* dengan beberapa parameter sebagai berikut:

- *Nama_movie* : Nama judul dari movie tersebut (*index* kemiripan *dataframe*).
- *Similarity_data* : *Dataframe* mengenai *similarity* yang telah didefinisikan sebelumnya
- *Items* : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah *‘movie_name’* dan *‘genre’*.
- *k* : Banyak rekomendasi yang ingin diberikan.
"""

def movie_recommendations(nama_movie, similarity_data=cosine_sim_df, items=data[['movie_name', 'genre']], k=5):
    """
    Rekomendasi Movie berdasarkan kemiripan dataframe

    Parameter:
    ---
    nama_movie : tipe data string (str)
                Nama judul dari movie tersebut (index kemiripan dataframe).
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan movie sebagai
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_movie].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_movie agar nama movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_movie, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""Terapkan kode di atas untuk menemukan rekomendasi movie yang mirip dengan Thor: Ragnarok (2017)."""

data[data.movie_name.eq('Thor: Ragnarok (2017)')]

"""Hasil di atas dapat dilihat bahwa pengguna menyukai *movie* yang berjudul *Thor: Ragnarok (2017)* yang bergenre *Action*, *Adventure*, dan *Sci-Fi*.
Mendapatkan rekomendasi movie yang mirip dengan *Thor: Ragnarok (2017*).
"""

# Mendapatkan rekomendasi movie yang mirip dengan Thor: Ragnarok (2017)
movie_recommendations('Thor: Ragnarok (2017)')

"""# **Model Development dengan Collaborative Filtering**

## **Data Understanding**

*Import library* yang dibutuhkan
"""

# Import library
import pandas as pd
import numpy as np
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

"""Ubah nama *variabel ratings* yang telah dibuat menjadi *df*."""

# Membaca dataset

df = ratings_df
df

"""## **Data Preparation**

Melakukan persiapan data untuk menyandikan (*encode*) fitur *‘user’* dan *‘movieId’* ke dalam *indeks integer*. Terapkan kode berikut.
"""

# Mengubah userId menjadi list tanpa nilai yang sama
user_ids = df['userId'].unique().tolist()
print('list userId: ', user_ids)

# Melakukan encoding userId
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userId : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke userId
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userId: ', user_encoded_to_user)

# Mengubah movieId menjadi list tanpa nilai yang sama
movie_ids = df['movieId'].unique().tolist()

# Melakukan proses encoding movieId
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}

# Melakukan proses encoding angka ke movieId
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

# Selanjutnya, petakan userId dan movieId ke dataframe yang berkaitan.

# Mapping userId ke dataframe genres
df['genres'] = df['userId'].map(user_to_user_encoded)

# Mapping movieD ke dataframe movies
df['movies'] = df['movieId'].map(movie_to_movie_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah movie
num_movie = len(movie_encoded_to_movie)
print(num_movie)

# Mengubah rating menjadi nilai float
df['ratings'] = df['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(df['rating'])


# Nilai maksimal rating
max_rating = max(df['rating'])

print('Number of User: {}, Number of movie: {}, Min Rating: {}, Max Rating: {}'.format(num_users, num_movie, min_rating, max_rating))

"""## **Membagi Data untuk Training dan Validasi**"""

# Mengacak dataset
df = df.sample(frac=1, random_state=42)
df

# membagi data train dan validasi dengan komposisi 80:20.
# Membuat variabel x untuk mencocokkan data genres  dan movies menjadi satu value
x = df[['genres', 'movies']].values

# Membuat variabel y untuk membuat ratings dari hasil
y = df['ratings'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""## **Data Training**

Membuat *class* *RecommenderNet* dengan keras *Model class*.
"""

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_movie, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movie = num_movie
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.movie_embedding = layers.Embedding( # layer embeddings movies
        num_movie,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movie, 1) # layer embedding movies bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    movie_vector = self.movie_embedding(inputs[:, 1]) # memanggil layer embedding 3
    movie_bias = self.movie_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)

    x = dot_user_movie + user_bias + movie_bias

    return tf.nn.sigmoid(x) # activation sigmoid

"""Selanjutnya, lakukan proses *compile* terhadap `model`."""

model = RecommenderNet(num_users, num_movie, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""menggunakan *Binary Crossentropy* untuk menghitung *loss function*, Adam (*Adaptive Moment Estimation*) sebagai *optimizer*, *dan root mean squared error* (RMSE) sebagai *metrics evaluation*.

Langkah berikutnya, mulailah proses training.
"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 64,
    epochs = 150,
    validation_data = (x_val, y_val)
)

"""## **Model Evaluasi**

Untuk melihat visualisasi proses training, buat plot metrik evaluasi dengan matplotlib.
"""

train_rmse = history.history['root_mean_squared_error']
val_rmse = history.history['val_root_mean_squared_error']

index_rmse_min = np.argmin(val_rmse)
index_rmse_max = np.argmax(val_rmse)

val_rmse_lowest = val_rmse[index_rmse_min]
val_rmse_highest = val_rmse[index_rmse_max]

epochs = [i + 1 for i in range(len(train_rmse))]
rmse_min_label = f"Best Epoch (lowest RMSE) is: {str(index_rmse_min + 1)}"
rmse_max_label = f"Best Epoch (highest RMSE) is: {str(index_rmse_max + 1)}"

plt.figure(figsize=(20, 8))
plt.style.use('fivethirtyeight')

plt.subplot(1, 2, 1)
plt.plot(epochs, train_rmse, 'r', label="Training RMSE")
plt.plot(epochs, val_rmse, 'g', label="Validation RMSE")
plt.scatter(index_rmse_min + 1, val_rmse_lowest, s=150, c='blue', label=rmse_min_label)
plt.title('Model_Metrics')
plt.xlabel("Epochs")
plt.ylabel('RMSE')
plt.legend()

plt.tight_layout()
plt.show()

"""Visualisasi diatas merupakan proses *training model* yang cukup *smooth* dan *model* *konvergen* pada *epochs* sekitar 150. Dari proses ini, memperoleh nilai *error* akhir sebesar sekitar 0.19 dan error pada data validasi sebesar 0.21.

## **Mendapatkan Rekomendasi Movie**
"""

movie_df = movie_new
df = pd.read_csv('/content/ml-latest-small/ratings.csv')

# Mengambil sample user
user_id = df.userId.sample(1).iloc[0]
movie_watched_by_user = df[df.userId == user_id]

# Operator bitwise (~), bisa diketahui di sini https://docs.python.org/3/reference/expressions.html
movie_not_watched = movie_df[~movie_df['id'].isin(movie_watched_by_user.movieId.values)]['id']
movie_not_watched = list(
    set(movie_not_watched)
    .intersection(set(movie_to_movie_encoded.keys())))

movie_not_watched = [[movie_to_movie_encoded.get(x)] for x in movie_not_watched]
user_encoder = user_to_user_encoded.get(user_id)
user_movie_array = np.hstack(
    ([[user_encoder]] * len(movie_not_watched), movie_not_watched))

"""Untuk mendapatkan rekomendasi *movies*, gunakan fungsi `model.predict()` dari *library Keras* dengan menerapkan kode berikut."""

ratings = model.predict(user_movie_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movie_ids = [
    movie_encoded_to_movie.get(movie_not_watched[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('movie with high ratings from user')
print('----' * 8)

top_movie_user = (
    movie_watched_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

movie_df_rows = movie_df[movie_df['id'].isin(top_movie_user)]
for row in movie_df_rows.itertuples():
    print(row.movie_name, ':', row.genre)

print('----' * 8)
print('Top 10 movie recommendation')
print('----' * 8)

recommended_movie = movie_df[movie_df['id'].isin(recommended_movie_ids)]
for row in recommended_movie.itertuples():
    print(row.movie_name, ':', row.genre)

"""Dari hasi di atas movie yang bergenre drama menjadi movie yang paling tinggi ratingsnya. Kemudian top 10 movie yang direkomendasikan sistem adalah movie dengan genre comedy dan romance.

Referensi :

[1] C.-S. M. Wu, D. Garg, and U. Bhandary, “Movie Recommendation System Using Collaborative Filtering,” IEEE Xplore, Nov. 01, 2018. https://ieeexplore.ieee.org/abstract/document/8663822

[2] J. F. Mohammad and S. Urolagin, “Movie Recommender System Using Content-based and Collaborative Filtering,” IEEE Xplore, May 01, 2022. https://ieeexplore.ieee.org/document/9872515

[3] “Movie Recommendation Data,” www.kaggle.com. https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data (accessed Jun. 07, 2024).
"""