import gradio as gr
from chatbot import generate_response

import gradio as gr

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.ChatInterface(
        fn=generate_response,
        title="Medical AI Assistant",
        description="Ask your medical questions."
    )

demo.launch()