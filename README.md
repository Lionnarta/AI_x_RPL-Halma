# Halma Game with Minimax and Local Search

## Deskripsi Permainan

Halma Game merupakan salah satu permainan jenis checker yang merupakan salah satu bagian dari competitive game yang bisa dimainkan oleh dua player. Pada kesempatan kali ini, Halma Game yang kami bangun akan menyediakan fitur untuk bermain melawan CPU atau Bot yang sudah diimplementasikan pada permainan ini. Bot yang kami bangun terdiri atas dua jenis, yaitu bot yang mengimplementasikan pendekatan Minimax Algorithm dalam penentuan aksinya dan bot yang mengimplementasikan Minimax Algorithm dengan kombinasi dengan algoritma Local Search.

## NOTICE

Aplikasi executable `.exe` berada di folder `exe`. Namun, file tersebut selalu _crash_ saat dijalankan dan penyebabnya masih belum diketahui.

## Getting Started

Instruksi-instruksi berikut ini akan membimbing Anda dalam tahap instalasi aplikasi dan cara menjalankannya. Langkah-langkah berikut dijalankan di OS Windows. Library PyGame yang kami gunakan ada masalah kompatibilitas dengan Linux.

### Prerequisites

Berikut ini adalah persiapan environment yang dibutuhkan untuk menjalankan aplikasi.

```
- Python >=3.7.7 && <3.9.0 (tested on Python 3.8)
- PyGame Library
- numpy library
```

### Installing

Berikut ini adalah langkah-langkah dalam penginstallan aplikasi:Untuk mempermudah dalam instalasi _dependencies_, kami sudah menyediakan `requirements.txt`. Untuk meng-_install_ _dependencies_ harap perhatikan langkah berikut

1. Pastikan Anda memiliki Python >= 3.7.7. Untuk instalasi, Anda bisa mengikuti langkahnya sendiri yang tertulis di website resmi [Python](https://www.python.org/). Pastikan versi yang Anda _install_ **BUKAN** 3.9.x.

2. Masuk ke directory ini dan buka `Command Prompt` Anda

3. Buat _virtual environment_ baru dalam direktori ini untuk meng-_install_ dependencies

```shell
$ py -m venv env
```

4. Masuk ke _virtual environment_ baru tersebut

```shell
$ .\env\Scripts\activate
```

5. Untuk memastikan Anda sudah berada di _virtual environment_ yang baru, Anda cukup melihat `Command Prompt` Anda yang akan diawali nama _virtual environment_ baru tersebut, yaitu `env`

```shell
(env)
```

5. Setelah proses pembuatan _virtual environment_ selesai dan Anda berada di dalamnya, Anda dapat meng-_install_ _dependencies_

```shell
$ pip install -r requirements.txt
```

## How to Run Program

### Alternatif 1: Menggunakan Python Script (Recommended)

1. Untuk menjalankan program, Anda harus masuk terlebih dahulu ke directory `./gui`. Hal ini dapat Anda lakukan dengan _command_ berikut

```shell
$ cd gui
```

2. Jalankan Python script `start_screen.py`

```shell
$ python start_screen.py
```

3. Program akan ditampilkan dalam tampilan Graphical User Interface (GUI).
4. User diberikan kebebasan untuk menentukan mode-mode permainan yang diinginkan.
5. Tekan PLAY untuk memulai permainan.

### Alternatif 2: Menggunakan Executable File (Not Working)

1. Masuk ke folder `./exe`

```shell
$ cd exe
```

2. Jalankan `start_screen.exe`

```shell
$ start_screen.exe
```

## Guideline: How To Use

1. Diberikan pilihan atau pengaturan mode permainan Halma, seperti

- Mode Permainan:
  - Player vs Minimax
  - Player vs Minimax Local Search
  - Minimax vs Minimax Local Search

2. Tentukan time limit per giliran yang diinginkan pada bagian T-limit
3. Jika memilih mode Player, pilih warna bidak yang diinginkan
4. Selamat bermain permainan Halma!

## Built With

- [Python](https://www.python.org/)

## Testing

Untuk menjalankan testing pada program pengekstrak, dapat dijalankan program secara command line interface sebagai berikut.

1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.

```shell
$ python GameManager.py
```

2. Masukkan input-input yang bersesuaian sesuai dengan yang diminta oleh program.

## Authors

1. **13518041 - Samuel**
2. **13518056 - Michael Hans**
3. **13518104 - Kevin Austin Stefano**
4. **13518128 - Lionnarta Savirandy**

## Acknowledgments

- Dosen IF3170 K1, Nur Ulfa Maulidevi
- Dosen IF3170 K2, Masayu Leylia Khodra
- Dosen IF3170 K3, Ayu Purwarianti
- IF3170 Inteligensi Buatan Tahun Ajaran 2020-2021
