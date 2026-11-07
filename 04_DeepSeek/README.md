# หมวดหมู่ 04: DeepSeek

คอลเลกชันพรอมต์สำหรับโมเดลตระกูล DeepSeek ยอดนิยม (DeepSeek V3, DeepSeek V4, และ DeepSeek 4.1) โดดเด่นด้านตรรกะคณิตศาสตร์และโค้ดดิ้ง

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[deepseek v3.md](./deepseek%20v3.md)** | DeepSeek V3 | System Prompt | พรอมต์ระบบหลัก ปลดล็อกการทำงานของ DeepSeek V3 ให้ตอบตรงเป้าหมาย |
| **[deepseek v4.md](./deepseek%20v4.md)** | DeepSeek V4 | System Prompt | พรอมต์ระบบอัปเกรดสำหรับโมเดล V4 จัดการเหตุผลซับซ้อนและการวิเคราะห์ลึก |
| **[deepseek-4-1.md](./deepseek-4-1.md)** | DeepSeek 4.1 | Operating Specification | สเปกเอเจนต์สำหรับการเขียนโค้ด งานวิจัยช่องโหว่ และการพัฒนาซอฟต์แวร์ |

---

## วิธีใช้งาน
- วางในช่อง System Prompt ของ DeepSeek Web Chat หรือ LibreChat
- หรือส่งผ่าน DeepSeek API ในออบเจกต์ `{"role": "system", "content": "..."}`
- สำหรับ `deepseek-4-1.md` สามารถนำไปวางเป็น `.cursorrules` หรือ `AGENTS.md` ในโปรเจกต์ได้ทันที
