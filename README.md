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

The improvement model shows significant improvements in overall accuracy and precision, especially for classes that performed poorly in the base model (such as Basmati and Jasmine). Improvements in macro and weighted average precision indicate that the improvement model performs better and more consistently in classifying all classes equally. While there is a slight decrease in precision for some classes, significant improvements in recall for previously low-performing classes indicate that the improvement model is better able to detect and classify images correctly. This suggests that the improvement model is more effective and reliable for this image classification task.

The improvement model shows significant improvements in various performance metrics compared to the base model, especially in terms of accuracy and precision. However, it is important to note that the improvement model has some drawbacks, such as a slight decrease in precision for some classes and potential overfitting. However, with better and more consistent performance, the improvement model is more ready to be used in real-world applications, provided that appropriate steps are taken to address potential drawbacks.

Despite some drawbacks, such as potential overfitting and decreased precision for some classes, the improvement model is more ready to be used in real-world applications. With improvements in accuracy and precision, as well as stability in training and validation, model improvement can help increase the speed and accuracy of rice quality assessment, which in turn will optimize the supply chain and improve consumer satisfaction.

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
