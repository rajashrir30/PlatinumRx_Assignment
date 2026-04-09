def convert_minutes(total_minutes: int) -> str:
    """Convert minutes into a human-readable hours/minutes string."""
    if not isinstance(total_minutes, int):
        raise TypeError("total_minutes must be an integer")
    if total_minutes < 0:
        raise ValueError("total_minutes cannot be negative")

    hours = total_minutes // 60
    minutes = total_minutes % 60

    hours_label = "hr" if hours == 1 else "hrs"
    minutes_label = "minute" if minutes == 1 else "minutes"

    return f"{hours} {hours_label} {minutes} {minutes_label}"


if __name__ == "__main__":
    samples = [130, 110, 59, 60, 0]
    for value in samples:
        print(f"{value} -> {convert_minutes(value)}")
