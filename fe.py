from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()