def add_numbers (a: float, b: float) -> float:
    return a + b
def count_words (text: str) -> int:
    return len (text.split())
def course_info (topic: str) -> str:

    courses={
    "python": "Variables, loops, functions, collections",
    "sql": "SELECT, filtering, joins, transactions",
    "agents": "Prompts, tools, state, control loops"
    }

    return courses.get(topic.lower().strip(), "No course found.")
print (add_numbers (4, 9))
print (count_words ("Gemini can call controlled tools"))
print (course_info("python"))