__author__ = 'TH'

w = []
s = []
k = ['add', 'read', 'read']
e = [1, 1]
a = []
test = [w, s, k, e, a]


def run(machine):
    # check if input is useable
    if len(machine) > 5:
        print('Wrong machine!')
        return 0
    w = machine[0]  # process stack
    s = machine[1]  # variable store
    k = machine[2]  # cmd stack
    e = machine[3]  # input (file)
    a = machine[4]  # output (file)
    # if len(e) == 0:
    #     print('empty input!')
    #     return 0
    i = 0
    while len(k) > 0:
        cmd = k.pop()
        if type(cmd) == int:
            w.append(cmd)
        elif cmd == 'read':
            # from first position on input to first position on process stack
            w.append(e.pop())
        elif cmd == 'add' or '+':
            w.append(w.pop() + w.pop())
        elif cmd == 'sub' or '-':
            w.append(w.pop() - w.pop())
        elif cmd == 'mul' or '*':
            w.append(w.pop() * w.pop())
        elif cmd == 'div' or '/':
            w.append(w.pop() / w.pop())
        print('run '+str(i)+': '+str(machine))
        i += 1
    print('success after '+str(i)+' iterations !')
    return 1


# LETS DO THIS!

def main():
    return run(test)

main()