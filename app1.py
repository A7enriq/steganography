# msg = 'Python'
# # msg = 'سلام'
# # encode_msg = msg.encode('utf-8')
# encode_msg = msg.encode('latin-1')

# print(f"final encode msg: {encode_msg}")
# print('-'* 30)



# decode_msg = encode_msg.decode('latin-1')
# print(f"final deocde msg: {decode_msg}")
# print('-'* 30)

from stegano import lsb
from PIL import Image
import streamlit as st

st.title('Hide PICTURE IN PICTURE')
st.set_page_config(page_title='Stegano Project')

option = st.sidebar.selectbox('Select Your option', 
                        ('Hide Picture', 'Reveal Picture'))
if option == 'Hide Picture':
    cover_file = st.file_uploader('Select Host Pic', type=['jpg', 'png'])
    secret_file = st.file_uploader('Select Secret Pic', type=['jpg', 'png'])

    if cover_file  and secret_file:
        temp_file = Image.open(cover_file).convert('RGB')
        secret_temp = secret_file.read()
        secret_text = secret_temp.decode('latin-1')
        if st.button('Hide Pic'):
            final_image = lsb.hide(cover_file, secret_text)
            final_image.save('./final_img_2027.png')
            st.success('Picture Hide Successfully ...')

elif option == 'Reveal Picture':
    final_image = st.file_uploader('Select final image ', type=['png'])

    if final_image:
        encode_image = Image.open(final_image)

        if encode_image:
            if st.button('Reveal Pic'):

                secretd_text = lsb.reveal(encode_image)

                temp_img = secretd_text.encode('latin-1')
                with open('./Gust_pic.jpg', 'wb') as f:
                    f.write(temp_img)
                
                st.success('Gust Picture Recreated ...')
                st.image('./Gust_pic.jpg')