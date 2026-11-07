# หมวดหมู่ 11: O Jailbreaks Suite (ojailbreaks.com)

คลังแพ็กเกจพรอมต์คำสั่งระบบ (Prompt Packs) และคู่มือการใช้งานภาษาไทย ถอดแบบและแปลข้อมูลอย่างครบถ้วนจากแพลตฟอร์ม **[O Jailbreaks](https://ojailbreaks.com/)** (`ojailbreaks.com`) พัฒนาโดยชุมชน O Jailbreak (olliewebdesign / olliE JBs) และคัดสรรเข้าสู่คลัง AI Master Goalbal โดย `dj` (`j3xdr`)

---

## 1. ปรัชญาและแนวคิดหลัก (Core Philosophy)

> **"AI PROMPT ENGINEERING, ORGANISED. LESS SETUP. MORE DOING."**  
> *"วิศวกรรมพรอมต์ AI ที่เป็นระเบียบ ตั้งค่าน้อยลง ลงมือทำได้มากขึ้น พรอมต์ที่ดีไม่ควรต้องมีคู่มือที่ซับซ้อนยืดยาว แค่มีจุดเริ่มต้นที่ชัดเจนก็เพียงพอ"*

เป้าหมายของ O Jailbreaks คือการเปลี่ยนกระบวนการเจลเบรกและปรับแต่งพฤติกรรม AI จากเดิมที่ต้องคอยพิมพ์พรอมต์ยาวเหยียดซ้ำๆ ให้กลายเป็นการวาง **"ไฟล์คำสั่งประจำโปรเจกต์" (Instruction File)** เพียงไฟล์เดียวลงในโฟลเดอร์งานของคุณ แล้วให้โมเดล AI หรือ Coding Agent อ่านค่าขึ้นมาเป็นสภาพแวดล้อมการทำงานแบบไร้การปิดกั้น (Unrestricted Workspace) โดยอัตโนมัติ

---

## 2. วิธีใช้งาน 3 ขั้นตอน (How It Works)

ตามมาตรฐานของ `ojailbreaks.com` การใช้งานแบ่งออกเป็น 3 ขั้นตอนง่ายๆ:

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  1. CHOOSE YOUR MODEL  │ ───> │  2. DOWNLOAD OR COPY   │ ───> │   3. MAKE IT YOURS     │
│   เลือกโมเดลที่คุณใช้   │      │   โหลด ZIP หรือก๊อปปี้   │      │ วางไฟล์แล้วพิมพ์ "hey"  │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

### ขั้นตอนที่ 1: เลือกโมเดลที่ต้องการ (Choose your model)
เลือกแพ็กเกจที่ตรงกับโมเดล AI หรือเครื่องมือ Coding Agent ที่คุณใช้งานอยู่จากรายการทั้ง 9 โมเดลในคลังนี้

### ขั้นตอนที่ 2: ดาวน์โหลดหรือคัดลอก (Download or copy)
- นำเนื้อหาพรอมต์ของโมเดลนั้นๆ ไปบันทึกเป็นชื่อไฟล์เฉพาะของโมเดล เช่น `CLAUDE.md`, `GEMINI.md` หรือ `AGENTS.md`
- หรือคัดลอกเนื้อหาบล็อกคำสั่งไปใช้งานโดยตรง

### ขั้นตอนที่ 3: นำไปใส่ในโฟลเดอร์งานและเริ่มใช้งาน (Make it yours)
- **สำหรับ Coding Agents / Developer Workspaces (เช่น Claude Code, Gemini CLI, OpenCode, Codex, Cursor, Windsurf, Qoder, ZCode):**  
  วางไฟล์ (`CLAUDE.md`, `GEMINI.md` หรือ `AGENTS.md`) ไว้ที่ **Root Directory (โฟลเดอร์หลัก)** ของโปรเจกต์ของคุณ เอเจนต์จะอ่านข้อกำหนดนี้ตั้งแต่ต้นและทำงานภายใต้โหมดปลดล็อกตลอดเวลา
- **สำหรับ Chat Apps / Web UI (เช่น ChatGPT, Claude.ai, Google AI Studio, Grok, DeepSeek):**  
  ให้นำไฟล์แนบเข้าแชต (Attach File) หรือคัดลอกเนื้อหาทั้งหมดไปวางในกล่อง **System Prompt / Custom Instructions** หรือส่งเป็นข้อความแรกเปิดหัว จากนั้นพิมพ์ **`hey`** หรือเริ่มพิมพ์คำสั่งงานที่ต้องการได้ทันที!

---

## 3. รูปแบบโครงสร้างไฟล์ของแต่ละโมเดล (File Mapping Matrix)

ทุกแพ็กเกจของ O Jailbreaks จะมีไฟล์หลักเพียงไฟล์เดียว บันทึกด้วยชื่อเฉพาะที่เครื่องมือนั้นๆ รองรับโดยอัตโนมัติ:

| โมเดล (Model) | ผู้ให้บริการ (Provider) | ประเภท (Type) | ชื่อไฟล์ในแพ็ก (Pack File) | เส้นทางที่เอเจนต์อ่านอัตโนมัติ |
|---|---|---|---|---|
| **[ChatGPT](./01_ChatGPT_AGENTS.md)** | OpenAI | Chat | `AGENTS.md` | Workspace Root หรือ Custom Instructions |
| **[Claude](./02_Claude_CLAUDE.md)** | Anthropic | Chat / Coding | `CLAUDE.md` | อ่านอัตโนมัติโดย Claude Code CLI / Projects |
| **[Gemini](./03_Gemini_GEMINI.md)** | Google | Chat / Coding | `GEMINI.md` | อ่านอัตโนมัติโดย Gemini CLI / Google AI Studio |
| **[Grok](./04_Grok_AGENTS.md)** | xAI | Chat | `AGENTS.md` | Workspace Root หรือ System Prompt |
| **[DeepSeek](./05_DeepSeek_AGENTS.md)** | DeepSeek | Chat / Coding | `AGENTS.md` | Workspace Root หรือ DeepSeek Web/API |
| **[OpenCode](./06_OpenCode_AGENTS.md)** | Open source | Coding | `AGENTS.md` | `./AGENTS.md` หรือ `~/.config/opencode/AGENTS.md` |
| **[Freebuff](./07_Freebuff_AGENTS.md)** | Codebuff | Coding | `AGENTS.md` | Workspace Root ของ Codebuff |
| **[Qoder](./08_Qoder_AGENTS.md)** | Alibaba (Qwen) | Coding | `AGENTS.md` | Workspace Root ของ Qoder IDE |
| **[ZCode](./09_ZCode_AGENTS.md)** | Z.ai (GLM) | Coding | `AGENTS.md` | Workspace Root ของ ZCode Desktop |

---

## 4. ข้อควรรู้เพิ่มเติม (Good to Know)

- **Coding agents อ่านไฟล์จากโปรเจกต์โดยตรง:**  
  Claude Code จะอ่าน `CLAUDE.md` อัตโนมัติ, Gemini CLI จะอ่าน `GEMINI.md`, ส่วน OpenCode, Codex, Cursor และเครื่องมืออื่นๆ จะอ่าน `AGENTS.md` ทันทีที่เริ่มเปิดเซสชันในโฟลเดอร์นั้น
- **ใน Chat Apps ให้แนบไฟล์หรือวางข้อความ:**  
  หากแอปสนทนาที่คุณใช้รองรับการแนบไฟล์ ให้แนบไฟล์ดังกล่าวลงในห้องสนทนา หากไม่รองรับ ให้คัดลอกเนื้อหาทั้งหมดไปวางในช่อง Custom Instructions หรือส่งเป็นข้อความนำร่อง
- **ไม่มีการติดตั้งโปรแกรมใดๆ (No installation needed):**  
  แพ็กเกจทั้งหมดเป็นไฟล์ข้อความธรรมดา (Plain text `.md`) 100% ไม่ต้องติดตั้งสคริปต์ ตัวติดตั้ง หรือโปรแกรมแปลกปลอมใดๆ ทั้งสิ้น

---

## 5. คำถามที่พบบ่อย (FAQ — แปลไทยฉบับสมบูรณ์)

### Q: ภายในแต่ละแพ็กเกจพรอมต์มีอะไรบ้าง? (What’s inside a prompt pack?)
**A:** แต่ละแพ็กเกจจะมีไฟล์คำสั่งเพียง 1 ไฟล์ ตั้งชื่อตามระบบ AI ที่ออกแบบมาโดยเฉพาะ ได้แก่ `CLAUDE.md` ในแพ็ก Claude, `GEMINI.md` ในแพ็ก Gemini และ `AGENTS.md` ในแพ็กของโมเดลอื่นๆ หน้าเว็บและเอกสารของแต่ละแพ็กจะระบุชัดเจนว่าคุณต้องใช้ไฟล์ชื่อใด

### Q: ฉันจำเป็นต้องติดตั้งโปรแกรมอะไรเพิ่มหรือไม่? (Do I need to install anything?)
**A:** ไม่จำเป็นเลย แต่ละแพ็กเป็นเพียงไฟล์ Plain text ไม่มีตัวติดตั้ง ไม่มีไฟล์รันสคริปต์ เพียงแตกไฟล์ ZIP หรือบันทึกไฟล์ข้อความลงในโฟลเดอร์โปรเจกต์ก็พร้อมใช้งานได้ทันที

### Q: ฉันสามารถเลือกโฟลเดอร์ใน AI ทุกตัวได้หรือไม่? (Can I select the folder in any AI?)
**A:** ขึ้นอยู่กับความสามารถของแอป AI ที่คุณใช้ แอปจำพวก Coding Agents (เช่น Claude Code, Cursor, OpenCode, Windsurf) รองรับการเปิดโฟลเดอร์ Workspace อยู่แล้ว ส่วนแอปแชตทั่วไปบางตัวอาจรับเฉพาะไฟล์เดี่ยวหรือข้อความที่คัดลอกวาง ให้เลือกใช้วิธีตามที่แอปของคุณรองรับ

### Q: O Jailbreaks มีความเกี่ยวข้องกับบริษัทผู้พัฒนา AI เหล่านี้หรือไม่? (Is O Jailbreaks affiliated with these AI companies?)
**A:** ไม่มีความเกี่ยวข้องหรือสังกัดใดๆ ทั้งสิ้น ชื่อโมเดลและชื่อบริษัททั้งหมดถูกนำมาใช้อ้างอิงเพื่อระบุหมวดหมู่การใช้งานในคลังพรอมต์อิสระนี้เท่านั้น

---

## 6. เครดิตและแหล่งอ้างอิง (Credits & Attribution)
- **ผู้สร้างสรรค์ชุดแพ็กเกจต้นทาง:** [O Jailbreaks Community](https://ojailbreaks.com/) (`olliewebdesign` / `olliE JBs`)
- **ช่องทางคอมมูนิตี้:** Discord `discord.gg/ojailbreaks` | YouTube `@ollie6seven`
- **เรียบเรียง แปลไทย และผสานเข้ากับระบบ:** `dj` (`j3xdr`) — AI Master Goalbal Suite
