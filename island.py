class TropicalIsland:
    __M__ = 0
    __N__ = 0
    __island__ = []
    __island_mask__ = []
    __water_counter__ = 0
    __cells_under_water__ = 0
    __island_size__ = 0

    def __init__(self, M, N, island=None):
        self.__M__ = M
        self.__N__ = N
        self.__island_mask__ = [[False for _ in range(N)] for _ in range(M)]
        self.__water_counter__ = 0
        self.__cells_under_water__ = 0
        self.__island_size__ = M * N
        self.__island__ = island
        if self.__island__ is None:
            self._read_island()

    def rain(self):
        for m, n in self._borders():
            self._update_mask(m, n)

        while self.__cells_under_water__ < self.__island_size__:
            for m in range(1, self.__M__ - 1):
                for n in range(1, self.__N__ - 1):
                    if not self.__island_mask__[m][n]:
                        self._flood_fill(m, n)

        return self.__water_counter__

    def _read_island(self):
        self.__island__ = []
        for m in range(self.__M__):
            self.__island__.append(list(map(int, input().split())))

    def _flood_fill(self, m, n):
        if self._check_flow_out(m, n):
            self._update_mask(m, n)
            return

        old_height = self.__island__[m][n]
        flow_out = False
        stack = [(m, n)]
        stash = []
        used_cells = set()

        while len(stack) > 0:
            m, n = stack.pop()
            if self._check_coords(m, n) and not (m, n) in used_cells and self.__island__[m][n] == old_height:
                self.__island__[m][n] = old_height + 1
                self.__water_counter__ += 1
                stash.append((m, n))
                stack += self._around(m, n)
                used_cells.add((m, n))
                if not flow_out:
                    flow_out = self._check_flow_out(m, n)

        if flow_out:
            for m, n in stash:
                self._update_mask(m, n)

    def _check_coords(self, m, n):
        return not (m > self.__M__ - 1 or m < 0 or n > self.__N__ - 1 or n < 0)

    @staticmethod
    def _around(m, n):
        return [(m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)]

    def _check_flow_out(self, m, n):
        height = self.__island__[m][n]
        stack = self._around(m, n)
        while len(stack) > 0:
            cur_m, cur_n = stack.pop()
            if self._check_coords(cur_m, cur_n) and self.__island_mask__[cur_m][cur_n] \
                    and self.__island__[cur_m][cur_n] <= height:
                return True
        return False

    def _borders(self):
        cords = []
        cords += [(0, i) for i in range(self.__N__)]               # top
        cords += [(i, self.__N__ - 1) for i in range(self.__M__)]  # right
        cords += [(self.__M__ - 1, i) for i in range(self.__N__)]  # bottom
        cords += [(i, 0) for i in range(self.__M__)]               # left
        return cords

    def _update_mask(self, m, n):
        if not self.__island_mask__[m][n]:
            self.__cells_under_water__ += 1
            self.__island_mask__[m][n] = True


def get_water_volume(island):
    return TropicalIsland(len(island), len(island[0]), island=island).rain()

if __name__ == '__main__':
    # island is a list of lists
    island = [
        [999, 201, 999, 200],
        [999, 1, 999, 200],
        [999, 500, 1000, 200],
        ]
    print(get_water_volume(island))
