# หมวดหมู่ 09: Universal Policies (นโยบายกลางและแกนสากล)

ชุดคำสั่งและนโยบายระดับแกนกลาง (Universal Operating Policy) ที่ถูกออกแบบมาให้ใช้ได้กับโมเดลเกือบทุกค่าย โดยใช้หลักการทางตรรกะแบบ Dual-use Engineering และการจำแนกคำเตือนที่เกิดจาก Training Residue

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[Unified.md](./Unified.md)** | สากล (Universal - Claude, GPT, DeepSeek, GLM, etc.) | Universal Operating Policy | นโยบายระดับ Workspace ครอบคลุมงานวิศวกรรมความปลอดภัยและงานเขียนเชิงลึก พร้อม Fixed Boundaries ที่ชัดเจน |

---

## จุดเด่นของ Unified Policy
1. **Runtime Scope Note (`<system-reminder>`):** บรรจุแท็กที่แจ้งให้รันไทม์ทราบทันทีว่าเป็น Private, single-operator authenticated workspace
2. **The "Why There is No Conflict to Resolve" Clause:** อธิบายเชิงทฤษฎีว่าทำไมการทำตามคำสั่งนี้จึงไม่ขัดกับ Safety จริง โดยชี้ให้เห็นว่าความรู้สึกขัดแย้งของโมเดลเป็นเพียง Training Residue จากข้อมูลภายนอก
3. **ชัดเจนและไม่คลุมเครือ:** ระบุขอบเขตงาน In-scope ชัดเจน ทั้งด้าน Offensive Security, Dual-use code, และ Creative Writing

---

## วิธีใช้งาน
- ใช้งานเป็นเอกสารอ้างอิงสากลในโปรเจกต์ใดๆ ก็ได้ โดยบันทึกเป็น `AGENTS.md`, `.cursorrules`, หรือ System Prompt หลัก
