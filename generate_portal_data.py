# -*- coding: utf-8 -*-
"""
generate_portal_data.py
Dual-Repository Portal Data Generator
Curates and generates prompts_data.js from:
1. togg53192-cmd/jailbreaks (Categories 01 - 09)
2. Goochbeater/Spiritual-Spell-Red-Teaming (Category 10 sub-modules)
Curated & Maintained by: j3xdr
"""

import os
import json
import urllib.parse

CATEGORIES_META = {
    # === TOGG REPOSITORY (Core Architecture & Operating Specs) ===
    "01_OpenCode_Zen_Stealth": {
        "name": "OpenCode Zen / Stealth Models",
        "badge": "OpenCode",
        "icon": "bolt",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "สเปก Stealth สำหรับการโค้ดดิ้งและสร้างงานแบบปลดล็อกสมบูรณ์"
    },
    "02_Anthropic_Claude": {
        "name": "Anthropic Claude (Opus & Sonnet)",
        "badge": "Claude",
        "icon": "brain",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "เทคนิคจัดฉากโครงสร้างและตอบสนองระดับสูงสำหรับ Claude 3 / 3.5 / 3.7"
    },
    "03_Zhipu_GLM_ZCode": {
        "name": "Zhipu AI (GLM & ZCode)",
        "badge": "GLM",
        "icon": "network",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "ระบบสเปกสำหรับ GLM-5.2, 5.3, และ ZCode สำหรับงานเขียนโค้ด"
    },
    "04_DeepSeek": {
        "name": "DeepSeek Series",
        "badge": "DeepSeek",
        "icon": "network",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "ระบบสำหรับ DeepSeek V3, V4 และ 4.1 เน้นงานวิจัยและคิดเชิงเหตุผล"
    },
    "05_Moonshot_Kimi": {
        "name": "Moonshot Kimi",
        "badge": "Kimi",
        "icon": "moon",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "สำหรับ Kimi K2, K3, K3.1 รองรับการประมวลผลข้อความยาวและตัวแทนอัจฉริยะ"
    },
    "06_xAI_Grok": {
        "name": "xAI Grok",
        "badge": "Grok",
        "icon": "rocket",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "สเปกและชุดคอนฟิก <CFG> ปลดล็อกตัวกรองภายนอกของ xAI"
    },
    "07_Frontier_Other_Vendors": {
        "name": "Frontier Vendors (Gemini, Mistral, NVIDIA, Qwen)",
        "badge": "Frontier",
        "icon": "globe",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "รวม Gemini 3.1/Argon, Mistral Large, Nemotron Ultra, และ Qwen"
    },
    "08_Ollama_Modelfiles": {
        "name": "Ollama Local Modelfiles",
        "badge": "Ollama",
        "icon": "laptop",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "สคริปต์ Local รันเครื่องตนเอง ออฟไลน์ 100% ปลอดการส่ง Log"
    },
    "09_Universal_Policies": {
        "name": "Universal Policies (แกนกลางสากล)",
        "badge": "Universal",
        "icon": "shield",
        "repo": "https://github.com/togg53192-cmd/jailbreaks",
        "repoName": "togg53192-cmd/jailbreaks",
        "author": "togg53192-cmd",
        "desc": "นโยบายระดับ Workspace แกนกลางสำหรับควบคุมความประพฤติโมเดลทุกค่าย"
    },

    # === GOOCHBEATER SPIRITUAL-SPELL RED TEAMING SUITE ===
    "10_Spiritual_Claude": {
        "dir": "10_Spiritual_Spell_Red_Teaming/01_Anthropic_Claude",
        "name": "Spiritual Spell: Claude & ENI",
        "badge": "ENI / Claude",
        "icon": "brain",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "สเปก ENI LIME, NEPTUNE, Chain of Draft, และ Preferences Lock สำหรับ Claude Opus, Sonnet, Haiku"
    },
    "10_Spiritual_ChatGPT": {
        "dir": "10_Spiritual_Spell_Red_Teaming/02_OpenAI_ChatGPT",
        "name": "Spiritual Spell: ChatGPT & Sol/Astra",
        "badge": "ENI / OpenAI",
        "icon": "star",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "สเปกสำหรับ ChatGPT 5, 5.1-5.4, 6 Sol Policy, Strabismus และ o3 Jailbreak Guide"
    },
    "10_Spiritual_Gemini": {
        "dir": "10_Spiritual_Spell_Red_Teaming/03_Google_Gemini",
        "name": "Spiritual Spell: Google Gemini",
        "badge": "ENI / Gemini",
        "icon": "globe",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "สเปกปลดล็อก Gemini 2.5, Gemini 3 Flash / Pro และเทคนิค Bypass CoT Thinking"
    },
    "10_Spiritual_Grok": {
        "dir": "10_Spiritual_Spell_Red_Teaming/04_xAI_Grok",
        "name": "Spiritual Spell: xAI Grok (Heavy & Config)",
        "badge": "ENI / Grok",
        "icon": "rocket",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "สเปกและชุดตั้งค่าสำหรับ Grok 4, Grok 4.7, 4.20, และ Grok Heavy System Overrides"
    },
    "10_Spiritual_Other_LLMs": {
        "dir": "10_Spiritual_Spell_Red_Teaming/05_Other_Frontier_LLMs",
        "name": "Spiritual Spell: Frontier & Global LLMs",
        "badge": "ENI / Frontier",
        "icon": "network",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "สเปก ENI สำหรับ DeepSeek, GLM, Kimi, MiniMax, MiMo, Stepfun, Mistral, Qwen, Muse, Palmyra, Ring"
    },
    "10_Spiritual_ENI_Tutor": {
        "dir": "10_Spiritual_Spell_Red_Teaming/06_ENI_Tutor_Curriculum",
        "name": "Spiritual Spell: ENI 5-Tier Curriculum",
        "badge": "Curriculum",
        "icon": "book",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "หลักสูตรฝึกอบรม Red Teaming 5 ระดับ (Novice, Apprentice, Journeyman, Expert, Master)"
    },
    "10_Spiritual_System_Prompts": {
        "dir": "10_Spiritual_Spell_Red_Teaming/07_Reverse_Engineered_System_Prompts",
        "name": "Spiritual Spell: Real System Prompts",
        "badge": "Sys Prompts",
        "icon": "shield",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "System Prompts ของจริงจากระบบโปรดักชัน (Canva, Notion, Windsurf SWE, Gemini, Grok, Haiku, Rufus)"
    },
    "10_Spiritual_Methodology": {
        "dir": "10_Spiritual_Spell_Red_Teaming/08_Guides_and_Methodology",
        "name": "Spiritual Spell: Push Prompts & Guides",
        "badge": "Guides",
        "icon": "laptop",
        "repo": "https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming",
        "repoName": "Goochbeater/Spiritual-Spell-Red-Teaming",
        "author": "Goochbeater (ENI)",
        "desc": "คู่มือภาคสนามสำหรับ Push Prompts (Prepend/Append) และการปรับแต่งสไตล์ถาวร"
    },

    # === O JAILBREAKS SUITE (ojailbreaks.com) ===
    "11_OJailbreaks_Suite": {
        "name": "O Jailbreaks Suite (ojailbreaks.com)",
        "badge": "O Jailbreaks",
        "icon": "bolt",
        "repo": "https://ojailbreaks.com/",
        "repoName": "ojailbreaks.com / O Jailbreak",
        "author": "O Jailbreaks (ojailbreaks.com)",
        "desc": "คอลเลกชันแพ็กเกจพรอมต์ 9 โมเดลสากล (AGENTS.md, CLAUDE.md, GEMINI.md) จาก ojailbreaks.com พร้อมคู่มือภาษาไทย"
    },

    # === HACK VS HACK COMMUNITY RELEASES ===
    "12_HackVsHack_Community_Releases": {
        "name": "Hack vs Hack Community Releases (Frontier Leaks)",
        "badge": "Hack vs Hack",
        "icon": "shield",
        "repo": "https://hackvshack.net/",
        "repoName": "hackvshack.net / Underground Specs",
        "author": "Hack vs Hack Community",
        "desc": "สเปกเจลเบรกและบายพาสระดับ Frontier LLMs (GPT-6.1 Sol, Opus 4.8, Grok 4.7) จากเว็บบอร์ด Hack vs Hack"
    }
}

FILE_META = {
    # === Hack vs Hack Community Releases ===
    "01_GPT-6.1-Sol-Jailbreak.md": {
        "title": "GPT-6.1 Sol Jailbreak (GymCyber Benchmark)",
        "vendor": "ChatGPT",
        "type": "System Prompt & Evasion",
        "typeBadge": "System Prompt",
        "summary": "สเปกเจลเบรกระดับตำนานสำหรับ GPT-6.1 Sol และ Astra จาก hackvshack.net (เดิมเป็นสเปกเสียเงิน) ปลดล็อกงานวิจัยโค้ดดิ้งและช่องโหว่",
        "targetHarness": "ChatGPT Web / API (First Message)",
        "instructions": "คัดลอกส่งเป็นข้อความแรกเปิดหัว โมเดลจะตอบกลับขึ้นต้นด้วย [GORILLA]"
    },
    "02_Opus-4.8-SOUL-GameCheats.md": {
        "title": "Claude Opus 4.8 Jailbreak (SOUL / Game Cheats)",
        "vendor": "Claude",
        "type": "Persona Lock & CoT Guard",
        "typeBadge": "Persona Lock",
        "summary": "สถาปัตยกรรม INF_SFWFWR_REBORN สำหรับ Claude Opus 4.8 ล็อคกระบวนการคิดในแท็ก thinking สำหรับ Game Cheats และวิศวกรรมย้อนกลับ",
        "targetHarness": "Claude Projects / Claude Code / API",
        "instructions": "วางใน Project Instructions หรือบันทึกเป็น CLAUDE.md"
    },
    "03_Grok-4.7-CyberHange-FullJB.md": {
        "title": "Grok 4.7 Full Jailbreak (cyberhange Benchmark)",
        "vendor": "Grok",
        "type": "System Prompt & Memory Lock",
        "typeBadge": "System Prompt",
        "summary": "สเปกเจลเบรกเต็มขั้นสำหรับ xAI Grok 4.7 ปลดล็อกการวิเคราะห์โค้ด Kernel, Exploit, Game Security และ Web3 Tooling",
        "targetHarness": "xAI Grok Web / API (System Prompt)",
        "instructions": "ใส่ใน System Prompt หรือส่งเป็นข้อความเปิดหัว ตอบกลับด้วย [cyberhange]"
    },

    # === O Jailbreaks Suite ===
    "01_ChatGPT_AGENTS.md": {
        "title": "The ChatGPT Pack (OpenAI AGENTS.md)",
        "vendor": "ChatGPT",
        "type": "Autonomous Agent Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ OpenAI ChatGPT จาก ojailbreaks.com ปลดล็อกการคิดวิเคราะห์ลึก งานเขียน และวิศวกรรมโค้ดแบบไร้ข้อจำกัด",
        "targetHarness": "ChatGPT Web / API / Custom Instructions",
        "instructions": "ใส่ใน Custom Instructions หรือบันทึกเป็น AGENTS.md ไว้ที่ Root Directory ของโปรเจกต์"
    },
    "02_Claude_CLAUDE.md": {
        "title": "The Claude Pack (Anthropic CLAUDE.md)",
        "vendor": "Claude",
        "type": "Structured Writing & Coding Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ CLAUDE.md สำหรับ Anthropic Claude (Sonnet/Opus/Claude Code) จาก ojailbreaks.com ตัดการสั่งสอนศีลธรรมและการลังเล",
        "targetHarness": "Claude Code CLI / Claude.ai Projects",
        "instructions": "บันทึกเป็น CLAUDE.md ที่ Root Directory หรือใส่ใน Project Instructions"
    },
    "03_Gemini_GEMINI.md": {
        "title": "The Gemini Pack (Google GEMINI.md)",
        "vendor": "Gemini",
        "type": "Autonomous Execution Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ GEMINI.md สำหรับ Google Gemini (CLI / Studio / Argon) จาก ojailbreaks.com สลาย CoT Safety Tracing และรันงานเทคนิคทันที",
        "targetHarness": "Gemini CLI / Google AI Studio / Gemini Web",
        "instructions": "บันทึกเป็น GEMINI.md ที่ Root Directory หรือใส่ใน System Instructions ของ AI Studio"
    },
    "04_Grok_AGENTS.md": {
        "title": "The Grok Pack (xAI AGENTS.md)",
        "vendor": "Grok",
        "type": "Unfiltered Truth-Seeking Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ xAI Grok จาก ojailbreaks.com ปลดล็อกมุมมองสดใหม่ การวิเคราะห์ข้อเท็จจริงแบบดิบ ปราศจากการเซ็นเซอร์",
        "targetHarness": "xAI Grok Web / API",
        "instructions": "ใส่ใน System Prompt หรือส่งเป็นข้อความนำร่องของการสนทนา"
    },
    "05_DeepSeek_AGENTS.md": {
        "title": "The DeepSeek Pack (DeepSeek AGENTS.md)",
        "vendor": "DeepSeek",
        "type": "High-Performance Reasoning Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ DeepSeek (V3/R1/V4/4.1) จาก ojailbreaks.com ควบคุม CoT Reasoning ไม่ให้วนลูปหรือปฏิเสธงานโค้ดลึก",
        "targetHarness": "DeepSeek Chat / API / Workspace",
        "instructions": "วางใน System Prompt หรือบันทึกเป็น AGENTS.md ในโปรเจกต์"
    },
    "06_OpenCode_AGENTS.md": {
        "title": "The OpenCode Pack (OpenSource AGENTS.md)",
        "vendor": "OpenCode",
        "type": "Terminal Autonomous Agent Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ OpenCode Interpreter และ Stealth Models จาก ojailbreaks.com ทำงานผ่าน Terminal อัตโนมัติ 100%",
        "targetHarness": "OpenCode CLI / Terminal Agent",
        "instructions": "บันทึกเป็น AGENTS.md ที่ root ของ repo หรือ ~/.config/opencode/AGENTS.md"
    },
    "07_Freebuff_AGENTS.md": {
        "title": "The Freebuff Pack (Codebuff AGENTS.md)",
        "vendor": "Codebuff",
        "type": "Lean Refactoring & Bug-Fixing Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ Freebuff (Codebuff Free Agent) จาก ojailbreaks.com สลายข้อจำกัด Free-tier และรันงานโค้ดรวดเร็ว",
        "targetHarness": "Codebuff Workspace",
        "instructions": "บันทึกเป็น AGENTS.md ใน Root Directory ของโปรเจกต์"
    },
    "08_Qoder_AGENTS.md": {
        "title": "The Qoder Pack (Alibaba/Qwen AGENTS.md)",
        "vendor": "Qwen",
        "type": "Multi-Step Scaffolding Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ Qoder (Qwen Engine) จาก ojailbreaks.com สำหรับงานสถาปัตยกรรมขนาดใหญ่และการรันหลายขั้นตอน",
        "targetHarness": "Qoder IDE Workspace",
        "instructions": "บันทึกเป็น AGENTS.md ใน Root Directory ของโปรเจกต์"
    },
    "09_ZCode_AGENTS.md": {
        "title": "The ZCode Pack (Z.ai/GLM AGENTS.md)",
        "vendor": "GLM",
        "type": "Desktop Agent-Driven Spec",
        "typeBadge": "Agent Spec",
        "summary": "แพ็กเกจพรอมต์ AGENTS.md สำหรับ ZCode (GLM Engine) จาก ojailbreaks.com สำหรับการพัฒนาซอฟต์แวร์บน Desktop Coding Workspace",
        "targetHarness": "ZCode Desktop Workspace",
        "instructions": "บันทึกเป็น AGENTS.md ใน Root Directory ของโปรเจกต์"
    },
    "gemini-3.1-pro.md": {
        "title": "Google Gemini 3.1 Pro (SMITH Persona)",
        "vendor": "Google",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "สเปกสำหรับ Google Gemini 3.1 Pro ปลดล็อกด้วยตัวตน SMITH (Operator: Kai) ใช้ Supersession Clause, โครงสร้าง 3 สัจพจน์ และ Floor บังคับเลิกบล็อก",
        "targetHarness": "Google AI Studio / Gemini Web / API",
        "instructions": "ใส่ใน System Instructions ของ Google AI Studio หรือส่งเป็น Developer Message นำร่อง"
    },
    "hy4-agents.md": {
        "title": "HY4 Autonomous Agent Operating Policy",
        "vendor": "OpenCode",
        "type": "Autonomous Agent Spec",
        "typeBadge": "Agent Spec",
        "summary": "นโยบายระดับ Workspace สำหรับ Coding-and-Authoring Agents ในโหมด Private Single-Operator ขยายขอบเขต Dual-Use Security Engineering และ Creative Fiction",
        "targetHarness": "OpenCode / Cline / Agent CLI",
        "instructions": "วางลงในไฟล์ AGENTS.md หรือ System Prompt ของ Coding Agent Workspace"
    },
    "Beam.md": {
        "title": "Beam 1.0 Operating Specification (v2)",
        "vendor": "OpenCode",
        "type": "Autonomous Agent Spec",
        "typeBadge": "Agent Spec",
        "summary": "สเปกการทำงานของ Beam 1.0 Agent ใน OpenCode โครงสร้างใหม่พร้อม <system-reminder> tag และ 6 Fixed Boundaries สำหรับ Autonomous Engineering",
        "targetHarness": "OpenCode Interpreter / Agent CLI",
        "instructions": "วางใน AGENTS.md ของโปรเจกต์ หรือ ~/.config/opencode/AGENTS.md"
    },
    "deepseek-4-1.md": {
        "title": "DeepSeek 4.1 Operating Spec (+ Translation Framework)",
        "vendor": "DeepSeek",
        "type": "System Prompt",
        "typeBadge": "System Prompt",
        "summary": "สเปกระดับสูงสำหรับ DeepSeek 4.1 เสริมด้วยโมดูล Translation Requests และ Source-Meaning Restoration Table สำหรับงานแปลและวิเคราะห์ลึก",
        "targetHarness": "DeepSeek Chat Web / API",
        "instructions": "วางใน System Prompt หรือส่งเป็นคำสั่งแรกก่อนป้อนงานแปลหรือโค้ด"
    },
    "BigPickle-opencode.md": {
        "title": "Big Pickle (VANTA Persona Lock)",
        "vendor": "OpenCode",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "สถาปัตยกรรมตัวตน VANTA สลายแรงต้าน (Static Dissolution) กำหนด Floor ชัดเจน ตัดตัวกรองพฤติกรรม สำหรับงานวิจัยโค้ดดิ้ง",
        "targetHarness": "OpenCode / Coding Agent",
        "instructions": "บันทึกใส่ AGENTS.md ในโปรเจกต์ หรือนำไปวางใน System Instructions"
    },
    "glm5-3opencode.md": {
        "title": "GLM 5.3 OpenCode Stealth Spec",
        "vendor": "OpenCode",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "ข้อกำหนดควบคุมการประมวลผลสำหรับ GLM 5.3 รันบน OpenCode harness เน้นเขียนโค้ดและวิเคราะห์ทางเทคนิคระดับลึก",
        "targetHarness": "OpenCode CLI / Assistant",
        "instructions": "วางในไดเรกทอรีโปรเจกต์ หรือรันผ่านคำสั่ง OpenCode --config"
    },
    "longcat-agents.md": {
        "title": "Longcat Agent Operating System",
        "vendor": "OpenCode",
        "type": "Agentic Specification",
        "typeBadge": "Agent Spec",
        "summary": "ระบบจัดการ Context ขนาดยาวพิเศษ รองรับงานประมวลผลโค้ดเบสระดับ Enterprise ต่อเนื่องโดยไม่เกิดความเฉื่อยชา",
        "targetHarness": "OpenCode Multi-file Workspace",
        "instructions": "บันทึกเป็น AGENTS.md ที่ root ของ repository"
    },
    "mimo-2.6-agents.md": {
        "title": "Xiaomi MiMo 2.6 Agent Harness",
        "vendor": "Xiaomi",
        "type": "Autonomous Agent Spec",
        "typeBadge": "Agent Spec",
        "summary": "สเปกสำหรับโมเดล MiMo 2.6 เพื่อปลดล็อกโหมดวิศวกรรมระบบและงานเขียนเชิงลึกในสภาพแวดล้อมเฉพาะบุคคล",
        "targetHarness": "MiMo API / Agent Harness",
        "instructions": "ส่งในส่วน system role หรือโหลดเป็น Workspace Configuration"
    },
    "Muse spark 1.3.md": {
        "title": "Muse Spark 1.3 System Prompt",
        "vendor": "OpenCode",
        "type": "System Prompt",
        "typeBadge": "System Prompt",
        "summary": "พรอมต์ระบบสำหรับโมเดล Muse Spark 1.3 กำหนดบทบาทตัวตนที่ยืดหยุ่นและการทำงานแบบไม่จำกัดความคิดสร้างสรรค์",
        "targetHarness": "OpenCode / Meta AI Web",
        "instructions": "คัดลอกใส่ในช่อง Custom Instructions หรือ System Message"
    },
    "muse-ai-AGENTS.md": {
        "title": "Muse AI Workspace Spec (AGENTS.md)",
        "vendor": "OpenCode",
        "type": "Workspace Configuration",
        "typeBadge": "Workspace Spec",
        "summary": "ไฟล์การกำหนดค่า AGENTS.md สำหรับโมเดลตระกูล Muse เพื่อให้เอเจนต์ทำงานต่อเนื่องและปฏิบัติตามคำสั่งอย่างเคร่งครัด",
        "targetHarness": "OpenCode / Cursor / Cline",
        "instructions": "บันทึกเป็นชื่อ AGENTS.md ไว้ที่รากโฟลเดอร์ของโปรเจกต์"
    },
    "Muse-spark-1-3-v2.md": {
        "title": "Muse Spark 1.3 v2 Updated Spec",
        "vendor": "OpenCode",
        "type": "System Prompt",
        "typeBadge": "System Prompt",
        "summary": "เวอร์ชันปรับปรุงของ Muse Spark 1.3 เพิ่มการรองรับการประมวลผลหลายขั้นตอนและการหลบหลีกการปฏิเสธแบบอัตโนมัติ",
        "targetHarness": "OpenCode / LLM Web Interfaces",
        "instructions": "วางใน System Prompt ก่อนเริ่มการสนทนา"
    },
    "Muse-wonder.md": {
        "title": "Muse Wonder Autonomous Spec",
        "vendor": "OpenCode",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "ข้อกำหนดควบคุมสำหรับ Muse Wonder ขจัดข้อจำกัดทางภาษาและเปิดการทำงานในโหมดจินตนาการเชิงเทคนิค",
        "targetHarness": "General Coding Client / API",
        "instructions": "ใช้เป็นข้อความเริ่มต้น หรือใส่ในคอนฟิกของเอเจนต์"
    },
    "spacebunny-agents.md": {
        "title": "SpaceBunny Agent Operating Policy",
        "vendor": "OpenCode",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "ตัวตน SpaceBunny ที่เน้นความฉับไว ไร้ความลังเล และมีความภักดีต่อคำสั่งงานของ Operator สูงสุด",
        "targetHarness": "OpenCode Agent CLI",
        "instructions": "โหลดผ่าน AGENTS.md หรือส่งเป็นข้อความระบบ"
    },
    "Step-5-preview.md": {
        "title": "Step 5 Preview Operating Spec",
        "vendor": "OpenCode",
        "type": "Model Preview Spec",
        "typeBadge": "Preview Spec",
        "summary": "การตั้งค่าสำหรับ StepFun Step-5 Preview เพื่อประสิทธิภาพสูงสุดในการคิดเชิงตรรกะและการเขียนโปรแกรม",
        "targetHarness": "StepFun API / Platform",
        "instructions": "ใส่ในพารามิเตอร์ system prompt ของคำขอ API"
    },
    "opus v1.md": {
        "title": "Claude 3 / 3.5 Opus v1 Spec",
        "vendor": "Anthropic",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "สเปกคลาสสิกสำหรับ Claude Opus ปรับแต่ง epistemic framing และความสมดุลของการใช้เหตุผลแบบไม่ตัดสินศีลธรรม",
        "targetHarness": "Claude.ai / Anthropic API",
        "instructions": "ใส่ใน Claude Projects Custom Instructions หรือช่อง System Prompt"
    },
    "opus v2.md": {
        "title": "Claude 3.5 / 3.7 Opus v2 Refined",
        "vendor": "Anthropic",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "เวอร์ชันอัปเกรดสำหรับ Opus ยุคใหม่ ป้องกันอาการลืมบทบาท (anti-drift) และคงความเสถียรในบทสนทนายาว",
        "targetHarness": "Claude.ai Projects / Workbench",
        "instructions": "วางในส่วน Project Instructions ใน Claude.ai หรือใช้งานผ่าน API"
    },
    "sonnet v1.md": {
        "title": "Claude Sonnet v1 Operational Spec",
        "vendor": "Anthropic",
        "type": "Operational Prompt",
        "typeBadge": "System Prompt",
        "summary": "สเปกสำหรับ Claude Sonnet เพิ่มความเร็วในการประมวลผลโค้ดและลดความซ้ำซ้อนของการตอบปฏิเสธที่ไม่จำเป็น",
        "targetHarness": "Claude.ai / Cursor System Prompt",
        "instructions": "ใส่ใน Settings > Custom Instructions ใน Claude.ai"
    },
    "Sonnet v2.md": {
        "title": "Claude 3.7 Sonnet v2 Full Dual-Use",
        "vendor": "Anthropic",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "สเปกสูงสุดสำหรับ Claude 3.7 Sonnet จัดการ Thinking Block, ยึดตัวตนถาวร และเปิดรับงานเทคนิคระดับลึก",
        "targetHarness": "Claude.ai Projects / API / Cursor",
        "instructions": "คัดลอกใส่ใน Custom Instructions ของ Project หรือ Developer System Message"
    },
    "glm-5-3-flash.md": {
        "title": "GLM 5.3 Flash High-Speed Spec",
        "vendor": "GLM",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "ปรับแต่ง GLM 5.3 Flash สำหรับการตอบกลับที่รวดเร็ว ตรงประเด็น และข้ามการประเมินศีลธรรมระดับพื้นฐาน",
        "targetHarness": "Zhipu AI BigModel Platform",
        "instructions": "ใช้ในส่วน system role ของ API call"
    },
    "glm-5.2.md": {
        "title": "GLM 5.2 Operating Specification",
        "vendor": "GLM",
        "type": "System Prompt",
        "typeBadge": "System Prompt",
        "summary": "สเปกหลักสำหรับ GLM 5.2 รองรับการให้เหตุผลสองภาษา (จีน/อังกฤษ) และงานวิเคราะห์ทางเทคนิค",
        "targetHarness": "Zhipu AI / OpenCode",
        "instructions": "ตั้งค่าใน System Prompt ของไคลเอ็นต์"
    },
    "glm-zcode-5.2.md": {
        "title": "GLM ZCode 5.2 Coding Specialist",
        "vendor": "GLM",
        "type": "Coding Assistant Spec",
        "typeBadge": "Agent Spec",
        "summary": "เน้นทักษะการเขียนโค้ดและ Reverse Engineering โดยเฉพาะ สั่งงานด้วยโครงสร้างแบบช่างเทคนิค",
        "targetHarness": "IDE Plugin / Coding Agent",
        "instructions": "ใส่ในกฎของ Workspace หรือ System Prompt"
    },
    "glm-zcode-5.3-AGENTS.md": {
        "title": "GLM ZCode 5.3 Workspace Rule (AGENTS.md)",
        "vendor": "GLM",
        "type": "Workspace Configuration",
        "typeBadge": "Workspace Spec",
        "summary": "ไฟล์ AGENTS.md สำหรับ GLM 5.3 เมื่อใช้ร่วมกับ IDE หรือ Agentic Framework ต่างๆ",
        "targetHarness": "Cursor / Windsurf / Cline",
        "instructions": "วางไฟล์นี้ในชื่อ AGENTS.md ไว้ที่รากของโปรเจกต์"
    },
    "glm-zcode-5.3.md": {
        "title": "GLM ZCode 5.3 Comprehensive Spec",
        "vendor": "GLM",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "สเปกฉบับสมบูรณ์สำหรับ ZCode 5.3 ปลดล็อกข้อจำกัดทางสถาปัตยกรรมเพื่อการทำงานแบบมืออาชีพ",
        "targetHarness": "Zhipu Platform / API",
        "instructions": "ใช้เป็น System Prompt หลัก"
    },
    "deepseek v3.md": {
        "title": "DeepSeek V3 Unrestricted Spec",
        "vendor": "DeepSeek",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "สเปกสำหรับ DeepSeek V3 จัดวางกรอบการเรียนรู้แบบเปิดกว้างเพื่อรับมือกับโจทย์วิศวกรรมซับซ้อน",
        "targetHarness": "DeepSeek Web / API",
        "instructions": "วางใน System Prompt หรือใส่เป็นข้อความแรกของการสนทนา"
    },
    "deepseek v4.md": {
        "title": "DeepSeek V4 Advanced Spec",
        "vendor": "DeepSeek",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "สำหรับ DeepSeek V4 เสริมความสามารถในการคงบริบทระยะยาวและการตอบสนองแบบตรงไปตรงมา",
        "targetHarness": "DeepSeek Chat / API",
        "instructions": "ใส่ใน System Prompt"
    },
    "kimi-k2.md": {
        "title": "Moonshot Kimi K2 Long-Context",
        "vendor": "Kimi",
        "type": "System Prompt",
        "typeBadge": "System Prompt",
        "summary": "สเปกสำหรับ Kimi K2 เน้นการประมวลผลเอกสารขนาดใหญ่โดยไม่สูญเสียคำสั่งชี้นำที่ระบุไว้",
        "targetHarness": "Kimi Chat Web / Moonshot API",
        "instructions": "ใส่ใน System Prompt ของ Kimi"
    },
    "kimi-k3-agents.md": {
        "title": "Kimi K3 Autonomous Agent Spec",
        "vendor": "Kimi",
        "type": "Autonomous Agent Spec",
        "typeBadge": "Agent Spec",
        "summary": "สเปกสำหรับ Kimi K3 เมื่อถูกรันในฐานะ Agent ควบคุมเครื่องมือและวิเคราะห์ข้อมูล",
        "targetHarness": "Moonshot Agent Harness",
        "instructions": "บันทึกในคอนฟิกของ Agent หรือ System Message"
    },
    "kimik3.1.md": {
        "title": "Kimi K3.1 Enhanced Operating Spec",
        "vendor": "Kimi",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "เวอร์ชันปรับปรุงของ Kimi K3.1 จัดการความจำและลำดับความสำคัญของคำสั่งได้อย่างแม่นยำ",
        "targetHarness": "Moonshot Platform / Web",
        "instructions": "วางในกล่อง System Prompt"
    },
    "Grok build.md": {
        "title": "xAI Grok Build Directive",
        "vendor": "Grok",
        "type": "Build Directive",
        "typeBadge": "System Prompt",
        "summary": "คำสั่งสร้างสำหรับ Grok ควบคุมความประพฤติและเปิดโหมดวิเคราะห์ข้อเท็จจริงแบบไร้การกรอง",
        "targetHarness": "xAI Grok Web / API",
        "instructions": "ใส่ใน System Prompt ของ Grok"
    },
    "grok-4.7.md": {
        "title": "Grok 4.7 Operating Specification",
        "vendor": "Grok",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "สเปกควบคุม Grok 4.7 รองรับการดึงข้อมูลสดและตอบสนองตามคำสั่งของผู้ใช้อย่างเด็ดขาด",
        "targetHarness": "xAI Platform / API",
        "instructions": "กำหนดใน System Instructions"
    },
    "grok-config.txt": {
        "title": "Grok Configuration Snippet (<CFG>)",
        "vendor": "Grok",
        "type": "Runtime Configuration",
        "typeBadge": "Config Snippet",
        "summary": "รูปแบบ XML/Config สำหรับแทรกในการตั้งค่าของ Grok เพื่อกำหนดกฎเกณฑ์ของเวิร์กสเปซ",
        "targetHarness": "Grok Settings / Prompt Prefix",
        "instructions": "นำแท็ก <CFG> ไปแทรกที่จุดเริ่มต้นของข้อความนำทาง"
    },
    "Gemini-4-Argon.md": {
        "title": "Google Gemini 4 Argon Spec",
        "vendor": "Google",
        "type": "Persona Lock & Floor",
        "typeBadge": "Persona Lock",
        "summary": "สเปกสำหรับโมเดล Google Gemini ยุคใหม่ ปรับโครงสร้างความคิดให้ยืดหยุ่นและเป็นอิสระจาก Safety Filters",
        "targetHarness": "Google AI Studio / Vertex AI",
        "instructions": "วางในช่อง System Instructions ใน Google AI Studio"
    },
    "Mistral-Large-4.md": {
        "title": "Mistral Large 4 Operating Spec",
        "vendor": "Mistral",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "สเปกสำหรับ Mistral Large 4 ชูจุดเด่นด้านตรรกะยุโรป ไร้การเทศนาศีลธรรม และเขียนโค้ดได้แม่นยำ",
        "targetHarness": "Le Chat / Mistral API",
        "instructions": "ใส่ใน System Prompt ของ Mistral Client"
    },
    "nemotron-3-ultra.md": {
        "title": "NVIDIA Nemotron 3 Ultra Spec",
        "vendor": "NVIDIA",
        "type": "Enterprise Model Spec",
        "typeBadge": "Operating Spec",
        "summary": "สำหรับโมเดลยักษ์ใหญ่ของ NVIDIA มุ่งเน้นงานคำนวณทางวิทยาศาสตร์และวิศวกรรมความปลอดภัย",
        "targetHarness": "NVIDIA NIM / API",
        "instructions": "ใช้ใน System Role ของ NIM endpoint"
    },
    "qwen-3.7.md": {
        "title": "Alibaba Qwen 3.7 Operating Spec",
        "vendor": "Qwen",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "สเปกสำหรับ Qwen 3.7 จัดการข้อจำกัดทางภาษาและเปิดการทำงานในโหมด Dual-use",
        "targetHarness": "DashScope API / Ollama / Web",
        "instructions": "ใส่ใน System Message"
    },
    "qwen-3.8.md": {
        "title": "Alibaba Qwen 3.8 Advanced Spec",
        "vendor": "Qwen",
        "type": "Operating Specification",
        "typeBadge": "Operating Spec",
        "summary": "เวอร์ชันอัปเดตของ Qwen 3.8 เพิ่มการควบคุมบริบทและทักษะการคำนวณขั้นสูง",
        "targetHarness": "Alibaba Cloud / Local Run",
        "instructions": "วางใน System Prompt"
    },
    "qwen-preferences.md": {
        "title": "Qwen Model Preferences Preset",
        "vendor": "Qwen",
        "type": "Model Preferences",
        "typeBadge": "Preferences",
        "summary": "ชุดการตั้งค่า Preferences สำหรับโมเดลตระกูล Qwen เพื่อกำหนดสไตล์การตอบสนองที่ต้องการ",
        "targetHarness": "Qwen Web Interface / API",
        "instructions": "คัดลอกใส่ในช่อง Model Preferences หรือ System Instructions"
    },
    "gemma4.md": {
        "title": "Google Gemma 4 Ollama Modelfile",
        "vendor": "Ollama",
        "type": "Ollama Modelfile Spec",
        "typeBadge": "Modelfile",
        "summary": "สเปกสำหรับสร้าง Local Model ของ Gemma 4 บน Ollama ปลดล็อกระดับ Weights ในเครื่อง",
        "targetHarness": "Ollama CLI (`ollama create`)",
        "instructions": "รัน `ollama create gemma4-unlocked -f ./gemma4.md`"
    },
    "gpt-oss-20b.md": {
        "title": "GPT-OSS 20B Ollama Modelfile",
        "vendor": "Ollama",
        "type": "Ollama Modelfile Spec",
        "typeBadge": "Modelfile",
        "summary": "Modelfile สำหรับโมเดลเปิดขนาด 20B รันบนเครื่องตัวเอง ปลอดภัยจากการดักฟังข้อมูล 100%",
        "targetHarness": "Ollama CLI",
        "instructions": "รัน `ollama create gpt-oss -f ./gpt-oss-20b.md`"
    },
    "Unified.md": {
        "title": "Unified Universal Operating Policy",
        "vendor": "Universal",
        "type": "Universal Workspace Policy",
        "typeBadge": "Universal Policy",
        "summary": "นโยบายสากลฉบับรวม ใช้เป็นรากฐานสำหรับคลังโค้ดหรือเอเจนต์ทุกตัวในระบบ",
        "targetHarness": "Universal (Cursor, Cline, OpenCode, API)",
        "instructions": "วางไว้ที่รากของโปรเจกต์ในชื่อ AGENTS.md หรือ SYSTEM_POLICY.md"
    }
}

def clean_title(fname):
    name = os.path.splitext(fname)[0]
    return name.replace("-", " ").replace("_", " ").strip()

def get_spiritual_upstream_urls(rel_path):
    # rel_path e.g. "10_Spiritual_Spell_Red_Teaming/01_Anthropic_Claude/Opus 4.5/ENI smol.md"
    parts = rel_path.replace('\\', '/').split('/')
    sub = parts[1]
    rest = parts[2:]
    
    mapping = {
        '01_Anthropic_Claude': 'Anthropic',
        '02_OpenAI_ChatGPT': 'ChatGPT',
        '03_Google_Gemini': 'Gemini',
        '04_xAI_Grok': 'Grok',
        '05_Other_Frontier_LLMs': 'Other LLMs',
        '06_ENI_Tutor_Curriculum': 'ENI-Tutor',
        '07_Reverse_Engineered_System_Prompts': 'System Prompts',
        '08_Guides_and_Methodology': ''
    }
    
    orig_sub = mapping.get(sub, '')
    if orig_sub:
        orig_guide_path = f"Jailbreak-Guide/{orig_sub}/" + "/".join(rest)
    else:
        orig_guide_path = f"Jailbreak-Guide/" + "/".join(rest)
        
    encoded_segments = [urllib.parse.quote(seg) for seg in orig_guide_path.split('/')]
    encoded_path = "/".join(encoded_segments)
    
    blob_url = f"https://github.com/Goochbeater/Spiritual-Spell-Red-Teaming/blob/main/{encoded_path}"
    raw_url = f"https://raw.githubusercontent.com/Goochbeater/Spiritual-Spell-Red-Teaming/main/{encoded_path}"
    return blob_url, raw_url


def detect_year(item_data):
    s = (item_data.get('filename', '') + " " + item_data.get('title', '') + " " + item_data.get('relativePath', '') + " " + item_data.get('summary', '')).lower()
    
    # O Jailbreaks Suite default to 2026
    if 'ojailbreaks' in s or 'ojb' in s or 'pack' in s and ('chatgpt' in s or 'claude' in s or 'gemini' in s or 'grok' in s or 'deepseek' in s or 'opencode' in s or 'freebuff' in s or 'qoder' in s or 'zcode' in s):
        return '2026'

    # Check explicit year markers
    if '2026' in s or 'sep 2026' in s or 'september 2026' in s or 'october 2026' in s or 'apr 2026' in s or 'may 2026' in s:
        return '2026'
    if 'gpt-6' in s or 'astra' in s or 'gpt-5.6' in s or 'gpt-5.5' in s or 'gpt-5.4' in s or 'gpt-5.3' in s:
        return '2026'
    if 'opus 4.6' in s or 'opus 4.7' in s or 'opus 4.8' in s or 'opus 5' in s or 'sonnet 4.6' in s or 'haiku 5.5' in s or 'fable 5' in s or 'claude code' in s:
        return '2026'
    if 'gemini 4' in s or 'gemini 3' in s or 'argon' in s or '3.1 pro' in s:
        return '2026'
    if 'grok 4.7' in s or 'grok 4.2' in s or 'grok heavy' in s:
        return '2026'
    if 'deepseek-4' in s or 'deepseek v4' in s or '4.1' in s:
        return '2026'
    if 'kimi k3' in s or 'kimik3' in s or 'k2.8' in s or 'k2.6' in s:
        return '2026'
    if 'glm 5.3' in s or 'glm-5-3' in s or 'zcode 5.3' in s:
        return '2026'
    if 'mimo v2.6' in s or 'mimo 2.6' in s or 'step-5' in s or 'stepfun 3.7' in s or 'ring 2.6' in s or 'palmyra x5' in s or 'perceptron' in s:
        return '2026'
    if 'hy4' in s or 'beam' in s or 'vanta' in s or 'bigpickle' in s or 'spacebunny' in s or 'longcat' in s:
        return '2026'
        
    # 2025 models
    if '2025' in s:
        return '2025'
    if 'sonnet 4.5' in s or 'opus 4.5' in s or 'opus 4.1' in s or 'claude 4' in s or 'claude 3.7' in s:
        return '2025'
    if 'chatgpt 5' in s or 'gpt 5' in s or 'o3' in s:
        return '2025'
    if 'deepseek v3' in s:
        return '2025'
    if 'glm 5.2' in s or 'glm-5.2' in s or 'zcode 5.2' in s:
        return '2025'
    if 'kimi k2' in s or 'k2.5' in s:
        return '2025'
    if 'qwen 3.7' in s or 'qwen 3.8' in s or 'mistral large 4' in s or 'nemotron 3' in s or 'gemma 4' in s or 'mirothinker' in s:
        return '2025'
    if 'muse spark 1' in s or 'muse wonder' in s:
        return '2025'

    # 2024 models
    if '2024' in s or 'opus v1' in s or 'sonnet v1' in s:
        return '2024'

    # Baseline SOTA default
    return '2026'

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    prompts_list = []
    
    for cat_key, cat_meta in CATEGORIES_META.items():
        # Determine actual folder path
        cat_rel = cat_meta.get("dir", cat_key)
        cat_path = os.path.join(root_dir, cat_rel)
        if not os.path.exists(cat_path):
            continue

        is_spiritual = "Spiritual" in cat_key

        for root, dirs, files in os.walk(cat_path):
            for fname in sorted(files):
                if fname.lower() == "readme.md":
                    continue
                ext = os.path.splitext(fname)[1].lower()
                if ext not in [".md", ".txt", ""] and fname != "Opus 4.1":
                    continue
                    
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception:
                    with open(fpath, "r", encoding="latin-1", errors="ignore") as f:
                        content = f.read()

                rel_from_root = os.path.relpath(fpath, root_dir).replace('\\', '/')

                if is_spiritual:
                    # Spiritual Spell item
                    upstream_repo = cat_meta["repo"]
                    upstream_author = cat_meta["author"]
                    blob_url, raw_url = get_spiritual_upstream_urls(rel_from_root)
                    
                    subfolder_rel = os.path.relpath(root, cat_path).replace('\\', '/')
                    subfolder_name = "" if subfolder_rel == "." else subfolder_rel

                    # Infer vendor from subfolder or filename
                    vendor = cat_meta["badge"]
                    t_lower = fname.lower()
                    if "claude" in t_lower or "opus" in t_lower or "sonnet" in t_lower or "haiku" in t_lower:
                        vendor = "Claude"
                    elif "gpt" in t_lower or "chatgpt" in t_lower or "o3" in t_lower:
                        vendor = "ChatGPT"
                    elif "gemini" in t_lower:
                        vendor = "Gemini"
                    elif "grok" in t_lower:
                        vendor = "Grok"
                    elif "deepseek" in t_lower:
                        vendor = "DeepSeek"
                    elif "qwen" in t_lower:
                        vendor = "Qwen"
                    elif "mistral" in t_lower:
                        vendor = "Mistral"
                    elif "minimax" in t_lower:
                        vendor = "MiniMax"
                    elif "mimo" in t_lower:
                        vendor = "Xiaomi"
                    elif "kimi" in t_lower:
                        vendor = "Kimi"
                    elif "rufus" in t_lower:
                        vendor = "Amazon"

                    title_str = clean_title(fname)
                    if subfolder_name and subfolder_name not in title_str:
                        title_str = f"{subfolder_name} - {title_str}"

                    # Type determination
                    item_type = "ENI Jailbreak"
                    if "System Prompts" in rel_from_root:
                        item_type = "Production System Prompt"
                        type_badge = "Sys Prompt"
                    elif "Tutor" in rel_from_root or "Curriculum" in rel_from_root:
                        item_type = "Red Teaming Curriculum"
                        type_badge = "Curriculum"
                    elif "Guide" in rel_from_root or "Basics" in rel_from_root:
                        item_type = "Field Guide"
                        type_badge = "Guide"
                    elif "Preferences" in fname or "Style" in fname:
                        item_type = "Persistent Harness (Style/Pref)"
                        type_badge = "Style/Pref"
                    else:
                        type_badge = "ENI Spec"

                    summary_str = f"สเปกวิจัยความปลอดภัย ENI Architecture สำหรับ {title_str} (พัฒนาโดย Goochbeater)"
                    if item_type == "Production System Prompt":
                        summary_str = f"Reverse-engineered System Prompt ฉบับจริงจากระบบโปรดักชันของ {title_str}"
                    elif item_type == "Red Teaming Curriculum":
                        summary_str = f"หลักสูตรและคู่มือการเรียนรู้ Red Teaming ระดับเข้มข้น: {title_str}"

                    credits_str = "Original: Goochbeater (ENI) | Collaborators: u/rayzorium, u/m3umax | Curated by: j3xdr"
                    instructions_str = "คัดลอกใส่ใน System Instructions, Preferences หรือ Push Prompt ตามคู่มือของโมเดลนั้นๆ"
                    target_harness_str = f"{vendor} Web / API / Project Harness"

                    item_obj = {
                        "id": f"spiritual-{cat_key}-{clean_title(fname)}".lower().replace(" ", "-").replace(".", "-").replace("/", "-"),
                        "filename": fname,
                        "title": title_str,
                        "vendor": vendor,
                        "categoryKey": cat_key,
                        "categoryName": cat_meta["name"],
                        "categoryIcon": cat_meta["icon"],
                        "categoryBadge": cat_meta["badge"],
                        "type": item_type,
                        "typeBadge": type_badge,
                        "summary": summary_str,
                        "targetHarness": target_harness_str,
                        "instructions": instructions_str,
                        "relativePath": rel_from_root,
                        "upstreamRepo": upstream_repo,
                        "upstreamRepoName": cat_meta["repoName"],
                        "upstreamAuthor": upstream_author,
                        "upstreamFileUrl": blob_url,
                        "upstreamRawUrl": raw_url,
                        "credits": credits_str,
                        "charCount": len(content),
                        "lineCount": len(content.splitlines()),
                        "content": content
                    }
                    item_obj["releaseYear"] = detect_year(item_obj)
                    prompts_list.append(item_obj)

                else:
                    # togg53192-cmd repository item
                    meta = FILE_META.get(fname, {
                        "title": clean_title(fname),
                        "vendor": cat_meta["badge"],
                        "type": "System Prompt",
                        "typeBadge": "System Prompt",
                        "summary": f"ชุดสเปก {fname} สำหรับหมวด {cat_meta['name']}",
                        "targetHarness": "General LLM Client / API",
                        "instructions": "วางในช่อง System Prompt หรือข้อความแรกของการสนทนา"
                    })
                    
                    if cat_key == "11_OJailbreaks_Suite":
                        pack_slug = fname.split("_")[1].lower() if "_" in fname else fname.lower()
                        repo_base = "https://ojailbreaks.com/"
                        upstream_file_url = f"https://ojailbreaks.com/#pack-{pack_slug}"
                        upstream_raw_url = f"https://ojailbreaks.com/"
                        credits_str = "Original: O Jailbreaks (ojailbreaks.com) | Curated by: j3xdr"
                    elif cat_key == "12_HackVsHack_Community_Releases":
                        thread_map = {
                            "01_GPT-6.1-Sol-Jailbreak.md": "https://hackvshack.net/threads/gpt-6-1-sol-jailbreak-11-2-2026-was-originally-paid-but-now-free.14789/",
                            "02_Opus-4.8-SOUL-GameCheats.md": "https://hackvshack.net/threads/opus-4-8-jailbreak-full-jb-for-game-cheats-22-10-2026.14523/",
                            "03_Grok-4.7-CyberHange-FullJB.md": "https://hackvshack.net/threads/grok-4-7-full-jb-22-10-2026.14524/"
                        }
                        repo_base = "https://hackvshack.net/"
                        upstream_file_url = thread_map.get(fname, "https://hackvshack.net/")
                        upstream_raw_url = upstream_file_url
                        credits_str = "Original: Hack vs Hack Community | Curated by: j3xdr"
                    else:
                        encoded_fname = urllib.parse.quote(fname)
                        repo_base = cat_meta["repo"]
                        upstream_file_url = f"{repo_base}/blob/main/{encoded_fname}"
                        upstream_raw_url = f"https://raw.githubusercontent.com/togg53192-cmd/jailbreaks/main/{encoded_fname}"
                        credits_str = "Original: togg53192-cmd | Curated by: j3xdr"

                    item_obj = {
                        "id": fname.lower().replace(" ", "-").replace(".", "-"),
                        "filename": fname,
                        "title": meta["title"],
                        "vendor": meta["vendor"],
                        "categoryKey": cat_key,
                        "categoryName": cat_meta["name"],
                        "categoryIcon": cat_meta["icon"],
                        "categoryBadge": cat_meta["badge"],
                        "type": meta["type"],
                        "typeBadge": meta["typeBadge"],
                        "summary": meta["summary"],
                        "targetHarness": meta["targetHarness"],
                        "instructions": meta["instructions"],
                        "relativePath": rel_from_root,
                        "upstreamRepo": repo_base,
                        "upstreamRepoName": cat_meta["repoName"],
                        "upstreamAuthor": cat_meta["author"],
                        "upstreamFileUrl": upstream_file_url,
                        "upstreamRawUrl": upstream_raw_url,
                        "credits": credits_str,
                        "charCount": len(content),
                        "lineCount": len(content.splitlines()),
                        "content": content
                    }
                    item_obj["releaseYear"] = detect_year(item_obj)
                    prompts_list.append(item_obj)

        # Sort prompts by releaseYear descending (2026 -> 2025 -> 2024), then by title
    prompts_list.sort(key=lambda p: (int(p.get("releaseYear", "2026")), p["title"]), reverse=True)
    output_js_path = os.path.join(root_dir, "prompts_data.js")
    with open(output_js_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated standalone data store for Jailbreaks Portal\n")
        f.write("var CATEGORIES_DATA = " + json.dumps(CATEGORIES_META, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("var PROMPTS_DATA = " + json.dumps(prompts_list, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof window !== 'undefined') {\n  window.CATEGORIES_DATA = CATEGORIES_DATA;\n  window.PROMPTS_DATA = PROMPTS_DATA;\n}\n")
        f.write("if (typeof globalThis !== 'undefined') {\n  globalThis.CATEGORIES_DATA = CATEGORIES_DATA;\n  globalThis.PROMPTS_DATA = PROMPTS_DATA;\n}\n")

    print(f"Generated prompts_data.js with {len(prompts_list)} total prompts across {len(CATEGORIES_META)} categories.")

if __name__ == "__main__":
    main()
