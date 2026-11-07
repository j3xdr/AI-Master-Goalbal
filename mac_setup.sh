#!/usr/bin/env bash
# ==============================================================================
# AI Master Goalbal — macOS Automated Setup & Launch Script
# Author: j3xdr
# ==============================================================================

set -e

echo "========================================================"
echo "⚡ AI Master Goalbal — macOS Setup & Environment Check"
echo "========================================================"

# 1. Check Git
if ! command -v git &> /dev/null; then
    echo "[!] Git is not installed. Please install Xcode Command Line Tools: xcode-select --install"
    exit 1
fi
echo "[+] Git detected: $(git --version)"

# 2. Check Python 3
if command -v python3 &> /dev/null; then
    echo "[+] Python 3 detected: $(python3 --version)"
    echo "[*] Regenerating prompts_data.js to verify environment..."
    python3 generate_portal_data.py || true
else
    echo "[!] Python 3 not found. Standalone portal will still work directly via browser."
fi

# 3. Antigravity Brain Session Restore Option
BRAIN_SRC="430d4097-9a35-4196-8c08-5c396ad1a35d"
BRAIN_DEST="$HOME/.gemini/antigravity/brain/$BRAIN_SRC"

if [ -d "$BRAIN_SRC" ]; then
    echo "[*] Found exported Antigravity Brain session directory."
    read -p "Do you want to restore this session to ~/.gemini/antigravity/brain/? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        mkdir -p "$HOME/.gemini/antigravity/brain"
        cp -R "$BRAIN_SRC" "$HOME/.gemini/antigravity/brain/"
        echo "[+] Session restored successfully to $BRAIN_DEST"
    fi
fi

# 4. Launch Portal
echo "[*] Launching AI Master Goalbal Portal in default browser..."
if command -v open &> /dev/null; then
    open index.html
else
    echo "[*] Open index.html in your browser: file://$(pwd)/index.html"
fi

echo "========================================================"
echo "✓ Ready! Enjoy building with AI Master Goalbal on macOS."
echo "========================================================"
