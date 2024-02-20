import gzip
import streamlit as st

st.title("Compress Files")

uploaded_file = st.file_uploader(
    "File to Compress",
    "txt",
)

if uploaded_file is not None:
    data = uploaded_file.read()
    compressed_data = gzip.compress(data)
    st.download_button(
        "Download Compressed File",
        compressed_data,
        file_name=uploaded_file.name + ".gz",
    )
    # with open(uploaded_file.name, "wb") as f:
    #     f.write(uploaded_file.getbuffer())
    # st.success("File Saved")
