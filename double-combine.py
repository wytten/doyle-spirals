from PIL import Image

frames = [Image.open(f"double-{i:02d}.png") for i in range(15)]
frames[0].save(
    "double-spiral.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
)