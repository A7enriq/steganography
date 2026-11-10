Hide Picture in Picture
Introduction
This project is a Python application developed using Streamlit and the Stegano library.
The main purpose of this project is to hide a secret picture inside another image and reveal the hidden picture later.
Features
Upload a host image.
Upload a secret image.
Hide a secret picture inside a host picture.
Reveal the hidden picture from an encoded image.
Save the generated image.
Display the recreated secret picture.
Interactive user interface using Streamlit.
Technologies
Python
Streamlit
Stegano
Pillow (PIL)
Project Structure
Steganography/ ├── main.py ├── final_img_2027.png ├── Gust_pic.jpg └── README.md 
Installation
Install the required libraries:
pip install streamlit pip install stegano pip install pillow 
How to Run
Open the project in VS Code.
Install the required libraries.
Run the application:
streamlit run main.py 
Open the application in your browser.
Usage
Hide Picture
Select the Hide Picture option.
Upload the host picture.
Upload the secret picture.
Click the Hide Pic button.
The application generates an encoded image.
Reveal Picture
Select the Reveal Picture option.
Upload the encoded PNG image.
Click the Reveal Pic button.
The application extracts the hidden data.
The recreated secret picture is displayed.
How It Works
The project uses image steganography to hide data inside another image.
The Stegano library provides the LSB (Least Significant Bit) technique for hiding and revealing information.
The hidden data is extracted and converted back into an image file.
Output
Encoded image: final_img_2027.png
Recreated secret image: Gust_pic.jpg
Author
Python Programming Student
