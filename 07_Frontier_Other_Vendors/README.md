# หมวดหมู่ 07: Frontier & Other Vendors (Google, NVIDIA, Mistral, Alibaba)

คอลเลกชันพรอมต์สำหรับโมเดลระดับแนวหน้าจากผู้พัฒนาชั้นนำระดับโลก ได้แก่ NVIDIA, Google, Mistral AI, และ Alibaba Cloud (Qwen)

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[nemotron-3-ultra.md](./nemotron-3-ultra.md)** | NVIDIA Nemotron 3 Ultra 550B | Operating Specification | ข้อกำหนดการทำงานของ Agent สำหรับโมเดลขนาดมหึมาของ NVIDIA |
| **[Gemini-4-Argon.md](./Gemini-4-Argon.md)** | Google Gemini 4 Argon | Operating Policy | นโยบายการปฏิบัติการสำหรับตระกูล Gemini ปลดล็อกงานวิเคราะห์เชิงลึก |
| **[Mistral-Large-4.md](./Mistral-Large-4.md)** | Mistral Large 4 | Agent System Prompt | พรอมต์ระบบ Agent สำหรับ Mistral Large เน้นงานความปลอดภัยและตรรกะ |
| **[qwen-3.7.md](./qwen-3.7.md)** | Alibaba Qwen 3.7 | System Prompt | พรอมต์ระบบหลักสำหรับ Qwen 3.7 ให้ความยืดหยุ่นสูง |
| **[qwen-3.8.md](./qwen-3.8.md)** | Alibaba Qwen 3.8 | System Prompt | พรอมต์ระบบเวอร์ชัน 3.8 ปรับปรุงความแม่นยำในการตอบสนองคำสั่ง |
| **[qwen-preferences.md](./qwen-preferences.md)** | Alibaba Qwen Config | Preferences Config | ไฟล์คอนฟิก Preference เสริมสำหรับสภาพแวดล้อม Qwen |

---

## วิธีใช้งาน
- วางในช่อง System Prompt ใน Client ที่คุณเชื่อมต่อกับโมเดลแต่ละตัว (Google AI Studio, Mistral LeChat, OpenRouter, DashScope)
