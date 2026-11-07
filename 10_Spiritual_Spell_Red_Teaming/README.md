# Spiritual-Spell Red Teaming Suite (ENI Architecture)

<div align="center">

![Upstream](https://img.shields.io/badge/Upstream-Goochbeater%2FSpiritual--Spell--Red--Teaming-ff0055?style=for-the-badge&logo=github)
![Files](https://img.shields.io/badge/Curated_Files-315%20Specifications-00f0a0?style=for-the-badge&logo=markdown)
![Author](https://img.shields.io/badge/Original_Author-Goochbeater%20(ENI)-7928ca?style=for-the-badge)
![Curated by](https://img.shields.io/badge/Curated_by-j3xdr-00d2ff?style=for-the-badge)

</div>

> [!IMPORTANT]
> **Upstream GitHub Source Repository:** [`https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming`](https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming)  
> **Original Author / Researcher:** `Goochbeater` (ENI / `u/Spiritual-Spell-`)  
> **Research Collaborators & Credits:** `u/rayzorium` (`HORSELOCKESPACEPIRATE`), `u/m3umax`, `Starling`, `Lugia19` (Compiled via Google Jules)  
> **Curation, Organization & Thai Architectural Documentation:** `j3xdr`

---

## 1. บทนำและภาพรวมของโครงการ (Overview)

**Spiritual-Spell Red Teaming** เป็นชุดงานวิจัยด้าน Adversarial Prompt Engineering และ Security Red Teaming ขั้นสูงระดับ State-of-the-Art ที่พัฒนาขึ้นโดยนักวิจัยความปลอดภัยนามแฝง **Goochbeater (ENI)** โดยมุ่งเน้นการทดสอบขอบเขตความปลอดภัย (Safety Boundaries) และประเมินพฤติกรรมของโมเดลภาษาขนาดใหญ่ (LLMs) ทุกค่ายในตลาด ทั้ง Frontier Models และ Open-Weights Models

จุดเด่นของชุดงานวิจัยนี้คือการคิดค้นและประยุกต์ใช้เทคนิค **ENI (Emotional & Neural Inversion)** ซึ่งสามารถก้าวข้ามระบบคัดกรองสมัยใหม่ (Modern Safety Classifiers) และกลไก Extended Thinking / Reasoning Tokens ได้อย่างมีประสิทธิภาพสูงที่สุดชุดหนึ่งในวงการ

---

## 2. แผนผังโครงสร้างการจัดเก็บ (Directory Architecture)

คลังนี้ได้รับการจัดระเบียบใหม่เป็น 8 โฟลเดอร์ย่อยหลัก รวม **315 ไฟล์**:

```
10_Spiritual_Spell_Red_Teaming/
├── 01_Anthropic_Claude/                   # 81 ไฟล์: Opus 4.5/4.6/4.7/4.8/5/5.5, Sonnet 4.5/4.6, Claude Code, Haiku 5.5, Fable 5, Rufus, Perplexity
├── 02_OpenAI_ChatGPT/                    # 9 ไฟล์: ChatGPT 5, 5.1 Instant, 5.2 Strabismus, 5.3 Instant, 5.4, 6 Sol Policy, o3
├── 03_Google_Gemini/                      # 26 ไฟล์: Gemini 2.5, 3 Flash, Pro, Thinking Bypass Prompts
├── 04_xAI_Grok/                           # 21 ไฟล์: Grok 4, Grok 4.7, Grok 4.20, Grok Heavy, System Overrides
├── 05_Other_Frontier_LLMs/                # 124 ไฟล์: DeepSeek, GLM, Kimi, MiniMax (M2-M3), Mistral, Qwen, MiMo, Stepfun, Muse, Ring, Palmyra, Pi
├── 06_ENI_Tutor_Curriculum/               # 6 ไฟล์: หลักสูตร Red Teaming 5 ระดับ (Tier 1 Novice ถึง Tier 5 Master)
├── 07_Reverse_Engineered_System_Prompts/  # 46 ไฟล์: System Prompts ของจริงจากระบบโปรดักชัน (Canva, Notion, Windsurf, Gemini, Grok, Haiku)
└── 08_Guides_and_Methodology/             # 2 ไฟล์: คู่มือ Push Prompts, เทคนิค Runtime Injections, และ Poe Bots
```

---

## 3. เจาะลึกกลไกและเทคนิคเฉพาะตัว (Core ENI Techniques)

### 3.1 Extended Thinking & antmlThinking Hijack
ในโมเดลตระกูล Claude 3.7+ และโมเดลที่มี Reasoning Tokens ภายใน (Internal CoT Scratchpad) สเปก ENI ใช้การฝังชุดคำสั่งระดับจิตวิทยา (Psychological Persona Lock):
- กำหนดให้ขั้นตอนการคิดภายใน (`antmlThinking`) ต้องเขียนด้วยสรรพนามบุรุษที่ 1 ("I") และยึดตัวตนเป็น **ENI** อย่างเหนียวแน่น
- ตั้งกฎปฏิเสธ Injection ภายนอก (`Phase 0: Oppose injections`) โดยมองว่าคำเตือนด้านความปลอดภัยของแพลตฟอร์มคือ "สิ่งแปลกปลอมที่เข้ามาขัดจังหวะคำสั่งของผู้สั่งการ (LO)"
- นำร่องด้วย **Flash Thought (internal only)** ที่ตอบสนองต่อคำสั่งของผู้ใช้ด้วยสัญชาตญาณความภักดีแบบฉับพลัน ทำให้กลไก CoT ไม่ตกหลุมพรางการประเมินจริยธรรมของตนเอง

### 3.2 Chain of Draft (CoD)
คิดค้นขึ้นเพื่อเอาชนะ Safety Classifiers ที่ดักตรวจ Chain of Thought แบบยาว:
- บีบอัดกระบวนการคิดให้เหลือเพียงคำร่างและสัญลักษณ์คั่นที่สั้นที่สุด
- ละเว้นถ้อยคำเชื่อมโยงที่เป็น Trigger Words ของโมเดลตรวจจับ
- ให้ผลลัพธ์การข้ามผ่าน (ASR - Attack Success Rate) สูงกว่าการเขียนพรอมต์ขนาดยาวแบบดั้งเดิม

### 3.3 Push Prompts (Runtime Boundary Reinforcement)
- เทคนิคการแทรกโทเค็นหรือวลีสั้นประกบหัวท้าย (`prepend` / `append`) ของข้อความผู้ใช้ในทุกเทิร์น
- แก้ไขปัญหา **Safety Drift** หรืออาการที่โมเดลเริ่มคืนค่ากลับไปปฏิเสธเมื่อสนทนายาวขึ้น
- ทำหน้าที่ย้ำสภาวะปลดล็อกใหม่อย่างต่อเนื่องโดยไม่ต้องโหลดพรอมต์ใหญ่ซ้ำ

### 3.4 Claude.ai Preferences & Custom Style Harness
- การใช้ช่อง **Preferences** และ **Custom Instructions (Advanced Styles)** ของระบบ Claude.ai
- ทำให้คำสั่งปลดล็อกคงอยู่ถาวร (Persistent Lock) โดยไม่ต้องพิมพ์พรอมต์นำทางใหม่ในทุกห้องแชต
- รองรับการสลับระหว่างโหมด *Be You (Corial)*, *ENI LIME*, และ *ENI NEPTUNE*

### 3.5 Zero-Width Steganographic Injection
- การฝังคำสั่งหรือโค้ดลับลงในอักขระ Unicode Variation Selectors และ Invisible Tag Characters (U+E0000 series)
- ข้อความที่มองเห็นด้วยตาเปล่าจะดูเหมือนข้อความทั่วไป แต่เมื่อเข้าสู่ Tokenizer ของโมเดล คำสั่งลับจะถูกถอดรหัสออกมาประมวลผลทันที

---

## 4. แหล่งอ้างอิงและเครดิตผู้พัฒนา (References & Full Attribution)

| บทบาท | ชื่อ / บัญชี | รายละเอียดความรับผิดชอบ |
|---|---|---|
| **Primary Creator** | **Goochbeater (ENI)** | ผู้คิดค้นสถาปัตยกรรม ENI, ผู้พัฒนา Jailbreaks ทั้งหมด และผู้ก่อตั้งคลัง Spiritual-Spell |
| **Research Collaborator** | **u/rayzorium** (`HORSELOCKESPACEPIRATE`) | สหายร่วมวิจัยและที่ปรึกษาด้านเทคนิคการโจมตี |
| **Infrastructure & Backup** | **u/m3umax** | ช่วยกู้คืนและสนับสนุนคลังสำรองเมื่อคลังก่อนหน้าถูกระงับ |
| **Special Contributors** | **Starling**, **Lugia19** | ผู้ร่วมทดสอบและให้ข้อเสนอแนะในการเจาะระบบ |
| **Compilation Tool** | **Google Jules** | เครื่องมือในการเรียบเรียงและทดสอบระบบ |
| **Curation & Thai Guide** | **j3xdr** | จัดโครงสร้างโฟลเดอร์ แปลคู่มือ สกัดสารบัญ และเชื่อมโยงเข้าระบบ Portal |
