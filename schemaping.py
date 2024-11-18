import tkinter as tk
from tkinter import ttk
import os
import tempfile
import glob
import argparse

def _calc_pos():
    # Get the temporary 
    temp_dir = tempfile.gettempdir()
    all_files = os.listdir(temp_dir)
    pattern = os.path.join(temp_dir, "SCP_*")

    # Get matching files
    matching_files = glob.glob(pattern)
    if matching_files:
        for file in matching_files:
            print
    else:
        print
        # we are the first queueist!
    queuepos = len(matching_files)
    file = tempfile.NamedTemporaryFile(delete=True, prefix=f"SCP_{queuepos}_", dir=temp_dir)

    # write some data to the file to keep it alive
    file.write(b"file actively in use by schemaping.")
    globals()['lockfile'] = file
    return queuepos



def _fade(root, direction):
    alpha = root.attributes("-alpha")
    
    if direction == "out":
        # fade out by decreasing alpha
        if alpha > 0:
            alpha -= 0.01
            root.attributes("-alpha", alpha)
            root.after(1, lambda: _fade(root, "out"))
        else:
            
            globals()['lockfile'].close()
            root.destroy()
    
    if direction == "in":
        if alpha < 0.8:
            alpha += 0.01
            root.attributes("-alpha", alpha)
            root.after(1, lambda: _fade(root, "in"))
        else:
            root.attributes("-alpha", 0.8)

def _timebar(root,bar,var):
    if var == "":
        var = "|"
        bar.configure(text=var)
    else:
        var += "|"
        bar.configure(text=var)
    root.after(50,lambda:_timebar(root,bar,var))
    

    

def create_notif(title,content):
    try:
        queuepos = _calc_pos()
        tbar = ""
        root = tk.Tk()
        root.geometry("400x100")
        ww = 400;    wh = 100
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = sw - ww - 10 ;    y = sh - wh - 80 
        cnt = 0
        while cnt != queuepos:
            y -= 120  # increase y-coordinate by 120 for each new instance
            cnt += 1 
        root.geometry(f"{ww}x{wh}+{x}+{y}")
        root.wm_attributes('-topmost', True)
        root.wm_attributes("-alpha", 0)
        root.configure(background='#383838')
        root.overrideredirect(True)
        
        tk.Label(text=title,font= ('Segoe UI',16),bg="#383838",fg="white").place(x=10,y=10)
        if len(content) > 200:
            tk.Label(text=content,font= ('Segoe UI',2),bg="#383838",fg="white",wraplength=380,justify="left").place(x=10,y=40)
        if len(content) > 100:
            tk.Label(text=content,font= ('Segoe UI',9),bg="#383838",fg="white",wraplength=380,justify="left").place(x=10,y=40)
        else:
            tk.Label(text=content,font= ('Segoe UI',12),bg="#383838",fg="white",wraplength=380,justify="left").place(x=10,y=40)

        timerbar = tk.Label(text="",font=('Segoe UI',12),bg="#383838",fg="white")
        timerbar.place(x=0,y=90)
        
        exitbtn = tk.Button(text="✖",height=1,width=2,bg="#383838",command=lambda:_fade(root,"out"), borderwidth=0)
        exitbtn.place(x=370,y=10)
        root.after(0, lambda: _fade(root,"in"))
        root.after(10000, lambda: _fade(root,"out"))
        root.after(1000,lambda:_timebar(root,timerbar,tbar))
        root.mainloop()
    except Exception as e:
        print(f"[SchemaPing] Fatal error.\n{e}")
        exit()

def __create_notif_argd(title,content):
    title = title.replace("_", " ")
    content = content.replace("_", " ")
    create_notif(title,content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='SchemaPing',
                    description='Pythonic Notification Library')
    parser.add_argument('-t', '--title', help='Notification Title (Underscores for spaces. Converts automatically.)')
    parser.add_argument('-c', '--content', help='Notification Content (Underscores for spaces. Converts automatically.)')
    parser.add_argument('-v', '--version', help='Displays version info.')

    
    args = parser.parse_args()
    if args.version:
        print("\nSchemaPing Version 1 [Beta]\n")
        exit()
    title = args.title
    message = args.content
    if message == None:
        message = ''
    if title == None:
        title = ''
    __create_notif_argd(title,message)
