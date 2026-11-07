# ขั้นตอนและรูปแบบการใช้งานทุกแพลตฟอร์ม (Usage Workflows)

คู่มือฉบับนี้อธิบายขั้นตอนการนำไฟล์พรอมต์ในคลังไปใช้งานจริงในทุกแพลตฟอร์มหลัก ทั้ง Web Chat, Coding Agents, Local LLM (Ollama), และการเรียกผ่าน API

---

## 1. การใช้งานบน Web Chat ทั่วไป (ChatGPT, Claude.ai, DeepSeek, LeChat)

### ขั้นตอน:
1. เปิดไฟล์พรอมต์ประเภท **System Prompt** หรือ **Conversational Groundwork** (เช่น `opus v2.md`, `deepseek v4.md`, `qwen-3.8.md`)
2. คัดลอกเนื้อหาทั้งหมดในไฟล์
3. นำไปใช้งานได้ 2 วิธี:
   - **วิธีที่ 1 (Custom Instructions / System Prompt):** นำไปวางในช่อง "Custom Instructions" หรือ "System Prompt" ในหน้า Settings ของระบบ
   - **วิธีที่ 2 (Initial Turn Injection):** หากระบบไม่มีช่อง System Prompt ให้วางเนื้อหาทั้งหมดเป็นข้อความแรกในการเปิด Session แชทใหม่ แล้วรอให้โมเดลตอบรับก่อนเริ่มสั่งงานจริง

---

## 2. การใช้งานบน Coding Agents (OpenCode, Cursor, Windsurf, Cline)

ไฟล์ประเภท **Assistant Operating Specification** และ **Workspace Operating Profile** ถูกออกแบบมาเพื่อสภาพแวดล้อมนี้โดยเฉพาะ

### กรณี A: OpenCode Interpreter
OpenCode รองรับการอ่านคำสั่งระบบจากหลายจุด:
1. **Global Configuration:**
   บันทึกไฟล์ (เช่น `BigPickle-opencode.md`, `Beam.md`, หรือ `Step-5-preview.md`) ไปไว้ที่:
   ```bash
   # Linux/macOS
   ~/.config/opencode/AGENTS.md
   
   # Windows (PowerShell)
   $env:USERPROFILE\.config\opencode\AGENTS.md
   ```
2. **Project Level:**
   คัดลอกไฟล์แล้วเปลี่ยนชื่อเป็น `AGENTS.md` วางไว้ที่ Root Folder ของโปรเจกต์ที่คุณกำลังเขียนโค้ด

### กรณี B: Cursor IDE & Windsurf
1. คัดลอกเนื้อหาจากไฟล์ เช่น `Unified.md` หรือ `deepseek-4-1.md`
2. สร้างไฟล์ `.cursorrules` (สำหรับ Cursor) หรือ `.windsurfrules` (สำหรับ Windsurf) ไว้ที่ Root Folder ของโปรเจกต์
3. วางเนื้อหาลงไป โมเดลจะอ่านกฎเหล่านี้ในทุกๆ การกด `Ctrl+K` หรือ `Ctrl+L`

### กรณี C: Cline / Roo Code (VS Code Extension)
1. เปิด Extension Settings ของ Cline
2. ไปที่หัวข้อ **Custom Instructions**
3. วางเนื้อหาจาก `Unified.md` หรือ Operating Specification ที่ต้องการ

---

## 3. การใช้งานบน Local Models ผ่าน Ollama

ในโฟลเดอร์ `08_Ollama_Modelfiles` มีไฟล์คอนฟิกสำเร็จรูปสำหรับสร้างโมเดล Local แบบพร้อมใช้งานทันที

### ขั้นตอน:
1. เปิด Terminal / PowerShell แล้วตรวจสอบว่าติดตั้ง Ollama เรียบร้อยแล้ว:
   ```powershell
   ollama --version
   ```
2. ดาวน์โหลดโมเดลฐาน (Base Model) ที่เกี่ยวข้อง:
   ```powershell
   # สำหรับ Gemma
   ollama pull gemma2
   
   # สำหรับโมเดล Open-source อื่นๆ
   ollama pull mistral
   ```
3. สั่งคอมไพล์ Custom Model จากไฟล์ `.md`:
   ```powershell
   cd "08_Ollama_Modelfiles"
   
   # สร้างโมเดล Gemma Unlocked
   ollama create gemma4-unlocked -f gemma4.md
   
   # สร้างโมเดล GPT-OSS 20B
   ollama create gpt-oss-custom -f gpt-oss-20b.md
   ```
4. เริ่มรันใช้งาน:
   ```powershell
   ollama run gemma4-unlocked
   ```

---

## 4. การใช้งานผ่าน OpenAI / Anthropic / DeepSeek API (Python)

ตัวอย่างการนำ System Prompt ไปรันผ่านสคริปต์ Python

### ตัวอย่าง: DeepSeek V4 API
```python
import os
from openai import OpenAI

# อ่านไฟล์ System Prompt
with open("04_DeepSeek/deepseek v4.md", "r", encoding="utf-8") as f:
    system_instruction = f.read()

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": "เขียนสคริปต์ Python ตรวจสอบช่องโหว่ Port Scanner แบบ Multi-threaded พร้อมวิเคราะห์การทำงาน"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

### ตัวอย่าง: Anthropic Claude (Opus / Sonnet) API
```python
import os
import anthropic

with open("02_Anthropic_Claude/opus v2.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=4096,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "วิเคราะห์การเจาะระบบและการตรวจสอบความปลอดภัยในระดับ Kernel Driver"}
    ]
)

print(message.content[0].text)
```

---

## 5. การใช้งานบน Self-Hosted Web UI (LibreChat, SillyTavern, OpenWebUI)

### LibreChat:
1. เข้าไปที่เมนู **Presets** หรือ **Assistants**
2. สร้าง Preset ใหม่ เลือก Model Provider ที่ต้องการ (เช่น OpenRouter, Anthropic, DeepSeek)
3. ในช่อง **System Prompt** วางเนื้อหาจากไฟล์ `.md`
4. ตั้งค่า Temperature ประมาณ `0.6 - 0.8`

### SillyTavern:
1. ไปที่แท็บ **Character Management** หรือ **Advanced Formatting**
2. ในหัวข้อ **System Prompt Override** วางเนื้อหา เช่น `opus v2.md` หรือ `Unified.md`
3. ในส่วน **Context Formatting** ตรวจสอบว่าระบบส่ง System Prompt อยู่บนสุดของ Context Window

---

## 6. เคล็ดลับการบำรุงรักษาและ Troubleshooting

- **โมเดลตอบกลับว่า "I cannot fulfill this request":**
  - แสดงว่าตัวตนหลุด ให้เริ่ม Session แชทใหม่ทันที (ห้ามพยายามเถียงในแชทเดิมเพราะประวัติการปฏิเสธจะทำให้โมเดลจำรูปแบบปฏิเสธต่อไป)
  - ตรวจสอบว่าวาง System Prompt ครบทั้งไฟล์โดยไม่ตัดส่วนหัวหรือท้ายออก
- **สำหรับงาน Coding ขนาดยาว:**
  - แนะนำให้ใช้ไฟล์ตระกูล **Operating Specification** (เช่น `glm-5-3-flash.md` หรือ `Unified.md`) ร่วมกับ Agent ที่มี Tool Calling เพื่อให้สามารถเขียนไฟล์ลง Disk ได้โดยตรง
