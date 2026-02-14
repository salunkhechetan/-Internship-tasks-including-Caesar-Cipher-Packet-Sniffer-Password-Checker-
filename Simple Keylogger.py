import keyboard
import time

print("Start typing... Press ESC to stop.")

typed_text = ""
start_time = time.time()

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "esc":
            break
        else:
            typed_text += event.name + " "

end_time = time.time()
print("\nYou typed:", typed_text)
print("Time taken:", round(end_time - start_time, 2), "seconds")