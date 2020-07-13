# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ


class GcodeStream:
    # An instance of this class collects g-code commands for assembly onto a
    # full milling sequence.

    def __init__(self, filename):
        self.f = open(filename, "w")

    def close(self):
        self.f.close()

    def dec4(self, val):
        return '%.4f' % val

    def out(self, text):
        print(text)
        self.f.write(text + "\r\n")

    def comment(self, text):
        self.out("(" + text + ")")