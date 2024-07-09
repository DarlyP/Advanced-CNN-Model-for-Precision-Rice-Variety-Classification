import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = image.resize((img_height, img_width))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Mapping numerical predictions to class labels
class_labels = {0: "Arborio", 1: "Basmati", 2: "Ipsala", 3: "Jasmine", 4: "Karacadag"}

# Main function to run the Streamlit app
def main():
    st.title("Rice Classifier")
    st.write("Upload a picture of rice to predict its type..")

    # File upload
    uploaded_file = st.file_uploader("Select the rice image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)

        # Load the model (once the image is uploaded)
        model = load_model("my_model.keras")

        # Preprocess and predict
        img_array = preprocess_image(image)
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # Display prediction
        st.write(f'Prediksi: {class_labels[predicted_class]}')

if __name__ == "__main__":
    main()
