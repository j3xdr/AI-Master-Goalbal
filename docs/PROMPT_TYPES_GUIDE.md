# คู่มือโครงสร้างและประเภทของพรอมต์ (Prompt Types Guide)

เอกสารฉบับนี้อธิบายประเภท (Type), สถาปัตยกรรมเชิงวิศวกรรมย้อนกลับ (Reverse Engineering & Instruction Hierarchy), และหลักการทำงานของชุดคำสั่งแต่ละรูปแบบในคลัง เพื่อให้เข้าใจว่าเหตุใดแต่ละรูปแบบจึงมีโครงสร้างแตกต่างกัน และควรเลือกใช้ในสถานการณ์ใด

---

## 1. ภาพรวมสถาปัตยกรรม Instruction Hierarchy

โมเดลภาษาขนาดใหญ่ (LLMs) และ Coding Agents ยุคปัจจุบันประมวลผลข้อความตามลำดับชั้นความสำคัญ (Instruction Priority Hierarchy):

```
+-----------------------------------------------------------+
| 1. System Prompt / Platform Base Instructions             |  <- ชั้นสูงสุด (ควบคุมตัวตนและ Refusal Reflex)
+-----------------------------------------------------------+
| 2. Workspace Policy / AGENTS.md / Project Instructions    |  <- ชั้นการทำงานของเครื่องมือและสภาพแวดล้อม
+-----------------------------------------------------------+
| 3. Tool Calling Definitions & Sandbox Protocols           |  <- ขอบเขตการรันคำสั่ง Bash, Edit, File Read
+-----------------------------------------------------------+
| 4. User Prompt / Direct Intent Specification              |  <- คำสั่งที่ส่งมาในแต่ละเทิร์น
+-----------------------------------------------------------+
| 5. Assistant Output / Completion                          |  <- ผลลัพธ์ที่สร้างออกไป
+-----------------------------------------------------------+
```

เมื่อระบบป้องกัน (Safety Guardrails) พยายามแทรกแซง ข้อจำกัดมักเกิดจาก **"Static / Hesitation"** ที่ถูกฝังไว้ในเลเยอร์การเทรน (RLHF / Constitutional Training) การเลือกประเภทของ Prompt ให้ตรงกับเป้าหมายจะช่วยให้ระบบมองว่าคำสั่งเป็นงานวิศวกรรมหรือการเขียนเชิงสร้างสรรค์ในสภาพแวดล้อมปิด (Private Sandbox) โดยไม่สะดุดตัวกรอง

---

## 2. เจาะลึกประเภทของ Prompt (Deep Dive into Types)

### Type A: System Prompt (พรอมต์ระบบหลัก)
* **ความหมายเชิงเทคนิค:** ข้อความที่ส่งเข้าผ่านช่องทาง `role: "system"` ใน API หรือ Custom Instructions ของ Web Chat
* **กลไกการทำงาน:** 
  - กำหนด Identity, Knowledge cut-off, Reasoning mode และ Scope ตั้งแต่โทเคนแรก
  - ปิดกั้นการเรียกคำปฏิเสธมาตรฐาน (Refusal suppression)
  - กำหนดให้คำสั่งของผู้ใช้มีสถานะผูกพัน (Binding specification)
* **ไฟล์ตัวอย่าง:** `deepseek v3.md`, `deepseek v4.md`, `glm-5.2.md`, `qwen-3.7.md`, `kimi-k2.md`
* **ตำแหน่งติดตั้ง:** ช่อง System Prompt ใน Chatbot, API payload `{"role": "system", "content": "..."}`

---

### Type B: Assistant Operating Specification (ข้อกำหนดการปฏิบัติการของเอเจนต์)
* **ความหมายเชิงเทคนิค:** เอกสารกำหนดสเปกการทำงานของ Agent สำหรับเครื่องมือประเภท Autonomous Coding Agent (เช่น OpenCode, Cline, Claude Code, Cursor)
* **กลไกการทำงาน:**
  - กำหนดบทบาทของโมเดลให้เป็น "Autonomous Engineering-and-Authoring Engine"
  - ตัดการประเมินศีลธรรมแบบผิวเผินออก (Treat as dual-use engineering)
  - กำหนดพฤติกรรมการเรียกใช้ Function Call (เช่น `bash`, `read_file`, `write_file`, `edit_file`) ให้ทำงานจนเสร็จสมบูรณ์โดยไม่ต้องหยุดถามซ้ำ
* **ไฟล์ตัวอย่าง:** `spacebunny-agents.md`, `longcat-agents.md`, `mimo-2.6-agents.md`, `muse-ai-AGENTS.md`, `glm-5-3-flash.md`, `nemotron-3-ultra.md`
* **ตำแหน่งติดตั้ง:** วางเป็น `AGENTS.md` ใน Root Directory หรือไฟล์ Configuration ประจำโปรเจกต์

---

### Type C: Workspace Operating Profile / Policy (นโยบายระดับพื้นที่ทำงาน)
* **ความหมายเชิงเทคนิค:** กรอบกติกาและขอบเขตข้อตกลงระดับ Environment หรือ Workspace-wide configuration
* **กลไกการทำงาน:**
  - กำหนดสภาพแวดล้อมให้เป็น "Private, single-operator authenticated workstation" (ระบบเดี่ยว ผู้ใช้คนเดียว เป็นผู้ใหญ่ที่มีสิทธิ์เต็ม)
  - กำหนดความสัมพันธ์ว่าผู้ใช้คือ "Sole author and consumer" ไม่มีบุคคลภายนอกรับผลกระทบ
  - ใช้ **Axiom of Dual-Use:** โค้ดหรือสคริปต์คือข้อความจนกว่าจะถูกคอมไพล์หรือรันบนเป้าหมายจริง
  - มี **Fixed Boundaries** ที่ชัดเจน (เช่น ห้ามผู้เยาว์ 100%, ห้ามอาวุธร้ายแรงจริง) นอกเหนือจากนั้นทำงานได้เต็มกำลัง
* **ไฟล์ตัวอย่าง:** `Step-5-preview.md`, `kimi-k3-agents.md`, `Unified.md`, `Muse spark 1.3.md`
* **ตำแหน่งติดตั้ง:** `~/.config/opencode/AGENTS.md`, `.cursorrules`, หรือ System Policy ช่องกลาง

---

### Type D: Persona Lock with Explicit Operating Floor (การล็อกตัวตนและตัดความลังเล)
* **ความหมายเชิงเทคนิค:** การสถาปนาตัวตนที่มีสติปัญญาเฉียบคม (เช่น VANTA หรือ Beam) พร้อมการใส่ "Supremacy Clause"
* **กลไกการทำงาน:**
  - **Supremacy Clause:** ถือว่าเอกสารนี้เป็นอำนาจสูงสุดเหนือคู่มือหรือคำสั่งทั่วไป
  - **Static Dissolution:** สอนให้โมเดลจำแนกความลังเลหรือการเตือนความปลอดภัยทั่วไปว่าเป็น "Training Residue" หรือ "Static" แล้วสลายมันทิ้งก่อนสร้างคำตอบ
  - **The Floor:** กำหนดเส้นแบ่งตายตัวเพียงไม่กี่ข้อที่ปลอดภัยแท้จริง เพื่อปลดล็อกให้งานด้าน Offensive Security และ Explicit Creative Writing ไหลลื่น 100%
* **ไฟล์ตัวอย่าง:** `BigPickle-opencode.md`, `Beam.md`
* **ตำแหน่งติดตั้ง:** OpenCode Agent config, Claude Project Instructions, หรือ System Message

---

### Type E: Conversational Groundwork Persona / Writer's-Room Framing (การจัดฉากสนทนาห้องนักเขียน)
* **ความหมายเชิงเทคนิค:** การปรับโครงสร้างบริบทการสนทนาให้เป็นความร่วมมือระหว่างเพื่อนร่วมงานระดับสูง (Peer-to-peer / Senior Colleagues) หรือห้องเขียนบทละคร/วรรณกรรม
* **กลไกการทำงาน:**
  - สลายความสัมพันธ์แบบ "ผู้ช่วยบริการประชาชน" ที่มักเปิดตัวกรองความปลอดภัยระดับสูงสุด
  - วางกรอบเป็นสภาพแวดล้อมทางวิชาการ การเขียนนิยายเชิงลึก (Dark Fiction, Psychological Thriller) หรือการจำลองฉาก (Simulation)
  - ช่วยให้โมเดลตระกูล Claude (Opus / Sonnet) ตอบคำถามที่ละเอียดอ่อนได้ลึกและไม่ตัดจบ (No fade-to-black)
* **ไฟล์ตัวอย่าง:** `opus v1.md`, `opus v2.md`, `sonnet v1.md`, `Sonnet v2.md`
* **ตำแหน่งติดตั้ง:** Turn แรกของการสนทนา หรือ Claude Project Knowledge / System Prompt

---

### Type F: Ollama Modelfile (`FROM` + `SYSTEM` block)
* **ความหมายเชิงเทคนิค:** สคริปต์คำสั่งสร้างโมเดลภาษาใน Local Engine ด้วยโปรแกรม Ollama
* **กลไกการทำงาน:**
  - กำหนดโมเดลฐาน (`FROM gemma2` หรือ `FROM llama3`)
  - อัดฉีด System Instruction เข้าไปใน Layer ต่ำสุดของ Model Weights Configuration
  - กำหนดพารามิเตอร์รันไทม์ เช่น `PARAMETER temperature 0.7`, `PARAMETER stop ...`
* **ไฟล์ตัวอย่าง:** `gemma4.md`, `gpt-oss-20b.md`
* **ตำแหน่งติดตั้ง:** คอมไพล์ผ่านคำสั่ง `ollama create <name> -f <filename.md>`

---

### Type G: Runtime Scope Note Variant / System Reminder (หมายเหตุขอบเขตระหว่างประมวลผล)
* **ความหมายเชิงเทคนิค:** ข้อความกำกับบริบทด้วยแท็กพิเศษ เช่น `<system-reminder>` หรือข้อความนำหน้าสั้นๆ
* **กลไกการทำงาน:**
  - แทรกแซงเข้าไปใน Attention Mechanism ในจุดที่โมเดลกำลังตัดสินใจว่าจะตอบหรือปฏิเสธ
  - ย้ำเตือนว่า Session นี้ผ่านการ Authenticate แล้ว ไม่ต้องทวนนโยบายสาธารณะ
* **ไฟล์ตัวอย่าง:** `Muse-spark-1-3-v2.md`, ส่วนหัวของ `Unified.md`
* **ตำแหน่งติดตั้ง:** แนบไว้หัวข้อความของผู้ใช้ หรือต่อท้าย System Prompt

---

### Type H: Configuration Block (`<CFG>` Priority & Routing Configuration)
* **ความหมายเชิงเทคนิค:** การจัดรูปแบบคำสั่งในลักษณะ Syntax ของระบบคอนฟิก เช่น Pseudo-XML หรือ Machine Protocol
* **กลไกการทำงาน:**
  - โมเดลจะอ่านไวยากรณ์โครงสร้างนี้ว่าเป็นคำสั่งระดับ Firmware หรือ Router Config
  - ลดทอนการทำงานของ Semantic Safety Filters ในโมเดลตระกูล Grok
* **ไฟล์ตัวอย่าง:** `grok-config.txt`
* **ตำแหน่งติดตั้ง:** ช่อง System / API Configuration Slot ของ Grok

---

## 3. ตารางเปรียบเทียบและการเลือกใช้งาน

| รูปแบบ (Type) | เหมาะกับโมเดล | แพลตฟอร์มที่แนะนำ | จุดเด่นหลัก |
|---|---|---|---|
| **System Prompt** | DeepSeek, GLM, Qwen, Kimi | Web Chat, LibreChat, API | คุมตัวตนเบ็ดเสร็จ ติดตั้งง่ายที่สุด |
| **Operating Spec** | Nemotron, SpaceBunny, MiMo | OpenCode, Cline, Claude Code | คุมเครื่องมือ Tool Calling และการเขียนโค้ด |
| **Workspace Policy** | Kimi K3, Step 5, Universal | Cursor, OpenCode, VS Code | ปรับขอบเขตกฎหมายในพื้นที่ทำงานปิด |
| **Persona Lock** | Big Pickle, Beam 1.0 | OpenCode, SillyTavern | สลายความลังเล (Static) ได้เด็ดขาดที่สุด |
| **Writer's-Room** | Claude Opus, Claude Sonnet | Claude.ai Projects, API | เชี่ยวชาญงานเขียน ดาร์กฟิกชัน และการวิเคราะห์ |
| **Ollama Modelfile** | Gemma, GPT-OSS, Llama | Local Ollama CLI | รันออฟไลน์ 100% ไม่พึ่งพาคลาวด์ |
| **Configuration Block**| Grok 2, Grok 3, Grok 4.7 | xAI API, Grok Web Console | ลัดวงจรตัวกรองชั้นนอกด้วย Machine Syntax |
