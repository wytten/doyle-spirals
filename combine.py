from PIL import Image

frames = [Image.open(f"frame-{i:02d}.png") for i in range(22)]
frames[0].save(
    "spiral.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
)