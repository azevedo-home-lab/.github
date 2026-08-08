<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img src="assets/banner.svg" alt="AZEVEDO-HOME-LAB — personal infrastructure, automation, LoRa" width="100%">
  </picture>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SHELL-0d1117?style=flat-square&logo=gnubash&logoColor=white" alt="Shell">
  <img src="https://img.shields.io/badge/PYTHON-0d1117?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JAVASCRIPT-0d1117?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript">
  <img src="https://img.shields.io/badge/SWIFT-0d1117?style=flat-square&logo=swift&logoColor=white" alt="Swift">
  <img src="https://img.shields.io/badge/ROUTEROS-0d1117?style=flat-square&logo=mikrotik&logoColor=white" alt="RouterOS">
</p>

<p align="center">
  <img src="assets/divider.svg" alt="" width="600">
</p>

<p align="center"><sub>M I S S I O N&nbsp;&nbsp;&nbsp;S Y S T E M S</sub></p>

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"transparent","primaryColor":"#0d1117","primaryTextColor":"#c9d1d9","primaryBorderColor":"#484f58","lineColor":"#6e7681","secondaryColor":"#161b22","tertiaryColor":"#161b22","fontSize":"12px"}}}%%
flowchart LR
    WAN[INTERNET] --> RTR[MIKROTIK ROUTER]
    RTR --> SRV[LAN SERVER<br>SELF-HOSTED SERVICES]
    RTR --> GW[LORA GATEWAY]
    GW -.-> FLD[ESP32 / STM32<br>FIELD DEVICES]
    SRV --> EXT[EXTERNAL APIS<br>DROPBOX / ANTHROPIC]
```

<p align="center">
  <img src="assets/divider.svg" alt="" width="600">
</p>

<p align="center"><sub>M A N I F E S T</sub></p>

| REPOSITORY | LANGUAGE | FUNCTION |
|:---|:---|:---|
| [save-note-api](https://github.com/azevedo-home-lab/save-note-api) | PYTHON | KNOWLEDGE-BASE API — NOTES, TRANSCRIPTION, INSIGHTS |
| [homelab](https://github.com/azevedo-home-lab/homelab) | SHELL | PROXMOX + K3S INFRASTRUCTURE AS CODE |
| [loralab-infra](https://github.com/azevedo-home-lab/loralab-infra) | SHELL | LORAWAN NETWORK — CHIRPSTACK, GATEWAY, VPN |
| [Lab-Infrastructure](https://github.com/azevedo-home-lab/Lab-Infrastructure) | ROUTEROS SCRIPT | MIKROTIK ROUTER CONFIGURATION |
| [claude-code-workflows](https://github.com/azevedo-home-lab/claude-code-workflows) | SHELL | AI DEVELOPMENT WORKFLOWS AND JUDGES |
| [codex-workflows](https://github.com/azevedo-home-lab/codex-workflows) | — | CODEX AGENT WORKFLOWS |
| [privacy-web-search-mcp](https://github.com/azevedo-home-lab/privacy-web-search-mcp) | JAVASCRIPT | PRIVACY-FOCUSED WEB SEARCH MCP SERVER |
| [TokenEater](https://github.com/azevedo-home-lab/TokenEater) | SWIFT | MACOS WIDGET — AI USAGE MONITORING |

<p align="center">
  <img src="assets/divider.svg" alt="" width="600">
</p>

<p align="center"><sub>L A B&nbsp;&nbsp;&nbsp;P R I N C I P L E S</sub></p>

<p align="center">
  Build it yourself. Know every layer.<br>
  Automate what repeats. Record what matters.<br>
  Small machines, precisely instructed.
</p>

<p align="center">
  <img src="assets/divider.svg" alt="" width="600">
</p>

<p align="center"><sub>PERSONAL LABORATORY — NOT A PRODUCT</sub></p>
