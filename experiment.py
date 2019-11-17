import glob
from PIL import Image


fp_in = "./Figure/2019-11-16/-20.0000/*.png"
fp_out = "./image.gif"

print(glob.glob(fp_in))
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,save_all=True, duration=200, loop=0)
