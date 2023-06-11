import abc
from fly_behavior import FlyBehavior, FlyWithWings, FlyNoWay
from quack_behavior import QuackBehavior, Quack


class Duck(abc.ABC):
    _fly_behavior: FlyBehavior = None
    _quack_behavior: QuackBehavior = None

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, value: FlyBehavior):
        self._fly_behavior = value

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, value: QuackBehavior):
        self._quack_behavior = value

    @abc.abstractmethod
    def display(self):
        pass

    @staticmethod
    def swim(self):
        print("All ducks float, even decoys!")

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(self):
        # this breaks the second principle of programming to an interface
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")
