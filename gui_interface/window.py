import tkinter as tk


class GPSWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GPS Monitor")
        self.root.geometry("600x400")

        # Add a Text widget to display output
        self.text = tk.Text(self.root, height=20, width=70)
        self.text.pack(pady=20)

        # Optional: a scrollbar
        scrollbar = tk.Scrollbar(self.root, command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def update_display(self, message: str):
        """Insert message into the text box"""
        self.text.insert(tk.END, message + "\n")
        self.text.see(tk.END)  # auto-scroll

    def run(self):
        self.root.mainloop()
