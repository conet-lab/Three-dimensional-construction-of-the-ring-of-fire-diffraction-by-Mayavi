import numpy as np
from mayavi import mlab
from tvtk.util.ctf import ColorTransferFunction

s=  np.load('data.npy')
s /= 255
gamma = 20
s = 1/(1+np.exp(gamma*(0.5-s)))
s *= 255

size = (500, 500)
fig = mlab.figure(bgcolor=(0.,0.,0.), fgcolor=(0.,0.,0.) , size=size)
fig.scene.disable_render = True

src = mlab.pipeline.scalar_field(s)
src.spacing = [20, 0.5, 0.5]

vol = mlab.pipeline.volume(src, vmin=20, vmax=255)

ctf = ColorTransferFunction()

for i in range(256):
    b = i * 0.5 / 255
    g = i * 0.78 / 255
    r = (i * 1.2439 / 255) if i < 205 else 1
    ctf.add_rgb_point(i, r, g, b)
    
vol._volume_property.set_color(ctf)
vol._ctf = ctf
vol.update_ctf = True

mlab.orientation_axes()
fig.scene.disable_render = False
mlab.view(45,45)

mlab.show()



