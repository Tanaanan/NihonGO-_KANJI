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

## ขั้นตอนการรันโค้ดโปรเจกต์

- ### การดึงข้อมูล
  - #### run file name : 1_load_data.ipynb ตาม instruction markdown ใน file
    - ใน Data_clean.ipynb
- ### การ preprocess ข้อมูล

  - เป็นไฟล์สำหรับการทำความสะอาดข้อมูล ซึ่งข้อมูลที่ราได้มาเป็นข้อมูลที่มีชื่อไฟล์เป็น Binary กับกับซึ่งตรงกับตัวอักษรญี่ปุ่น การ run file นี้เป็น optional เนื่องจากว่าเราได้ทำการรันไว้ให้ก่อนแล้ว เพราะการรันไฟล์นี้ค่อนข้างใช้เวลาค่อนข้างเยอะ เราจึงแนะนำให้ท่านข้ามไฟล์นี้ไปรันไฟล์ `3_split_valid_test.ipynb` ที่ได้เรียกใช้ข้อมูลจากโฟล์เดอร์ `KanjiN5_normalize` ที่เราได้ cleaning เรียบร้อยแล้ว ซึ่งได้คัดข้อมูลตัวอักษรภาษาญี่ปุ่นระดับ N5 มาแล้วทั้งหมด 81 ตัว

  #### ขั้นตอนการทำำ Data Cleaning

    - การสร้างโฟลเดอร์สำหรับแต่ละตัวอักษร เราจะสร้างโฟลเดอร์ใหม่สำหรับแต่ละตัวอักษรโดยใช้ Unicode character เป็นชื่อโฟลเดอร์ เพื่อให้ง่ายต่อการจัดการและสร้างฐานข้อมูลสำหรับการฝึกโมเดล

    - หลังจากนั้นเราจะนำข้อมูลที่ได้มาจากขั้นตอนก่อนหน้าเข้าสู่โมเดลเพื่อใช้ในการฝึก โดยใช้โครงสร้างโฟลเดอร์ที่ถูกจัดเตรียมไว้ในขั้นตอนก่อนหน้า เพื่อสร้างโมเดล OCR ซึ่งสามารถอ่านและแยกแยะตัวอักษรจากภาพได้โดยอัตโนมัติ

    - สุดท้ายเราจะสร้างโฟลเดอร์ใหม่สำหรับแต่ละตัวอักษรที่สำคัญ โดยใช้เฉพาะตัวอักษรที่มีความสำคัญตามระดับ N5 ในภาษาญี่ปุ่น ซึ่งจะนำไปใช้ในการฝึกโมเดล OCR ให้มีความแม่นยำและเชื่อถือได้ในการอ่านและแยกแยะตัวอักษรในภาพ








- ### การโหลดข้อมูล
-
- ### การสร้างโมเดล VGG16
- ### การสร้างโมเดล LeNet5
- ### การเทรนโมเดล

- ### การวัดประสิทธิภาพโมเดล
- ### รวมถึงการใช้โมเดล
