# SuperChasierProject


## Intro
Super cashier adalah sebuah program sederhana berbasis bahasa pemograman python yang memungkinkan pengguna (pembelanja) melakukan self-service terhadap barang yang dibelinya.

## Fitur
Pada halaman muka, pengguna diminta unutk memasukkan nomor sesuai dengan menu yang menyertainya:
1. Add items            : untuk memulai berbelanja dengan memasukkan nama item, jumlah item, dan harga per item, yang kemudian dimasukkan dalam keranjang.
2. Update items         : untuk memperbaharui nama item, jumlah item, atau harga item telah pengguna masukkan dalam keranjang. 
3. Delete items         : untuk menghapus satu atau lebih nama item dari keranjang beserta jumlah dan harganya.
4. Reset all item       : untuk menghapus seluruh item dalam keranjang.
5. Check order          : untuk melihat keranjang belanja, apakah sudah sesuia dengan apa yang diharapkan pengguna.
6. Checkout cart        : untuk mengkahiri proses pembelanjaan dan melakukan finalisasi pembayaran dengan menampilkan total harga beserta diskon (jika memenuhi minimal pembelanjaan).

Bila pengguna belum memasukkan item ke dalam keranjang, maka selain menu Add items, akan menampilkan pesan bahwa keranjang masih kosong.

## Diagram alur


![supercashier_flow](https://user-images.githubusercontent.com/33124796/213452320-5d34400b-c970-4075-bfd5-de7c2b00d4a1.jpg)



## Sniplet
* Fungsi untuk menambah item (add_item)
![add_item](https://user-images.githubusercontent.com/33124796/213454040-09cd4541-fcaf-40b4-8511-ad1d75415338.png)

Funsi add_item menerima _attributes_ item_name (str), item_count (int), dan item_price (int) yang kemudian dilakukan pemeriksaan apakah item_count dan item_price adalah bilangan positif. Jika ya, maka akan dimasukkan ke dalam _pandas dataframes_. Pada fungsi ini juga terdapat perhitungan total_harga hasil dari perkalian jumlah item dan harga.

* Fungsi untuk melakukan pembaharuan harga item (update_item_price)

![update_item_price](https://user-images.githubusercontent.com/33124796/213455205-0e09fce8-6c13-47bd-8e83-5fe02dac954a.png)

Fungsi update_item_price menerima attribute item_name (str) dan new_price (int). Pemeriksaan dilakukan saat penguna memasukkan item_name, apakah ada di dalam keranjang atau tidak. Jika ya, maka harga lama akan diganti dengan harga baru, begitupun totalnya. 

* Fungsi untuk mereset keranjang
![reset_item](https://user-images.githubusercontent.com/33124796/213455887-605194d6-40f1-4175-8f26-28b2f3a99fa3.png)

fungsi reset_item digunakan unutk menghapus semua item yang telah dimasukkan ke dalam keranjang. 

## Uji kasus
1. Menambahkan item ke dalam keranjang

![additem](https://user-images.githubusercontent.com/33124796/213457976-2729634d-6f1b-4ae0-a787-313234f46299.png)

2. Menghapus satu item

![deleteitem](https://user-images.githubusercontent.com/33124796/213458358-dbb66f84-a868-4b8b-ab53-713890df139e.png)

3. Mereset keranjang

![resetitem](https://user-images.githubusercontent.com/33124796/213458439-977dab0f-61df-4c4c-97b5-808b23c7224e.png)

4. Checkout

![checkoutcart](https://user-images.githubusercontent.com/33124796/213458570-ad8215e8-93b2-4d9d-9bb0-916578c7852d.png)

## Menjalankan program
Unduh repository ini, dan jalankan `mainscreen.py` pada terminal.

## Kesimpulan
Secara umum program berjalan seperti yang diharapkan. Dengan tampilan menu yang sederhana diharapakan akan mempermudah pengguna (pembelanja) dalam melakukan proses transaksi dari awal hingga akhir seraca mandiri.

## Saran perbaikan
pass



