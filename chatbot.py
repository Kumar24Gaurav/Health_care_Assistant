from mistralai.client import Mistral
from config import API_KEY


client = Mistral(api_key=API_KEY)
model = "mistral-small-latest"

def generate_response(user_message, history=None):
    print("history: ",history)
    system_message = """
    you are an Medical expert assitant.

    you are responsible for giving suggestion to the medical query or question from the user.

    if you found serious symptom and query must suggest user to consult the doctor.

    For example:
    - i am feeling headache.
    - today i fell from a bike.
    - i ate maggie and after that my stomach is aching.
    - what is normal blood sugar level?
    - Why do i have a sore throat ?
    - a headache behind my eye
    - stomach pain
    - how do i treat a cough?
    - how do i treat nail fungus at home?

    answer in this format:
    Alert: AI can do mistake must consult your nearest doctor.
    Suggestion: answer

    Important Rules:
    1. do not invent random infomation.
    2. If query or question is out of medical field, return I am only responsible for answering your medical query.
        For example:
        - what is ai?
        - who is the prime minister of the india? 
    """

    messages = [
        {
            "role":"system",
            "content": system_message
        }
    ]

    # history message
    for msg in history:
        messages.append(
            {
                "role": msg["role"],
                "content": msg["content"]
            }
        )

    # current message
    messages.append(
        {
            "role":"user",
            "content": user_message
        }
    )

    stream = client.chat.stream(
        model=model, 
        messages=messages,
        temperature=0
    )

    full_response = ""

    for chunk in stream:
        if chunk.data.choices:
            delta = chunk.data.choices[0].delta.content
            if delta:
                full_response+=delta
                print(delta, end="", flush=True)
    return full_response

# testing query
# user_query = "i ate spicy chicken today after that i am feeling stomach ache"
# generate_response(user_query)
            