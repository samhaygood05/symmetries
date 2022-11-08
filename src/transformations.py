import pygame


class Permutation:

    def __init__(self, perm):
        self.perm = perm

    def concatinate(self, other):
        return Permutation([self.perm[other.perm[i]] for i in range(len(self.perm))])

    def classify(self):
        if self.perm == [0, 1, 2, 3, 4]:
            return "identity"
        elif self.perm in [perm.perm for perm in Permutation.order3rotations()]:
            return "order3rotation"
        elif self.perm in [perm.perm for perm in Permutation.order2rotations()]:
            return "order2rotation"
        elif self.perm in [perm.perm for perm in Permutation.flips()]:
            return "flip"
        elif self.perm in [perm.perm for perm in Permutation.order5rotations()]:
            return "order5rotation"
        else:
            return "other"

    @staticmethod
    def identity():
        return Permutation([0, 1, 2, 3, 4])

    @staticmethod
    def order3rotation(static, direction):
        identity = Permutation.identity()
        cycle = [i for i in identity.perm if i not in static]
        if direction == 1:
            identity.perm[cycle[0]], identity.perm[cycle[1]], identity.perm[cycle[2]] = \
                identity.perm[cycle[2]], identity.perm[cycle[0]], identity.perm[cycle[1]]
        elif direction == -1:
            identity.perm[cycle[0]], identity.perm[cycle[1]], identity.perm[cycle[2]] = \
                identity.perm[cycle[1]], identity.perm[cycle[2]], identity.perm[cycle[0]]
        return identity

    @staticmethod
    def flip(cycle):
        identity = Permutation.identity()
        identity.perm[cycle[0]], identity.perm[cycle[1]] = \
            identity.perm[cycle[1]], identity.perm[cycle[0]]
        return identity

    @staticmethod
    def order2rotation(flip1, flip2):
        identity = Permutation.identity()
        return identity.concatinate(Permutation.flip(flip1)).concatinate(Permutation.flip(flip2))

    @staticmethod
    def order3rotations():
        return [
            Permutation.order3rotation([0, 1], 1),
            Permutation.order3rotation([0, 2], -1),
            Permutation.order3rotation([0, 3], 1),
            Permutation.order3rotation([0, 4], -1),
            Permutation.order3rotation([1, 2], -1),
            Permutation.order3rotation([1, 3], 1),
            Permutation.order3rotation([1, 4], -1),
            Permutation.order3rotation([2, 3], 1),
            Permutation.order3rotation([2, 4], -1),
            Permutation.order3rotation([3, 4], 1),
            Permutation.order3rotation([3, 4], -1),
            Permutation.order3rotation([2, 4], 1),
            Permutation.order3rotation([2, 3], -1),
            Permutation.order3rotation([1, 4], 1),
            Permutation.order3rotation([1, 3], -1),
            Permutation.order3rotation([1, 2], 1),
            Permutation.order3rotation([0, 4], 1),
            Permutation.order3rotation([0, 3], -1),
            Permutation.order3rotation([0, 2], 1),
            Permutation.order3rotation([0, 1], -1),
        ]

    @staticmethod
    def flips():
        flips = []
        for i in range(5):
            for j in range(i + 1, 5):
                flips.append(Permutation.flip([i, j]))
        return flips

    @staticmethod
    def order2rotations():
        rotations = [
            Permutation.order2rotation([0, 1], [2, 3]),
            Permutation.order2rotation([0, 2], [1, 3]),
            Permutation.order2rotation([0, 3], [1, 2]),
            Permutation.order2rotation([0, 1], [2, 4]),
            Permutation.order2rotation([0, 2], [1, 4]),
            Permutation.order2rotation([0, 4], [1, 2]),
            Permutation.order2rotation([0, 1], [3, 4]),
            Permutation.order2rotation([0, 3], [1, 4]),
            Permutation.order2rotation([0, 4], [1, 3]),
            Permutation.order2rotation([0, 2], [3, 4]),
            Permutation.order2rotation([0, 3], [2, 4]),
            Permutation.order2rotation([0, 4], [2, 3]),
            Permutation.order2rotation([1, 2], [3, 4]),
            Permutation.order2rotation([1, 3], [2, 4]),
            Permutation.order2rotation([1, 4], [2, 3]),

        ]
        return rotations

    @staticmethod
    def order5rotations():
        return [
            Permutation([4, 0, 1, 2, 3]),
            Permutation([3, 4, 0, 1, 2]),
            Permutation([3, 0, 4, 2, 1]),
            Permutation([2, 0, 4, 1, 3]),
            Permutation([1, 2, 4, 0, 3]),
            Permutation([1, 3, 4, 2, 0]),
            Permutation([1, 4, 0, 2, 3]),
            Permutation([4, 2, 0, 1, 3]),
            Permutation([2, 4, 1, 0, 3]),
            Permutation([2, 4, 3, 1, 0]),
            Permutation([4, 3, 1, 0, 2]),
            Permutation([3, 4, 1, 2, 0]),
            Permutation([4, 2, 3, 0, 1]),
            Permutation([3, 2, 4, 1, 0]),
            Permutation([4, 3, 0, 2, 1]),
            Permutation([3, 2, 0, 4, 1]),
            Permutation([2, 3, 1, 4, 0]),
            Permutation([2, 0, 3, 4, 1]),
            Permutation([4, 0, 3, 1, 2]),
            Permutation([3, 0, 1, 4, 2]),
            Permutation([1, 3, 0, 4, 2]),
            Permutation([1, 4, 3, 0, 2]),
            Permutation([2, 3, 4, 0, 1]),
            Permutation([1, 2, 3, 4, 0]),
        ]

    @staticmethod
    def rotations():
        return [Permutation.identity()] + Permutation.order3rotations() + Permutation.order2rotations() + Permutation.order5rotations()

    def color_by_type(self):
        if self.classify() == "identity":
            return 180, 167, 214
        elif self.classify() == "order3rotation":
            return 234, 153, 153
        elif self.classify() == "order2rotation":
            return 249, 190, 156
        elif self.classify() == "flip":
            return 182, 215, 168
        elif self.classify() == "order5rotation":
            return 255, 229, 153
        else:
            return 164, 194, 244

    @staticmethod
    def create_table(row, col):
        table = []
        for i in range(len(row)):
            table.append([])
            for j in range(len(col)):
                table[i].append(row[i].concatinate(col[j]))
        return table

    @staticmethod
    def disply_table(table, size):
        screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Symmetry Table")
        for i in range(len(table)):
            for j in range(len(table[i])):
                pygame.draw.rect(screen, table[i][j].color_by_type(), (j * size, i * size, size, size))
                pygame.display.flip()

    @staticmethod
    def create_txt_from_table(table, path, name):
        with open(path + name + ".txt", "w") as f:
            for i in range(len(table)):
                for j in range(len(table[i])):
                    f.write(str(table[i][j]) + " & ")
                f.write(r"\\" + "\n")

    def __str__(self):
        if self.classify() == "identity":
            return "1"
        elif self.classify() == "order3rotation":
            if self.perm == Permutation.order3rotations()[0].perm:
                return "r_12"
            elif self.perm == Permutation.order3rotations()[1].perm:
                return "r_-13"
            elif self.perm == Permutation.order3rotations()[2].perm:
                return "r_14"
            elif self.perm == Permutation.order3rotations()[3].perm:
                return "r_-15"
            elif self.perm == Permutation.order3rotations()[4].perm:
                return "r_-23"
            elif self.perm == Permutation.order3rotations()[5].perm:
                return "r_24"
            elif self.perm == Permutation.order3rotations()[6].perm:
                return "r_-25"
            elif self.perm == Permutation.order3rotations()[7].perm:
                return "r_34"
            elif self.perm == Permutation.order3rotations()[8].perm:
                return "r_-35"
            elif self.perm == Permutation.order3rotations()[9].perm:
                return "r_45"
            elif self.perm == Permutation.order3rotations()[10].perm:
                return "r_-45"
            elif self.perm == Permutation.order3rotations()[11].perm:
                return "r_35"
            elif self.perm == Permutation.order3rotations()[12].perm:
                return "r_-34"
            elif self.perm == Permutation.order3rotations()[13].perm:
                return "r_25"
            elif self.perm == Permutation.order3rotations()[14].perm:
                return "r_-24"
            elif self.perm == Permutation.order3rotations()[15].perm:
                return "r_23"
            elif self.perm == Permutation.order3rotations()[16].perm:
                return "r_15"
            elif self.perm == Permutation.order3rotations()[17].perm:
                return "r_-14"
            elif self.perm == Permutation.order3rotations()[18].perm:
                return "r_13"
            elif self.perm == Permutation.order3rotations()[19].perm:
                return "r_-12"
        elif self.classify() == "order2rotation":
            if self.perm == Permutation.order2rotations()[0].perm:
                return "r_12;34"
            elif self.perm == Permutation.order2rotations()[1].perm:
                return "r_12;35"
            elif self.perm == Permutation.order2rotations()[2].perm:
                return "r_12;45"
            elif self.perm == Permutation.order2rotations()[3].perm:
                return "r_13;24"
            elif self.perm == Permutation.order2rotations()[4].perm:
                return "r_13;25"
            elif self.perm == Permutation.order2rotations()[5].perm:
                return "r_13;45"
            elif self.perm == Permutation.order2rotations()[6].perm:
                return "r_14;23"
            elif self.perm == Permutation.order2rotations()[7].perm:
                return "r_14;25"
            elif self.perm == Permutation.order2rotations()[8].perm:
                return "r_14;35"
            elif self.perm == Permutation.order2rotations()[9].perm:
                return "r_15;23"
            elif self.perm == Permutation.order2rotations()[10].perm:
                return "r_15;24"
            elif self.perm == Permutation.order2rotations()[11].perm:
                return "r_15;34"
            elif self.perm == Permutation.order2rotations()[12].perm:
                return "r_23;45"
            elif self.perm == Permutation.order2rotations()[13].perm:
                return "r_24;35"
            elif self.perm == Permutation.order2rotations()[14].perm:
                return "r_25;34"
        elif self.classify() == "order5rotation":
            if self.perm == Permutation.order5rotations()[0].perm:
                return "r_12:34"
            elif self.perm == Permutation.order5rotations()[1].perm:
                return "r_13:25"
            elif self.perm == Permutation.order5rotations()[2].perm:
                return "r_12:35"
            elif self.perm == Permutation.order5rotations()[3].perm:
                return "r_12:45"
            elif self.perm == Permutation.order5rotations()[4].perm:
                return "r_12:-45"
            elif self.perm == Permutation.order5rotations()[5].perm:
                return "r_12:-35"
            elif self.perm == Permutation.order5rotations()[6].perm:
                return "r_12:-34"
            elif self.perm == Permutation.order5rotations()[7].perm:
                return "r_13:24"
            elif self.perm == Permutation.order5rotations()[8].perm:
                return "r_13:45"
            elif self.perm == Permutation.order5rotations()[9].perm:
                return "r_13:-25"
            elif self.perm == Permutation.order5rotations()[10].perm:
                return "r_14:23"
            elif self.perm == Permutation.order5rotations()[11].perm:
                return "r_14:25"
            elif self.perm == Permutation.order5rotations()[12].perm:
                return "r_23:-15"
            elif self.perm == Permutation.order5rotations()[13].perm:
                return "r_35:-24"
            elif self.perm == Permutation.order5rotations()[14].perm:
                return "r_24:15"
            elif self.perm == Permutation.order5rotations()[15].perm:
                return "r_25:-14"
            elif self.perm == Permutation.order5rotations()[16].perm:
                return "r_15:-24"
            elif self.perm == Permutation.order5rotations()[17].perm:
                return "r_34:-12"
            elif self.perm == Permutation.order5rotations()[18].perm:
                return "r_24:35"
            elif self.perm == Permutation.order5rotations()[19].perm:
                return "r_14:-23"
            elif self.perm == Permutation.order5rotations()[20].perm:
                return "r_24:-13"
            elif self.perm == Permutation.order5rotations()[21].perm:
                return "r_14:-35"
            elif self.perm == Permutation.order5rotations()[22].perm:
                return "r_-13:-24"
            elif self.perm == Permutation.order5rotations()[23].perm:
                return "r_-12:-45"
        else:
            return "cyclic"

    def __repr__(self):
        if self.classify() == "identity":
            return "1"
        elif self.classify() == "order3rotation":
            if self.perm == Permutation.order3rotations()[0].perm:
                return "r_12"
            elif self.perm == Permutation.order3rotations()[1].perm:
                return "r_-13"
            elif self.perm == Permutation.order3rotations()[2].perm:
                return "r_14"
            elif self.perm == Permutation.order3rotations()[3].perm:
                return "r_-15"
            elif self.perm == Permutation.order3rotations()[4].perm:
                return "r_-23"
            elif self.perm == Permutation.order3rotations()[5].perm:
                return "r_24"
            elif self.perm == Permutation.order3rotations()[6].perm:
                return "r_-25"
            elif self.perm == Permutation.order3rotations()[7].perm:
                return "r_34"
            elif self.perm == Permutation.order3rotations()[8].perm:
                return "r_-35"
            elif self.perm == Permutation.order3rotations()[9].perm:
                return "r_45"
            elif self.perm == Permutation.order3rotations()[10].perm:
                return "r_-45"
            elif self.perm == Permutation.order3rotations()[11].perm:
                return "r_35"
            elif self.perm == Permutation.order3rotations()[12].perm:
                return "r_-34"
            elif self.perm == Permutation.order3rotations()[13].perm:
                return "r_25"
            elif self.perm == Permutation.order3rotations()[14].perm:
                return "r_-24"
            elif self.perm == Permutation.order3rotations()[15].perm:
                return "r_23"
            elif self.perm == Permutation.order3rotations()[16].perm:
                return "r_15"
            elif self.perm == Permutation.order3rotations()[17].perm:
                return "r_-14"
            elif self.perm == Permutation.order3rotations()[18].perm:
                return "r_13"
            elif self.perm == Permutation.order3rotations()[19].perm:
                return "r_-12"
        elif self.classify() == "order2rotation":
            if self.perm == Permutation.order2rotations()[0].perm:
                return "r_12;34"
            elif self.perm == Permutation.order2rotations()[1].perm:
                return "r_12;35"
            elif self.perm == Permutation.order2rotations()[2].perm:
                return "r_12;45"
            elif self.perm == Permutation.order2rotations()[3].perm:
                return "r_13;24"
            elif self.perm == Permutation.order2rotations()[4].perm:
                return "r_13;25"
            elif self.perm == Permutation.order2rotations()[5].perm:
                return "r_13;45"
            elif self.perm == Permutation.order2rotations()[6].perm:
                return "r_14;23"
            elif self.perm == Permutation.order2rotations()[7].perm:
                return "r_14;25"
            elif self.perm == Permutation.order2rotations()[8].perm:
                return "r_14;35"
            elif self.perm == Permutation.order2rotations()[9].perm:
                return "r_15;23"
            elif self.perm == Permutation.order2rotations()[10].perm:
                return "r_15;24"
            elif self.perm == Permutation.order2rotations()[11].perm:
                return "r_15;34"
            elif self.perm == Permutation.order2rotations()[12].perm:
                return "r_23;45"
            elif self.perm == Permutation.order2rotations()[13].perm:
                return "r_24;35"
            elif self.perm == Permutation.order2rotations()[14].perm:
                return "r_25;34"
        elif self.classify() == "order5rotation":
            if self.perm == Permutation.order5rotations()[0].perm:
                return "r_12:34"
            elif self.perm == Permutation.order5rotations()[1].perm:
                return "r_13:25"
            elif self.perm == Permutation.order5rotations()[2].perm:
                return "r_12:35"
            elif self.perm == Permutation.order5rotations()[3].perm:
                return "r_12:45"
            elif self.perm == Permutation.order5rotations()[4].perm:
                return "r_12:-45"
            elif self.perm == Permutation.order5rotations()[5].perm:
                return "r_12:-35"
            elif self.perm == Permutation.order5rotations()[6].perm:
                return "r_12:-34"
            elif self.perm == Permutation.order5rotations()[7].perm:
                return "r_13:24"
            elif self.perm == Permutation.order5rotations()[8].perm:
                return "r_13:45"
            elif self.perm == Permutation.order5rotations()[9].perm:
                return "r_13:-25"
            elif self.perm == Permutation.order5rotations()[10].perm:
                return "r_14:23"
            elif self.perm == Permutation.order5rotations()[11].perm:
                return "r_14:25"
            elif self.perm == Permutation.order5rotations()[12].perm:
                return "r_23:-15"
            elif self.perm == Permutation.order5rotations()[13].perm:
                return "r_35:-24"
            elif self.perm == Permutation.order5rotations()[14].perm:
                return "r_24:15"
            elif self.perm == Permutation.order5rotations()[15].perm:
                return "r_25:-14"
            elif self.perm == Permutation.order5rotations()[16].perm:
                return "r_15:-24"
            elif self.perm == Permutation.order5rotations()[17].perm:
                return "r_34:-12"
            elif self.perm == Permutation.order5rotations()[18].perm:
                return "r_24:35"
            elif self.perm == Permutation.order5rotations()[19].perm:
                return "r_14:-23"
            elif self.perm == Permutation.order5rotations()[20].perm:
                return "r_24:-13"
            elif self.perm == Permutation.order5rotations()[21].perm:
                return "r_14:-35"
            elif self.perm == Permutation.order5rotations()[22].perm:
                return "r_-13:-24"
            elif self.perm == Permutation.order5rotations()[23].perm:
                return "r_-12:-45"
        else:
            return "flip or other"


if __name__ == "__main__":
    table = Permutation.create_table(Permutation.rotations(), Permutation.rotations())
    # Permutation.create_txt_from_table(table, "/Users/samhaygood/Desktop/", "pentachoron")
    pygame.init()
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if i == 0:
            Permutation.disply_table(table, 12)
            i = 1
