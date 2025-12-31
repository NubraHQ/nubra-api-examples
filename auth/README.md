## Authentication Examples (Python)

Authentication is the foundation of every algorithmic trading system.
For an algo to run autonomously on servers, restart safely, or recover
from downtime, the authentication flow must be scriptable, predictable,
and free from manual intervention.

This folder demonstrates all supported Nubra authentication methods,
ordered from **fully automated** to **manual fallback**.

---

## Authentication Modes

### 1️⃣ Fully Automated — TOTP + pyotp (Recommended)

**File:** `totp_full_automation.py`

This method enables **100% hands-free authentication** using a
TOTP secret generated programmatically with `pyotp`.

**Best suited for:**
- Production servers
- Cloud deployments
- CI/CD pipelines
- Fully autonomous algo trading systems

**Characteristics:**
- No SMS OTP
- No browser redirects
- No human input
- Safe for restarts and crashes

---

### 2️⃣ Semi-Automated — Authenticator Apps

**File:** `totp_semi_automation.py`

This method uses an authenticator app (Google Authenticator, Authy,
1Password) to generate TOTP codes.

Only the TOTP entry is manual; all other steps are automated by the SDK.

**Best suited for:**
- Individual traders
- Desktop or VPS setups

**Characteristics:**
- No SMS delays
- One manual step (TOTP entry)
- Faster and more reliable than phone OTP

---

### 3️⃣ Manual — Phone OTP + MPIN (Fallback)

**File:** `phone_otp_mpin.py`

This is the default authentication method using SMS OTP and MPIN.

**Best suited for:**
- First-time login
- Backup / fallback access

**Characteristics:**
- Requires SMS OTP
- Human intervention required
- Not suitable for unattended automation

---

## Environment Variables

The examples expect credentials to be loaded from environment variables
or a `.env` file.

```env
PHONE_NO=9XXXXXXXXX
MPIN=XXXX
NUBRA_TOTP_SECRET=BASE32SECRET   # Required only for full automation
```
---

## Usage

Install dependencies:
pip install pyotp requests


Run an example:
python totp_full_automation.py

For detailed authentication flows and SDK reference, see:
https://nubra.io/products/api/docs/

© 2025 Zanskar Securities Private Limited. All rights reserved.
