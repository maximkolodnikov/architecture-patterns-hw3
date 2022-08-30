from typing import Tuple

from exceptions import MoveParamsReadError, MoveParamsSetError, CommandException
from abstracts import Rotatable, Movable
from utils import Vector


class MoveCommand:
    """Команда движения объекта по прямой."""

    def __init__(self, m: Movable) -> None:
        self.m = m

    def _read_params(self) -> Tuple[Vector, Vector]:
        try:
            position = self.m.get_position()
            velocity = self.m.get_velocity()
        except Exception as e:
            raise MoveParamsReadError(f"Can't read params for moving object[{self.m}]") from e

        return position, velocity

    def execute(self) -> None:
        position, velocity = self._read_params()
        new_position = position + velocity

        try:
            self.m.set_position(new_position)
        except Exception as e:
            raise MoveParamsSetError(f"Can't set params for moving object[{self.m}]") from e


class RotateCommand:
    """Команда поворота объекта."""

    def __init__(self, r: Rotatable) -> None:
        self.r = r

    def execute(self):
        new_direction = (
            (self.r.get_direction() + self.r.get_angular_velocity())
            % self.r.get_directions_number()
        )
        self.r.set_direction(new_direction)


class CheckFuelCommand:
    """Команда для проверки наличия топлива."""

    def __init__(self, o):
        self.o = o

    def execute(self):
        if self.o.fuel <= 0:
            raise CommandException('run out of fuel')


class BurnFuelCommand:
    """Команда сжигания топлива при движении."""

    def __init__(self, o, burn_rate: int = 1):
        self.o = o
        self.burn_rate = burn_rate

    def execute(self):
        self.o.set_fuel(self.o.fuel - self.burn_rate)


class Move:
    """Макрокоманда движения по прямой с расходом топлива."""

    def __init__(self, o):
        self.subcommands = [
            CheckFuelCommand(o),
            MoveCommand(o),
            BurnFuelCommand(o),
        ]
        self.o = o

    def execute(self):
        for command in self.subcommands:
            command.execute()
