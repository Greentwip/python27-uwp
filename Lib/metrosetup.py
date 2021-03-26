import metroui, sys, codeop

class PseudoFile:
    def __init__(self, readline=None, write=None):
        self.readline=readline
        self.write=write

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def flush(self):
        pass

    def isatty(self):
        return True

    def read(self, *args):
        raise NotImplementedError

    def fileno(self):
        return 1

def eval(code):
    try:
        exec(code, globals())
    except SystemExit:
        metroui.exit()
        return

compile = codeop.CommandCompiler()
class DontPrint(object):
    def __init__(self, readline=None, write=None):
        self._readline=readline
        self._write=write

    def write(self, message): 
        self._write(message)

sys.path.append("ZIP")
sys.stdout = DontPrint(write=metroui.add_to_stdout) #PseudoFile(write=metroui.add_to_stdout)
#sys.stderr = PseudoFile(write=metroui.add_to_stderr)
#sys.stdin = PseudoFile(readline=metroui.readline)
#sys.stdout = open(os.devnull, 'w')
#sys.stderr = open(os.devnull, 'w')


