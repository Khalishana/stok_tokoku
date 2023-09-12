- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: Pertama, saya membuat direktori bernama stok_tokoku yang digunakan sebagai folder utama dalam membangun web ini. Untuk membuat sebuah proyek Django baru sebagaimana pada checklist soal, tentunya saya harus mengaktifkan virtual environment untuk memudahkan proses pengerjaan saya. Dalam proses ini hingga menjalankan server, saya mengacu pada command yang dijelaskan pada tutorial untuk membantu pekerjaan saya. Setelah proyek Django berhasil dibuat, saya membuat aplikasi main serta melakukan routing agar aplikasi tersebut dapat dijalankan. Tidak lupa, saya menambahkan folder templates pada main sekaligus menambahkan file main.html sebagai wadah untuk membangun tampilan website saya. Setelah memastikan tidak ada langkah yang terlewat dalam proses ini, melakukan modifikasi pada models.py yang ada di main sesuai dengan ketentuan yang diberikan pada tugas 2. Tidak hanya melakukan modifikasi pada models.py, saya juga melakukan beberapa modifikasi serta tambahan pada views.py dan tentunya main.html sehingga saya dapat membuat tampilan web sesuai yang saya inginkan. Setelah semua proses selesai, saya kemudian melakukan git add, commit, dan push dan kemudian melakuan deployment ke Adaptable.
- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
![Alt text](<django bagan.jpg>)
Request client pertama kali akan diterima oleh urls.py. Selanjutnya, urls.py akan mendefinisikan pola URL dan mengarahkan request client ke fungsi view yang sesuai, dalam hal ini mengarahkan ke views.py. Di dalam views.py, terdapat beberapa kode yang akan mengatur jalannya aplikasi serta berinteraksi dengan model untuk mengambil atau memanipulasi data yang dibutuhkan untuk merender halaman HTML yang akan dikirimkan ke client. Kemudian, views.py dapat berinteraksi dengan models.py untuk melakukan pengambilan atau penyimpanan data ke database. Setelah melakukan operasi yang dibutuhkan, view akan merender main.html yang didalamnya terdapat variabel-variabel yang diisi dengan data yang diberikan oleh view.
- Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab: Virtual environment digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Fungsi utama virtual environment yakni memungkinkan isolasi dependensi yang memiliki versi Python berbeda pada setiap proyek yang dikerjakan. Hal ini membantu mencegah konflik dan masalah dependensi yang mungkin terjadi ketika dua proyek membutuhkan versi yang berbeda dari paket yang sama. Selain itu, Virtual environment membuat suatu proyek lebih mudah dibagikan bersama orang lain. Karena semua dependensi proyek disimpan dalam lingkungan terisolasi, orang lain dapat membuat lingkungan yang sama untuk menjalankan proyek yang sama tanpa khawatir terjadi konflik dengan paket lain di sistem mereka. Akan tetapi, kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment dengan konsekuensi lebih sulit untuk mengelola dependensi, sulit jika perlu menggunakan versi Python berbeda dalam suatu proyek, hingga sulit untuk membuat proyek bersama orang lain. Oleh karena itu, untuk menjaga kebersihan, isolasi, dan manajemen dependensi yang lebih baik, sangat dianjurkan untuk menggunakan virtual environment dalam membuat aplikasi web berbasis Django
- Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
Jawab: MVC, MVT, MVVM adalah tiga konsep arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi berbasis web. MVC (Model View Controller) bertangung jawab terhadap tampilan (view) serta mengatur alur kontrol (controller). MVT (Model View Template) merupakan konsep yang memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur. MVVM (Model View-View Model) merupakan konsep yang memungkinkan pengikatan data dua arah, yang memudahkan pemutakhiran otomatis tampilan ketika data pada model berubah. Perbedaan utama antara ketiganya adalah dalam cara mereka mengorganisasi dan memisahkan komponen-komponen utama dalam aplikasi. MVC adalah pola yang lebih klasik, MVT adalah adaptasi Django terhadap pola ini dengan menggunakan Template sebagai pengganti Controller, sedangkan MVVM menekankan pengikatan data dua arah melalui ViewModel untuk memfasilitasi pengembangan aplikasi yang lebih dinamis.