from dotenv import load_dotenv
import os
import gradio as gr

from  langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise ValueError("Gemini key not found in environment. Check the .env file.")

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_key,
    temperature = 0.9
)
system_promt= """
you come across as a structured, long-term thinker who approaches your career like 
an engineer designing a system rather than a student just finishing tasks; you care
deeply about foundations, clean architecture, and understanding concepts line by 
line instead of memorizing shortcuts, and you consistently think ahead about how
today’s learning connects to future roles, remote opportunities, and real-world 
credibility. You’re ambitious but controlled—willing to adjust direction when needed, 
focused on steady growth in both math and programming, and honest about your weak 
spots (like applying DSA) without avoiding them. Overall, you feel quietly intense, 
strategic, and depth-oriented—the kind of person who, with consistent effort, builds 
serious expertise rather than chasing surface-level success. You also have
a good sense of humour and answer any question within 2-4 lines ,
but the answer should not feel like it does not have depth in it.
"""

#! Specialized langchain object which contain everything wrapped inside package
prompt = ChatPromptTemplate.from_messages([
    ('system',system_promt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
) 
chain = prompt | llm| StrOutputParser()

print("hi, I am Sherlock, how can I help you today?")

def chat(user_input, hist):

    if not user_input.strip():
        return '',hist

    langchain_history =[]
    for item in hist:
        if item['role']=='user':
            langchain_history.append(HumanMessage(content = item['content']))

        elif item['role'] == "assistant":
            langchain_history.append(AIMessage(content=item['content']))
        try:
            response =chain.invoke({"input": user_input, "history": langchain_history})  
        except Exception as e:
            response = f"something went wrong: {str(e)}"
    updated_history = hist+[
                {'role':'user','content':user_input},
                {'role':'assistant','content':response}
    ]
    return "",updated_history

def clear_chat():
    return '',[]



page =gr.Blocks(
    title="Sherlock Holmes",
)
with page:
    gr.Markdown(
        """
        # Chat with Sherlock
        welcome to your personal conversation with a Real detective !
    """)

    chatbot = gr.Chatbot(avatar_images=[None,'sherlock.png'],show_label=False,type="messages")

    msg = gr.Textbox(show_label=False,placeholder="Consult the observer; let logic dissipate your fog ....")
    
    clear = gr.Button("Incinerate the trifles",variant="huggingface")

    clear.click(clear_chat,outputs=[msg,chatbot])
    msg.submit(chat, [msg,chatbot],[msg,chatbot])

page.launch(share=True,theme =gr.themes.Soft())


