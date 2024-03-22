from PIL import Image

# 打开 JPG 格式的图像文件
jpg_image_path = "changed.jpg"
jpg_image = Image.open(jpg_image_path)

# 保存为 GIF 格式的图像文件
gif_image_path = "changed.gif"
jpg_image.save(gif_image_path)

print("JPG 图像已成功转换为 GIF 格式！")