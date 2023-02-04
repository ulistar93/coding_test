import sys
import copy

class room_state:
    def __init__(self, row, col, A):
        self.row = row
        self.col = col
        self.vacuum_loc = []
        self.dust_loc = set()
        self.dust_map = {}
        self.dust_num = 0
        for r in range(self.row):
            for c in range(self.col):
                k = str(r)+','+str(c)
                if A[r][c] > 0:
                    self.dust_loc.add(k)
                    self.dust_map[k] = A[r][c]
                elif A[r][c] == -1:
                    self.vacuum_loc.append(k)
                    self.dust_map[k] = 0
                else:
                    self.dust_map[k] = 0
        self.dust_num = sum(self.dust_map.values())
        self.vacuum_routine_upper = []
        _vr0, _ = list(map(int, self.vacuum_loc[0].split(',')))
        self.vacuum_routine_upper += [ str(r)+',0' for r in range(_vr0-1, 0, -1) ]
        self.vacuum_routine_upper += [ '0,'+str(c) for c in range(col) ]
        self.vacuum_routine_upper += [ str(r)+','+str(col-1) for r in range(1, _vr0) ]        
        self.vacuum_routine_upper += [ str(_vr0)+','+str(c) for c in range(col-1, -1, -1) ]
        self.vacuum_routine_lower = []
        _vr1, _ = list(map(int, self.vacuum_loc[1].split(',')))
        self.vacuum_routine_lower += [ str(r)+',0' for r in range(_vr1+1, row-1) ]
        self.vacuum_routine_lower += [ str(row-1)+','+str(c) for c in range(col) ]
        self.vacuum_routine_lower += [ str(r)+','+str(col-1) for r in range(row-2, _vr1, -1) ]
        self.vacuum_routine_lower += [ str(_vr1)+','+str(c) for c in range(col-1, -1, -1) ]
        return

    def spread_dust(self):
        new_dust_loc = set()
        new_dust_map = {}
        for r in range(self.row):
            for c in range(self.col):
                k = str(r)+','+str(c)
                new_dust_map[k] = 0
        for d in sorted(list(self.dust_loc)):
            r, c = map(int, d.split(','))
            a = self.dust_map[d]
            new_dust_map[d] += a
            new_dust_loc.add(d)
            if a >=5:
                if r != 0: # up
                    k = str(r-1)+','+str(c)
                    if k not in self.vacuum_loc:
                        new_dust_loc.add(k)
                        new_dust_map[k] += a//5
                        new_dust_map[d] -= a//5
                if c != 0: # left
                    k = str(r)+','+str(c-1)
                    if k not in self.vacuum_loc:
                        new_dust_loc.add(k)
                        new_dust_map[k] += a//5
                        new_dust_map[d] -= a//5
                if r != self.row -1: # below
                    k = str(r+1)+','+str(c)
                    if k not in self.vacuum_loc:
                        new_dust_loc.add(k)
                        new_dust_map[k] += a//5
                        new_dust_map[d] -= a//5
                if c != self.col -1: # right
                    k = str(r)+','+str(c+1)
                    new_dust_loc.add(k)
                    new_dust_map[k] += a//5
                    new_dust_map[d] -= a//5
        self.dust_map = new_dust_map
        self.dust_loc = new_dust_loc
        self.dust_num = sum(self.dust_map.values())
        return self

    def vacuum(self):
        for i in range(1, len(self.vacuum_routine_upper)):
            prev, next = self.vacuum_routine_upper[i-1:i+1]
            self.dust_map[prev] = self.dust_map[next]
            self.dust_loc.discard(next)
            if self.dust_map[prev] > 0:
                self.dust_loc.add(prev)
        for i in range(1, len(self.vacuum_routine_lower)):
            prev, next = self.vacuum_routine_lower[i-1:i+1]
            self.dust_map[prev] = self.dust_map[next]
            self.dust_loc.discard(next)
            if self.dust_map[prev] > 0:
                self.dust_loc.add(prev)
        self.dust_num = sum(self.dust_map.values())
        return self

    def showroom(self, temp_map=''):
        show_map = temp_map if temp_map else self.dust_map
        print_text=""
        for r in range(self.row):
            for c in range(self.col):
                k = str(r)+','+str(c)
                if k in self.vacuum_loc:
                    print_text+="-1 "
                else:
                    print_text+="%2d "% show_map[k]
            print_text+="\n"
        print(print_text)
        return self

def main(r,c,t,a):
    roomState = room_state(r,c,a)
    print("time 0")
    roomState.showroom()
    for t in range(1,t+1):
        print("time %d" % t)
        roomState.spread_dust()
        roomState.showroom()
        roomState.vacuum()
        roomState.showroom()
    return roomState.dust_num

if __name__ == "__main__":
    input_file, answer_file = '', ''
    if len(sys.argv) >= 3:
        answer_file = sys.argv[2]
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]        
    if input_file:
        print("run %s" % input_file)
        input_list = []
        with open(input_file, 'r') as f:
            for line in f:
                input_list.append(list(map(int, line.strip().split(' '))))
        r, c, t = input_list[0]
        a = input_list[1:]
        ans = main(r, c, t, a)
        if answer_file:
            with open(answer_file, 'r') as f:
                answer = int(f.readline().strip())
            print("return %d" % ans)
            print("answer %d" % answer)
            if ans == answer:
                print("Right!")
            else:
                print("Wrong")
        else:
            print("ans: %d" % ans)