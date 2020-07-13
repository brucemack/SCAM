# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from Element import Element
from Components.Dip14 import Dip14
from Components.Grid import Grid
from Components.AmpLM386 import AmpLM386
from Components.ADE1 import ADE1
from GcodeStream import GcodeStream
from CAMParameters import CAMParameters

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root = tk.Tk()
root.title("SCAM v0.1 2020-07-11 KC1FSZ")
scale = 1
# My Mac desktop seems to have a different dot-pitch than what TK is expecting
ppmm = scale * root.winfo_fpixels('1m') * (100 / 70)
Element.set_pixels_per_mm(ppmm)

depth = -0.25
size = (100, 150)
c = tk.Canvas(root, bg="#b87333", width=size[0] * ppmm, height=size[1] * ppmm)

# -----------------------------------------------------------------
# A hard-coded board design for testing.  This will come from
# an external file once we are finished.
e = Compound()
# Top grid
e.add((32, 80), Grid(6, 1))
# Top amp
e.add((12, 65), Grid(4, 2))
e.add((12, 45), Grid(4, 2))
e.add((40, 50), Dip14(True))
e.add((64, 65), Grid(4, 2))
e.add((64, 45), Grid(4, 2))
# Bottom amp
e.add((12, 25), Grid(4, 2))
e.add((12, 5), Grid(4, 2))
e.add((40, 10), Dip14(True))
e.add((64, 25), Grid(4, 2))
e.add((64, 5), Grid(4, 2))
# Extra stuff
e.add((12, 90), AmpLM386())
e.add((50, 90), ADE1())
# -----------------------------------------------------------------

# Draw on the screen
e.render(c, 0, 0, 150 * ppmm, "#ffffff", 1.0)
c.pack()

# Generate g-code onto the lab computer for milling
gcs = GcodeStream("/pi4/nfsshare/out.nc")
gcs.comment("SCAM G-Code Generator")
gcs.comment("Bruce MacKinnon KC1FSZ")
# Units in mm
gcs.out("G21")
# Absolute distance mode
gcs.out("G90")
# Units per minute feed rate mode
gcs.out("G94")
# Spindle speed
gcs.out("M03 S10000")

cp = CAMParameters()
e.mill(gcs, 0, 5, depth, cp)

# Pull out the tool at the end of the work
gcs.comment("Park")
gcs.out("G00 Z" + gcs.dec4(cp.safe_z))
gcs.out("M05")
gcs.close()

root.mainloop()

