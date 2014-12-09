#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
    	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "blue")
       	    self.down.grid(row=0,column=2)
       	    self.down.bind("<Button-1>", self.downClicked)

            self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "yellow")
       	    self.left.grid(row=0,column=3)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=0,column=4)
       	    self.right.bind("<Button-1>", self.rightClicked)
            # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
            self.animate()
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	 
        def downClicked(self, event):
           global oval
           global player
           drawpad.move(player,0,20)
           
        def rightClicked(self, event):
           global oval
           global player
           drawpad.move(player,20,0)
		
        def leftClicked(self, event):
           global oval
           global player
           drawpad.move(player,-20,0)
         # Animate function that will bounce target left and right, and trigger the collision detection  
	direction = 1
	def animate(self):
	    global target
	    global direction
   	    
   	    # Insert the code here to make the target move, bouncing on the edges    
   	        
   	        
                
            global direction
        # Get the x and y co-ordinates of the circle
            x1, y1, x2, y2 = drawpad.coords(target)
            if x2 > drawpad.winfo_width(): 
                direction = - 3
            elif x1 < 0:
                direction = 3
        #Move our oval object by the value of direction
            drawpad.move(target,direction,0)
        # Wait for 1 millisecond, then recursively call our animate function
             
                #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
                # Use the value of didWeHit to create an if statement
                # that determines whether to run drawpad.after(1,self.animate) or not
            if didWeHit == False:
                drawpad.after(10,self.animate)
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1,y1,x2,y2 = drawpad.coords(player)
                targetx1, targety1, targetx2, targety2 = drawpad.coords(target)
                if targetx1 < x1 and targetx2 > x2 and targety1 < y1 and targety2 > y2:
                    drawpad.itemconfig(target,fill = 'red')
                    return True
                else:
                    return False
                    
                global target
		global drawpad
                global player
                x1,y1,x2,y2 = drawpad.coords(Canvas)
                targetx1, targety1, targetx2, targety2 = drawpad.coords(Cavas)
                if targetx1 < x1 and targetx2 > x2 and targety1 < y1 and targety2 > y2:
                    drawpad.itemconfig(target,fill = 'red')
                    return True
                else:
                    return False
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)

                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()