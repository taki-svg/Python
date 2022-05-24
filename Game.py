from tkinter import*
import random

root=Tk()
root.geometry("503x400")
#root.iconbitmap('favicon.ico')
root.title("Game")
#root.config(bg="blue")#(a way to change back ground colour)








mylab0=Label(root,text="WELCOME TO MY GAME",bg="blue",fg="white")
mylab0.grid(row=0,column=0,columnspan=3)

num_1=0
try_0=0
def myclick(inpo,inpo1):
	lis=['Stone','Paper','scissor']
	ran=random.choice(lis)
	global try_0
	try_0=try_0+1

	mybut1.config(bg="white")
	mybut2.config(bg="white")
	mybut3.config(bg="white")


	if inpo == ran:
		inpo1.config(bg="green")
		hello=text="computer chose "+ran+" so you won"
		global num_1
		num_1=num_1+5
		mylab10=Label(root,text=num_1)
		mylab10.grid(row=5,column=1)


	else:
		inpo1.config(bg="red")
		hello=text="computer chose "+ran+" so you lost"
		num_1=num_1-1
		mylab10=Label(root,text=num_1)
		mylab10.grid(row=7,column=0,columnspan=1)


		if ran == 'Stone':
			mybut1.config(bg="yellow")
		elif ran=='Paper':
			mybut2.config(bg="yellow")
		elif ran=='scissor':
			mybut3.config(bg="yellow")


	mylab1=Label(root,text=hello)
	mylab1.grid(row=2,column=0,columnspan=3)



mylable9=Label(root,text="computer output.").grid(row=2,column=1,columnspan=1)


e=Entry(root,width=20)
#if we use these two tohether it will not work.
e.grid(row=10,column=1,columnspan=1)

labn112=Label(root,text="ENTER YOUR NAME").grid(column=0,row=10,columnspan=1)


def opn():
    nw=Toplevel(root)
    nw.title("save")
    nw.geometry("400x400")
    button12=Button(nw,text="save",command=new).grid(row=2,column=0,columnspan=3)
    Button13=Button(nw,text="preview",command=get).grid(row=3,column=0,columnspan=3)
    button14=Button(nw,text="save permnently",command=txt_wrt).grid(row=4,column=0,columnspan=3)
    button15=Button(nw,text="view results",command=get_results).grid(row=5,column=0,columnspan=3)


def get_results():
	nw1=Toplevel(root)
	nw1.title("results")
	nw1.geometry("400x400")
	with open('scoref.txt') as obj:
		context=obj.read()
		lable_new=Label(nw1,text=context).grid(row=0,column=0)
	 


data={}


def txt_wrt ():
	scoref=open('scoref.txt','a')
	scoref.write(str(data))
	scoref.close()


		

def new():
        
        name=e.get().title()
        score=num_1
        data[name]=str(score)+str(" points in "+str(try_0)+" tries.")

	


def get():
	nwn=Toplevel(root)
	nwn.title("results")

	lb=Label(nwn,text=data).pack()



		
def clear():
	global num_1
	num_1=0.00
	mylab10=Label(root,text=num_1)
	mylab10.grid(row=5,column=1)
	mylable9=Label(root,text="computer output .").grid(row=2,column=1,columnspan=1)
	e.delete(0,END)
	mybut1.config(bg="white")
	mybut2.config(bg="white")
	mybut3.config(bg="white")

	
       		

mybut1=Button(root,text="Stone",fg='black',bg='white',padx=60,pady=50,command=lambda:myclick('Stone',mybut1))
mybut2=Button(root,text="Paper",fg='black',bg='white',padx=80,pady=50,command=lambda:myclick('Paper',mybut2))
mybut3=Button(root,text="scissor",fg='black',bg='white',padx=50,pady=50,command=lambda:myclick('scissor',mybut3))



mybut4=Button(root,text="EXIT",fg='black',bg='white',padx=50,command=root.destroy)
mybut5=Button(root,text="RESET",fg='black',bg='white',padx=50,command=clear).grid(row=4,column=0,columnspan=1)
mybut7=Button(root,text="OPTIONS",fg='black',bg='white',padx=35,command=opn)



lab3=Label(root,text="POINTS",bg="blue",padx=50).grid(row=5,column=0,columnspan=1)
lab4=Label(root,text="PLAYER",padx=50).grid(row=6,column=0,columnspan=1)
lab5=Label(root,text="COMPUTER",padx=50).grid(row=6,column=1,columnspan=1)



mybut1.grid(row=1,column=0,columnspan=1)
mybut2.grid(row=1,column=1,columnspan=1)
mybut3.grid(row=1,column=2,columnspan=1)
mybut4.grid(row=3,column=0,columnspan=1)
mybut7.grid(row=9,column=0,columnspan=1)




root.mainloop()
