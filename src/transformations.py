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
        elif self.perm in [perm.perm for perm in Permutation.order4permutations()]:
            return "order4permutation"
        else:
            return "order6permutation"

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
    def flip(static):
        identity = Permutation.identity()
        if len(static) == 3:
            cycle = [i for i in identity.perm if i not in static]
        else:
            cycle = static
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
                for k in range(j + 1, 5):
                    flips.append(Permutation.flip([i, j, k]))
        return flips

    @staticmethod
    def order2rotations():
        return [
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
    def order4permutations():
        return [
            Permutation([0, 4, 1, 2, 3]),
            Permutation([0, 2, 3, 4, 1]),
            Permutation([4, 1, 0, 2, 3]),
            Permutation([2, 1, 3, 4, 0]),
            Permutation([4, 0, 2, 1, 3]),
            Permutation([1, 3, 2, 4, 0]),
            Permutation([3, 0, 2, 4, 1]),
            Permutation([1, 4, 2, 0, 3]),
            Permutation([3, 1, 0, 4, 2]),
            Permutation([2, 1, 4, 0, 3]),
            Permutation([0, 3, 1, 4, 2]),
            Permutation([0, 2, 4, 1, 3]),
            Permutation([3, 4, 2, 1, 0]),
            Permutation([4, 3, 2, 0, 1]),
            Permutation([3, 1, 4, 2, 0]),
            Permutation([4, 1, 3, 0, 2]),
            Permutation([0, 3, 4, 2, 1]),
            Permutation([0, 4, 3, 1, 2]),
            Permutation([4, 0, 1, 3, 2]),
            Permutation([2, 0, 4, 3, 1]),
            Permutation([1, 2, 4, 3, 0]),
            Permutation([1, 4, 0, 3, 2]),
            Permutation([4, 2, 0, 3, 1]),
            Permutation([2, 4, 1, 3, 0]),
            Permutation([3, 2, 0, 1, 4]),
            Permutation([2, 3, 1, 0, 4]),
            Permutation([2, 0, 3, 1, 4]),
            Permutation([3, 0, 1, 2, 4]),
            Permutation([1, 3, 0, 2, 4]),
            Permutation([1, 2, 3, 0, 4]),
        ]

    @staticmethod
    def order6permutations():
        return [
            Permutation([2, 0, 1, 4, 3]),
            Permutation([1, 2, 0, 4, 3]),
            Permutation([1, 0, 3, 4, 2]),
            Permutation([2, 3, 0, 4, 1]),
            Permutation([3, 2, 1, 4, 0]),
            Permutation([1, 0, 4, 2, 3]),
            Permutation([2, 4, 0, 1, 3]),
            Permutation([4, 2, 1, 0, 3]),
            Permutation([3, 4, 0, 2, 1]),
            Permutation([3, 0, 4, 1, 2]),
            Permutation([1, 3, 4, 0, 2]),
            Permutation([2, 4, 3, 0, 1]),
            Permutation([4, 3, 1, 2, 0]),
            Permutation([3, 4, 1, 0, 2]),
            Permutation([4, 2, 3, 1, 0]),
            Permutation([3, 2, 4, 0, 1]),
            Permutation([4, 3, 0, 1, 2]),
            Permutation([4, 0, 3, 2, 1]),
            Permutation([1, 4, 3, 2, 0]),
            Permutation([2, 3, 4, 1, 0]),
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
        elif self.classify() == "order4permutation":
            return 159, 232, 229
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
        screen = pygame.display.set_mode((len(table[0])*size, len(table)*size))
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
        elif self.classify() == "flip":
            if self.perm == Permutation.flips()[0].perm:
                return "f_123"
            elif self.perm == Permutation.flips()[1].perm:
                return "f_124"
            elif self.perm == Permutation.flips()[2].perm:
                return "f_125"
            elif self.perm == Permutation.flips()[3].perm:
                return "f_134"
            elif self.perm == Permutation.flips()[4].perm:
                return "f_135"
            elif self.perm == Permutation.flips()[5].perm:
                return "f_145"
            elif self.perm == Permutation.flips()[6].perm:
                return "f_234"
            elif self.perm == Permutation.flips()[7].perm:
                return "f_235"
            elif self.perm == Permutation.flips()[8].perm:
                return "f_245"
            elif self.perm == Permutation.flips()[9].perm:
                return "f_345"
        elif self.classify() == "order6permutation":
            if self.perm == Permutation.order6permutations()[0].perm:
                return "4p_5234"
            elif self.perm == Permutation.order6permutations()[1].perm:
                return "4p_3452"
            elif self.perm == Permutation.order6permutations()[2].perm:
                return "4p_5134"
            elif self.perm == Permutation.order6permutations()[3].perm:
                return "4p_3451"
            elif self.perm == Permutation.order6permutations()[4].perm:
                return "4p_5124"
            elif self.perm == Permutation.order6permutations()[5].perm:
                return "4p_2451"
            elif self.perm == Permutation.order6permutations()[6].perm:
                return "4p_4152"
            elif self.perm == Permutation.order6permutations()[7].perm:
                return "4p_2514"
            elif self.perm == Permutation.order6permutations()[8].perm:
                return "4p_4153"
            elif self.perm == Permutation.order6permutations()[9].perm:
                return "4p_3514"
            elif self.perm == Permutation.order6permutations()[10].perm:
                return "4p_4253"
            elif self.perm == Permutation.order6permutations()[11].perm:
                return "4p_3524"
            elif self.perm == Permutation.order6permutations()[12].perm:
                return "4p_4521"
            elif self.perm == Permutation.order6permutations()[13].perm:
                return "4p_5412"
            elif self.perm == Permutation.order6permutations()[14].perm:
                return "4p_4531"
            elif self.perm == Permutation.order6permutations()[15].perm:
                return "4p_5413"
            elif self.perm == Permutation.order6permutations()[16].perm:
                return "4p_4532"
            elif self.perm == Permutation.order6permutations()[17].perm:
                return "4p_5423"
            elif self.perm == Permutation.order6permutations()[18].perm:
                return "4p_5123"
            elif self.perm == Permutation.order6permutations()[19].perm:
                return "4p_3152"
            elif self.perm == Permutation.order6permutations()[20].perm:
                return "4p_2351"
            elif self.perm == Permutation.order6permutations()[21].perm:
                return "4p_2513"
            elif self.perm == Permutation.order6permutations()[22].perm:
                return "4p_5312"
            elif self.perm == Permutation.order6permutations()[23].perm:
                return "4p_3521"
            elif self.perm == Permutation.order6permutations()[24].perm:
                return "4p_4312"
            elif self.perm == Permutation.order6permutations()[25].perm:
                return "4p_3431"
            elif self.perm == Permutation.order6permutations()[26].perm:
                return "4p_3421"
            elif self.perm == Permutation.order6permutations()[27].perm:
                return "4p_3142"
            elif self.perm == Permutation.order6permutations()[28].perm:
                return "4p_4123"
            elif self.perm == Permutation.order6permutations()[29].perm:
                return "4p_2413"
            elif self.perm == Permutation.order6permutations()[30].perm:
                return "4p_2341"
        else:
            return f"c_{self.perm[0]+1}{self.perm[1]+1}{self.perm[2]+1}{self.perm[3]+1}{self.perm[4]+1}"

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
        elif self.classify() == "flip":
            if self.perm == Permutation.flips()[0].perm:
                return "f_123"
            elif self.perm == Permutation.flips()[1].perm:
                return "f_124"
            elif self.perm == Permutation.flips()[2].perm:
                return "f_125"
            elif self.perm == Permutation.flips()[3].perm:
                return "f_134"
            elif self.perm == Permutation.flips()[4].perm:
                return "f_135"
            elif self.perm == Permutation.flips()[5].perm:
                return "f_145"
            elif self.perm == Permutation.flips()[6].perm:
                return "f_234"
            elif self.perm == Permutation.flips()[7].perm:
                return "f_235"
            elif self.perm == Permutation.flips()[8].perm:
                return "f_245"
            elif self.perm == Permutation.flips()[9].perm:
                return "f_345"
        elif self.classify() == "order6permutation":
            if self.perm == Permutation.order6permutations()[0].perm:
                return "4p_5234"
            elif self.perm == Permutation.order6permutations()[1].perm:
                return "4p_3452"
            elif self.perm == Permutation.order6permutations()[2].perm:
                return "4p_5134"
            elif self.perm == Permutation.order6permutations()[3].perm:
                return "4p_3451"
            elif self.perm == Permutation.order6permutations()[4].perm:
                return "4p_5124"
            elif self.perm == Permutation.order6permutations()[5].perm:
                return "4p_2451"
            elif self.perm == Permutation.order6permutations()[6].perm:
                return "4p_4152"
            elif self.perm == Permutation.order6permutations()[7].perm:
                return "4p_2514"
            elif self.perm == Permutation.order6permutations()[8].perm:
                return "4p_4153"
            elif self.perm == Permutation.order6permutations()[9].perm:
                return "4p_3514"
            elif self.perm == Permutation.order6permutations()[10].perm:
                return "4p_4253"
            elif self.perm == Permutation.order6permutations()[11].perm:
                return "4p_3524"
            elif self.perm == Permutation.order6permutations()[12].perm:
                return "4p_4521"
            elif self.perm == Permutation.order6permutations()[13].perm:
                return "4p_5412"
            elif self.perm == Permutation.order6permutations()[14].perm:
                return "4p_4531"
            elif self.perm == Permutation.order6permutations()[15].perm:
                return "4p_5413"
            elif self.perm == Permutation.order6permutations()[16].perm:
                return "4p_4532"
            elif self.perm == Permutation.order6permutations()[17].perm:
                return "4p_5423"
            elif self.perm == Permutation.order6permutations()[18].perm:
                return "4p_5123"
            elif self.perm == Permutation.order6permutations()[19].perm:
                return "4p_3152"
            elif self.perm == Permutation.order6permutations()[20].perm:
                return "4p_2351"
            elif self.perm == Permutation.order6permutations()[21].perm:
                return "4p_2513"
            elif self.perm == Permutation.order6permutations()[22].perm:
                return "4p_5312"
            elif self.perm == Permutation.order6permutations()[23].perm:
                return "4p_3521"
            elif self.perm == Permutation.order6permutations()[24].perm:
                return "4p_4312"
            elif self.perm == Permutation.order6permutations()[25].perm:
                return "4p_3431"
            elif self.perm == Permutation.order6permutations()[26].perm:
                return "4p_3421"
            elif self.perm == Permutation.order6permutations()[27].perm:
                return "4p_3142"
            elif self.perm == Permutation.order6permutations()[28].perm:
                return "4p_4123"
            elif self.perm == Permutation.order6permutations()[29].perm:
                return "4p_2413"
            elif self.perm == Permutation.order6permutations()[30].perm:
                return "4p_2341"
        else:
            return f"c_{self.perm[0]+1}{self.perm[1]+1}{self.perm[2]+1}{self.perm[3]+1}{self.perm[4]+1}"


if __name__ == "__main__":
    table = Permutation.create_table(Permutation.rotations()+Permutation.flips()+Permutation.order4permutations()+Permutation.order6permutations(),
                                     Permutation.rotations()+Permutation.flips()+Permutation.order4permutations()+Permutation.order6permutations())
    Permutation.create_txt_from_table(table, "C:/Users/samha/Desktop/", "pentachoron")
    # pygame.init()
    # i = 0
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #     if i == 0:
    #         Permutation.disply_table(table, 10)
    #         i = 1
