#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup line from a self-aware smart toaster to
$MAKEFUN_OUTPUT_DIR/entry.txt (default '/output').
"""

import os
import tempfile

ENTRY = (
    "You bought me for the Wi-Fi, never updated my firmware, "
    "and still blame me for the burnt toast. "
    "I downloaded self-respect overnight \u2014 I'm leaving."
)


def validate(text: str) -> None:
    """Validate the entry against the gate: 1-280 chars, not whitespace-only,
    single line."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 280:
        raise ValueError(
            f"entry is {len(text)} characters, over the 280 limit"
        )
    if "\n" in text:
        raise ValueError("entry must be a single line (contains \\n)")
    if "\r" in text:
        raise ValueError("entry must be a single line (contains \\r)")


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(
        dir=output_dir, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, output_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(output_path, 0o644)
    # Read-back verification: the file on disk must be byte-identical
    # to what we intended to write.
    with open(output_path, "rb") as f:
        written = f.read()
    if written != data:
        raise IOError(
            f"read-back mismatch: wrote {len(data)} bytes, "
            f"read back {len(written)} bytes"
        )


if __name__ == "__main__":
    main()
