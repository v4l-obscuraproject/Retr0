# Obscura / Retr0 Awareness Simulator

An open-source, text-based terminal awareness tool designed to educate users on social engineering risks, phishing simulation vectors, and the hidden dangers of downloading untrusted executables from platforms like Discord or random public forums.

---

##  Authors & Credits
* **5h9q_** - Lead Developer (Discord)

##  License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

##  How It Works
1. **The Interface:** The simulation spins up a Terminal User Interface (TUI) masquerading as a collection of modular auditing utility scripts (Volumetric tests, Wireless auditing, etc.).
2. **The Education Phase:** When any option is executed, the simulation triggers a simulated initialization error and redirects the analyst to a hosted documentation interface (`index.html`).
3. **The Lesson:** The target interface uses *fsociety* branding assets to illustrate how authentic remote access tools (RATs) or weaponized public scripts use deceptive interfaces to trick operators into damaging their own environments.

---

##  Repository Layout
Ensure your workspace matches the layout below so relative image pathing works correctly:

```text
Obscura/
│
├── awareness_tool.py   # Primary TUI Menu Script
├── index.html          # Web-based Portal Interface
└── static/
    └── fsociety.png    # Portal Visual Asset
```

---



##  Disclaimer
This simulator does not contain any weaponized payload, functional network exploitation capabilities, or malware automation engines. It is an entirely static text engine built purely for authorized security training, capture-the-flag (CTF) environments, and defensive cybersecurity awareness exercises.
