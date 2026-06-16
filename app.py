import streamlit as st
import base64

# 1. ضبط الصفحة لتوسيط العناصر وإخفاء القوائم الزائدة
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# دالة لتحويل الملفات المحلية المرفوعة إلى صيغة تدعمها لغة HTML داخل ستريمليت
def get_base64_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# قراءة ملفاتك المحلية المرفوعة (تأكد أن الأسماء مطابقة تماماً لصورتك)
try:
    video_base64 = get_base64_file("butterflies.mp4.MP4")
    img_base64 = get_base64_file("my-project.png")
except FileNotFoundError as e:
    st.error(f"تأكد من وجود الملفات بالأسماء الصحيحة في المستودع: {e}")
    video_base64 = ""
    img_base64 = ""

# 2. كود التنسيق المزدوج + تحريك الزر ليمين حافة الصورة
st.markdown("""
    <style>
    /* جعل طبقات ستريمليت شفافة لتظهر الخلفية الخارجية */
    .stApp, .main, .block-container, iframe {
        background: transparent !important;
    }
    
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* 1. فيديو الخلفية الخارجية (خارج إطار الصورة) */
    .background-video {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -100;
        object-fit: cover;
        opacity: 0.65;
    }
    
    /* حاوية العرض الخاصة بالصورة والفيديو الداخلي */
    .showcase-container {
        position: relative;
        width: 100%;
        max-width: 850px;
        margin: 0 auto 15px auto;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.15);
        z-index: 10;
    }
    
    /* 2. فيديو الخلفية الداخلية (يتحرك داخل تفاصيل الصورة) */
    .showcase-container video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 1;
    }
    
    /* دمج تفاصيل صورتك الوردية مع الفيديو الداخلي */
    .showcase-container img {
        position: relative;
        display: block;
        width: 100%;
        height: auto;
        z-index: 2;
        mix-blend-mode: multiply;
    }

    /* تنسيق زر Next الوردي ليكون على جهة اليمين تلقائياً */
    div.stButton > button:first-child {
        background-color: #E91E63;
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 12px 45px;
        border-radius: 30px;
        border: none;
        box-shadow: 0px 5px 15px rgba(233, 30, 99, 0.4);
        transition: 0.3s;
        position: relative;
        z-index: 10;
        display: block;
        margin: 0 0 0 auto; /* تم التعديل هنا ليدفع الزر لأقصى اليمين تماماً */
    }
    div.stButton > button:first-child:hover {
        background-color: #C2185B;
        color: white;
        box-shadow: 0px 8px 20px rgba(194, 24, 91, 0.6);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. تشغيل فيديو الفراشات في الخلفية الكاملة للموقع (خارج الصورة)
st.markdown(f"""
<video autoplay loop muted playsinline class="background-video">
    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# 4. تشغيل الفيديو ودمجه داخل إطار صورتك my-project.png
st.markdown(f"""
<div class="showcase-container">
    <video autoplay loop muted playsinline>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    <img src="data:image/png;base64,{img_base64}">
</div>
""", unsafe_allow_html=True)

# 5. عرض زر Next المطور والمحاذي لليمين (تم تغيير السهم أيضاً ليتجه لليمين)
if st.button("Next ➡️"):
    pass
