![Rice Image Computer Vision Classification](https://github.com/DarlyP/Rice-Image-Dataset/blob/main/Notebook/rice.jpg)

# Rice Image Classification Using Computer Vision

---

## Tools
[<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Seaborn-388E3C?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" />](https://seaborn.pydata.org/)
[<img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />](https://numpy.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Scikit%20learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />](https://scikit-learn.org/)
[<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow" />](https://www.tensorflow.org/)
[<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras" />](https://keras.io/)

---

## Data Source

Kaggle: [Rice Image Dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset).

---

## Introduction

The main goal of this project is to develop a machine-learning model that can accurately classify the quality and type of rice based on visual characteristics such as shape and color. By leveraging image processing techniques and classification algorithms, the project aims to create a system that can assist in the automatic and efficient determination of rice quality. This includes building and training models using labeled rice image datasets for each class, as well as evaluating model performance to ensure accuracy and reliability. Therefore, the project is expected to improve the speed and accuracy of rice quality assessment, thereby optimizing supply chains and enhancing customer satisfaction.

---

## Conclusion

- *Model improvement* menunjukkan peningkatan yang signifikan dalam akurasi keseluruhan dan precision, terutama untuk kelas yang memiliki performa rendah pada base model (seperti `Basmati` dan `Jasmine`). Peningkatan dalam *macro* dan *weighted average* precision menunjukkan bahwa model improvement memiliki performa yang lebih baik dan lebih konsisten dalam mengklasifikasikan semua kelas secara merata. Meskipun ada sedikit penurunan dalam precision untuk beberapa kelas, peningkatan signifikan dalam recall untuk kelas-kelas yang sebelumnya berkinerja rendah menunjukkan bahwa model *improvement* memiliki kemampuan yang lebih baik dalam mendeteksi dan mengklasifikasikan gambar dengan benar. Ini menunjukkan bahwa model *improvement* lebih efektif dan andal untuk tugas klasifikasi citra ini.

- *Model improvement* menunjukkan peningkatan yang signifikan dalam berbagai metrik kinerja dibandingkan dengan base model, terutama dalam hal akurasi dan precision. Namun, perlu diingat bahwa *model improvement* memiliki beberapa kelemahan, seperti sedikit penurunan precision pada beberapa kelas dan potensi *overfitting*. Meskipun demikian, dengan performa yang lebih baik dan lebih konsisten, *model improvement* lebih siap untuk digunakan dalam aplikasi nyata, asalkan langkah-langkah yang tepat diambil untuk mengatasi potensi kelemahan.

- Meskipun ada beberapa kelemahan seperti potensi *overfitting* dan penurunan precision pada beberapa kelas, *model improvement* lebih siap untuk digunakan dalam aplikasi nyata. Dengan peningkatan dalam akurasi dan precision, serta stabilitas dalam training dan validation, model improvement dapat membantu meningkatkan kecepatan dan akurasi dalam penilaian kualitas beras, yang pada gilirannya akan mengoptimalkan rantai pasokan dan meningkatkan kepuasan konsumen.

---

## Model Development

- Perform data augmentation on the base model to show a more equal comparison of performance between the base model and the augmented model.
   
- Add a Confusion Matrix to evaluate model performance.

- Conduct queries to find data categorized as TP (True Positive), TN (True Negative), FP (False Positive), and FN (False Negative) for each class, then analyze their characteristics.

---

## Deployment Model

Hugging Face: [Rice Image Dataset](https://huggingface.co/spaces/darly9991/Rice_Image_Classification).

Model: [Rice Image Computer Vision Classification](https://drive.google.com/file/d/1H-NmiarcH41X4w7tSFGknVg8EV_NkFX6/view?usp=sharing)

---

**Disclaimer**: 
- This notebook is created solely for learning and exploration purposes. There is no intention to offend or harm any party. All content and analysis presented are based on publicly available data online. I undertake this process to enhance my understanding of data analysis techniques and methodologies and hone my skills in implementing relevant algorithms and models within the context of data science learning. In conducting this analysis, I strive to maintain objectivity and professionalism in interpreting the existing data. Any conclusions or recommendations provided result from personal analysis and are not intended as professional advice in any specific capacity. I hope the information obtained from this notebook can be useful to anyone reading it to learn and develop data analysis skills.
- This notebook is written in Indonesian.
