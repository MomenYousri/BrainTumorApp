# 🧠 Brain Tumor Classification Web Application

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

نظام ذكاء اصطناعي متكامل (End-to-End) يهدف إلى مساعدة الأطباء وأخصائيي الأشعة في التحليل السريع لصور أشعة الرنين المغناطيسي (**MRI**) واكتشاف أورام الدماغ بدقة.

---

## 🎯 أهداف المشروع (Project Objectives)
يقوم النظام بتصنيف صور الأشعة إلى 4 فئات رئيسية:
1. **Glioma Tumor** (ورم دبقي)
2. **Meningioma Tumor** (ورم سحائي)
3. **Pituitary Tumor** (ورم الغدة النخامية)
4. **No Tumor** (دماغ سليم / لا يوجد ورم)

---

## 🛠️ التقنيات المستخدمة (Tech Stack)
* **لغة البرمجة:** Python
* **بناء النماذج:** TensorFlow & Keras
* **معالجة الصور:** OpenCV, PIL, NumPy
* **التقييم والرسم البياني:** Matplotlib, Seaborn, Scikit-learn
* **واجهة الويب:** Streamlit

---

## 🚀 مراحل التنفيذ (Methodology)

### 1️⃣ معالجة البيانات (Pre-processing)
* **Normalization:** تحويل قيم البيكسل لتكون بين [0, 1].
* **Resizing:** توحيد حجم الصور إلى (224x224).
* **Data Augmentation:** تطبيق تقنيات (الدوران، الإزاحة، التكبير) لزيادة دقة النموذج وتجنب الـ **Overfitting**.

### 2️⃣ بناء النماذج (Modeling)
تمت المقارنة بين نهجين:
* **CNN From Scratch:** نموذج مخصص حقق دقة 80% في التدريب و54% في الاختبار.
* **Transfer Learning (VGG16):** باستخدام نموذج **VGG16** مسبق التدريب، حققنا قفزة في الأداء لتصل الدقة إلى **70%** في عدد دورات (Epochs) قليل جداً.

### 3️⃣ التقييم (Evaluation)
* مراقبة منحنيات الـ **Accuracy** والـ **Loss**.
* تحليل النتائج عبر **Classification Report** و **Confusion Matrix**.

---

## 💻 تطبيق الويب (Web Application)
واجهة تفاعلية بسيطة تسمح للمستخدم برفع صورة أشعة MRI والحصول على:
* **النتيجة (نوع الورم).**
* **نسبة الثقة (Confidence Score).**

---

## 📂 هيكلة الملفات (Project Structure)
```text
├── dataset/             # مجلد البيانات (Train/Test)
├── models/              # النماذج المحفوظة (.h5)
├── notebooks/           # كود التدريب (Jupyter Notebook)
├── app.py               # كود تطبيق Streamlit
├── requirements.txt     # المكتبات المطلوبة
└── README.md            # وصف المشروع
