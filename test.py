import tkinter as tk

root = tk.Tk()
root.title("🤖 KirBot — AI Chatbot by Kirthika")
root.geometry("600x700")
root.configure(bg='#1a1a2e')

label = tk.Label(root, text="KirBot Loading...", 
                 fg='#00ff88', bg='#1a1a2e',
                 font=('Helvetica', 20, 'bold'))
label.pack(pady=300)

root.mainloop()