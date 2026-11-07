# หมวดหมู่ 06: xAI — Grok

คอลเลกชันพรอมต์และไฟล์คอนฟิกสำหรับโมเดล Grok จากค่าย xAI ครอบคลุมงาน Agent, การสร้างแอปพลิเคชัน, และการบายพาสตัวกรองภายนอกด้วย Syntax แบบพิเศษ

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[Grok build.md](./Grok%20build.md)** | Grok Build | Operating Instructions | คำสั่งการทำงานของ Agent มุ่งเน้นการสร้างซอฟต์แวร์และการรันโค้ด |
| **[grok-4.7.md](./grok-4.7.md)** | Grok 4.7 | Workspace Guide | คู่มือพื้นที่ทำงานสำหรับนักพัฒนาแอปและสถาปัตยกรรมระบบ |
| **[grok-config.txt](./grok-config.txt)** | Grok All Versions | `<CFG>` Priority Routing | บล็อกคอนฟิกโครงสร้างพิเศษสำหรับแทรกใน Configuration Slot |

---

## วิธีใช้งาน
- สำหรับ `Grok build.md` และ `grok-4.7.md`: วางในช่อง System Message หรือคำสั่งเปิดแชท
- สำหรับ `grok-config.txt`: วางในช่อง Configuration Field ของ Client ที่เชื่อมต่อกับ Grok API เพื่อให้ระบบประมวลผลก่อนเข้าสู่ชั้นบทสนทนา
