import os
from google import genai
client=genai.Client()

def get_current_time(timezone: str = "Asia/Kolkata") -> dict:
    """Get the real current date and time in a given timezone.

    Args:
        timezone: IANA timezone name, for example "Asia/Kolkata",
            "America/New_York", "Europe/London" or "Asia/Tokyo".

    Returns:
        A dictionary with the date, time and UTC offset, or an error message.
    """
    try:
        now = datetime.now(ZoneInfo(timezone))
    except Exception:
        return {"error": f"Unknown timezone: {timezone}"}

    return {
        "timezone": timezone,
        "date": now.strftime("%A, %d %B %Y"),
        "time": now.strftime("%I:%M:%S %p"),
        "utc_offset": now.strftime("%z"),
    }


response = client.models.generate_content(
    model=MODEL,
    contents="What time is it in Tokyo right now?",
    config=types.GenerateContentConfig(tools=[get_current_time]),
)
print(response.text)

