import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    # Make the image editable
    txt = Image.new('RGBA', original_image.size, (255, 255, 255, 0))

    # Choose a font and size
    font = ImageFont.truetype("arial.ttf", 36)

    # Initialize ImageDraw
    draw = ImageDraw.Draw(txt)

    # Position for the watermark text
    textwidth, textheight = draw.textsize(watermark_text, font)
    x = width - textwidth - 10
    y = height - textheight - 10

    # Add watermark
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    watermarked = Image.alpha_composite(original_image.convert('RGBA'), txt)
    watermarked = watermarked.convert("RGB")  # Remove alpha for saving in jpg format
    watermarked.save(output_image_path)

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, file_path)

def save_image():
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    if save_path:
        watermark_text = watermark_entry.get()
        add_watermark(image_path_entry.get(), save_path, watermark_text)
        status_label.config(text="Watermark added and image saved successfully!")

# Set up the GUI
root = tk.Tk()
root.title("Watermark Adder")

# Image path entry
tk.Label(root, text="Image Path:").grid(row=0, column=0, padx=10, pady=10)
image_path_entry = tk.Entry(root, width=50)
image_path_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_image).grid(row=0, column=2, padx=10, pady=10)

# Watermark text entry
tk.Label(root, text="Watermark Text:").grid(row=1, column=0, padx=10, pady=10)
watermark_entry = tk.Entry(root, width=50)
watermark_entry.grid(row=1, column=1, padx=10, pady=10)

# Save button
tk.Button(root, text="Add Watermark & Save", command=save_image).grid(row=2, column=1, padx=10, pady=20)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

# Run the application
root.mainloop()





# from PIL import Image, ImageDraw, ImageFont
# from tkinter import filedialog
# from tkinter import Tk

# # Initialize Tkinter and hide the root window
# root = Tk()
# root.withdraw()

# # Prompt user to select an image file
# filename = filedialog.askopenfilename(
#     initialdir='/This PC/Downloads/hotcoffee',
#     title='Select an Image:'
# )

# # Function to add a watermark to an image
# def add_watermark(image_path, wm_text):
#     try:
#         # Open the image file
#         opened_image = Image.open(image_path)

#         # Get image size
#         image_width, image_height = opened_image.size

#         # Create an ImageDraw object
#         draw = ImageDraw.Draw(opened_image)

#         # Specify a font size based on image width
#         font_size = int(image_width / 8)

#         # Try to use a specific font, fallback to default if not found
#         try:
#             font = ImageFont.truetype('arial.ttf', font_size)
#         except IOError:
#             font = ImageFont.load_default()

#         # Coordinates for watermark placement
#         x, y = int(image_width / 2), int(image_height / 2)

#         # Add the watermark text
#         draw.text(
#             (x, y),
#             wm_text,
#             font=font,
#             fill='#FFF',
#             stroke_width=5,
#             stroke_fill='#222',
#             anchor='ms'
#         )

#         # Show the image with watermark
#         opened_image.show()

#     except Exception as e:
#         print(f"Error: {e}")

# # Add watermark to the selected image
# add_watermark(filename, 'hotcoffee')