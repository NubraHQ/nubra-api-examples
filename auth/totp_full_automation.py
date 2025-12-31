"""
Fully automated authentication using TOTP + pyotp.

- No SMS OTP
- No browser redirects
- No human input
- Safe for servers, restarts, and CI/CD

Prerequisites:
- TOTP must already be enabled on the Nubra account
- PHONE_NO, MPIN, and TOTP secret stored securely
"""

from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
import pyotp, builtins, getpass

# --- Your TOTP Secret ---
secret = "YOUR_TOTP_SECRET"
totp_gen = pyotp.TOTP(secret)

# Save originals so they can be restored later if needed
orig_input = builtins.input
orig_getpass = getpass.getpass

# Patch input() and getpass() so Nubra receives fresh TOTP automatically
def auto_totp_input(prompt=""):
    return totp_gen.now()

def auto_totp_getpass(prompt=""):
    return totp_gen.now()

builtins.input = auto_totp_input
getpass.getpass = auto_totp_getpass

# Initialize Nubra with fully automated authentication
nubra = InitNubraSdk(
    env=NubraEnv.PROD,
    totp_login=True,   # Enables TOTP-based authentication
    env_creds=True     # Loads PHONE_NO & MPIN from .env
)

print("✅ Login Successful (TOTP auto-filled)")
