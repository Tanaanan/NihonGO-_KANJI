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

## การดึงข้อมูล (1_load_data.ipynb)

- #### run file name : 1_load_data.ipynb ตาม instruction markdown ใน file
  - ใน Data_clean.ipynb

## การ preprocess ข้อมูล (2_Data clean.ipynb, 3_split_valid_test.ipynb)

- เป็นไฟล์สำหรับการทำความสะอาดข้อมูล ซึ่งข้อมูลที่ราได้มาเป็นข้อมูลที่มีชื่อไฟล์เป็น Binary กับกับซึ่งตรงกับตัวอักษรญี่ปุ่น การ run file นี้เป็น optional เนื่องจากว่าเราได้ทำการรันไว้ให้ก่อนแล้ว ซึ่งจะอยู่ที่ file ... เนื่องจากว่าการรันไฟล์นี้ค่อนข้างใช้เวลาค่อนข้างเยอะ เราจึงแนะนำให้ท่านไปรันไฟล์ ... ที่ได้เรียกใช้ ... ที่เราได้ cleaning เรียบร้อยแล้ว ซึ่งได้คัดข้อมูลตัวอักษรภาษาญี่ปุ่นระดับ N5 มาแล้วทั้งหมด 81 ตัว

## การโหลดข้อมูล

- ใช้ Keras ImageGenerator และ Augmentation จาก file path Train Valid และ Test

## การสร้างโมเดล VGG16 (4_VGG16_finetune.ipynb)

- สร้าง model รูปแบบ sequential ด้วย VGG16 ด้วย weight จาก imageNet และนำมาทำ Freeze เปลี่ยน last layers เป็น dense และ output layer ให้ model เรียนรู้จาก wieght ของ VGG16
- แล้วจึง unfreeze และ train model โดยใช้ earlystopping

## การสร้างโมเดล LeNet5 (5_LeNet5_augment.ipynb)

- สร้าง model รูปแบบ sequential และ Augmentation from scratch จากรูปแบบ โครงสร้างของ LeNet5 train model โดยใช้ earlystopping

## การเทรนโมเดล

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

## การวัดประสิทธิภาพโมเดล

## รวมถึงการใช้โมเดล
