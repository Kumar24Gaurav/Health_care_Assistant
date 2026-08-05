import inspect
import streamlit as st
from chatbot import generate_response

# -----------------------------------------------------------------------------
# 1. Page Config & Custom Styling (Crimson Night Inspired Theme)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Medical AI Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern dark UI with crimson accents
st.markdown("""
<style>
    /* Dark Theme Base */
    .stApp {
        background-color: #0D1117;
        color: #E6EDF3;
    }

    /* Header Styling */
    .title-text {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF4B4B, #9E0031);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .subtitle-text {
        color: #8B949E;
        font-size: 0.95rem;
        margin-bottom: 20px;
    }

    /* Disclaimer Box */
    .disclaimer-card {
        background: rgba(255, 75, 75, 0.08);
        border-left: 4px solid #FF4B4B;
        padding: 12px 15px;
        border-radius: 6px;
        color: #F85149;
        font-size: 0.85rem;
        margin-bottom: 15px;
    }

    /* Modern Chat Bubble Enhancements */
    .stChatMessage {
        border-radius: 12px;
        padding: 10px 14px;
        margin-bottom: 10px;
    }

    /* Customizing Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }

    /* Quick Prompt Buttons */
    div.stButton > button {
        border-radius: 8px;
        border: 1px solid #30363D;
        background-color: #21262D;
        color: #C9D1D9;
        text-align: left;
        padding: 10px;
        font-size: 0.85rem;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        border-color: #FF4B4B;
        color: #FF4B4B;
        background-color: #161B22;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Helper Functions
# -----------------------------------------------------------------------------
def safe_generate_response(prompt, history):
    """
    Dynamically calls generate_response whether chatbot.py expects:
    1 argument:  generate_response(prompt)
    2 arguments: generate_response(prompt, history)
    """
    sig = inspect.signature(generate_response)
    if len(sig.parameters) >= 2:
        return generate_response(prompt, history)
    return generate_response(prompt)

# -----------------------------------------------------------------------------
# 3. Sidebar (Medical Disclaimer & Tools)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🩺 Medical AI")
    st.markdown("Your intelligent health companion.")
    
    st.markdown("---")
    
    # Emergency & Disclaimer Badge
    st.markdown("""
    <div class="disclaimer-card">
        <strong>⚠️ Disclaimer:</strong><br>
        This AI provides general health information only and is not a substitute for professional medical advice, diagnosis, or treatment.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💡 Sample Prompts")
    
    # Quick starter questions
    sample_prompts = [
        "What are common remedies for a mild headache?",
        "How do I improve my sleep hygiene?",
        "What are the symptoms of seasonal allergies?",
        "When should I consult a doctor for a fever?"
    ]
    
    for prompt in sample_prompts:
        if st.button(prompt, key=prompt):
            st.session_state.pending_prompt = prompt

    st.markdown("---")

    # Clear Chat Button
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -----------------------------------------------------------------------------
# 4. Main Chat Interface
# -----------------------------------------------------------------------------
st.markdown('<p class="title-text">Medical AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Ask health questions, understand symptoms, or explore wellness guidance.</p>', unsafe_allow_html=True)

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Medical AI Assistant. How can I help you with your health questions today?"}
    ]

# Display existing messages
for message in st.session_state.messages:
    avatar = "🩺" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# Process input from text box OR quick prompt buttons
prompt_input = st.chat_input("Type your medical question here...")

if "pending_prompt" in st.session_state and st.session_state.pending_prompt:
    prompt_input = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if prompt_input:
    # 1. Display User Message
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user", avatar="👤"):
        st.write(prompt_input)

    # 2. Pass the prior conversation history to the backend in the shape it expects
    formatted_history = st.session_state.messages[:-1]

    # 3. Generate Assistant Response
    with st.chat_message("assistant", avatar="🩺"):
        with st.spinner("Analyzing medical context..."):
            try:
                response = safe_generate_response(prompt_input, formatted_history)
            except Exception as e:
                response = f"An error occurred while generating the response: {str(e)}"
            
            st.write(response)

    # 4. Save response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})