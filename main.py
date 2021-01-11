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
from Components.MAX2650 import MAX2650
from Components.FeedbackAmp import FeedbackAmp
from Components.SA612 import SA612
from Components.Trace import Trace
from Components.DBM import DBM
from Components.SC70 import SC70
from Components.SC70a import SC70a
from Components.GALI3_Biased import GALI3_Biased
from Components.PA_1 import PA_1
from Components.PA_2 import PA_2
from Components.PA_3 import PA_3
from Components.PA_4 import PA_4

from GcodeStream import GcodeStream
from CAMParameters import CAMParameters
from RenderParameters import RenderParameters
from utils import *


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


def render_corners(canvas, origin_x, origin_y, color, render_params):
    canvas.create_rectangle(0, 0, render_params.u2px(7), render_params.u2px(7), fill="red")
    canvas.create_rectangle(0, render_params.height - render_params.u2px(7),
        render_params.u2px(7), render_params.height, fill="red")


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
"""
# ---- DSB Transmitter -------------------------------------
e.add((10, 0), Trace(5, 5, rotation_ccw=0))
e.add((20, 0), Trace(110, 5, rotation_ccw=0))
# Mic amp
e.add((0, 10), Grid(3, 3))
# Mixer
e.add((25, 10), DBM(rotation_ccw=0))
# RF amp
e.add((75, 10), Grid(3, 4))
e.add((110, 10), Grid(3, 4))
"""

"""
# ----- MAX4466 Mic Amp --------------------------------------

e.add((10, 5), Grid(3, 3))
e.add((30, 10), SC70a(rotation_ccw=0))
e.add((10, 25), Trace(30, 5, rotation_ccw=0))
"""
"""
# ----- Mixer with Buffers --------------------------------------

# Bus
#e.add((10, 2), Trace(50, 3, rotation_ccw=0))

#e.add((5, 24), Grid(3, 3))
#e.add((30, 24), Grid(3, 3))
#e.add((55, 24), Grid(3, 3))
e.add((2, 12), MAX2650())
e.add((26, 12), ADE1())
e.add((54, 12), MAX2650())
"""

"""
# -----------------------------------------------------------------
# Mixer with Buffers

e.add((2, 10), Grid(1, 3))
e.add((10, 2), ADE1())
e.add((20, 15), Grid(2, 2))
e.add((38, 2), FeedbackAmp())
e.add((61, 2), Grid(1, 2))
e.add((70, 2), FeedbackAmp())

e.add((15, 30), Trace(80, 5, rotation_ccw=0))
"""
"""
# -----------------------------------------------------------------
# GALI3+ and BJT Amp

e.add((10, 12), GALI3_Biased())
e.add((5, 22), Grid(2, 2))
e.add((35, 2), FeedbackAmp())
e.add((10, 40), Trace(50, 5, rotation_ccw=0))
"""
"""
# -----------------------------------------------------------------
# Power Amp (WORKING!)

e.add((80, 10), PA_1())
e.add((80, 35), PA_1())

e.add((30, 8), PA_3())
e.add((30, 38), Grid(1, 1))

e.add((2, 10), FeedbackAmp())

e.add((10, 50), Trace(60, 5, rotation_ccw=0))

e.add((10, 58), Grid(2, 1))
"""
# -----------------------------------------------------------------
# Power Amp Output

e.add((10, 15), PA_4())

# -----------------------------------------------------------------
# Draw on the screen
render_corners(c, 0, 0, "#ff0000", render_params)
e.render(c, 0, 0, "#ffffff", render_params)
c.pack()

# Generate g-code onto the lab computer for milling
#gcs = GcodeStream("/tmp/pi4/out.nc")
gcs = GcodeStream("./out.nc")
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
e.mill(gcs, 0, 0, depth, cp)

# Pull out the tool at the end of the work
gcs.comment("Park")
gcs.out("G00 Z" + gcs.dec4(cp.safe_z))
gcs.out("M05")
gcs.close()

root.mainloop()
