from tkinter import Tk,Entry,Button,Label

from PIL import Image, ImageDraw, ImageFont




def default_text_():
    watermark_text = "Lingesh's Water Mark"
    text(w=watermark_text)

def default_image_():
    
    watermark = Image.open(r'C:\Users\linge\Desktop\python 100 days\projects\pr-85\img\L.png')
    image(w=watermark)


def text(w):
    original_image = Image.open(rf'{file.get()}')
    draw = ImageDraw.Draw(original_image)
    watermark_text = w
    font_size = 14
    font = ImageFont.truetype("arial.ttf", font_size)  
    text_color = (255, 255, 355)  

    #White color (RGB)
    text_width = draw.textlength(watermark_text, font)
    text_height=draw.textlength(watermark_text, font)


    image_width, image_height = original_image.size
    margin = 10  

    #Margin from the right and bottom edges
    position = (image_width - text_width - margin, image_height - text_height - margin)
    draw.text(position, watermark_text, font=font, fill=text_color)
    # original_image.save("output Image/watermarked_image.png")
    original_image.show() 



def image(w):
    original_image = Image.open(rf'{file.get()}')
    watermark = w  
    
    target_width =100 

    #Adjust this to our preferred size
    aspect_ratio = float(target_width) /( watermark.width-100)
    target_height = int(watermark.height * aspect_ratio)
    watermark = watermark.resize((target_width, target_height), Image.LANCZOS)
    watermarked_image = original_image.copy()

    #Adjust the position where you want to place the watermark (e.g., bottom right corner)
    position = (original_image.height - watermark.height,original_image.width - watermark.width,)# original_image.height - watermark.height)
    watermarked_image.paste(watermark, position, watermark)
    # watermarked_image.save("output Image/watermarked_image.jpg")
    watermarked_image.show()

# def new_image():
#     image_label=Label(text="Water Mark Image File Location:")
#     image_label.grid(column=3,row=8)

#     img_file=Entry(width=10)
#     img_file.focus()
#     img_file.grid(column=4,row=8)

#     image(w=Image.open(rf'{img_file.get()}'))

#     # image(file.get())
# def new_text():
#     text_label=Label(text="Water Mark text:")
#     text_label.grid(column=3,row=8)

#     txt_file=Entry(width=10)
#     txt_file.focus()
#     txt_file.grid(column=4,row=8)

#     image(w=txt_file.get())



window=Tk()
window.title("Water Mark Project")
window.minsize(300,50)



file_label=Label(text="File Location:")
file_label.grid(column=3,row=5)


file=Entry(width=10)
file.focus()
file.grid(column=4,row=5)

default_text=Button(text="Default Text",command=default_text_)
default_text.grid(column=5,row=5)

default_image=Button(text="Default Image",command=default_image_)
default_image.grid(column=6,row=5)

# text_or_image=Label(text="Click the watermark type:")
# text_or_image.grid(column=3,row=6)

# text_button=Button(text="Text",command=new_text)
# text_button.grid(column=4,row=6)

# image_button=Button(text="Image",command=new_image)
# image_button.grid(column=5,row=6)


window.mainloop()