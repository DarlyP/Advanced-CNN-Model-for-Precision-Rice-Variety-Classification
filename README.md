![Rice Image Computer Vision Classification](https://github.com/DarlyP/Rice-Image-Dataset/blob/main/Notebook/rice.jpg)

# Rice Image Classification Using Computer Vision

---


## Data Source

Kaggle: [Rice Image Dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset).

---

## Introduction

Tujuan utama dari proyek ini adalah untuk mengembangkan model *machine learning* yang dapat secara akurat mengklasifikasikan kualitas dan jenis beras berdasarkan karakteristik visual seperti bentuk dan warna. Dengan memanfaatkan teknik pengolahan citra dan algoritma klasifikasi, proyek ini bertujuan untuk menghasilkan sistem yang dapat membantu dalam proses penentuan kualitas beras secara otomatis dan efisien. Ini akan mencakup pembuatan dan pelatihan model menggunakan dataset gambar beras yang telah diberi label untuk tiap kelasnya, serta evaluasi kinerja model untuk memastikan akurasi dan keandalannya. Dengan demikian, proyek ini diharapkan dapat meningkatkan kecepatan dan akurasi dalam penilaian kualitas beras, yang pada gilirannya akan mengoptimalkan rantai pasokan dan meningkatkan kepuasan konsumen.

---

## Conclusion

- *Model improvement* menunjukkan peningkatan yang signifikan dalam akurasi keseluruhan dan precision, terutama untuk kelas yang memiliki performa rendah pada base model (seperti `Basmati` dan `Jasmine`). Peningkatan dalam *macro* dan *weighted average* precision menunjukkan bahwa model improvement memiliki performa yang lebih baik dan lebih konsisten dalam mengklasifikasikan semua kelas secara merata. Meskipun ada sedikit penurunan dalam precision untuk beberapa kelas, peningkatan signifikan dalam recall untuk kelas-kelas yang sebelumnya berkinerja rendah menunjukkan bahwa model *improvement* memiliki kemampuan yang lebih baik dalam mendeteksi dan mengklasifikasikan gambar dengan benar. Ini menunjukkan bahwa model *improvement* lebih efektif dan andal untuk tugas klasifikasi citra ini.

- *Model improvement* menunjukkan peningkatan yang signifikan dalam berbagai metrik kinerja dibandingkan dengan base model, terutama dalam hal akurasi dan precision. Namun, perlu diingat bahwa *model improvement* memiliki beberapa kelemahan, seperti sedikit penurunan precision pada beberapa kelas dan potensi *overfitting*. Meskipun demikian, dengan performa yang lebih baik dan lebih konsisten, *model improvement* lebih siap untuk digunakan dalam aplikasi nyata, asalkan langkah-langkah yang tepat diambil untuk mengatasi potensi kelemahan.

- Meskipun ada beberapa kelemahan seperti potensi *overfitting* dan penurunan precision pada beberapa kelas, *model improvement* lebih siap untuk digunakan dalam aplikasi nyata. Dengan peningkatan dalam akurasi dan precision, serta stabilitas dalam training dan validation, model improvement dapat membantu meningkatkan kecepatan dan akurasi dalam penilaian kualitas beras, yang pada gilirannya akan mengoptimalkan rantai pasokan dan meningkatkan kepuasan konsumen.

---

## Model Development

1. Melakukan *data augmentation* pada model dasar sehingga performa pada model dasar dan model peningkatan lebih terlihat perbandingan yang setara.
2. Menambahkan *Confusion Matrix*.
3. Melakukan *query* untuk mencari data yang terkategori sebagai TP, TN, FP, dan FN pada masing-masing kelas, kemudian menganalisis karakteristiknya.

---

## Deployment Model

Hugging Face: [Rice Image Dataset](https://huggingface.co/spaces/darly9991/Rice_Image_Classification).

---

**Disclaimer**: Notebook ini dibuat semata-mata untuk tujuan pembelajaran dan eksplorasi. Tidak ada maksud untuk menyinggung atau merugikan pihak mana pun. Segala konten dan analisis yang disajikan didasarkan pada data publik yang tersedia secara online. Saya melakukan proses ini untuk meningkatkan pemahaman tentang teknik dan metodologi analisis data, serta untuk mengasah keterampilan dalam mengimplementasikan algoritma dan model yang relevan dalam konteks pembelajaran data science.

Dalam melakukan analisis ini, saya berusaha menjaga objektivitas dan profesionalitas dalam menginterpretasikan data yang ada. Segala kesimpulan atau rekomendasi yang disampaikan merupakan hasil dari analisis pribadi dan tidak bermaksud sebagai saran profesional dalam kapasitas tertentu. Saya berharap informasi yang diperoleh dari notebook ini dapat bermanfaat bagi siapa pun yang membacanya untuk kepentingan belajar dan pengembangan keterampilan analisis data.
