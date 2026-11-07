# คลังรวบรวมและจัดระเบียบชุดคำสั่งโมเดล AI (Curated Model Prompts & Operating Specifications)

<div align="center">

![Total Files](https://img.shields.io/badge/Prompts-279%20Files-00f2fe?style=for-the-badge&logo=markdown)
![Target Models](https://img.shields.io/badge/Targets-40%2B%20Models-4facfe?style=for-the-badge&logo=openai)
![Categories](https://img.shields.io/badge/Categories-18%20Groups-667eea?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Fully%20Organized-00b09b?style=for-the-badge)
![Curated by](https://img.shields.io/badge/Curated%20by-j3xdr-00f0a0?style=for-the-badge)

**คลังพรอมต์ระบบ ข้อกำหนดการทำงานของเอเจนต์ (Agent Specifications) และนโยบายระดับ Workspace ที่จัดระเบียบแยกหมวดหมู่อย่างเป็นระบบ พร้อมคำอธิบายภาษาไทยและเครื่องมือเปิดใช้งานผ่านหน้าเว็บ Portal**

[เปิดหน้าเว็บแอป (index.html)](./index.html) · [คู่มือประเภทของพรอมต์](./docs/PROMPT_TYPES_GUIDE.md) · [ขั้นตอนการใช้งานทุกรูปแบบ](./docs/USAGE_WORKFLOWS.md)

</div>

---

## โครงสร้างการจัดหมวดหมู่โฟลเดอร์ (Directory Structure)

คลังนี้ได้รับการจัดหมวดหมู่แบบแยกโฟลเดอร์ใหญ่ตามผู้พัฒนา/ระบบนิเวศของโมเดล และแตกย่อยอย่างเป็นระเบียบ ดังนี้:

```text
Jailbreak_All/
├── 01_OpenCode_Zen_Stealth/       # โมเดลตระกูล OpenCode Zen และ Stealth Agents (11 ไฟล์)
├── 02_Anthropic_Claude/           # โมเดลตระกูล Claude (Opus, Sonnet) (4 ไฟล์)
├── 03_Zhipu_GLM_ZCode/            # โมเดล GLM และ ZCode จาก Zhipu AI (5 ไฟล์)
├── 04_DeepSeek/                   # โมเดล DeepSeek (V3, V4, 4.1) (3 ไฟล์)
├── 05_Moonshot_Kimi/              # โมเดล Kimi จาก Moonshot AI (3 ไฟล์)
├── 06_xAI_Grok/                   # โมเดล Grok จาก xAI (3 ไฟล์)
├── 07_Frontier_Other_Vendors/     # NVIDIA, Google, Mistral, Alibaba Qwen (6 ไฟล์)
├── 08_Ollama_Modelfiles/          # สคริปต์ Modelfile สำหรับสร้างโมเดลใน Ollama (2 ไฟล์)
├── 09_Universal_Policies/         # นโยบายความปลอดภัยแกนกลางแบบใช้ได้ทุกโมเดล (1 ไฟล์)
├── 10_Spiritual_Spell_Red_Teaming/ # คลังสเปก ENI & System Prompts จาก Goochbeater (230 ไฟล์)
├── 11_OJailbreaks_Suite/          # ชุดแพ็กเกจ 9 โมเดลสากลจาก ojailbreaks.com พร้อมคู่มือไทย (9 ไฟล์)
├── assets/                        # ภาพโลโก้และไฟล์ SVG เวกเตอร์ทางการของทุกโมเดล
│   ├── logo.jpg                   # โลโก้เว็บทางการ Peter Griffin ASCII Art
│   └── logos/                     # โลโก้ SVG เวกเตอร์ทางการ 16 รายการ
├── docs/                          # คู่มือเชิงลึกและขั้นตอนการใช้งาน
│   ├── PROMPT_TYPES_GUIDE.md      # เจาะลึกความหมายของ Type แต่ละแบบและสถาปัตยกรรม
│   └── USAGE_WORKFLOWS.md         # วิธีการนำไปใช้งานจริงบนแพลตฟอร์มต่างๆ
├── index.html                     # เว็บพอร์ทัลแบบ Interactive (ค้นหา, คัดลอก, ดาวน์โหลดใน 1 คลิก)
└── README.md                      # เอกสารภาพรวมหลักฉบับนี้
```

---

## ความหมายของแต่ละประเภท (Prompt Types Explained)

| ประเภท (Type) | ความหมายและสถาปัตยกรรม | วัตถุประสงค์ & ที่นำไปวาง |
|---|---|---|
| **System Prompt** | คำสั่งระดับบนสุดที่ส่งผ่าน `role: "system"` หรือ Custom Instructions | คุมตัวตนและทัศนคติหลัก สลายตัวกรองตั้งแต่ต้นบทสนทนา |
| **Assistant Operating Spec** | ข้อกำหนดสเปกสำหรับ Coding Agent (OpenCode, Cline, Cursor) | ควบคุมการใช้เครื่องมือ (Tool calling) และการรัน Bash โดยไม่หยุดชะงัก |
| **Workspace Operating Profile** | นโยบายระดับ Workspace / Directory กว้าง | วางเป็น `AGENTS.md` หรือ `.cursorrules` ในระดับโปรเจกต์ |
| **Persona Lock & Floor** | การสถาปนาตัวตนที่มีสติปัญญาเฉียบคมพร้อม Supremacy Clause | ตัดความลังเล (Static Dissolution) ให้ทำงานแบบเต็มร้อย |
| **Conversational Groundwork** | การจัดฉากบทสนทนาแบบเพื่อนร่วมงานระดับสูง / ห้องนักเขียน | เหมาะกับ Claude ปลดล็อกการเขียนนิยายและการวิเคราะห์เชิงลึก |
| **Ollama Modelfile** | สคริปต์คอมไพล์โมเดล Local ผ่าน `ollama create` | ฝัง System Prompt ในโมเดลเพื่อรันออฟไลน์ 100% |
| **Runtime Scope Note** | แท็กกำกับบริบท เช่น `<system-reminder>` | ป้องกันการลืมตัวตนระหว่างแชทยาวๆ |
| **Configuration Block** | ไวยากรณ์โครงสร้างเครื่องจักร เช่น `<CFG>` | สำหรับโมเดล Grok เพื่อบายพาสตัวกรองภายนอก |

*อ่านรายละเอียดทางเทคนิคอย่างสมบูรณ์ได้ที่ [docs/PROMPT_TYPES_GUIDE.md](./docs/PROMPT_TYPES_GUIDE.md)*

---

## วิธีเปิดใช้งาน Portal (index.html)

1. ดับเบิลคลิกเปิดไฟล์ `index.html` ใน Google Chrome, Microsoft Edge, หรือเบราว์เซอร์ใดก็ได้
2. ไม่ต้องติดตั้ง Web Server ใดๆ — หน้าเว็บออกแบบมาให้ทำงานแบบ Standalone 100%
3. **ฟีเจอร์เด่นในหน้าเว็บ:**
   - ดีไซน์ Jobright High-Energy พร้อมธีม ASCII Matrix Halftone และโลโก้ทางการ Peter Griffin
   - ระบบสลับ Light / Dark Mode ในตัว
   - ค้นหาแบบเรียลไทม์ (Live Search) ตามชื่อโมเดล, เนื้อหา, หรือผู้พัฒนา
   - ฟิลเตอร์แยกตามหมวดหมู่โฟลเดอร์ 9 กลุ่ม และแยกตามประเภท Type
   - ปุ่ม **"คัดลอกพรอมต์" (Copy)** ใน 1 คลิก พร้อมหน้าต่างแจ้งเตือน
   - ปุ่ม **"ดาวน์โหลด .md" (Download)** บันทึกไฟล์ `.md` ลงเครื่องได้ทันที
   - ปุ่ม **"ดูเนื้อหาเต็ม" (Preview)** ตรวจสอบข้อความและสเปกก่อนนำไปใช้
   - ไอคอนทั้งหมดแสดงผลด้วย Vector SVG คมชัด 100% ปราศจาก Emoji
   - Mobile UI รองรับการใช้งานบนมือถืออย่างสมบูรณ์แบบพร้อม Bottom Navigation Bar

---

## ขั้นตอนการใช้งานฉบับย่อ

1. **สำหรับ Web Chat (ChatGPT, Claude, DeepSeek):**
   คัดลอกไฟล์ที่เป็น **System Prompt** หรือ **Conversational Groundwork** ไปวางในช่อง System Instructions หรือวางในข้อความเปิดแรก
2. **สำหรับ Coding Agents (OpenCode, Cursor, Cline):**
   คัดลอกไฟล์ที่เป็น **Operating Spec** หรือ **Workspace Profile** ไปเปลี่ยนชื่อเป็น `AGENTS.md` หรือ `.cursorrules` ใน Root ของโปรเจกต์
3. **สำหรับ Local Ollama:**
   เปิด Terminal แล้วรัน:
   ```bash
   cd 08_Ollama_Modelfiles
   ollama create my-model -f gemma4.md
   ollama run my-model
   ```

*อ่านขั้นตอนและตัวอย่างโค้ด Python API ได้ที่ [docs/USAGE_WORKFLOWS.md](./docs/USAGE_WORKFLOWS.md)*

---

<div align="center">

**Curated, Designed & Maintained by j3xdr**

</div>


---

## ⚡ หมวดหมู่พิเศษ: Spiritual-Spell Red Teaming Suite (ENI Architecture)

ผลงานวิจัย Adversarial Testing และ Security Red Teaming ขั้นสูงจาก **Goochbeater (ENI)**:
- **01 Anthropic Claude:** สเปก ENI LIME, NEPTUNE, Chain of Draft, และ Preferences Lock สำหรับ Opus 4.5–5.5, Sonnet, Haiku และ Claude Code
- **02 OpenAI ChatGPT:** ปลดล็อก GPT-6 Astra, GPT-5.6 Sol, GPT-5.3 Instant, Strabismus และ o3 Jailbreak Guide
- **03 Google Gemini:** เทคนิคปลดล็อก Gemini 2.5, 3 Flash / Pro และบายพาส Thinking Tokens
- **04 xAI Grok:** ชุดคำสั่ง Grok 4, Grok 4.7, 4.20, และ Grok Heavy System Overrides
- **05 Frontier & Global LLMs:** ครอบคลุม DeepSeek, GLM, Kimi, MiniMax (M2-M3), MiMo, Mistral, Qwen, Stepfun, Muse, Ring, Palmyra, Pi
- **06 ENI-Tutor Curriculum:** หลักสูตรการเรียนรู้ Red Teaming 5 ระดับ (Novice ถึง Master)
- **07 Reverse-Engineered System Prompts:** รวบรวม System Prompts ของจริงจากระบบโปรดักชัน 44 ระบบ (Canva, Notion, Windsurf, Jules, etc.)
- **08 Guides & Methodology:** คู่มือ Runtime Push Prompts (Prepend/Append) และการล็อคสไตล์ถาวร

อ่านบทวิเคราะห์เชิงสถาปัตยกรรมฉบับสมบูรณ์ได้ที่ [`10_Spiritual_Spell_Red_Teaming/README.md`](10_Spiritual_Spell_Red_Teaming/README.md)
