import streamlit as st
from rembg import remove
from PIL import Image
import io
import numpy as np

st.title('Pic.Ly \U0001F600')


def change_background_color(image, color):
    
    color_map = {
        'Purple': (128, 0, 128),
        'Red': (255, 0, 0),
        'Yellow': (255, 255, 0)
    }
    
    # Create background with selected color
    background = Image.new('RGB', image.size, color_map[color])
    
    # Paste the foreground onto colored background using alpha channel
    background.paste(image, mask=image.getchannel('A'))
    
    return background

def main():
    st.title("Profile Picture Background Changer")
    st.write("Upload your image and create a professional profile picture with custom background!")

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file", 
        type=['png', 'jpg', 'jpeg'],
        help="Supported formats: PNG, JPG, JPEG"
    )

    # Create columns for layout
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Original Image:")
            # Display original image
            original_image = Image.open(uploaded_file)
            st.image(original_image, use_column_width=True)

        # Background color selection
        background_color = st.selectbox(
            'Choose background color:',
            ('Purple', 'Red', 'Yellow')
        )

        if st.button('Remove Background and Apply Color'):
            try:
                with st.spinner('Processing... Please wait...'):
                    # Remove background
                    output = remove(original_image)
                    
                    # Apply new background color
                    final_image = change_background_color(output, background_color)
                    
                    with col2:
                        st.write("Processed Image:")
                        st.image(final_image, use_column_width=True)
                    
                    # Convert image for download
                    buf = io.BytesIO()
                    final_image.save(buf, format='PNG')
                    byte_im = buf.getvalue()
                    
                    # Add download button
                    st.download_button(
                        label="Download Profile Picture",
                        data=byte_im,
                        file_name=f"profile_pic_{background_color.lower()}.png",
                        mime="image/png",
                        help="Click to download your processed image"
                    )
                    
                    st.success('Background removed and color applied successfully!')
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.error("Please try with a different image or check if the image is valid.")
    
    else:
        # Show instructions when no file is uploaded
        st.info("👆 Please upload an image to get started!")
        
        # Add example/placeholder image
        st.write("Example of how your processed image will look:")
        placeholder_image = "https://via.placeholder.com/400x300"
        st.image(placeholder_image, caption="Sample Image", width=300)

   
    
if __name__ == "__main__":
  main()    



