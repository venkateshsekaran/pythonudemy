row1=["y","y","y"]
row2=["y","y","y"]
row3=["y","y","y"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=(input("where do you want to put the treasure: "))
horizontal=int(position[0])-1
vertical=int(position[1])-1
map[horizontal][vertical]="x"
print(f"{row1}\n{row2}\n{row3}\n")


        