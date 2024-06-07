# Movies System Recommendation 🎬

## Project Overview

Sistem rekomendasi adalah suatu system yang digunakan oleh para *user* / *customer* / pelanggan untuk mendapatkan produk yang diinginkan. Ide awal dari sistem rekomendasi sendiri adalah untuk menggunakan beberapa sumber informasi, tujuan utama dari sistem rekomendasi adalah untuk meningkatkan penjualan produk.Beberapa platform yang menyuguhkan film, seperti *Vidio*, *Netflix*, *WeTV*, *Viu*, *Disney+*, *Amazon Prime*, *HBO*, dan lainnya menerapkan sistem rekomendasi yang sama.

Proyek ini penting untuk diselesaikan karena sistem rekomendasi dapat memberikan nilai tambah yang signifikan bagi pengguna dan penyedia layanan. Bagi pengguna, sistem rekomendasi memungkinkan mereka menemukan konten yang sesuai dengan preferensi mereka tanpa perlu mencari secara manual, sehingga meningkatkan kepuasan dan pengalaman menonton. Bagi penyedia layanan, sistem rekomendasi dapat meningkatkan keterlibatan pengguna dan loyalitas pelanggan, yang pada akhirnya dapat meningkatkan pendapatan. Selain itu, dengan persaingan yang semakin ketat di industri streaming, memiliki sistem rekomendasi yang efektif dapat menjadi keunggulan kompetitif bisnis.

Mengembangkan sistem rekomendasi yang akurat dan relevan juga membantu dalam memahami tren dan perilaku pelanggan, yang dapat digunakan untuk strategi pemasaran yang lebih efektif dan pengembangan konten yang lebih tepat sasaran. Oleh karena itu, menyelesaikan proyek ini tidak hanya memberikan manfaat langsung kepada pengguna dan penyedia layanan, tetapi juga mendukung pertumbuhan dan inovasi dalam industri hiburan secara keseluruhan.

Referensi dari proyek ini adalah sebagai berikut:

[*Movie Recommendation System Using Collaborative Filtering*](https://ieeexplore.ieee.org/abstract/document/8663822) [1]

[*Movie Recommender System Using Content-based and Collaborative Filtering*](https://ieeexplore.ieee.org/document/9872515) [2]
  
## Business Understanding

### Problem Statements

Bagaimana cara merekomendasikan *movie* yang disukai pengguna lain dapat direkomendasikan kepada pengguna lainnya?

### Goals

Dapat membuat sistem rekomendasi yang akurat berdasarkan *ratings* dan aktivitas pengguna pada masa lalu.

### Solution Statements

Solusi pembuatan model yang dilakukan adalah dengan menerapkan 2 algoritma *machine learning*, terbatas pada ***Content Based Filtering*** dan ***Collaborative Filtering***. Diterapkannya 2 algoritma tersebut sama-sama bertujuan untuk memberikan rekomendasi mengenai film kepada pengguna. Algoritma *content based filtering* akan merekomendasikan film kepada pengguna berdasarkan aktivitas film pengguna di masa lalu. Sedangkan, algoritma *collaborative filtering* akan merekomendasikan pengguna berdasarkan rating yang paling tinggi.

- ***Collaborative-filtering*** : Algoritma *Collaborative Filtering* menggunakan pendekatan model dari tingkah laku pengguna sebelumnya seperti kunjungan pengguna pada suatu alamat tayangan atau memberikan rating terhadap beberapa *item* pilihan pengguna dan juga yang dilakukan oleh pengguna lain yang nantinya *item* tersebut akan dijadikan acuan untuk memberikan prediksi terhadap pengguna lain atau pengguna yang berkaitan.

- ***Content-based filtering*** : Algoritma *Content Based Filtering* melakukan pedekatan melalui pendekatan diskrit sesuai dengan item yang memiliki kedekatan dalam tipikal *item*, pendekatan ini melakukan pengambilan data dari suatu item yang memiliki karakterisitik yang berdekatan.

## Data Understanding
Data atau dataset yang digunakan pada proyek machine learning ini adalah data ***Movie Recommendation Data*** yang didapat dari situs [kaggle](https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data) [3]. 

Variabel-variabel pada *movie recommendation data* adalah sebagai berikut :

1. *links* : merupakan daftar tautan movie.
2. *movies* : merupakan daftar *movie* yang tersedia
3. *ratings* : merupakan daftar penilaian yang diberikan pengguna terhadap *movie*.
4. *tags* : merupakan daftar kata kunci dari *movie* tersebut

### Explanatory Data Analysis (EDA)

#### Univariate Analysis

Untuk memahami keempat dataset `movies`, `ratings`, `links`, dan `tags`, maka dilakukan EDA *Univariate Analysis*.

Tabel 1. Ratings Variable

|       | userId        | movieId       | rating        | timestamp    |
|-------|---------------|---------------|---------------|--------------|
| count | 100836.000000 | 100836.000000 | 100836.000000 | 1.008360e+05 |
| mean  | 326.127564    | 19435.295718  | 3.501557      | 1.205946e+09 |
| std   | 182.618491    | 35530.987199  | 1.042529	    | 2.162610e+08 |
| min   | 1.000000      | 1.000000      | 0.500000      | 8.281246e+08 |
| 25%   | 177.000000    | 1199.000000   | 3.000000      | 1.019124e+09 |
| 50%   | 325.000000    | 2991.000000   | 3.500000      | 1.186087e+09 |
| 75%   | 477.000000    | 8122.000000   | 4.000000      | 1.435994e+09 |
| max   | 610.000000    | 193609.000000 | 5.000000      | 1.537799e+09 |

Pada Tabel 1, dapat diketahui dengan detail bahwa data `rating` memiliki minimum *rating* sebesar 0.5, dan maksimal *rating* sebesar 5, serta rata-rata *rating* sebesar 3.5.

## Data Preparation

Proses *Data Preparation* yang digunakan yaitu:

1. Mengatasi *missing value* : menyeleksi data, apakah data tersebut ada yang kosong atau tidak, jika ada data kosong maka kemudian akan dihapus.
2. Membagi data menjadi data *training* dan *validasi* : untuk membagi data untuk dilatih dan validasi. Dalam melakukan *splitting*, digunakan rasio 80:20, yang berarti 80% *data training*, dan 20% *data testing*.
3. Menggabungkan variabel : untuk menggabungkan beberapa variabel berdasarkan *id* yang sifatnya unik (berbeda dari yang lain).
4. Mengurutan data : mengurutkan data berdasarkan *movieId* secara *asceding*.
5. Mengatasi duplikasi data : menghilangkan duplikasi data yang memiliki nilai sama.
6. Konversi data menjadi *list* : untuk mengubah data menjadi *list*
7. Membuat *dictionary* : Untuk membuat *dictionary* dari data yang ada.
8. Menggunakan TF-IDF Vectorizer : untuk melakukan pembobotan.
9. Melakukan *preprocessing* : untuk menghilangkan permasalahan-permasalahan yang dapat mengganggu hasil daripada proses data.
9. Mapping data : untuk memetakan data.
10. *Cosine Similarity*: menggunakan *cosine_similarity* dari *library sklearn* untuk mendapatkan mengetahui *similarity degree*.

## Modeling

Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Proses ini dilakukan dengan menggunakan tiga algoritma, yakni ***Content Based Filtering*** dan ***Collaborative Filtering***. Hasil akhir yang diharapkan dari sistem rekomendasi ini adalah dapat memudahkan pengguna untuk mencari film yang diinginkan, baik berdasarkan preferensi film yang serupa, ataupun rekomendasi berdasarkan rating.

1. Dalam membangun ***Content Based Filtering***, hal pertama yang akan dilakukan adalah melakukan pembobotan terhadap fitur `*genre*` menggunakan module `*TfidfVectorizer*` dari *library* `*sklearn*` untuk mendapatkan genre apa saja yang ada. Selanjutnya, digunakan `*module*` `*cosine_similarity*` dari *library* `*sklearn*`. Digunakan fungsi `*movie_recommendation* `dengan parameter `*movie_name*` untuk membangun model. Pada fungsi tersebut juga ditetapkan `*k = 5*` yang berarti akan mengeluarkan rekomendasi 5 film teratas berdasarkan genre.

Tabel 2. *Movie* yang disukai oleh pengguna dimasa lalu.

|      | id     | movie_name            | genre                   |
|------|--------|-----------------------|-------------------------|
| 1505 | 122916 | Thor: Ragnarok (2017) | Action|Adventure|Sci-Fi | 

Pada Tabel 2, dapat dilihat bahwa pengguna menyukai *movie* yang berjudul *Thor: Ragnarok (2017)* yang bergenre *Action*, *Adventure*, dan *Sci-Fi*.
Mendapatkan rekomendasi movie yang mirip dengan *Thor: Ragnarok (2017*).

Tabel 3. Rekomendasi movie yang mirip dengan *Thor: Ragnarok (2017)*

|   | movie_name                                       | genre                   | 
|---|--------------------------------------------------|-----------------------  |
| 0 | Star Wars: Episode I - The Phantom Menace (1999) | Action|Adventure|Sci-Fi |
| 1 | Star Wars: Episode III - Revenge of the Sith     | Action|Adventure|Sci-Fi |
| 2 | Fantastic Four (2005)                            | Action|Adventure|Sci-Fi |
| 3 | Serenity (2005)                                  | Action|Adventure|Sci-Fi |
| 4 | Star Wars: Episode IV - A New Hope (1977)	       | Action|Adventure|Sci-Fi |

Pada Tabel 3, dapat dilihat bahwa pengguna menyukai *movie* yang berjudul *Thor: Ragnarok (2017)* yang bergenre *Action*, *Adventure*, dan *Sci-Fi*.
Mendapatkan rekomendasi movie yang mirip dengan *Thor: Ragnarok (2017*).

2. Dalam membangun **Collaborative Filtering**, dilakukan `training` dan pembuatan model `RecommenderNet`. Training dilakukan dengan optimizer `Adam` dan matriks evaluasi `RMSE`. Model `RecommenderNet` akan menghitung skor _match_ di antara dua _embedding layers_ milik _user_ dan _movie_ melalui `dot_product`, dan menambahkan bias ke keduanya. _Match_ skor kemudian akan berada pada skala interval 0 hingga 1 melalui `sigmoid`.

Tabel 4. Movie genre yang direkomendasikan berdasarkan rating tertinggi.

| Movie Name                                                                  | Genre                          |
| ----------------------------------------------------------------------------| -------------------------------|
| Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964) | Comedy|War                     |
| 2001: A Space Odyssey (1968)                                                | Adventure|Drama|Sci-Fi         |
| It's a Wonderful Life (1946)                                                | Children|Drama|Fantasy|Romance |
| Great Escape, The (1963)                                                    | Action|Adventure|Drama|War     |
| Princess and the Warrior, The (Krieger und die Kaiserin, Der) (2000)        | Drama|Romance                  |

Tabel 5. Movie Top 10 yang direkomendasikan.

| Movie Name                                              | Genre                            |
| --------------------------------------------------------| ---------------------------------|
| More (1998)                                             | Animation|Drama|Sci-Fi|IMAX      |
| Crossing Delancey (1988)                                | Comedy|Romance                   |
| Lady Jane (1986)                                        | Drama|Romance                    |
| Awful Truth, The (1937)                                 | Comedy|Romance                   |
| Come and See (Idi i smotri) (1985)                      | Drama|War                        |
| Adam's Rib (1949)                                       | Comedy|Romance                   |
| Safety Last! (1923)                                     | Action|Comedy|Romance            |
| Into the Woods (1991)                                   | Adventure|Comedy|Fantasy|Musical |
| Match Factory Girl, The (Tulitikkutehtaan tyttö) (1990) | Comedy|Drama                     |
| Reefer Madness: The Movie Musical (2005)                | Comedy|Drama|Musical             |

Pada Tabel 4 dan Tabel 5, *movie* yang bergenre drama menjadi *movie* yang paling tinggi ratingnya. Kemudian *top 10 movie* yang direkomendasikan sistem adalah *movie* dengan genre *comedy* dan *romance*.

## Evaluation

### Content Based Filtering
Evaluasi yang dapat digunakan adalah matriks presisi. Presisi merupakan sebuah kemampuan dari alat ukur untuk menunjukkan angka yang sama bila dipakai secara berulang-ulang dalam kondisi pengukuran dan obyek ukur yang sama. Pada kasus ini, presisi akan memprediksi label yang benar terhadap keseluruhan prediksi. 

Rumus perhitungan matrik presisi:

\[ \text{Precision} = \frac{\text{Number of relevant recommendations}}{\text{Total number of recommendations}} \]

Dari hasil rekomendasi yang ditampilkan pada bagian modeling, diketahui bahwa pengguna akan mencari rekomendasi film terkait ` Thor: Ragnarok (2017)`. Kemudian, sistem rekomendasi memberikan 5 film terkait yang memiliki genre serupa, yakni `Action|Adventure|Sci-Fi`. Berdasarkan rumus presisi di atas, diketahui bahwa keseluruhan rekomendasi yang diberikan memiliki genre serupa dengan film yang dicari rekomendasinya. Artinya, presisi sistem yang dibangun sebesar 5/5 atau 100%.

### Collaborative Filtering
Evaluasi metrik yang digunakan untuk mengukur kinerja model adalah metrik RMSE (*Root Mean Squared Error*). RMSE merupakan metode pengukuran dengan mengukur perbedaan nilai dari prediksi sebuah model sebagai estimasi atas nilai yang diobservasi, dan merupakan hasil kuadrat dari MSE. Keakuratan metode estimasi kesalahan pengukuran ditandai dengan adanya nilai RMSE yang kecil. 

Semakin kecil nilai yang diperoleh RMSE, semakin akurat juga modelnya.

Rumus perhitungan matrik MSE: 

$$RMSE = \sqrt {\frac{1}{N} \sum_{i=1}^{N} (\hat{y_{i}} - y_{i})^2}$$

ket:

$\mathrm{RMSE}$	= _mean squared error_

${n}$ = _number of data points_

$Y_{i}$	= _observed values_ atau _ground truth_ dari nilai sebenarnya.

$\hat{Y}_{i}$ =	_predicted values_ atau _estimated target values_.

Gambar 1. Model Evaluasi

![model_evaluasi](https://github.com/muhammadsahrul59/Movie-System-Recommendation/assets/101655285/c27a8ca8-4d14-4f24-999d-74d2f043519d)

Pada Gambar 1, visualisasi tersebut terdaoat proses *training model* yang cukup *smooth* dan model *konvergen* pada *epochs* sekitar 150. Dari proses ini, diperoleh nilai *error* akhir sebesar sekitar 0.19 dan *error* pada data validasi sebesar 0.21. Hasil analisis akhir menyatakan bahwa model yang dibuat mengalami *`Overvitting`*, karena hasil plot dari data test terus mengalami penurunan dibandingkan dengan hasil plot dari *`data_train`*.

Referensi :


[1] C.-S. M. Wu, D. Garg, and U. Bhandary, “Movie Recommendation System Using Collaborative Filtering,” IEEE Xplore, Nov. 01, 2018. https://ieeexplore.ieee.org/abstract/document/8663822

[2] J. F. Mohammad and S. Urolagin, “Movie Recommender System Using Content-based and Collaborative Filtering,” IEEE Xplore, May 01, 2022. https://ieeexplore.ieee.org/document/9872515

[3] “Movie Recommendation Data,” www.kaggle.com. https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data (accessed Jun. 07, 2024).
