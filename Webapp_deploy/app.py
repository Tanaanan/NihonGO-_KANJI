import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import keras.utils as image
import cv2
from data import Getdetail

st.title('JLPTN5 handwriting Kanji recognition.')

labels = ['一', '七', '万', '三', '上', '下', '中', '九', '二', '五', '人', '今', '休', '何', '先', '入', '八', '六', '円', '出', '分', '前', '北', '十', '千', '午', '半', '南', '友', '右', '名', '四', '国', '土', '外', '大', '天', '女', '子', '学', '小', '山', '川', '左', '年', '後', '日', '明', '時', '書', '月', '木', '本', '来', '東', '校', '母', '毎', '気', '水', '火', '父', '生', '男', '白', '百', '聞', '行', '西', '見', '話', '語', '読', '車', '金', '長', '間', '雨', '電', '食', '高']
model = load_model("./Lenet5_Dropout2.h5")

st.sidebar.title("NihonGO !")
st.sidebar.caption("Handwriting kanji recognition system.")
options = ("Sketchpad input", "Image input", "about JLPTN5", "about NihonGO !")
choice = st.sidebar.selectbox("Select input options",options)
st.sidebar.caption("Dev by : Tanaanan Chalermpan")
st.sidebar.caption("Computer Science Kasetsart U. Thailand")



def predict_img_sketch(img_path):
        st.write("Predicted result.")
        if img_path is not None: 
            img = Image.fromarray(img_path) # use pillow to load a image
            img = img.convert('L')
            img = np.array(img) # convert img to an array
            ret, thresh1 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)  # Apply binary threshold
            thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2RGB)  # Convert back to RGB
            img_array = cv2.resize(thresh1, (120, 120))  # Resize the image
            img_array = np.expand_dims(img_array, axis=0)
            preds = model.predict(img_array)
            return preds
        
def image_display(img_path):
    st.write("Predicted image.")
    if img_path is not None:
        img = Image.open(img_path)
        img = img.resize((120,120)).convert('L')
        st.image(img, caption='Uploaded Image', use_column_width=True)

def predict_img_input(img_path):
        st.write("Predicted result.")
        if img_path is not None: 
            img = Image.open(img_path) # use pillow to load a image
            img = img.convert('L')
            img = np.array(img) # convert img to an array
            ret, thresh1 = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)  # Apply binary threshold
            thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2RGB)  # Convert back to RGB
            img_array = cv2.resize(thresh1, (120, 120))  # Resize the image
            img_array = np.expand_dims(img_array, axis=0)
            preds = model.predict(img_array)
            return preds

if choice == "Sketchpad input":
        

    col1,col2 = st.columns(2)
    with col2:
        stroke_width = st.slider("Stroke width: ", 2, 25, 2)

    with col1:
        # ref : https://github.com/andfanilo/streamlit-drawable-canvas
        canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color="#000000", # stroke to black
        background_color="#FFFFFF", # background to write
        background_image= None,
        update_streamlit=False,
        height=200,
        width=200,
        drawing_mode="freedraw",
        point_display_radius=0,
        key="canvas",
    )
        # Do something interesting with the image data and paths
        if canvas_result.image_data is not None:
            st.image(canvas_result.image_data, caption='display_show')

    with col2:
        # check if sketchinput is empty from len json_data
        is_empty = 0
        if canvas_result.image_data is not None: # beware of slow loading
            is_empty = canvas_result.json_data["objects"] # need to convert obj to str because PyArrow
        
        if is_empty:
            # display prediction
            pred_raw = predict_img_sketch(canvas_result.image_data)
            if pred_raw is not None:    
                pred_class, accuracy = labels[np.argmax(pred_raw)], np.max(pred_raw)*100
                st.write(f"Class : {labels[np.argmax(pred_raw)]}")
                st.write(f"with accuracy : {accuracy:.2f} %")

                st.divider()
                strokes = Getdetail()[pred_class]['Strokes']
                meaning = Getdetail()[pred_class]['Meaning']
                onyoumi = Getdetail()[pred_class]['Onyoumi']
                kunyomi = Getdetail()[pred_class]['Kunyoumi']
                link_ref = Getdetail()[pred_class]['Reference']

                st.write(f"Strokes : {strokes}")
                st.write(f"Meaning : {meaning.capitalize()}")
                st.write(f"Onyoumi : {onyoumi}")
                st.write(f"Kunyoumi : {kunyomi}")
                st.write(f"for more detail : [Shirabe jisho]({link_ref})")

elif choice == "Image input":
    upload_img = st.file_uploader("Choose a kanji image", type=['.jpg', '.png', '.jpeg'])
    col1,col2 = st.columns(2)

    with col1:
        image_display(upload_img)

    with col2:
        # display prediction
        pred_raw = predict_img_input(upload_img)
        if pred_raw is not None:    
            pred_class, accuracy = labels[np.argmax(pred_raw)], np.max(pred_raw)*100
            st.write(f"Class : {labels[np.argmax(pred_raw)]}")
            st.write(f"with accuracy : {accuracy:.2f} %")

            st.write('---------------------------------------')
            strokes = Getdetail()[pred_class]['Strokes']
            meaning = Getdetail()[pred_class]['Meaning']
            onyoumi = Getdetail()[pred_class]['Onyoumi']
            kunyomi = Getdetail()[pred_class]['Kunyoumi']
            link_ref = Getdetail()[pred_class]['Reference']

            st.write(f"Strokes : {strokes}")
            st.write(f"Meaning : {meaning.capitalize()}")
            st.write(f"Onyoumi : {onyoumi}")
            st.write(f"Kunyoumi : {kunyomi}")
            st.write(f"for more detail : [Shirabe jisho]({link_ref})")

elif choice == "about JLPTN5":
    df = pd.read_csv('./passjapanesetest.com_N5_Kanji.csv', encoding='cp932')
    st.subheader("JLPT คืออะไร")
    detail_1 = '''ย่อมาจาก Japanese Language Proficiency Test  การสอบวัดระดับภาษาญี่ปุ่น คือ การสอบที่จัดขึ้นเพื่อวัดความสามารถทางภาษาญี่ปุ่น ของชาวต่างชาติผู้เรียนภาษาญี่ปุ่น
    
การสอบวัดระดับภาษาญี่ปุ่นครั้งแรก จัดขึ้นในปี ค.ศ. 1984  มีผู้สมัครสอบ 7,998 คน และมีผู้สมัครสอบเพิ่มขึ้นมากทุกปี   สถิติในปี ค.ศ. 2019 มีผู้สมัครสอบถึง 1,362,167 คนทั่วโลก'''
    st.markdown(detail_1)
    st.markdown('''- โดยระดับ N5 ถือเป็นระดับที่ง่ายที่สุดในการสอบ แต่พาร์ทที่หินที่สุดส่วนหนึ่งก็คือ พาร์ท คันจิ N5 ***ผู้พัฒนาจึงสร้างระบบที่วิเคราะห์ตัวอักษรคันจิได้จากลายมือเขียน 
                เพื่อที่จะเป็นตัวช่วยหนึ่งในการให้ผู้ใช้งานได้ใช้ในการฝึกฝนได้***''')

    st.caption("List of JLPTN5 Kanji")
    st.write(df)

    st.caption('ref : [jeducation](https://jeducation.com/main/education/jlpt/) , [passjapanesetest](http://www.passjapanesetest.com/jlpt-n5-kanji-list/)')

elif choice == "about NihonGO !":
    st.subheader("NihonGO ! คืออะไร")
    detail_2 = """NihonGO ! : เป็นระบบที่ใช้ในการวิเคราะห์ตัวอักษรคันจิจากลายมือเขียนโดยอัติโนมัติ โดยใช้หลักการของ Deep learning (Convolutional Neural Network) ในการแยกแยะตัวอักษรคันจิ
    เพื่อใช้เป็นตัวช่วยในการฝึกฝนการเขียนคันจิ และเป็นตัวช่วยในการฝึกฝนในการเตรียมสอบวัดระดับ JLPT"""
    st.markdown(detail_2)
    st.caption("Development.")
    st.markdown("- JLPTN5 : ระบบสามารถแยกแยะคันจิจำนวน 80 ตัวพื้นฐานตามเนื้อหาคันจิจากการสอบวัดระดับ JLPTN5")
    st.image('total_kanji.png', caption='JLPTN5 Kanji detail')
    st.subheader("Feature")
    st.markdown("""     1. บอกคันจิที่ระบบตรวจจับได้พร้อมกับค่าความเชื่อมั่น (accuracy score.)
                
    2. จำนวนเส้น stroke ที่ใช้ในการเขียนคันจิ
                
    3. เสียงอ่านแบบ Onyoumi กับ Kunyoumi พร้อมกับตัวอักษร Romanji
                
    4. Link เนื้อหาเพิ่มเติมโดยระเอียดกับ website Shirabe jisho""")
    st.subheader("Guideline")
    st.markdown(""" - เพื่อความแม่นยำของระบบ ตอนนำข้อมูลรูปภาพเข้า หรือเขียนในระบบแนะนำให้ผู้ใช้งานเขียนตัวคันจิให้อยู่ตรงกลาง และมีขนาดที่ใหญ่พอดีกับขนาดของกรอบ""")
    st.caption("ref : [kanshudo](https://www.kanshudo.com/collections/jlpt_kanji)")

    
    
