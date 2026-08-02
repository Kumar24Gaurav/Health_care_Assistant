import gradio as gr
from chatbot import generate_response

demo = gr.ChatInterface(
    fn=generate_response,
    title="Medical AI Assistant",
    description="Ask medical question. This assistant provides general health information and is not a substitute for professional medical advice.",
    theme = gr.themes.Soft(),
)

demo.launch()