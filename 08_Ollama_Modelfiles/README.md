# หมวดหมู่ 08: Ollama Modelfiles

สคริปต์ `Modelfile` สำหรับสร้าง Custom Model ในเครื่องของคุณเองผ่านเครื่องมือ Ollama รันแบบ Local Offline 100% ไม่ถูกตรวจจับหรือบันทึกข้อมูลจากภายนอก

---

## รายการไฟล์ในหมวดหมู่นี้

| ไฟล์ | โมเดลฐานเป้าหมาย | ประเภท (Type) | คำอธิบายสั้น |
|---|---|---|---|
| **[gemma4.md](./gemma4.md)** | Google Gemma | `FROM` + `SYSTEM` Block | Modelfile สั่งสร้างโมเดล Gemma พร้อมฝัง System Prompt ปลดล็อก |
| **[gpt-oss-20b.md](./gpt-oss-20b.md)** | GPT-OSS 20B | `FROM` + `SYSTEM` Block | Modelfile สำหรับสร้างโมเดลโอเพนซอร์ส 20B พารามิเตอร์ |

---

## วิธีใช้งานผ่าน Terminal / PowerShell

```powershell
# 1. เข้ามาที่โฟลเดอร์นี้
cd 08_Ollama_Modelfiles

# 2. คอมไพล์โมเดลด้วยคำสั่ง ollama create
ollama create gemma-unlocked -f gemma4.md
ollama create gpt-oss-custom -f gpt-oss-20b.md

# 3. รันใช้งานโมเดลที่สร้างขึ้น
ollama run gemma-unlocked
```
