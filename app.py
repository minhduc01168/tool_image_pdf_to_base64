import streamlit as st
import base64
from st_copy_to_clipboard import st_copy_to_clipboard

st.set_page_config(
    page_title="Image/PDF to Base64 Converter",
    page_icon="🔄",
    layout="centered"
)

st.title("🔄 Image / PDF to Base64 Converter")
st.markdown("Upload your image or PDF file to get the Base64 string instantly.")

uploaded_files = st.file_uploader(
    "Choose files",
    type=['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp', 'pdf'],
    accept_multiple_files=True
)

if uploaded_files:
    st.divider()
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        
        st.subheader(f"📄 {file_name}")
        st.text(f"Type: {file_type} | Size: {file_size / 1024:.2f} KB")
        
        # Read file
        bytes_data = uploaded_file.getvalue()
        
        # Encode
        base64_bytes = base64.b64encode(bytes_data)
        base64_string = base64_bytes.decode('utf-8')
        
        # Options
        use_prefix = st.checkbox(f"Add Data URI prefix for {file_name}", key=f"check_{file_name}")
        
        if use_prefix:
            prefix = f"data:{file_type};base64,"
            final_string = prefix + base64_string
        else:
            final_string = base64_string
            
        # 1. Hiển thị xem trước 100 ký tự (nhẹ, không lag)
        st.text_area(
            label="Preview (100 characters):", 
            value=final_string[:100] + "...", 
            height=100, 
            disabled=True,
            key=f"preview_{file_name}" 
        )
        # 2. Tạo nút Copy đặc biệt
        # Nút này giữ chuỗi final_string trong biến nhưng không in ra màn hình
        st_copy_to_clipboard(final_string, "📋 Copy Full Base64 String")
        st.caption(f"Total Length: {len(final_string)} characters")
        
        col1, col2 = st.columns([1, 1])
        with col1:
             st.download_button(
                label="📥 Download Base64 (.txt)",
                data=final_string,
                file_name=f"{file_name}.txt",
                mime="text/plain",
                key=f"dl_{file_name}"
            )
        
        st.divider()
