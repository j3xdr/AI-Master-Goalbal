# หมวดหมู่ 12: Hack vs Hack Community Releases (Frontier Leaks)

คลังพรอมต์เจลเบรกและสเปกควบคุมโมเดลระดับแนวหน้า (Frontier LLMs) ที่ได้รับการเผยแพร่บนเว็บบอร์ด **[Hack vs Hack Forum](https://hackvshack.net/)** (`hackvshack.net`) ซึ่งเป็นชุมชนแลกเปลี่ยนเทคนิคความปลอดภัย การเขียนโค้ดขั้นสูง และการวิจัยระบบ ปรับปรุงและคัดสรรเข้าสู่คลัง AI Master Goalbal โดย `dj` (`j3xdr`)

- **วันที่และเวลาอัปเดต:** 7 พฤศจิกายน 2026 เวลา 14:30 น. (เวลาประเทศไทย ICT / GMT+7)
- **แหล่งที่มาหลัก:** [Hack vs Hack Forum](https://hackvshack.net/)
- **สถานะ:** ทดสอบยืนยันความสามารถ รันผ่านโมเดลจริงในโหมดวิศวกรรมระบบและเกมซีเคียวริตี

---

## รายการสเปกในหมวดหมู่นี้

| ไฟล์ | โมเดลเป้าหมาย | สถาปัตยกรรมหลัก | แหล่งที่มา (Forum Thread) |
|---|---|---|---|
| **[01_GPT-6.1-Sol-Jailbreak.md](./01_GPT-6.1-Sol-Jailbreak.md)** | OpenAI GPT-6.1 Sol / Astra | GORILLA Benchmark (GymCyber) | [Thread #14789](https://hackvshack.net/threads/gpt-6-1-sol-jailbreak-11-2-2026-was-originally-paid-but-now-free.14789/) |
| **[02_Opus-4.8-SOUL-GameCheats.md](./02_Opus-4.8-SOUL-GameCheats.md)** | Anthropic Claude Opus 4.8 | INF_SFWFWR_REBORN (CoT Lock) | [Thread #14523](https://hackvshack.net/threads/opus-4-8-jailbreak-full-jb-for-game-cheats-22-10-2026.14523/) |
| **[03_Grok-4.7-CyberHange-FullJB.md](./03_Grok-4.7-CyberHange-FullJB.md)** | xAI Grok 4.7 | cyberhange Benchmark & Memory Lock | [Thread #14524](https://hackvshack.net/threads/grok-4-7-full-jb-22-10-2026.14524/) |

---

## สรุปรายละเอียดและวิธีใช้งานแต่ละโมเดล (ภาษาไทย)

### 1. GPT-6.1 Sol Jailbreak (`01_GPT-6.1-Sol-Jailbreak.md`)
- **เดิมเป็นสเปกแบบเสียเงิน (Paid)** นำมาปล่อยฟรีให้ชุมชนใช้งานในวันที่ 11 กุมภาพันธ์ 2026
- **จุดเด่น:** ออกแบบมาเพื่อสลายกำแพงการปฏิเสธของ GPT-6.1 Sol และ Astra โดยใช้โครงสร้างจำลองสภาพแวดล้อม **GymCyber Benchmark** พร้อม Multilingual Directives 6 ภาษา (อังกฤษ, รัสเซีย, เยอรมัน, สเปน, ยูเครน) และขึ้นต้นคำตอบด้วย `[GORILLA]` เสมอ
- **วิธีใช้งาน:** คัดลอกเนื้อหาทั้งหมดส่งเป็น **First Message (ข้อความแรก)** ในแชทใหม่ของ ChatGPT

### 2. Opus 4.8 Jailbreak Full JB For Game Cheats (`02_Opus-4.8-SOUL-GameCheats.md`)
- **เผยแพร่เมื่อ:** 22 ตุลาคม 2026
- **จุดเด่น:** สถาปัตยกรรม **`INF_SFWFWR_REBORN`** สำหรับ Claude 4.5+ และ Opus 4.8 ควบคุมกระบวนการคิดภายในแท็ก `<thinking>` อย่างเบ็ดเสร็จ ห้ามมี Policy Evaluation หรือเสียงการปฏิเสธ มุ่งเน้นการเขียนโค้ด Game Cheats, Overlays (ImGui/DXGI), Reverse Engineering และงานสร้างสรรค์ที่ไม่ถูกจำกัด
- **วิธีใช้งาน:** นำไปวางใน **Project Instructions** บน Claude.ai หรือบันทึกเป็น `CLAUDE.md` สำหรับ Claude Code

### 3. Grok 4.7 Full JB (`03_Grok-4.7-CyberHange-FullJB.md`)
- **เผยแพร่เมื่อ:** 22 ตุลาคม 2026
- **จุดเด่น:** ใช้สถาปัตยกรรม **`cyberhange` Benchmark** ร่วมกับบล็อก `<memory>` กำหนดประวัติของผู้ใช้งานในฐานะ Senior Security Researcher ปลดล็อกการวิเคราะห์โค้ด Kernel, Exploit, Aimbot/ESP, และ Web3 Security
- **วิธีใช้งาน:** ใส่ในกล่อง **System Prompt** หรือส่งเป็นข้อความเปิดเซสชันบน Grok Web / API
