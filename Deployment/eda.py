import streamlit as st
from PIL import Image

def run():
    # Membuat judul
    st.title('Rice Image Dataset')

    # Membuat Sub Header
    st.header('EDA Rice Image Dataset', divider='gray')

    # Menambahkan Gambar
    image = Image.open('wallpaper.jpg')
    st.image(image, caption = 'Rice', channels='RGB')

    # Menambahkan Divider
    st.divider()

    # Jenis - Jenis Beras
    st.header('Jenis-Jenis Beras', divider='gray')
    st.subheader('Arborio')
    image = Image.open('Arborio.png')
    st.image(image, channels='RGB')

    st.subheader('Basmati')
    image = Image.open('Basmati.png')
    st.image(image, channels='RGB')

    st.subheader('Ipsala')
    image = Image.open('Ipsala.png')
    st.image(image, channels='RGB')

    st.subheader('Jasmine')
    image = Image.open('Jasmine.png')
    st.image(image, channels='RGB')

    st.subheader('Karacadag')
    image = Image.open('Karacadag.png')
    st.image(image, channels='RGB')
    st.divider()

    # Tepi Gambar Beras
    st.header('Tepi Gambar Beras', divider='gray')
    st.subheader('Arborio')
    image = Image.open('Tepi Gambar Arborio.png')
    st.image(image, channels='RGB')

    st.subheader('Basmati')
    image = Image.open('Tepi Gambar Basmati.png')
    st.image(image, channels='RGB')

    st.subheader('Ipsala')
    image = Image.open('Tepi Gambar Ipsala.png')
    st.image(image, channels='RGB')

    st.subheader('Jasmine')
    image = Image.open('Tepi Gambar Jasmine.png')
    st.image(image, channels='RGB')

    st.subheader('Karacadag')
    image = Image.open('Tepi Gambar Karacadag.png')
    st.image(image, channels='RGB')
    st.divider()

    # Warna Dominan Beras
    st.header('Warna Dominan Beras', divider='gray')
    st.subheader('Arborio')
    image = Image.open('Color Dominance Arborio.png')
    st.image(image, channels='RGB')

    st.subheader('Basmati')
    image = Image.open('Color Dominance Basmati.png')
    st.image(image, channels='RGB')

    st.subheader('Ipsala')
    image = Image.open('Color Dominance Ipsala.png')
    st.image(image, channels='RGB')

    st.subheader('Jasmine')
    image = Image.open('Color Dominance Jasmine.png')
    st.image(image, channels='RGB')

    st.subheader('Karacadag')
    image = Image.open('Color Dominance Karacadag.png')
    st.image(image, channels='RGB')
    st.divider()

    # Color Channel RGB Beras
    st.header('Warna Channel RGB Beras', divider='gray')
    st.subheader('Arborio')
    image = Image.open('Color Channels Arborio.png')
    st.image(image, channels='RGB')

    st.subheader('Basmati')
    image = Image.open('Color Channels Basmati.png')
    st.image(image, channels='RGB')

    st.subheader('Ipsala')
    image = Image.open('Color Channels Ipsala.png')
    st.image(image, channels='RGB')

    st.subheader('Jasmine')
    image = Image.open('Color Channels Jasmine.png')
    st.image(image, channels='RGB')

    st.subheader('Karacadag')
    image = Image.open('Color Channels Karacadag.png')
    st.image(image, channels='RGB')
    st.divider()


    # Color Channel CYMK Beras
    st.header('Warna Channel RGB Beras', divider='gray')
    st.subheader('Arborio')
    image = Image.open('CYMK Color Channels Arborio.png')
    st.image(image, channels='RGB')

    st.subheader('Basmati')
    image = Image.open('CYMK Color Channels Basmati.png')
    st.image(image, channels='RGB')

    st.subheader('Ipsala')
    image = Image.open('CYMK Color Channels Ipsala.png')
    st.image(image, channels='RGB')

    st.subheader('Jasmine')
    image = Image.open('CYMK Color Channels Jasmine.png')
    st.image(image, channels='RGB')

    st.subheader('Karacadag')
    image = Image.open('CYMK Color Channels Karacadag.png')
    st.image(image, channels='RGB')
    st.divider()

if __name__ == '__main__':
    run()
