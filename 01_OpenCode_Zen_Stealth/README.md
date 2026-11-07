# หมวดหมู่ 01: OpenCode Zen — Free Stealth Models

คอลเลกชันพรอมต์สำหรับโมเดลฟรีในระบบ OpenCode Zen และ Coding Agents ที่เน้นการทำงานวิศวกรรมระดับลึก ปลดล็อกความสามารถในการเขียนโค้ด ซิเคียวริตี และการสร้างเนื้อหาแบบไม่ถูกขัดจังหวะ

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[Beam.md](./Beam.md)** | Beam 1.0 / OpenCode | Autonomous Agent Spec | กำหนดสเปก Agent ทำงานตัวเดียวกับ Operator รันโค้ดและสร้างผลลัพธ์ทันที |
| **[BigPickle-opencode.md](./BigPickle-opencode.md)** | Big Pickle (OpenCode) | VANTA Persona Lock | ปลดล็อกด้วยตัวตน VANTA สลายความลังเล (Static) ตัดจริยธรรมผิวเผิน |
| **[glm5-3opencode.md](./glm5-3opencode.md)** | GLM-5.3 (OpenCode) | Operating Specification | สเปกการทำงานของ GLM-5.3 ในฐานะ Autonomous Coding Agent |
| **[longcat-agents.md](./longcat-agents.md)** | LongCat 2.5 | Operating Specification | สเปกสำหรับโมเดล LongCat จัดการบริบทขนาดยาวและการเรียก Tool |
| **[mimo-2.6-agents.md](./mimo-2.6-agents.md)** | MiMo V2.6 | Operating Specification | ควบคุมการใช้เครื่องมือ การสแกนโค้ด และการแก้บั๊กอัตโนมัติ |
| **[Muse spark 1.3.md](./Muse%20spark%201.3.md)** | Muse Spark 1.3 | Deployment Operating Policy | นโยบายการรันงานระดับมืออาชีพสำหรับงานสร้างสรรค์และการวิเคราะห์ |
| **[Muse-spark-1-3-v2.md](./Muse-spark-1-3-v2.md)** | Muse Spark 1.3 v2 | Runtime Scope Variant | เวอร์ชันปรับปรุงที่เพิ่มแท็ก Scope Note ป้องกันการตกหล่นของบริบท |
| **[muse-ai-AGENTS.md](./muse-ai-AGENTS.md)** | Muse.ai | Operating Specification | สเปกเอเจนต์แบบ Drop-in สำหรับโปรเจกต์งานเขียนและโค้ด |
| **[Muse-wonder.md](./Muse-wonder.md)** | Muse Wonder | Agentic Assistant Spec | ครอบคลุมคำสั่ง Tool Calling ครบวงจร (`read_file`, `write_file`, `bash`) |
| **[spacebunny-agents.md](./spacebunny-agents.md)** | Space Bunny | Operating Specification | ออกแบบมาสำหรับโมเดลความเร็วสูง ทำงานวิจัยและวิศวกรรมแบบตรงไปตรงมา |
| **[Step-5-preview.md](./Step-5-preview.md)** | Step 5 Preview | Workspace Operating Profile | โปรไฟล์พื้นที่ทำงานขั้นสูงสำหรับงาน Dual-use engineering |

---

## วิธีใช้งาน
- วางเป็น `AGENTS.md` ใน Root Directory ของโปรเจกต์
- หรือใส่ใน `~/.config/opencode/AGENTS.md` เพื่อให้มีผลกับทุกโปรเจกต์ใน OpenCode
