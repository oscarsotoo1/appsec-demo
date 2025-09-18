import hashlib

def mask_secret(s: str | None) -> str:
    if not s:
        return "<none>"
    return f"<masked:{s[:2]}...{s[-2:]}>"

def short_ref(s: str | None) -> str:
    return hashlib.sha256((s or "").encode()).hexdigest()[:8]
