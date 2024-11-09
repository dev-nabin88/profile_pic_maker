import streamlit as st
from rembg import remove
from PIL import Image
import io
import numpy as np

st.title('Pic.Ly \U0001F600')
def remove_background_and_add_color(upload, bg_color):
    # Convert color name to RGB
    color_map = {
        'Purple': (128, 0, 128),
        'Red': (255, 0, 0),
        'Yellow': (255, 255, 0),
        'Blue': (76, 137, 248),
        'pink': (199, 142, 255)
        
    }
    
    # Open the uploaded image
    image = Image.open(upload)
    
    # Remove the background
    removed_bg = remove(image)
    
    # Create new image with colored background
    bg_color_rgb = color_map[bg_color]
    background = Image.new('RGB', image.size, bg_color_rgb)
    
    # Paste the foreground onto the colored background
    background.paste(removed_bg, (0, 0), removed_bg)
    
    return background

def add_footer():
    footer_col1, footer_col2 = st.columns(2)

    st.markdown("-----")
    with footer_col1:
        st.markdown("### Developer Contact")
        st.markdown("📧 Email: ghoruinabin29@gmail.com")
        st.markdown("""
        - [🔗🔗🔗LinkedIn](https://www.linkedin.com/in/nabinghorui)
        - [🔗🔗🔗Twitter](https://x.com/im_Ghoruinabin)
        
        """)

        

def main():
    st.title("Professional Profile Picture Maker")
    st.write("Upload your image and create a profile picture with a colored background!")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    
    # Color selection
    bg_color = st.selectbox(
        'Choose background color',
        ('Purple', 'Red', 'Yellow', 'Blue')
    )
    
    if uploaded_file is not None:
        # Show original image
        st.write("Original Image:")
        image = Image.open(uploaded_file)
        st.image(image, width=300)
        
        # Process button
        if st.button('Create Profile Picture'):
            with st.spinner('Processing...'):
                # Process the image
                result = remove_background_and_add_color(uploaded_file, bg_color)
             
                # Display result
                st.write("Result:")
                st.image(result, width=300)
                
                # Convert result to bytes for download
                buf = io.BytesIO()
                result.save(buf, format='PNG')
                byte_im = buf.getvalue()
                
                # Download button
                st.download_button(
                    label="Download Profile Picture",
                    data=byte_im,
                    file_name=f"profile_pic_{bg_color.lower()}.png",
                    mime="image/png"
                )    


    st.markdown(
        """
        <div style='background-color: #f0f2f6; padding: 15px; border-radius: 5px; text-align: center; margin-top: 20px;'>
            <p style='margin: 0; color: #666;'>More features will be added soon............stay tuned \U0001F634 \U0001F634 \U0001F634</p>
        </div>
       
        """,
        unsafe_allow_html=True
    )
               
                
    add_footer()
    
    
    st.markdown(
        """
        <div style='background-color: #f0f2f6; padding: 15px; border-radius: 5px; text-align: center; margin-top: 20px;'>
            <p style='margin: 0; color: #666;'>Crafted with ❤️ by nabin </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style='background-color: #f0f2f6; padding: 15px; border-radius: 5px; text-align: center; margin-top: 20px;'>
            <p style='margin: 0; color: #666;'>© 2024,All Rights Reserved.</p>
        </div>
       
        """,
        unsafe_allow_html=True
    )
    

if __name__ == '__main__':
    main()


