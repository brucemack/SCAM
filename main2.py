import tkinter as tk

root = tk.Tk()
root.title("SCAM v0.3 2020-10-22 KC1FSZ")
scale = 1
# My Mac desktop seems to have a different dot-pitch than what TK is expecting
ppmm = scale * root.winfo_fpixels('1m') * (100 / 70)
board_w = 450
board_h = 300
grid_x = 3
grid_y = 5

last_hair_point = None
hair_line_v = None
hair_line_h = None

c = tk.Canvas(root, width=board_w * ppmm, height=board_h * ppmm)


def draw_hair(point):
    global hair_line_h, hair_line_v
    # Undraw
    if hair_line_v is not None:
        c.delete(hair_line_v)
    if hair_line_h is not None:
        c.delete(hair_line_h)
    # Redraw
    hair_line_v = c.create_line((point[0], 0), (point[0], board_h * ppmm), fill="white")
    hair_line_h = c.create_line((0, point[1]), (board_w * ppmm, point[1]), fill="white")


img = tk.PhotoImage(file="~/Downloads/ampboard1.gif")
img = img.zoom(8)
img = img.subsample(3)
print(img.width(), img.height())
c.create_image(0, 0, anchor=tk.NW, image=img)

fill = False
drag = False
drag_start = 0, 0
drag_end = 0, 0
drag_shape = 0

rect_list = []


def render_all():
    for rect in rect_list:
        rect.render(c)


def load_list():
    global rect_list
    print("Loading layout ...")
    rect_list = []
    with open('layout.txt', 'r') as f:
        for line in f.readlines():
            if line.startswith("#"):
                pass
            tokens = line.split("\t")
            if tokens[0] == "rect":
                r = Rect((int(tokens[1]), int(tokens[2])), (int(tokens[3]), int(tokens[4])))
                rect_list.append(r)
    render_all()


def dump_list(event):
    print("Saving layout ...")
    with open('layout.txt', 'w') as the_file:
        for rect in rect_list:
            the_file.write("rect")
            the_file.write('\t')
            the_file.write(str(rect.start[0]))
            the_file.write('\t')
            the_file.write(str(rect.start[1]))
            the_file.write('\t')
            the_file.write(str(rect.end[0]))
            the_file.write('\t')
            the_file.write(str(rect.end[1]))
            the_file.write('\n')


def snap_x(c):
    c0 = int(c / grid_x)
    return c0 * grid_x


def snap_y(c):
    c0 = int(c / grid_y)
    return c0 * grid_y


class Rect:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.selected = False
        self.shape = None

    def contains_point(self, point):
        return (point[0] >= self.start[0]) and \
            (point[0] <= self.end[0]) and \
            (point[1] >= self.start[1]) and \
            (point[1] <= self.end[1])

    def unrender(self, c):
        if self.shape is not None:
            c.delete(self.shape)
            self.shape = None

    def render(self, c):
        self.unrender(c)
        color = "#00ff00"
        if self.selected:
            color = "white"
        fill_color = ""
        if fill:
            fill_color = color
        self.shape = c.create_rectangle(self.start[0], self.start[1],
            self.end[0], self.end[1], fill=fill_color, outline=color, width="2")



def start_drag(point):
    global drag
    global drag_start
    global drag_end
    drag_start = point
    drag_end = point
    drag = True


def end_drag():
    global drag
    global drag_start
    global drag_end
    drag_start = None
    drag_end = None
    drag = False
    c.delete(drag_shape)


def update_drag(point):
    global drag_start
    global drag_end
    global drag_shape
    # Get rid of old shape
    if drag_shape != 0:
        c.delete(drag_shape)
        drag_shape = 0
    drag_end = point[0], point[1]
    drag_shape = c.create_rectangle(drag_start[0], drag_start[1],
        drag_end[0], drag_end[1], fill="", outline="red", activeoutline="yellow", width="2")


def motion(event):
    point = snap_x(event.x), snap_y(event.y)
    if drag:
        update_drag(point)
    draw_hair(point)


def down(event):
    global drag
    global drag_start
    point = snap_x(event.x), snap_y(event.y)
    start_drag(point)


def shift_down(event):
    print("sd")


def up(event):
    global drag
    global rect_list
    point = snap_x(event.x), snap_y(event.y)
    # Create the real box if we've moved
    if drag_start != drag_end:
        r = Rect(drag_start, drag_end)
        r.render(c)
        rect_list.append(r)
    # If we've not moved do a selection
    else:
        # Clear selects
        for rect in rect_list:
            rect.selected = False
        # Select the first item that is under the mouse
        for rect in rect_list:
            if rect.contains_point(point):
                rect.selected = True
                break
        # Redraw
        render_all()

    end_drag()


def delete_key(event):
    global rect_list
    # Remove the deleted items from the screen
    for rect in rect_list:
        if rect.selected:
            rect.unrender(c)
    # Remove from list
    rect_list = [rect for rect in rect_list if not rect.selected]

def toggle_fill(event):
    global fill
    fill = not fill
    render_all()



c.bind('<Motion>', motion)
c.bind("<ButtonPress-1>", down)
c.bind("<ButtonRelease-1>", up)
c.bind("<Shift-ButtonPress-1>", shift_down)
root.bind("<BackSpace>", delete_key)
root.bind("s", dump_list)
root.bind("f", toggle_fill)
c.pack()

load_list()

root.mainloop()
