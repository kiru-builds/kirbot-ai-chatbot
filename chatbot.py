import tkinter as tk
from tkinter import scrolledtext, font
import datetime
import random
import threading

responses = {
    'hello': ["Hello! I'm KirBot 🤖 How can I help you today?"],
    'hi': ["Hi there! 😊 Ask me anything!"],
    'how are you': ["I'm running at 100%! 🚀"],
    'what is ai': ["🧠 AI is the simulation of human intelligence in machines!"],
    'what is machine learning': ["📊 ML is teaching computers to learn from data!"],
    'joke': ["😂 Why do programmers prefer dark mode? Light attracts bugs!"],
    'who made you': ["👩‍💻 I was created by Kirthika — B.Tech AI & Data Science student!"],
    'bye': ["Goodbye! 👋 Come back anytime!"],
    'thank you': ["You're welcome! 😊"],
    'thanks': ["Happy to help! 🤖"],
    'internship': ["🌍 Build GitHub projects, get certified, apply on LinkedIn!"],
    'germany': ["🇩🇪 Germany pays €800-1200/month for AI internships!"],
    'python': ["🐍 Python is the #1 language for AI and Data Science!"],
}

def get_response(user_input):
    text = user_input.lower().strip()
    for key in responses:
        if key in text:
            return random.choice(responses[key])
    return random.choice([
        "🤔 Interesting! Ask me about AI or ML!",
        "💡 Try asking about Python, internships or AI!",
        "🤖 I'm still learning! Ask me about Data Science!",
    ])

class KirBot:
    def __init__(self, root):
        self.root = root
        self.root.title("KirBot - AI Chatbot by Kirthika")
        self.root.geometry("600x700")
        self.root.configure(bg='#1a1a2e')

        # Header
        tk.Label(self.root,
                 text="KirBot - AI Chatbot by Kirthika",
                 font=('Helvetica', 14, 'bold'),
                 bg='#16213e', fg='#00ff88',
                 pady=15).pack(fill='x')

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD,
            font=('Helvetica', 11),
            bg='#0f3460', fg='white',
            state='disabled', relief='flat',
            padx=10, pady=10)
        self.chat_area.pack(padx=15, pady=10,
                            fill='both', expand=True)

        self.chat_area.tag_config('user', foreground='#4fc3f7')
        self.chat_area.tag_config('bot', foreground='#00ff88')

        # Input
        input_frame = tk.Frame(self.root, bg='#1a1a2e')
        input_frame.pack(fill='x', padx=15, pady=15)

        self.input_box = tk.Entry(
            input_frame,
            font=('Helvetica', 12),
            bg='#16213e', fg='white',
            insertbackground='white',
            relief='flat', bd=10)
        self.input_box.pack(side='left', fill='x',
                            expand=True, ipady=8)
        self.input_box.bind('<Return>', self.send_message)
        self.input_box.focus()

        tk.Button(input_frame, text="Send",
                  font=('Helvetica', 11, 'bold'),
                  bg='#00ff88', fg='#1a1a2e',
                  relief='flat', padx=15, pady=8,
                  command=self.send_message
                  ).pack(side='right', padx=(10,0))

        self.add_message("KirBot",
            "Hello! I'm KirBot by Kirthika! Ask me anything 😊",
            'bot')

    def add_message(self, sender, message, tag):
        self.chat_area.config(state='normal')
        self.chat_area.insert('end', f"\n{sender}: ", tag)
        self.chat_area.insert('end', f"{message}\n", tag)
        self.chat_area.config(state='disabled')
        self.chat_area.see('end')

    def send_message(self, event=None):
        user_input = self.input_box.get().strip()
        if not user_input:
            return
        self.input_box.delete(0, 'end')
        self.add_message("You", user_input, 'user')
        def respond():
            import time
            time.sleep(0.5)
            response = get_response(user_input)
            self.add_message("KirBot", response, 'bot')
        threading.Thread(target=respond, daemon=True).start()

root = tk.Tk()
app = KirBot(root)
root.mainloop()