# AIPrototype24  
	
SC664401	Prototyping for Artificial Intelligence and Machine Learning System

การสร้างต้นแบบสำหรับระบบปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง

Git by

Wuttichai Khamna 643020521-0 SIDS 

<wuttichai.kha@kkumail.com>

เกี่ยวกับ

แนวคิดและขั้นตอนในการสร้างต้นแบบระบบปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง การประมวลผลบนคลาวด์
เครื่องคอมพิวเตอร์แบบเสมือน การใช้งานชุดคำสั่งยูนิกส์เบื้องต้น การใช้งาน GIT เบื้องต้น การใช้งานไพธอนโน๊ตบุ๊คบนคลาวด์
การสร้างเว็ปแอพพลิเคชั่นและ API ด้วยภาษาไพธอน การพัฒนาระบบเรียนรู้เชิงลึกด้วยชุดคำสั่งไพธอน 
การลงบันทึกและการใช้แดชบอร์ดแสดงผลข้อมูล
about

Concepts of Artificial Intelligent/Machine Leaning system implementation and prototyping the AI/ML system: 
cloud computing, virtual machine, basic unix, basic GIT and version control, cloud Python notebook, webapplication 
and API development with Python, deep learning with Python, logging, and dashboard

*** วันที่เรียนวันแรก 20/11/2024 ***

*** วันที่นำเสนอ 12/3/2025 ***

*** สิ่งที่ต้องนำเสนอ: ***
-
- Git hub เว็ปนำเสนอผลงาน
- Git hub เว็ปไซต์โปรเจค
- Git hub ตัวเอง
- หน้าเว็ปไซต์โปรเจค
- หน้าเว็ป นำเสนอผลงาน

## งานวิจัยที่ต้องทำในเทอม 2 
1.พัฒนาโมเดลสำหรับการเเยก คลาส 3 คลาส  
2.ออกแบบการทดลองสำหรับการประเมิน Data Visualization เเละ Generative AI  
3.ยื่นขอจริยธรรม (เสร็จสิ้นเหมือน 7 มีนาคม 2565 หมดอายุวันที่ 
4.เเก้เว็ปไซต์หน้า Data Visualization (เพิ่มกราฟ เเละ เเก้ปัญหา)  
5.เเก้เล่ม Project โดยการออกแบบการทดลองในบทสามอย่างละเอียดๆ และ ผลการประเมินอัทกอริทึลของระบบ  
6.การประเมินอัทกอริทึลของระบบ  

## How to start
[link for guideinstarll](https://l.facebook.com/l.php?u=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1ucrIMVO-4pzv2_OoIB4JxZxY-oSVZrVv%3Fusp%3Dsharing%26fbclid%3DIwZXh0bgNhZW0CMTAAAR0bUHTC5VxIZdEAf989vNqZhF_ssXDiGnJ-cyKN2btjxiBENNY5yYKpkzE_aem_3msFBiaAvZJ800BAVFDxQw&h=AT0h9wvL9gXL3QngPZtQka90k4LJo5_3ZshYp-WACXhDxA9QnQF3uDpT4DdVQ46sVG4_Xr95FFOwiNly6imbeAelBeCDzmPM5zL8cN6j7d9cMvhvMrcH2rdRQxavW-r3w1Up&__tn__=-UK-R&c[0]=AT3YCy9vGA96AaiSZNNOcrK3r6WF9Ae9ApWgRNKNbcVprvOkZkrSJWnNp6s8KmnpFugCjO1nJe03SlkGndWJRhaodkTFe3BGTs0U1OKL0h2ZlR3cQS8LJwZP2jIdCQJzXXB2swJyMALnh_6DDVtLSKc3F1GGkyUAwPz5soofPBYfkY_b9X0ebmjXkPbXpPM8nm4lx3erG9svP0hPpOQk5d3m2RL-TA)

1.install ubuntu 

2.Use Microsoft Azure (cloud) 

3.คำสั่ง liunx

## Code Shortcut 
$pwd

$ls ---> ใช้ดูต่ำแหน่ง  

$ls -l ---> ใช้ดูต่ำแหน่งแบบยาว (long)

$ls -lh ---> ใช้ดูต่ำแหน่งที่มนุษย์อ่านได้ (Human)

$ls -ltr[h] ---> ใช้ดูต่ำแหน่งแบบเรียงตามเวลาจากเก่าไปใหม่[สามารถทำให้มนุษย์อ่านได้] (long time rever[human])

$cd --> เปลี่ยนพื้นที่่ทำงาน (เปิด/ปิด โฟลเดอร์)

$cd {name_file}--> เปิดโฟลเดอร์ name_file

$cd .. --> ออก 1 ขั้น

$cd ../.. --> ออก 2 ขั้น

$man {command}--> ใช้ดูคำสั่งต่างๆ (เป็นตัวช่วยเหลือว่าใช้อะไรได้บ้างในคำสั่งนี้)

$mv {ชื่อไฟล์} {ที่ไหน} ---> ย้ายโฟเดอร์

$cat {ชื่อไฟล์ / path file} ---> ไว้ใช้อ่าน ไฟล์ต่างๆ

$rm

## จัดการ minicoda

$conda create --name <my-env>

$conda create -n myenv <name of packger>

$coda activate <my-env>

$coda deactivate

$mv {ชื่อไฟล์} {ที่ไหน} ---> ย้ายโฟเดอร์

$cat {ชื่อไฟล์ / path file} ---> ไว้ใช้อ่าน ไฟล์ต่างๆ

$rm


