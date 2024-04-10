import tkinter as tk
from multiprocessing import Process
import subprocess

def run_script(args):
    subprocess.run(["python", "main.py"] + args)

def on_run():
    args = []
    for entry, arg in zip(entries, arg_names):
        args.append(f"--{arg}_lower")
        args.append(entry[0].get("1.0", "end-1c"))
        args.append(f"--{arg}_upper")
        args.append(entry[1].get("1.0", "end-1c"))
    run_script(args)

root = tk.Tk()
root.title("ReRAM Optimization")
root.geometry('350x600')

arg_names = [
    'beta', 'alphamin', 'alphamax', 'rsmax', 'rsmin', 'imax', 'imin', 'v0s', 'v0r', 't0s', 't0r'
]

default_values = [
    (0.275, 0.4), (3.3, 5.0), (0.3, 40.0), (256, 256), (117, 117), (1.23E-03, 1.23E-03), (1.80E-06, 1.80E-06),
    (0.05, 0.35), (0.05, 0.3), (80, 8.00E+06), (10, 2200)
]

entries = []

frame = tk.Frame(root)
frame.pack(fill='x', padx=5, pady=5)

#최상단 설명 각주
label = tk.Label(frame, text=f"args", font=("Arial", 17))
label.pack(side='left')

upper_label = tk.Label(frame, text="Upper", width=10, font=("Arial", 17))
upper_label.pack(side='right')

lower_label = tk.Label(frame, text="Lower", width=10, font=("Arial", 17))
lower_label.pack(side='right')

# 각 파라밑쌍 묶기
for arg, (default_lower, default_upper) in zip(arg_names, default_values):
    frame = tk.Frame(root)
    frame.pack(fill='x', padx=5, pady=5)

    label = tk.Label(frame, text=f"{arg}")
    label.pack(side='left')

    upper_entry = tk.Text(frame, height=1, width=10, font=("Arial", 17))
    upper_entry.insert('1.0', str(default_upper))
    upper_entry.pack(side='right')

    lower_entry = tk.Text(frame, height=1, width=10, font=("Arial", 17))
    lower_entry.insert('1.0', str(default_lower))
    lower_entry.pack(side='right')

    entries.append((lower_entry, upper_entry))

# 또다른 파라미터 입력
worker_frame = tk.Frame(root)
worker_frame.pack(fill='x', padx=5, pady=5)

worker_label = tk.Label(worker_frame, text='worker')
worker_label.pack(side='left')

worker_entry = tk.Text(worker_frame, height=1, width=10, font=("Arial", 17))
worker_entry.insert('1.0', str(1))
worker_entry.pack(side='right')

# 시작버튼
run_button = tk.Button(root, text='Run', command=on_run, height=2, width=20)
run_button.pack()

root.mainloop()
