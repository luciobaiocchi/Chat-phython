import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

class ChatClient:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        
        self.root = tkinter.Tk()
        self.root.title("Chat Room")
        
        self.chat_box = tkinter.scrolledtext.ScrolledText(self.root)
        self.chat_box.pack(padx=20, pady=5)
        self.chat_box.config(state=tkinter.DISABLED)
        
        self.input_area = tkinter.Text(self.root, height=3)
        self.input_area.pack(padx=20, pady=5)
        
        self.send_button = tkinter.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=20, pady=5)
        
        self.alias = simpledialog.askstring("Nickname", "Please choose a nickname", parent=self.root)
        if self.alias:
            self.client.send(self.alias.encode('utf-8'))
        
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.alias.encode('utf-8'))
                else:
                    self.chat_box.config(state=tkinter.NORMAL)
                    self.chat_box.insert(tkinter.END, message + '\n')
                    self.chat_box.config(state=tkinter.DISABLED)
                    self.chat_box.yview(tkinter.END)
            except:
                print('An error occurred!')
                self.client.close()
                break
    
    def send_message(self):
        message = f'{self.alias}: {self.input_area.get("1.0", tkinter.END)}'
        self.client.send(message.encode('utf-8'))
        self.chat_box.config(state=tkinter.NORMAL)
        self.chat_box.insert(tkinter.END, message + '\n')
        self.chat_box.config(state=tkinter.DISABLED)
        self.chat_box.yview(tkinter.END)
        self.input_area.delete('1.0', tkinter.END)
    
    def on_closing(self):
        self.client.close()
        self.root.destroy()

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5555
    ChatClient(host, port)
