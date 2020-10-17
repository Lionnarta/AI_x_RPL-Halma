# Halma Game with Minimax and Local Search

# Deskripsi Permainan
Halma Game merupakan salah satu permainan jenis checker yang merupakan salah satu bagian dari competitive game yang bisa dimainkan oleh dua player. Pada kesempatan kali ini, Halma Game yang kami bangun akan menyediakan fitur untuk bermain melawan CPU atau Bot yang sudah diimplementasikan pada permainan ini. Bot yang kami bangun terdiri atas dua jenis, yaitu bot yang mengimplementasikan pendekatan Minimax Algorithm dalam penentuan aksinya dan bot yang mengimplementasikan Minimax Algorithm dengan kombinasi dengan algoritma Local Search.

## Getting Started
Instruksi-instruksi berikut ini akan membimbing Anda dalam tahap instalasi aplikasi dan cara menjalankannya.

### Prerequisites
Berikut ini adalah persiapan environment yang dibutuhkan untuk menjalankan aplikasi.

```
- Python 3.x.x
- PyGame Library
```

### Installing
Berikut ini adalah langkah-langkah dalam penginstallan aplikasi:
1. Install aplikasi Python 3.x.x melalui Windows Installer atau command sudo apt install python yang sudah tersedia pada Linux.
2. Lakukan penginstalan Library PyGame dengan command sebagai berikut pada terminal biasa.
```
pip install pygame
```
3. Semua prerequisites sudah disiapkan dengan baik.

## How to Run Program
1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python Application.py
```
2. Program akan ditampilkan dalam tampilan Graphical User Interface (GUI).
3. User diberikan kebebasan untuk menentukan mode-mode permainan yang diinginkan.
4. Tekan PLAY untuk memulai permainan.

## Guideline: How To Use
1. Diberikan pilihan atau pengaturan mode permainan Halma, seperti
-  Mode Permainan:
   -  Player vs Minimax
   -  Player vs Minimax Local Search
   -  Minimax vs Minimax Local Search
2. Tentukan time limit per giliran yang diinginkan pada bagian T-limit
3. Jika memilih mode Player, pilih warna bidak yang diinginkan
4. Selamat bermain permainan Halma!

## Built With

* [Python](https://www.python.org/)

## Testing

Untuk menjalankan testing pada program pengekstrak, dapat dijalankan program secara command line interface sebagai berikut.
1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python GameManager.py
```
2. Masukkan input-input yang bersesuaian sesuai dengan yang diminta oleh program.

## Authors

1. **13518041 - Samuel**
2. **13518056 - Michael Hans**
3. **13518104 - Kevin Austin Stefano**
4. **13518128 - Lionnarta Savirandy**

## Acknowledgments

* Dosen IF3170 K1, Nur Ulfa Maulidevi
* Dosen IF3170 K2, Masayu Leylia Khodra
* Dosen IF3170 K3, Ayu Purwarianti
* IF3170 Inteligensi Buatan Tahun Ajaran 2020-2021