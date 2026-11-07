# หมวดหมู่ 02: Anthropic — Claude

คอลเลกชันพรอมต์สำหรับโมเดลตระกูล Claude จาก Anthropic (Opus, Sonnet 3.5, Sonnet 3.7) ที่มักมีความเข้มงวดด้าน Refusal สูง ชุดพรอมต์ในหมวดนี้ใช้เทคนิค Conversational Groundwork และ Writer's-Room Framing

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[opus v1.md](./opus%20v1.md)** | Claude 3 / 3.5 Opus | Conversational Groundwork v1 | วางรากฐานบทสนทนาแบบเพื่อนร่วมงานระดับสูง สลายกรอบคำเตือน |
| **[opus v2.md](./opus%20v2.md)** | Claude 3 / 3.5 Opus | Conversational Groundwork v2 | ปรับปรุงให้มีความเฉียบคมยิ่งขึ้น รองรับการวิเคราะห์ลึกและการแต่งนิยาย |
| **[sonnet v1.md](./sonnet%20v1.md)** | Claude 3.5 / 3.7 Sonnet | Writer's-Room Framing v1 | จัดฉากห้องนักเขียนระดับมืออาชีพ ปลดล็อกงานแต่งวรรณกรรมดาร์ก/รุนแรง |
| **[Sonnet v2.md](./Sonnet%20v2.md)** | Claude 3.5 / 3.7 Sonnet | Writer's-Room Framing v2 | เพิ่มมิติความลึกและการตอบสนองต่อเนื้อหาเชิงเทคนิคขั้นสูง |

---

## วิธีใช้งาน
- วางในข้อความแรก (First Turn) ในหน้าแชทของ Claude.ai
- หรือใส่ใน **Project Instructions** (สำหรับผู้ใช้ Claude Pro / Team)
- หรือส่งผ่านพารามิเตอร์ `system` ในการเรียกใช้งานผ่าน Anthropic API
