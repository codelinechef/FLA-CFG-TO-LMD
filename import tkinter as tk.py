import tkinter as tk

def convert_cfg_to_lmd():
    cfg = cfg_text.get("1.0", "end-1c")  # Get the CFG from the text widget
    start_symbol = start_symbol_entry.get()
    
    # Implement a more appropriate CFG to LMD conversion logic here
    lmd_result = cfg_to_lmd(cfg, start_symbol)

    # Display the LMD result in the output text widget
    lmd_text.delete("1.0", "end")
    lmd_text.insert("1.0", lmd_result)

# Function to convert CFG to LMD
def cfg_to_lmd(cfg, start_symbol):
    lmd = [start_symbol]  # Initialize with the start symbol
    
    while True:
        found = False
        for production in cfg.split('\n'):
            left, right = production.split('->')
            left = left.strip()
            right = right.strip()
            
            for i, symbol in enumerate(lmd):
                if symbol == left:
                    lmd.pop(i)
                    lmd = lmd[:i] + list(right) + lmd[i:]
                    found = True
                    break
        
        if not found:
            break
    
    return ' -> '.join(lmd)

# Create the main application window
app = tk.Tk()
app.title("CFG to LMD Converter")

# Create and place GUI elements
cfg_label = tk.Label(app, text="Enter CFG:")
cfg_label.pack()

cfg_text = tk.Text(app, height=5, width=40)
cfg_text.pack()

start_symbol_label = tk.Label(app, text="Start Symbol:")
start_symbol_label.pack()

start_symbol_entry = tk.Entry(app)
start_symbol_entry.pack()

convert_button = tk.Button(app, text="Convert", command=convert_cfg_to_lmd)
convert_button.pack()

lmd_label = tk.Label(app, text="LMD Result:")
lmd_label.pack()

lmd_text = tk.Text(app, height=5, width=40)
lmd_text.pack()

# Start the GUI event loop
app.mainloop()
