# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from Element import Element
from Components.DIP import DIP
from Components.Grid import Grid
from Components.AmpLM386 import AmpLM386
from Components.ADE1 import ADE1
from Components.SA612 import SA612
from GcodeStream import GcodeStream
from CAMParameters import CAMParameters
from RenderParameters import RenderParameters
from utils import *


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


root = tk.Tk()
root.title("SCAM v0.3 2020-10-22 KC1FSZ")
scale = 1
# My Mac desktop seems to have a different dot-pitch than what TK is expecting
ppmm = scale * root.winfo_fpixels('1m') * (100 / 70)
cp = CAMParameters()
render_params = RenderParameters(ppmm, cp)

depth = -0.25
c = tk.Canvas(root, bg="#b87333", width=cp.board_w * ppmm, height=cp.board_h * ppmm)

# -----------------------------------------------------------------
# A hard-coded board design for testing.  This will come from
# an external file once we are finished.
e = Compound()

"""
# ---- IQ Modulator Project ---------------------------------------
# Top grid
e.add((30, 0), Grid(6, 1))

e.add((15, 10), Dip8(True))
e.add((55, 10), Dip8(True))

e.add((10, 25), Grid(6, 2))
e.add((50, 25), Grid(6, 2))

e.add((35, 45), Dip14(True))
e.add((18, 70), Grid(10, 2))
"""

"""
# ---- Test Pattern  ---------------------------------------
e.add((0, 0), Grid(10, 2, 0))
e.add((10, 20), Grid(10, 2, 90))
e.add((20, 20), DIP())
e.add((20, 30), DIP(8, True, rotation_ccw=90))
e.add((50, 10), DIP(14, True))
e.add((80, 10), AmpLM386())
e.add((120, 10), ADE1())
"""
e.add((30, 30), SA612(rotation_ccw=-90))

# -----------------------------------------------------------------
# Draw on the screen
e.render(c, 0, 0, "#ffffff", render_params)
c.pack()

# Generate g-code onto the lab computer for milling
gcs = GcodeStream("/tmp/pi4/out.nc")
#gcs = GcodeStream("./out.nc")
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
