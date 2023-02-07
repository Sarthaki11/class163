from tkinter import*
root=Tk()
root.title("Fever report")
root.geometry("600x600")

q1_rb=StringVar(value="0")

question_label=Label(root,text="Are you having headache and soar throat")
question_label.pack()

question1_r1=Radiobutton(root, text="yes", variable=q1_rb, value="yes")
question1_r1.pack()

question1_r2=Radiobutton(root, text="no", variable=q1_rb, value="no")
question1_r2.pack()

q2_rb=StringVar(value="0")

question_label2=Label(root,text="Are you having fever")
question_label2.pack()

question2_r1=Radiobutton(root, text="yes", variable=q2_rb, value="yes")
question2_r1.pack()

question2_r2=Radiobutton(root, text="no", variable=q2_rb, value="no")
question2_r2.pack()

root.mainloop()