__author__ = 'TH'

# anfang
w = ['x']
s = []
k = ['output', '=', 1, 1, 'not', True, 'add', 'read', 'read', 'skip', 'assign', 42]
e = [1, 1]
a = []
test = [w, s, k, e, a]


def run(machine):   # delta
    w = machine[0]  # process stack
    s = machine[1]  # variable store
    k = machine[2]  # cmd stack
    e = machine[3]  # input (file)
    a = machine[4]  # output (file)
    i = 0
    while len(k) > 0:
        cmd = k.pop()
        if type(cmd) == int:
            w.append(cmd)
        elif type(cmd) == bool:
            w.append(cmd)
        elif cmd == 'not':
            b = not w.pop()
            w.append(b)
        elif cmd == '=':
            w.append(w.pop() == w.pop())
        elif cmd == 'read':
            w.append(e.pop())
        elif cmd == 'add' or cmd == '+':
            w.append(w.pop() + w.pop())
        elif cmd == 'sub' or cmd == '-':
            w.append(w.pop() - w.pop())
        elif cmd == 'mul' or cmd == '*':
            w.append(w.pop() * w.pop())
        elif cmd == 'div'or cmd == '/':
            w.append(w.pop() / w.pop())
        elif cmd == 'skip':
            pass
        elif cmd == 'assign':
            s.append((w.pop(), w.pop()))
        elif cmd == 'output':
            a.append(w.pop())
        print('run ' + str(i) + ': ' + str(machine))
        i += 1
    print('success after '+str(i)+' iterations !')
    return 1


# LETS DO THIS!

def main():
    return run(test)

main()