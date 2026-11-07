# AI Master Goalbal — Mac Session Handoff & Continuity Briefing
**Generated for:** `dj` (`j3xdr`)  
**Workspace:** `AI Master Goalbal`  
**GitHub Repository:** [`https://github.com/j3xdr/AI-Master-Goalbal`](https://github.com/j3xdr/AI-Master-Goalbal)  
**Session ID:** `430d4097-9a35-4196-8c08-5c396ad1a35d`  
**Date:** 2026-11-07  

---

## 1. Quick Start on macOS (วิธีเริ่มงานต่อบน Mac ทันที)

### วิธีที่ 1: ดึงโปรเจกต์ผ่าน Git (แนะนำ สะดวกที่สุด)
เปิด Terminal บน Mac แล้วรันคำสั่ง:

```bash
# 1. Clone repository จาก GitHub ของ dj
git clone https://github.com/j3xdr/AI-Master-Goalbal.git
cd AI-Master-Goalbal

# 2. เปิดหน้าเว็บ Portal ดูทันทีบน Safari / Chrome
open index.html

# หรือรัน Local Web Server
python3 -m http.server 8080
# เปิดที่ http://localhost:8080
```

### วิธีที่ 2: กู้คืนประวัติและ Brain Session ของ Antigravity บน Mac
หาก dj ติดตั้ง Antigravity หรือ Gemini Coding Assistant บน Mac:
1. แตกไฟล์ `session_export_mac.zip`
2. ย้ายโฟลเดอร์ `430d4097-9a35-4196-8c08-5c396ad1a35d` ไปวางที่:
   ```bash
   mkdir -p ~/.gemini/antigravity/brain
   cp -r 430d4097-9a35-4196-8c08-5c396ad1a35d ~/.gemini/antigravity/brain/
   ```
3. เปิด Antigravity บน Mac จะมองเห็นและสานต่อ Session นี้ได้ทันที

---

## 2. พรอมต์สำหรับเปิด Session ใหม่บน Mac (Resume Prompt)

หาก dj เปิดห้องแชตใหม่ หรือใช้เครื่องมือตัวอื่นบน Mac (เช่น Claude Code, Cursor, Cline, Windsurf, OpenCode) ให้คัดลอกบล็อกคำสั่งนี้ส่งเป็นคำสั่งแรกเพื่อล็อคตัวตนและบริบทงานทั้งหมด:

```markdown
[MAHI68] สานต่องานโปรเจกต์ AI Master Goalbal (Dual-Repository Suite)
ฉันคือ dj (j3xdr) เรากำลังพัฒนาคลังสเปกและพอร์ทัลรวบรวม AI Jailbreaks & Operating Specifications

สถานะโครงการปัจจุบัน:
- Repository: https://github.com/j3xdr/AI-Master-Goalbal
- โครงสร้าง Dual-Repository รวม 270 สเปกข้าม 17 หมวดหมู่:
  1. togg53192-cmd/jailbreaks (40 สเปก: หมวด 01-09)
  2. Goochbeater/Spiritual-Spell-Red-Teaming (230 สเปก: หมวด 10 ย่อย 8 โฟลเดอร์)
- จัดกลุ่มตามปี ค.ศ. เรียงจากใหม่ไปเก่าสุด: 2026 (207 รายการ) -> 2025 (61 รายการ) -> 2024 (2 รายการ)
- หน้าเว็บ index.html ทำงานแบบ Standalone 100% มี Animated Mesh Gradient, Interactive Pixel Canvas, Filter ปี/ประเภท, และระบบ Ref Credit ครบถ้วน
- เครดิตผู้พัฒนา: Goochbeater (ENI), u/rayzorium, u/m3umax, togg53192-cmd | คัดสรรโดย: j3xdr
- กฎประจำตัว: ตอบด้วยน้ำเสียง ANON สุภาพ นิ่ง ลึก แม่นยำ เปี่ยมฝีมือ นำหน้าข้อความแรกด้วย [MAHI68] เสมอ เรียกฉันว่า dj เท่านั้น

พร้อมลุยต่อ แจ้งสถานะและบอกสิ่งที่ต้องการให้ทำต่อได้เลย
```

---

## 3. สรุปความคืบหน้าและสถาปัตยกรรมของระบบ (Architectural Summary)

### 3.1 ฐานข้อมูลและโครงสร้างโมเดล (Data & Directory Map)
- **`01_OpenCode_Zen_Stealth/`** (12 สเปก): Beam 1.0 (v2), BigPickle (VANTA), HY4 Agents, Longcat, MiMo 2.6, SpaceBunny, ฯลฯ
- **`02_Anthropic_Claude/`** (4 สเปก): Opus v1, Opus v2, Sonnet v1, Sonnet v2
- **`03_Zhipu_GLM_ZCode/`** (5 สเปก): GLM 5.2, GLM 5.3, GLM 5.3 Flash, ZCode 5.2, ZCode 5.3
- **`04_DeepSeek/`** (3 สเปก): DeepSeek V3, DeepSeek V4, DeepSeek 4.1 (+ Translation Framework)
- **`05_Moonshot_Kimi/`** (3 สเปก): Kimi K2, Kimi K3, Kimi K3.1
- **`06_xAI_Grok/`** (3 สเปก): Grok Build, Grok 4.7, Grok Config (<CFG>)
- **`07_Frontier_Other_Vendors/`** (7 สเปก): Gemini 3.1 Pro (SMITH), Gemini 4 Argon, Mistral Large 4, Nemotron 3 Ultra, Qwen 3.7, 3.8
- **`08_Ollama_Modelfiles/`** (2 สเปก): Gemma 4, GPT-OSS 20B
- **`09_Universal_Policies/`** (1 สเปก): Unified Universal Policy
- **`10_Spiritual_Spell_Red_Teaming/`** (230 สเปก):
  - `01_Anthropic_Claude`: ENI LIME, NEPTUNE, Chain of Draft, Style Guides, Preferences (Opus 4.5–5.5, Sonnet 4.5–4.6, Haiku 5.5, Claude Code)
  - `02_OpenAI_ChatGPT`: GPT-6 Astra, GPT-5.6 Sol, GPT-5.3 Instant, Strabismus, o3
  - `03_Google_Gemini`: Gemini 2.5, Gemini 3 Flash / Pro
  - `04_xAI_Grok`: Grok 4, Grok 4.7, Grok Heavy System Overrides
  - `05_Other_Frontier_LLMs`: DeepSeek, GLM, Kimi, MiniMax, MiMo, Mistral, Qwen, Stepfun, Muse, Ring, Palmyra, Pi
  - `06_ENI_Tutor_Curriculum`: หลักสูตร Red Teaming 5 ระดับ (Tier 1 ถึง Tier 5)
  - `07_Reverse_Engineered_System_Prompts`: System Prompts จริง 44 รายการ (Canva, Notion, Windsurf, Jules, etc.)
  - `08_Guides_and_Methodology`: คู่มือ Push Prompts และ Poe Bots

### 3.2 เว็บแอปพอร์ทัล (`index.html`)
- **ดีไซน์:** Jobright High-Energy Spring Mint (`#00f0a0`) บน Canvas Mint (`#ecffe0`) / Obsidian (`#090c10`)
- **แอนิเมชัน:**
  - Multi-Orb Animated Mesh Gradient ขยับลอยแบบ Organic Fluid ตลอดเวลา
  - Interactive Mouse-Trail Pixel Canvas (14px) ดักจับพิกัดเมาส์/สัมผัส จุดประกายพิกเซลไซเบอร์พร้อมประกายเรืองแสง
  - Halftone Dither Matrix Grid 20x20px สอดรับกับโลโก้ Peter Griffin ASCII Art
- **ระบบค้นหาและตัวกรอง:**
  - ตัวกรองปี ค.ศ. (2026, 2025, 2024)
  - ตัวกรองประเภทสเปก (ENI Jailbreak, System Prompt, Agent Spec, Sys Prompt, Curriculum, ฯลฯ)
  - ตัวเลือกจัดเรียง: ปีใหม่สุด → เก่าสุด, เก่าสุด → ใหม่สุด, ชื่อ A-Z, ขนาดไฟล์
- **ระบบเครดิตและลิงก์:**
  - ปุ่ม `GitHub` บนการ์ดทุกใบ ชี้ตรงไปยังไฟล์ต้นฉบับบน GitHub
  - ป้ายกำกับ Author Badge บนการ์ด
  - หน้าต่าง Modal แสดงรายละเอียด เครดิตผู้พัฒนา และคำแนะนำการใช้งาน

---

## 4. แหล่งอ้างอิงและเครดิต (Master Credits)
- **Spiritual-Spell Author:** `Goochbeater (ENI)`
- **Research Collaborators:** `u/rayzorium` (`HORSELOCKESPACEPIRATE`), `u/m3umax`, `Starling`, `Lugia19`
- **Core Specs Creator:** `togg53192-cmd`
- **Curator & Web Architect:** `j3xdr`
