import math


class Behaviour:
    def get_result(self, n: int) -> int:
        pass


class Fact(Behaviour):
    def get_result(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


class Sum(Behaviour):
    def get_result(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            res += i
        return res


class Matesha:
    def get_result(self, b: Behaviour, n: int) -> int:
        self.behaviour = b
        return b.get_result(n)

    def get_sin(self) -> float:
        return self.calc_sin()

    def get_cos(self) -> float:
        return self.calc_cos()

    def calc_sin(self) -> float:
        return math.sin(136)

    def calc_cos(self) -> float:
        return math.cos(150)


class Matesha_2(Matesha):
    def get_sin(self) -> float:
        return self.calc_sin()

    def get_cos(self) -> float:
        return self.calc_cos()

    def calc_sin(self) -> float:
        return math.sin(150)

    def calc_cos(self) -> float:
        return math.sin(136)


if __name__ == '__main__':
    behaviour = None
    matesha = Matesha()
    sum_behave = Sum()
    fact_behave = Fact()
    behaviour = fact_behave
    print(matesha.get_result(behaviour, 10))
    matesha2 = Matesha_2()
    print(matesha.get_sin(), matesha2.get_sin())
