# รายละเอียดของสมาชิกในกลุ่ม

- ### 1.ธนอนันท์ เฉลิมพันธ์ 6610402078
- ### 2.ปฏิภัทธิ์ อุคำ 6610402141
- ### 3.ศิริสุข ทานธรรม 6610402230

# คำอธิบายเกี่ยวกับไฟล์และโฟลเดอร์

## ทำตามขั้นตอนชื่อ file (1 - 5) .ipynb

- `1_load_data.ipynb`
  - ใช้โหลดข้อมูล datasets ที่ยังไม่ clean และโหลด model VGG16 ที่เสร็จจสมบูรณ์ (เนื่องจากมีขนาดใหญ่ไม่สามารถอัพโหลดลง github ได้)
- `2_Data clean.ipynb`
  - ใช้ clean ข้อมูล raw datasets ให้พร้อม split
- `3_split_valid_test.ipynb`
  - ไฟล์ที่ใช้ split Datasets ออกเป็น Train Valid และ Test datasets ซึ่งรวมข้อมูลตัวอย่างที่เก็บเพิ่มไว้แล้ว
- `4_VGG16_finetune.ipynb`
  - ไฟล์ที่ใช้ train model ด้วย VGG16
- `5_LeNet5_augment.ipynb`

  - ไฟล์ที่ใช้ train model ด้วย LeNet5 from scratch

- ### -โฟลเดอร์ KanjiN5_normalize datasets หลัก
- ### -โฟลเดอร์ 明\_self labels เป็นข้อมูลตัวอย่างเก็บเพิ่ม

# ขั้นตอนการรันโค้ดโปรเจกต์

#### follow instruction

## \*การดึงข้อมูล (1_load_data.ipynb) (required)

- ดึงข้อมูล unclean datasets โดยใช้ 1_load_data.ipynb

## \*การ preprocess ข้อมูล (2_Data clean.ipynb, 3_split_valid_test.ipynb)

#### ขั้นตอนการทำ Data Cleaning (required)

- การสร้างโฟลเดอร์สำหรับแต่ละตัวอักษร เราจะสร้างโฟลเดอร์ใหม่สำหรับแต่ละตัวอักษรโดยใช้ Unicode character เป็นชื่อโฟลเดอร์ เพื่อให้ง่ายต่อการจัดการและสร้างฐานข้อมูลสำหรับการฝึกโมเดล

- หลังจากนั้นเราจะนำข้อมูลที่ได้มาจากขั้นตอนก่อนหน้าเข้าสู่โมเดลเพื่อใช้ในการฝึก โดยใช้โครงสร้างโฟลเดอร์ที่ถูกจัดเตรียมไว้ในขั้นตอนก่อนหน้า เพื่อสร้างโมเดล OCR ซึ่งสามารถอ่านและแยกแยะตัวอักษรจากภาพได้โดยอัตโนมัติ

- สุดท้ายเราจะสร้างโฟลเดอร์ใหม่สำหรับแต่ละตัวอักษรที่สำคัญ โดยใช้เฉพาะตัวอักษรที่มีความสำคัญตามระดับ N5 ในภาษาญี่ปุ่น ซึ่งจะนำไปใช้ในการฝึกโมเดล OCR ให้มีความแม่นยำและเชื่อถือได้ในการอ่านและแยกแยะตัวอักษรในภาพ

## \*การโหลดข้อมูล

- ใช้ Keras ImageGenerator และ Augmentation จาก file path Train Valid และ Test

## \*การสร้างโมเดล VGG16 (4_VGG16_finetune.ipynb)

- สร้าง model รูปแบบ sequential ด้วย VGG16 ด้วย weight จาก imageNet และนำมาทำ Freeze เปลี่ยน last layers เป็น dense และ output layer ให้ model เรียนรู้จาก wieght ของ VGG16
- แล้วจึง unfreeze และ train model โดยใช้ earlystopping

## \*การสร้างโมเดล LeNet5 (5_LeNet5_augment.ipynb)

- สร้าง model รูปแบบ sequential และ Augmentation from scratch จากรูปแบบ โครงสร้างของ LeNet5 train model โดยใช้ earlystopping

## \*การเทรนโมเดล

### Callback

ในการเทรนโมเดล เราใช้ Callbacks เพื่อตรวจสอบและควบคุมกระบวนการเทรน ในตัวอย่างนี้มีการใช้ EarlyStopping ซึ่งจะหยุดกระบวนการเทรนเมื่อไม่มีการปรับปรุงความแม่นยำบนชุดการตรวจสอบ (validation set) เป็นเวลา 3 รอบ สำหรับโมเดล Fine-Tune จาก VGG 16 และ 10 รอบ สำหรับโมเดล LeNet-5 และ ModelCheckpoint ซึ่งจะบันทึกโมเดลที่ดีที่สุดเมื่อมีความแม่นยำบนชุดการตรวจสอบ

```py
filepath = "./new_labels_weight/save-{epoch:02d}-{loss:.4f}.h5"
vggpatience = 3
lenetpatience = 10

callback = [
    EarlyStopping(patience=patience,
                    monitor='val_accuracy'),
    ModelCheckpoint(filepath,
                    monitor='val_accuracy',
                    verbose=1,
                    save_best_only=True,
                    mode='max')
]
```

### การ Compile Model

```py
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-6),
    loss=keras.losses.CategoricalCrossentropy(from_logits=False),metrics=['accuracy'])
```

Optimizer ใช้เป็น Adam ซึ่งเป็นวิธีการปรับค่า learning rate แบบอัตโนมัติตาม Gradient ของ gradient descent เพื่อช่วยในการควบคุมการเรียนรู้ของโมเดล

Loss Function ใช้เป็น Categorical Crossentropy เป็นฟังก์ชันสูญเสียที่ใช้ในการประมาณความแตกต่างระหว่างการทำนายจากโมเดลกับค่าเป้าหมาย ในกรณีที่มีหลายคลาส (multi-class classification)

Metrics ในกรณีนี้ใช้ metrics เพียงแค่ accuracy เพื่อวัดประสิทธิภาพของโมเดลในการจำแนกคลาส

## Fitting model

```py
history = model.fit(
    train_ds,
    epochs=epochs,
    validation_data=valid_ds,
    callbacks=callback
)
```

ในส่วนนี้จะเป็นการฝึกโมเดลโดยใช้ข้อมูลจาก train_ds และทดสอบโมเดลด้วยข้อมูลจาก valid_ds โดยกำหนดจำนวนรอบการฝึก (epochs) เท่ากับ 100 รอบสำหรับ VGG 16 และ 20 รอบสำหรับ LeNet-5 และใช้ข้อมูล validation_data เพื่อตรวจสอบประสิทธิภาพของโมเดลในแต่ละรอบการฝึก

## \*การวัดประสิทธิภาพโมเดล
  - `Classification Report` จะประกอบด้วยค่า precision, recall, F1-score และ support สำหรับแต่ละคลาสที่ได้จากการทำนายของโมเดล การวิเคราะห์ classification report ช่วยให้เข้าใจถึงประสิทธิภาพของโมเดลในการจำแนกคลาสแต่ละคลาสอย่างละเอียด
  การทำ Classification Report สามารถคำนวณได้ตามขั้นตอนต่อไปนี้

  ```py
  from sklearn.metrics import classification_report

  report = classification_report(true_labels, y_pred, target_names=list(train_ds.class_indices.keys()))
  print("Classification Report:")
  print(report)
  ```
  ขั้นตอนที่นำมาใช้คือการเรียกใช้ฟังก์ชัน classification_report จากไลบรารี Scikit-learn โดยกำหนดพารามิเตอร์ดังนี้
    - true_labels: คือค่าจริงของป้ายกำกับ (ground truth) ของข้อมูลที่ใช้ทดสอบโมเดล
    - y_pred: คือค่าทำนายที่โมเดลทำได้สำหรับข้อมูลทดสอบ
    - target_names: รายการชื่อของหมวดหมู่หรือป้ายกำกับที่ใช้ในการจำแนก ซึ่งสามารถระบุได้จาก 
    - train_ds.class_indices.keys() ซึ่งเป็นชื่อของหมวดหมู่ที่มีอยู่ในชุดข้อมูลการฝึก

  - `Confusion Matrix` เป็นตารางที่แสดงความถูกต้องและความผิดพลาดในการจำแนกคลาส ซึ่งแสดงจำนวนของข้อมูลที่ถูกจำแนกถูกต้องและไม่ถูกต้องในแต่ละคลาส การวิเคราะห์ confusion matrix ช่วยในการระบุว่าโมเดลมีประสิทธิภาพในการจำแนกคลาสใดบ้าง และคลาสใดที่มักจะทำให้โมเดลสับสนบ้าง ซึ่งสามารถคำนวณได้ดังนี้

  ```py
  from sklearn.metrics import confusion_matrix

  cm = confusion_matrix(true_labels, y_pred)
  ```
  เรียกใช้ฟังก์ชัน confusion_matrix จากไลบรารี Scikit-learn โดยกำหนดพารามิเตอร์ดังนี้

    - true_labels: คือค่าจริงของป้ายกำกับ (ground truth) ของข้อมูลที่ใช้ทดสอบโมเดล
    - y_pred: คือค่าทำนายที่โมเดลทำได้สำหรับข้อมูลทดสอบ
  
  ผลลัพธ์ที่ได้จะเป็นเมทริกซ์ที่แสดงจำนวนของตัวอย่างที่โมเดลทำนายได้ถูกและผิดสำหรับแต่ละคลาสหรือหมวดหมู่ที่มีอยู่ในข้อมูลทดสอบ จึงช่วยในการวิเคราะห์ประสิทธิภาพของโมเดลในการจำแนกประเภทและการจำแนกป้ายกำกับในชุดข้อมูลทดสอบ

  ## \*visulize file
  - ไฟล์แสดงตัวอย่างผลลัพธ์ที่ได้จากการทำ Image augmentation และการทำ Image pre-processing
  ```py
  - Image augmentation : ทำการเลื่อนไปด้านซ้าย ขวา และทำการซูมรูปภาพที่ละ 0.1
  - Image preprocessing : ทำ Binary Thresholding
  ```




## รวมถึงการใช้โมเดล
## \*model test file

- ใช้ในการทดลองทำนายโมเดลจากภายนอกโดยการแนบรูปภาพ โดยใช้ model_load  และ model.predict
```py
- ทดลองรูปแบบที่ Deploy ลงบน Huggingface space
1. LeNet5_model : https://huggingface.co/spaces/Tanaanan/NihonGO_MLPmodel
2. VGG16_model : https://huggingface.co/spaces/Tanaanan/NihonGO_JLPTN5
```
