import streamlit as st
import base64

# 1. ضبط الصفحة لتوسيط العناصر وإخفاء القوائم الزائدة
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# دالة لتحويل الملفات المحلية المرفوعة إلى صيغة تدعمها لغة HTML داخل ستريمليت
def get_base64_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# قراءة ملفاتك المحلية المرفوعة
try:
    video_base64 = get_base64_file("butterflies.mp4.MP4")
    img_base64 = get_base64_file("my-project.png")
except FileNotFoundError as e:
    st.error(f"تأكد من وجود الملفات بالأسماء الصحيحة في المستودع: {e}")
    video_base64 = ""
    img_base64 = ""

# 2. كود التنسيق المزدوج + إجبار حاوية الزر على المحاذاة لليمين
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
    
    /* 1. فيديو الخلفية الخارجية */
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
    
    /* 2. فيديو الخلفية الداخلية */
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

    /* إجبار الحاوية التي تحتوي على الزر على محاذاة عناصرها لليمين تماماً */
    [data-testid="stButton"] {
        display: flex !important;
        justify-content: flex-end !important;
        width: 100% !important;
    }

    /* تنسيق زر Next الوردي */
    div.stButton > button:first-child {
        background-color: #E91E63 !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 12px 45px !important;
        border-radius: 30px !important;
        border: none !important;
        box-shadow: 0px 5px 15px rgba(233, 30, 99, 0.4) !important;
        transition: 0.3s !important;
        position: relative !important;
        z-index: 10 !important;
        margin: 0 !important; /* نترك التحكم للـ Flexbox الخارجي */
    }
    div.stButton > button:first-child:hover {
        background-color: #C2185B !important;
        box-shadow: 0px 8px 20px rgba(194, 24, 91, 0.6) !important;
        transform: translateY(-2px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. تشغيل فيديو الفراشات في الخلفية الكاملة للموقع
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

# 5. عرض زر Next الموجه لليمين
if st.button("Next ➡️"):
    pass
