# การเทรนโมเดล

## Callback

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

## การ Compile Model

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