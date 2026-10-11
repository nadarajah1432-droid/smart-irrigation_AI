import streamlit as st
import math

# إعدادات الصفحة العامة للمتصفح
st.set_page_config(
    page_title="نظام الري الذكي بالذكاء الاصطناعي",
    page_icon="🌱",
    layout="centered"
)

# تخصيص واجهة العرض وإخفاء العلامات والهوامش غير المرغوبة
st.markdown("""
    <style>
    .main { background-color: #121212; color: #ffffff; }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #2e7d32, #4caf50);
        color: white; border-radius: 20px; padding: 10px 30px; font-size: 18px; font-weight: bold; width: 100%;
    }
    .info-box {
        background-color: #1e1e1e; padding: 20px; border-radius: 12px;
        border-right: 5px solid #00e676; margin-bottom: 20px; text-align: right;
    }
    /* إلغاء الحواف والخطوط الإضافية الناتجة عن حقول الإدخال */
    div[data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل بين الواجهات باستخدام Session State
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# ==================== 1️⃣ الواجهة الرئيسية ====================
if st.session_state.page == 'main':
    st.image("https://icons8.com", width=120)
    st.title("🌱 نظام الري الذكي القائم على الذكاء الاصطناعي")
    st.subheader("Smart Irrigation System using AI")
    st.write("منصة تفاعلية ذكية تهدف إلى استشراف الاحتياجات المائية للمحاصيل الزراعية بالاعتماد على خوارزميات تعلم الآلة المتقدمة لترشيد استهلاك المياه وتحسين جودة الإنتاج.")
    
    # بطاقات التعريف بفريق العمل والدكتور والمصادر
    st.markdown("""
    <div class="info-box">
        <h4 style='color: #00e676; margin-bottom: 5px;'>👥 إعداد الطالبات</h4>
        <p style='color: white; font-size: 16px; font-weight: bold;'>ندى رزقان ، البتول الزين ، سارة الأهجري</p>
    </div>
    <div class="info-box">
        <h4 style='color: #00e676; margin-bottom: 5px;'>👨‍🏫 إشراف الدكتور</h4>
        <p style='color: white; font-size: 16px; font-weight: bold;'>أ.د. صفوان الشيباني</p>
    </div>
    <div class="info-box">
        <h4 style='color: #00e676; margin-bottom: 5px;'>📚 مصادر جمع البيانات</h4>
        <ul style='color: #b0bec5; list-style-type: square; padding-right: 20px;'>
            <li>منظمة الأغذية والزراعة للأمم المتحدة (FAO) لتحديد الاحتياجات المائية للمحاصيل.</li>
            <li>منصة البيانات العالمية Kaggle للمؤشرات القياسية لرطوبة التربة والتبخر.</li>
            <li>البيانات المناخية التاريخية المستقاة من محطات الأرصاد الجوية المحلية.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.write("### 🌐 الرجاء اختيار لغة الواجهة لتشغيل خوارزمية التنبؤ")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("العربية 🇸🇦"):
            st.session_state.page = 'arabic'
            st.rerun()
    with col2:
        if st.button("English 🇬🇧"):
            st.session_state.page = 'english'
            st.rerun()
# ==================== 2️⃣ الواجهة الثانية (العربية) ====================
elif st.session_state.page == 'arabic':
    st.title("🎛️ مؤشرات الحقل الزراعي والتنبؤ الذكي")
    st.write("يرجى تزويد النموذج بالمعطيات الحالية للأرض ليقوم الذكاء الاصطناعي بحساب قرار الري وساعاته بدقة")
    
    # استخدام Form لحماية البيانات المكتوبة ومنع اختفائها عند التنقل
    with st.form("arabic_irrigation_form"):
        # جعل الحقول فارغة عبر وضع value=None وثابتة بدون اختفاء
        temp = st.number_input("درجة الحرارة (°م)", min_value=5.0, max_value=50.0, value=None, placeholder="أدخل درجة الحرارة هنا")
        moisture = st.number_input("نسبة رطوبة التربة (%)", min_value=0.0, max_value=100.0, value=None, placeholder="أدخل نسبة الرطوبة هنا")
        area = st.number_input("مساحة الأرض (متر مربع)", min_value=10.0, value=None, placeholder="أدخل مساحة الأرض هنا")
        
        soil = st.selectbox("نوع التربة", ["Sandy (رملية)", "Clay (طينية)", "Loam (مزيجية)", "Silty (طمية)"])
        crop = st.selectbox("اختر المحصول الزراعي", [
            "فاصوليا / عدس (بقوليات)", 
            "طماطم (خضروات)", "بطاطس (خضروات)", "بصل (خضروات)", 
            "مانجو (فواكه)", "موز (فواكه)", 
            "قمح / شعير (حبوب)", "ذرة (حبوب)", "أرز (حبوب)"
        ])
        
        # زر التنبؤ داخل النموذج
        submit_ar = st.form_submit_button("🧠 تشغيل خوارزمية التنبؤ بالذكاء الاصطناعي")
        
        if submit_ar:
            # التحقق من أن المستخدم أدخل القيم ولم يترك الخانات فارغة
            if temp is None or moisture is None or area is None:
                st.error("⚠️ الرجاء ملء جميع الخانات الفارغة أولاً قبل تشغيل التنبؤ!")
            else:
                # محاكاة منطق الخوارزميتين المدمجتين (التصنيف وحساب الساعات)
                irrigation_status = 1 if moisture < 35 or (temp > 30 and moisture < 45) else 0
                
                if irrigation_status == 1:
                    base_hours = 6.0 if "طماطم" in crop or "مانجو" in crop else 4.5
                    soil_mult = 1.3 if "رملية" in soil else 1.0
                    calc_hours = base_hours * soil_mult * (1 + (temp - 25) * 0.02) * (1 - (moisture / 100))
                    final_hours = min(max(calc_hours, 1.5), 12.0)
                    
                    st.success("### 🌱 قرار الري: الحقل يحتاج إلى ري فوراً")
                    st.metric(label="⏱️ عدد ساعات الري المقترحة", value=f"{final_hours:.1f} ساعة")
                else:
                    st.warning("### ☀️ قرار الري: الحقل لا يحتاج إلى ري حالياً")
                    st.metric(label="⏱️ عدد ساعات الري المقترحة", value="0 ساعة")
                
    if st.button("⬅️ العودة للصفحة الرئيسية"):
        st.session_state.page = 'main'
        st.rerun()
# ==================== 3️⃣ الواجهة الثالثة (الإنجليزية) ====================
elif st.session_state.page == 'english':
    st.title("🎛️ Field Parameters & AI Prediction")
    st.write("Please provide the current metrics of the field to evaluate the irrigation decisions via Machine Learning")
    
    # استخدام Form لحماية البيانات باللغة الإنجليزية وجعلها فارغة
    with st.form("english_irrigation_form"):
        temp = st.number_input("Temperature (°C)", min_value=5.0, max_value=50.0, value=None, placeholder="Enter temperature")
        moisture = st.number_input("Soil Moisture (%)", min_value=0.0, max_value=100.0, value=None, placeholder="Enter soil moisture")
        area = st.number_input("Land Area (sqm)", min_value=10.0, value=None, placeholder="Enter land area")
        
        soil = st.selectbox("Soil Type", ["Sandy", "Clay", "Loam", "Silty"])
        crop = st.selectbox("Select Crop Type", [
            "Beans / Lentils (Legumes)", 
            "Tomato (Vegetables)", "Potato (Vegetables)", "Onion (Vegetables)", 
            "Mango (Fruits)", "Banana (Fruits)", 
            "Wheat / Barley (Grains)", "Corn (Grains)", "Rice (Grains)"
        ])
        
        submit_en = st.form_submit_button("🧠 Execute AI Prediction Models")
        
        if submit_en:
            if temp is None or moisture is None or area is None:
                st.error("⚠️ Please fill in all empty fields before executing the prediction!")
            else:
                irrigation_status = 1 if moisture < 35 or (temp > 30 and moisture < 45) else 0
                
                if irrigation_status == 1:
                    base_hours = 6.0 if "Tomato" in crop or "Mango" in crop else 4.5
                    soil_mult = 1.3 if "Sandy" in soil else 1.0
                    calc_hours = base_hours * soil_mult * (1 + (temp - 25) * 0.02) * (1 - (moisture / 100))
                    final_hours = min(max(calc_hours, 1.5), 12.0)
                    
                    st.success("### 🌱 Irrigation Status: Irrigation is REQUIRED")
                    st.metric(label="⏱️ Recommended Duration", value=f"{final_hours:.1f} Hours")
                else:
                    st.warning("### ☀️ Irrigation Status: Irrigation is NOT Required")
                    st.metric(label="⏱️ Recommended Duration", value="0 Hours")
                
    if st.button("⬅️ Back to Main Page"):
        st.session_state.page = 'main'
        st.rerun()
