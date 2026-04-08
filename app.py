import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="Brain Tumor Detection", page_icon="🧠")

# عنوان الموقع
st.title("🧠 نظام الكشف عن أورام الدماغ")
st.write("قم برفع صورة أشعة الرنين المغناطيسي (MRI) ليقوم الذكاء الاصطناعي بتحليلها واكتشاف نوع الورم إن وجد.")

# 1. تحميل النموذج (استخدمنا cache لكي لا يتم تحميله من جديد مع كل ضغطة)
@st.cache_resource
def load_model():
    # تأكد أن اسم الملف هنا يطابق اسم الملف الذي قمت بتحميله
    model = tf.keras.models.load_model('brain_tumor_vgg16_model.h5')
    return model

model = load_model()

# أسماء التصنيفات (نفس ترتيب المجلدات في الداتا)
class_names = ['Glioma Tumor (ورم دبقي)', 
               'Meningioma Tumor (ورم سحائي)', 
               'No Tumor (لا يوجد ورم - سليم)', 
               'Pituitary Tumor (ورم الغدة النخامية)']

# 2. أداة رفع الصور
uploaded_file = st.file_uploader("ارفع صورة الأشعة هنا (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # عرض الصورة التي رفعها المستخدم
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة المرفوعة', use_column_width=True)
    st.write("جاري التحليل...")

    # 3. تجهيز الصورة (Pre-processing) لتناسب النموذج
    # تحويل الصورة إلى RGB وتغيير حجمها لـ 224x224
    img = image.convert('RGB')
    img = img.resize((224, 224))
    
    # تحويل الصورة لمصفوفة أرقام وعمل Normalization (قسمة على 255)
    img_array = np.array(img) / 255.0
    
    # إضافة بُعد إضافي لأن النموذج يتوقع مجموعة صور (Batch) وليس صورة واحدة
    img_array = np.expand_dims(img_array, axis=0)

    # 4. التوقع (Prediction)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions) * 100 # نسبة التأكد

    # 5. عرض النتيجة
    st.markdown("---")
    if predicted_class == 2: # إذا كان لا يوجد ورم
        st.success(f"النتيجة: **{class_names[predicted_class]}**")
    else: # إذا كان هناك ورم
        st.error(f"النتيجة: **{class_names[predicted_class]}**")
        
    st.info(f"نسبة تأكد الذكاء الاصطناعي: {confidence:.2f}%")