import tkinter as tk

def start_timer():
    try:
        # Get the input time in seconds
        total_seconds = int(entry.get())
        countdown(total_seconds)
    except ValueError:
        label_time.config(text="Invalid input!")

def countdown(seconds):
    # Update the label every 1 second
    if seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        label_time.config(text=time_str)
        root.after(1000, countdown, seconds - 1)  # Recursively call countdown after 1 second
    else:
        label_time.config(text="Time's up!")

# Set up the GUI window
root = tk.Tk()
root.title("Countdown Timer")

# Create a label to display the time
label_time = tk.Label(root, text="00:00", font=("Helvetica", 48), width=8)
label_time.pack()

# Create an entry box for input time in seconds
entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack()

# Create a start button
start_button = tk.Button(root, text="Start", font=("Helvetica", 24), command=start_timer)
start_button.pack()

# Run the Tkinter event loop
root.mainloop()