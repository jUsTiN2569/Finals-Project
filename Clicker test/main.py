#This is my main file



import tkinter as tk
from library.button import button

class game():
    def __init__(self, click_count):
        self.click_count = click_count

Speed = ""
click_count = 0  
switch = 1
def Click_Timer():
    root = tk.Tk()
    global switch
    global click_count
    click_count += 1  
    #Makes sure this message only runs once
    if switch == 1:
        Message = tk.Label(root,text="yall stop wasting time and click da button some more.")
        Message.pack()
    
    if switch == 1:
        #Waits 5000 milliseconds or 5 seconds
        root.after(5000, timer_done)
        #Adds one to the switch so it only runs once
        switch +=1
    elif switch != 1:
        click_count += 1




def timer_done():
    root = tk.Tk()
    global Speed
    global click_count
    global switch
    #Caculates that average in 5 seconds
    click_count /= 5
    speed()
    #Prints end message
    Message = tk.Label(root,text=f"5 seconds already have passed lol. Your average clicks in 5 seconds: {click_count}. Congrats, you are considered a {Speed}")
    Message.pack()
    
    
    


def speed():
    global Speed
    global click_count

    #Checks what animal you would be
    if click_count >= 35:
        Speed = "cheater with an auto clicker"
    elif click_count >= 7:
        Speed = "cheetah"
    elif click_count >= 5:
        Speed = "rabbit"
    elif click_count >= 4:
        Speed = "bird"
    elif click_count >= 1:
        Speed = "turtle"
    elif click_count >= 0.2:
        Speed = "AFKer"


def main():
    
    root = tk.Tk()
    root.title("Clicker Test")

    root.geometry("600x400")

    frame = tk.Frame(root,width = 500, height = 400, bg = "lightblue")
    frame.pack()
    

    button = tk.Button(frame,text = "Click me pls", command = Click_Timer)
    button.pack()

    Message = tk.Label(root,text=f"5 seconds already have passed lol. Your average clicks in 5 seconds: {click_count}. Congrats, you are considered a {Speed}")
    Message.pack()


    root.mainloop()

if __name__ == "__main__":
    main()
