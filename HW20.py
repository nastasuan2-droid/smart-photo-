import io
import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="𝙎𝙢𝙖𝙧𝙩 𝙋𝙝𝙤𝙩𝙤 𝙀𝙙𝙞𝙩𝙤𝙧",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
  
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    

    .title-text {
        font-size: 2.8rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

  
    .image-card {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

 
    .stDownloadButton > button {
        width: 100%;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #6d28d9);
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
    }
    </style>
""",
    unsafe_allow_html=True,
)


st.markdown(
    '<p class="title-text">🎨 𝙎𝙢𝙖𝙧𝙩 𝙋𝙝𝙤𝙩𝙤 𝙀𝙙𝙞𝙩𝙤𝙧</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="subtitle-text">𝑈𝑝𝑙𝑜𝑎𝑑 𝑎 𝑝ℎ𝑜𝑡𝑜 𝑎𝑛𝑑 𝑎𝑝𝑝𝑙𝑦 𝑠𝑡𝑦𝑙𝑖𝑠ℎ 𝑒𝑓𝑓𝑒𝑐𝑡𝑠 𝑖𝑛 𝑎 𝑓𝑒𝑤 𝑐𝑙𝑖𝑐𝑘𝑠</p>',
    unsafe_allow_html=True,
)


st.sidebar.markdown("## ⚙️ 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨")
uploaded_file = st.sidebar.file_uploader(
    "𝑈𝑝𝑙𝑜𝑎𝑑 𝑖𝑚𝑎𝑔𝑒", type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.sidebar.markdown("---")
    filter_option = st.sidebar.selectbox(
        "🔮 𝘾𝙝𝙤𝙤𝙨𝙚 𝙖𝙣 𝙚𝙛𝙛𝙚𝙘𝙩:",
        [
            "𝙤𝙧𝙞𝙜𝙞𝙣𝙖𝙡",
            "𝙱𝚕𝚊𝚌𝚔 𝚊𝚗𝚍 𝚠𝚑𝚒𝚝𝚎",
            "𝙱𝚕𝚞𝚛",
            "𝚁𝚎𝚏𝚕𝚎𝚌𝚝𝚒𝚘𝚗",
            "𝙱𝚛𝚒𝚐𝚑𝚝𝚗𝚎𝚜𝚜 𝚜𝚎𝚝𝚝𝚒𝚗𝚐𝚜",
            "𝙲𝚘𝚗𝚝𝚛𝚊𝚜𝚝 𝚊𝚍𝚓𝚞𝚜𝚝𝚖𝚎𝚗𝚝",
            "𝙸𝚗𝚟𝚎𝚛𝚜𝚒𝚘𝚗",
        ],
    )

    processed_img = img_array.copy()


    if filter_option == "𝙱𝚕𝚊𝚌𝚔 𝚊𝚗𝚍 𝚠𝚑𝚒𝚝𝚎":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    elif filter_option == "𝙱𝚕𝚞𝚛":
        blur_val = st.sidebar.slider("𝙱𝚕𝚞𝚛 𝙸𝚗𝚝𝚎𝚗𝚜𝚒𝚝𝚢", 1, 31, 15, step=2)
        processed_img = cv2.GaussianBlur(img_array, (blur_val, blur_val), 0)

    elif filter_option == "𝚁𝚎𝚏𝚕𝚎𝚌𝚝𝚒𝚘𝚗":
        flip_type = st.sidebar.radio(
            "𝙳𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗:", ["𝙷𝚘𝚛𝚒𝚣𝚘𝚗𝚝𝚊𝚕𝚕𝚢", "𝚅𝚎𝚛𝚝𝚒𝚌𝚊𝚕𝚕𝚢"]
        )
        code = 1 if flip_type == "𝙷𝚘𝚛𝚒𝚣𝚘𝚗𝚝𝚊𝚕𝚕𝚢" else 0
        processed_img = cv2.flip(img_array, code)

    elif filter_option == "𝙱𝚛𝚒𝚐𝚑𝚝𝚗𝚎𝚜𝚜 𝚜𝚎𝚝𝚝𝚒𝚗𝚐𝚜":
        brightness_val = st.sidebar.slider("𝙱𝚛𝚒𝚐𝚑𝚝𝚗𝚎𝚜𝚜 𝚕𝚎𝚟𝚎𝚕", -100, 100, 0)
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=1.0, beta=brightness_val
        )

    elif filter_option == "𝙲𝚘𝚗𝚝𝚛𝚊𝚜𝚝 𝚊𝚍𝚓𝚞𝚜𝚝𝚖𝚎𝚗𝚝":
        contrast_val = st.sidebar.slider(
            "𝙲𝚘𝚗𝚝𝚛𝚊𝚜𝚝 𝚕𝚎𝚟𝚎𝚕", 0.5, 3.0, 1.0, step=0.1
        )
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=contrast_val, beta=0
        )

    elif filter_option == "𝙸𝚗𝚟𝚎𝚛𝚜𝚒𝚘𝚗":
        processed_img = 255 - img_array


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### 📷𝙤𝙧𝙞𝙜𝙞𝙣𝙖𝙡")
        st.image(img_array, use_container_width=True)

    with col2:
        st.markdown("### ✨𝙧𝙚𝙨𝙪𝙡𝙩𝙨")
        st.image(processed_img, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

     
        result_image = Image.fromarray(processed_img)
        buf = io.BytesIO()
        result_image.save(buf, format="JPEG", quality=95)
        byte_im = buf.getvalue()

        st.download_button(
            label="📥 𝑈𝑝𝑙𝑜𝑎𝑑 𝑡ℎ𝑒 𝑒𝑑𝑖𝑡𝑒𝑑 𝑝ℎ𝑜𝑡𝑜",
            data=byte_im,
            file_name="smart_edit.jpeg",
            mime="image/jpeg",
        )
else:

    st.info("👈 𝙿𝚕𝚎𝚊𝚜𝚎 𝚞𝚙𝚕𝚘𝚊𝚍 𝚊 𝚙𝚑𝚘𝚝𝚘 𝚒𝚗 𝚝𝚑𝚎 𝚖𝚎𝚗𝚞 𝚘𝚗 𝚝𝚑𝚎 𝚕𝚎𝚏𝚝 𝚝𝚘 𝚜𝚝𝚊𝚛𝚝 𝚙𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐.")