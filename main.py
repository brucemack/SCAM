# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

import tkinter as tk
from Compound import Compound
from Line import Line
from Element import Element
from Rectangle import Rectangle
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
from Components.SOT23 import SOT23
from Components.SOT23_6a import SOT23_6a
from Components.SOT23_6c import SOT23_6c
from Components.GALI3_Biased import GALI3_Biased
from Components.PA_1 import PA_1
from Components.PA_2 import PA_2
from Components.PA_3 import PA_3
from Components.PA_4 import PA_4
from Components.IRF510 import IRF510
from Components.Multitrace import Multitrace
from Components.PlesseyBilatteral import PlesseyBilatteral
from Components.Poly import Poly

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


def s(point_x, point_y):
    return point_x, point_y


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
"""
# -----------------------------------------------------------------
# Power Amp Output

e.add((30, 55), Grid(2, 1))
e.add((40, 25), FeedbackAmp())
e.add((10, 25), FeedbackAmp())

# Variable pot
e.add((60, 50), DIP(8, True))
# LM358
e.add((35, 10), DIP(8, True))
e.add((30, 2), Grid(2, 1))

e.add((75, 5), Grid(2, 4))
e.add((85, 35), IRF510())
"""

# -----------------------------------------------------------------
# Driver
"""
e.add((15, 55), Grid(2, 1))
e.add((50, 55), Grid(2, 1))

e.add((75, 50), Grid(2, 2))
e.add((40, 20), FeedbackAmp())
e.add((5, 20), FeedbackAmp())

e.add((80, 5), Grid(2, 4))
e.add((85, 35), IRF510())
"""
"""
# ---- Mic Amp and Balanced Modulator
# Build on 3/17/2021, works well

# Mic Amp
e.add((10, 30), Grid(2, 2))
e.add((10, 20.5), SC70a(rotation_ccw=0))
e.add((10, 5), Grid(2, 2))

# Balanced Modulator
e.add((32, 20), Grid(2, 3))
e.add((47, 24), SOT23(rotation_ccw=0))

# Pad
e.add((60, 15), Grid(2, 2))

# IF AMP
e.add((32+12, 5), Grid(2, 1))
e.add((32, 5), Grid(2, 2))
"""

"""
# ---- Bi-Directional Crystal Filter and IF Amp
# Built on 3/21/2021, works well

# Left Amp
e.add((7, 20), Grid(2, 2))
e.add((7+12, 20), Grid(2, 1))

e.add((7, 3), SOT23_6a(rotation_ccw=0))
e.add((35-6, 7), Grid(7, 1))
e.add((93, 16), SOT23_6a(rotation_ccw=180))

# Right Amp
e.add((73, 20), Grid(2, 2))
e.add((73+12, 20), Grid(2, 1))
"""

"""
# ---- Bi-Directional Mixer and IF Amp
# Built on 3/21/2021, works well

# Left Amp
e.add((9, 20), Grid(2, 2))
e.add((9+12, 20), Grid(2, 1))

# Left pad
e.add((2, 10), Grid(2, 1))

# Left switch
e.add((14, 3), SOT23_6a(rotation_ccw=0))
e.add((37, 8), ADE1())
# LO pad
e.add((46, 20), Grid(1, 2))
# Right Switch
e.add((85, 16), SOT23_6a(rotation_ccw=180))

# Right Amp
e.add((77, 20), Grid(2, 2))
e.add((77-12, 26), Grid(2, 1))

# Right pad
e.add((85, 10), Grid(2, 1))
"""

"""
# ---- Audio I/O board and modulator
# Built on 3/27/21, works well

e.add((10, 2), SOT23_6c())
e.add((30, 2), AmpLM386())
# Pre-Amp
e.add((70, 2), Grid(3, 2))

# Balanced Modulator
e.add((72, 18), Grid(2, 3))
e.add((87, 21), Grid(1, 3))

# +5V Transmit
e.add((48, 32), Trace(20, 5, rotation_ccw=0))
# +5V Receive
e.add((25, 32), Trace(20, 5, rotation_ccw=0))
"""

"""
# ---- Band pass filter and amplifier
# Built on 4/1/21, works well

# BFP LC
e.add((16-12, 11), Grid(4, 1))
# Amp
e.add((40-12, 5), Grid(2, 2))
e.add((52-12, 5), Grid(2, 1))
# Amp
e.add((55, 5), Grid(2, 2))
e.add((67, 5), Grid(2, 1))
"""
"""
# ----- Two-band band pass filter -----

# Left switch 0
e.add((5, 9.6), SOT23_6a(rotation_ccw=0))
# Left switch 1
e.add((45, 22), SOT23_6a(rotation_ccw=180))
# Top filter
e.add((40, 17.5), Grid(3, 1))
# Bottom filter
e.add((40, 8), Grid(3, 1))
# Right switch
e.add((53, 9.6), SOT23_6a(rotation_ccw=0))
# Left switch 1
e.add((93, 22), SOT23_6a(rotation_ccw=180))
"""

"""
# ---- Testing multitrace

e.add((10, 10), Grid(2, 2))
points = [(25, 13), (25, 45), (55, 45), (65, 25)]
e.add((0, 0), Multitrace(points))
"""

"""
# ----- Cyrstal Filter and Bi-Directional Amps
# Plessy bilateral amp #1
bx = 5
by = 5
e.add((bx + 18, by +  0), Grid(1, 1))
e.add((bx +  0, by +  6), Grid(2, 1))
e.add((bx +  6, by + 12), Trace(12, 6, rotation_ccw=0))
e.add((bx + 18, by + 12), Grid(1, 1))
e.add((bx +  6, by + 18), Grid(3, 1))
points = [(bx + 9, by + 27), (bx + 33, by + 27), (bx + 33, by + 3), (bx + 21, by + 3)]
e.add((0, 0), Multitrace(points, trace_size=6))

# Plessy bilateral amp #2
bx = 60
by = 5
e.add((bx + 18, by +  0), Grid(1, 1))
e.add((bx +  0, by +  6), Grid(2, 1))
e.add((bx +  6, by + 12), Trace(12, 6, rotation_ccw=0))
e.add((bx + 18, by + 12), Grid(1, 1))
e.add((bx +  6, by + 18), Grid(3, 1))
points = [(bx + 9, by + 27), (bx + 33, by + 27), (bx + 33, by + 3), (bx + 21, by + 3)]
e.add((0, 0), Multitrace(points, trace_size=6))

# Filter
e.add((30, 45), Grid(1, 2))
e.add((36, 45 + 6), Trace(12, 6, rotation_ccw=0))
e.add((42, 32 + 6), Trace(12, 6, rotation_ccw=0))
e.add((48, 45 + 6), Trace(12, 6, rotation_ccw=0))
e.add((54, 32 + 6), Trace(12, 6, rotation_ccw=0))
e.add((60, 45 + 6), Trace(12, 6, rotation_ccw=0))
e.add((72, 45), Grid(1, 2))
"""

"""
# ----- Multi-bandpass filter -----
# NOTES:
# 1. Need a power rail for bottom filter
# 2. Second row of filter could be narrower
bx = 35
by = 10
e.add((bx + 3, by + 6), Grid(9, 1))
e.add((bx + 2*6, by + 0), Grid(1, 1))
e.add((bx + 7*6, by + 0), Grid(1, 1))
e.add((bx + 3*6, by + 0), Trace(6*4, 6, rotation_ccw=0))
e.add((bx + 3*6, by - 6), Grid(3, 1))

bx = 35
by = 40
e.add((bx + 3, by + 6), Grid(9, 1))
e.add((bx + 2*6, by + 0), Grid(1, 1))
e.add((bx + 7*6, by + 0), Grid(1, 1))
e.add((bx + 3*6, by + 0), Trace(6*4, 6, rotation_ccw=0))
e.add((bx + 3*6, by - 6), Grid(3, 1))

e.add((3, 22), PlesseyBilatteral())

# 6v bus
e.add((10, 60), Trace(80, 4, rotation_ccw=0))
"""

"""
# ----- 20m rig mixer ------
e.add((12, 10), ADE1())
e.add((3, 10), Grid(1, 2))
e.add((3, 25), Grid(1, 2))
# LO pad
e.add((18, 25), Grid(2, 1))
"""

# ----- Power Distribution Board

# Relay for controlling T6/G, R12, T12
org = (5, 7)
points = [(3, 0), (3, 1), (4, 1), (4, 0)]
e.add(org, Poly(points, pitch_mm=5))
points = [(4, 0), (4, 1), (5, 1), (5, 0)]
e.add(org, Poly(points, pitch_mm=5))
points = [(5, 0), (5, 4), (6, 4), (6, 0)]
e.add(org, Poly(points, pitch_mm=5))
points = [(0, 1), (5, 1), (5, 4), (6, 4), (6, 5), (0, 5)]
e.add(org, Poly(points, pitch_mm=5))
points = [(0, 6), (6, 6), (6, 9), (0, 9)]
e.add(org, Poly(points, pitch_mm=5))
points = [(6, 0), (12, 0), (12, 3), (7, 3), (7, 5), (6, 5)]
e.add(org, Poly(points, pitch_mm=5))
points = [(6, 5), (7, 5), (7, 3), (12, 3), (12, 6), (6, 6)]
e.add(org, Poly(points, pitch_mm=5))
points = [(6, 6), (12, 6), (12, 9), (6, 9)]
e.add(org, Poly(points, pitch_mm=5))
# LM317 regulator
points = [(0, 9), (1, 9), (1, 10), (0, 10)]
e.add(org, Poly(points, pitch_mm=5))
points = [(1, 9), (2, 9), (2, 10), (1, 10)]
e.add(org, Poly(points, pitch_mm=5))

# Extra for regulators
e.add((80, 2), Grid(1, 3))
e.add((80, 25), Grid(1, 3))
e.add((80, 47), Grid(1, 3))





# -----------------------------------------------------------------
# Draw on the screen
render_corners(c, 0, 0, "#ff0000", render_params)
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
e.mill(gcs, 0, 0, depth, cp)

# Pull out the tool at the end of the work (center of the board)
gcs.comment("Park")
gcs.out("G00 Z" + gcs.dec4(cp.highest_z))
gcs.out("G00 X" + gcs.dec4(cp.board_w / 2.0) + " Y" + gcs.dec4(cp.board_h / 2.0))
# Spindle stop
gcs.out("M05")
gcs.close()

root.mainloop()
