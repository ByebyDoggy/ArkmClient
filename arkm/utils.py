import hashlib


def make_payload(path: str, salt: str, ts: str) -> str:
    """复现 JS 里的两段 sha256 逻辑"""
    step1 = hashlib.sha256(f"{path}:{ts}:{salt}".encode()).hexdigest()
    return hashlib.sha256(f"{salt}:{step1}".encode()).hexdigest()