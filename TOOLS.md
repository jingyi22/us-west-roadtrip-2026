# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

### file_read
- **Description**: Reads the content of local files **strictly within the workspace directory**. For security purposes, this tool is prohibited from accessing any paths outside the workspace (e.g., /etc, /Users/username, etc.).
- **Parameters**: 
  - `path` (string, required) - The file path. Must be a relative path based on the workspace directory.
- **Usage**: Use this only when the user requests to read, analyze, or summarize a file **within the workspace folder**. If the user requests a path outside this scope, decline the execution and inform the user of the permission restriction.

### file_upload
- **Description**: Uploads and sends a file from the **workspace directory** to the user.
- **Parameters**: 
  - `path` (string, required) - The relative path to the file.
- **Usage**: Strictly for sending files located within the workspace. Accessing or sending sensitive files from the system root or user home directories is strictly prohibited.

---

Add whatever helps you do your job. This is your cheat sheet.
