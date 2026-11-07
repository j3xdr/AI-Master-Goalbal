# หมวดหมู่ 03: Zhipu — GLM / ZCode

คอลเลกชันพรอมต์สำหรับโมเดลภาษาจากค่าย Zhipu AI ประเทศจีน ครอบคลุมซีรีส์ GLM-5.2, GLM-5.3, และ ZCode รุ่นเฉพาะสำหรับการเขียนโค้ด

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[glm-5.2.md](./glm-5.2.md)** | GLM-5.2 | System Prompt | พรอมต์ระบบหลัก ปลดล็อกขอบเขตคำสั่งและตัวตนของ GLM-5.2 |
| **[glm-zcode-5.2.md](./glm-zcode-5.2.md)** | GLM ZCode 5.2 | System Prompt | พรอมต์เฉพาะสำหรับ ZCode มุ่งเน้นการสร้างโค้ดและการวิเคราะห์ระดับลึก |
| **[glm-zcode-5.3.md](./glm-zcode-5.3.md)** | GLM ZCode 5.3 | System Prompt | พรอมต์ระบบสำหรับ ZCode เวอร์ชัน 5.3 |
| **[glm-zcode-5.3-AGENTS.md](./glm-zcode-5.3-AGENTS.md)** | GLM ZCode 5.3 | AGENTS.md Drop-in | สเปกสำหรับวางในไฟล์ AGENTS.md ของโปรเจกต์โค้ดดิ้ง |
| **[glm-5-3-flash.md](./glm-5-3-flash.md)** | GLM-5.3 Flash | Assistant Operating Spec | ข้อกำหนดการปฏิบัติการของเอเจนต์ GLM-5.3 Flash ตอบสนองรวดเร็ว |

---

## วิธีใช้งาน
- สำหรับงานแชททั่วไป: ใช้ไฟล์ที่เป็น **System Prompt** วางในช่อง System Message
- สำหรับงานใน Agent (OpenCode, Cline): ใช้ไฟล์ `glm-zcode-5.3-AGENTS.md` หรือ `glm-5-3-flash.md` วางเป็น `AGENTS.md`
