def remove_duplicate_characters(text: str) -> str:
    """Remove duplicate characters while preserving first occurrence order."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        if char not in result:
            result += char
    return result


if __name__ == "__main__":
    samples = [
        "banana",
        "programming",
        "aabbcc",
        "",
        "PlatinumRx",
    ]
    for value in samples:
        print(f"{value!r} -> {remove_duplicate_characters(value)!r}")
