import streamlit as st
from PIL import Image
import io
from main import count_sheets,preprocess_image


# Function to count sheets (replace this with your actual sheet counting logic)



# Set page config
st.set_page_config(page_title="Sheet Counter", page_icon="📄", layout="centered")


# Main app
def main():
    st.title("📄 Sheet Counter App")

    st.write("""
    Welcome to the Sheet Counter App! 
    Upload an image of your sheets, and we'll count them for you.
    """)

    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Add a "Count Sheets" button
        if st.button("Count Sheets"):
            with st.spinner("Counting sheets..."):
                # Process the image and count sheets
                sheet_count = count_sheets(image)

            # Display result
            st.success(f"Sheet count: {sheet_count}")

            # Provide additional information or actions
            st.write("What would you like to do next?")
            if st.button("Count Another Image"):
                st.experimental_rerun()

            if st.button("Learn More About Sheet Counting"):
                st.write(
                    '''Sheet counting is a process of automatically determining the 
                    number of individual sheets in an image. It automates the counting of sheet stacks in a manufacturing plant. It has various applications in inventory management, 
                    printing, and document processing.''')

    # Add a sidebar with additional information
    st.sidebar.header("About Sheet Counter")
    st.sidebar.write("""
    This app uses advanced image processing techniques to count the number of sheets in your uploaded image.

    Features:
    - Fast and accurate sheet counting
    - Support for various image formats
    - User-friendly interface
    """)


if __name__ == "__main__":
    main()
