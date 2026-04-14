# Installation Guide

Follow these steps to prepare your production machine for the Movie Terminal script.

## Prerequisites
- **Python 3.7+**: Ensure Python is installed and added to your system PATH.
- **Modern Terminal**: For the best visual experience (especially background colors), use:
  - **Windows:** Windows Terminal or PowerShell (avoid legacy cmd.exe).
  - **macOS:** iTerm2 or the native Terminal.app.
  - **Linux:** Any modern emulator (Gnome Terminal, Alacritty, etc.).

## Setup Instructions

### 1. Virtual Environment (Recommended)
It is best practice to run this in a virtual environment to keep your system clean.
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate