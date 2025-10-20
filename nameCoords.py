import re
from pynput import mouse


# instructions: place the script in the same directory as the target_file
#               then run this script and left click on the desired midpoint (xG, xY). right click to cancel.
target_file = "aPerfectCircle.py"

def update_coords(x, y):
    with open(target_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Replace xG and yG definitions using regex
    code = re.sub(r"xG\s*=\s*\d+", f"xG = {x}", code)
    code = re.sub(r"yG\s*=\s*\d+", f"yG = {y}", code)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"\nupdated {target_file}:\n  xG = {x}\n  yG = {y}")

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        update_coords(int(x), int(y))
        print("left click detected → coordinates updated")
        return False 
    elif pressed and button == mouse.Button.right:
        print("cancelled")
        return False

print("move your cursor to the desired midpoint and left click to save coordinates")
print("right click to cancel")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()