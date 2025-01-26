from __future__ import annotations

def clip(text: str, max_len: int = 80) -> str:
    """Return new ``str`` clipped at last space before or after ``max_len``
    Return full ``text`` if no space found.
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()
