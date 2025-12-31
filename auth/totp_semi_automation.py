"""
Semi-automated authentication using an authenticator app.

Flow:
1. Generate TOTP secret (run once)
2. Enable TOTP on account (run once)
3. Login using TOTP (manual entry)

Best suited for:
- Individual traders
- Desktop / VPS setups
- Faster & more reliable than SMS OTP
"""

from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv

# =====================================================
# STEP 1: Generate TOTP Secret (RUN ONCE)
# =====================================================
nubra = InitNubraSdk(env=NubraEnv.PROD)

secret = nubra.totp_generate_secret()
print("\n TOTP Secret Generated:")
print(secret)
print(
    "\nAdd this secret to an authenticator app "
    "(Google Authenticator, Authy, 1Password).\n"
)

# =====================================================
# STEP 2: Enable TOTP on Account (RUN ONCE)
# =====================================================
print("➡️ Enabling TOTP on your Nubra account...")
nubra.totp_enable()
print("✅ TOTP enabled successfully\n")

# =====================================================
# STEP 3: Login using TOTP (NORMAL LOGIN FLOW)
# =====================================================
# During this step, the SDK will prompt for:
# - 6-digit TOTP from your authenticator app
# - MPIN (auto-loaded from .env if env_creds=True)

nubra = InitNubraSdk(
    env=NubraEnv.PROD,
    totp_login=True,
    env_creds=True
)

print("✅ Login successful (manual TOTP)")
