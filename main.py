from abstracts import Rotatable, Movable
from commands import Move
from utils import Vector


class SpaceShip(Movable, Rotatable):
    """Класс космического корабля."""

    def __init__(self, pos: Vector, vel: Vector, ang_vel: int, dir: int, dir_num: int, fuel: int):
        self.position = pos
        self.velocity = vel
        self.direction = dir
        self.directions_number = dir_num
        self.angular_velocity = ang_vel
        self.fuel = fuel

    def get_direction(self) -> int:
        return self.direction

    def get_directions_number(self) -> int:
        return self.directions_number

    def get_position(self) -> Vector:
        return self.position

    def get_velocity(self) -> Vector:
        return self.velocity

    def get_angular_velocity(self) -> int:
        return self.angular_velocity

    def set_direction(self, new_dir: int) -> None:
        self.direction = new_dir

    def set_position(self, new_pos: Vector) -> None:
        self.position = new_pos

    def set_fuel(self, val: int) -> None:
        self.fuel = val


if __name__ == '__main__':
    space_ship = SpaceShip(pos=Vector([12, 5]), vel=Vector([-7, 3]), ang_vel=3, dir=3, dir_num=8, fuel=0)

    print('Position before: ', space_ship.position)
    print('FUEL: ', space_ship.fuel)
    move = Move(o=space_ship)
    move.execute()
    print('Position after: ', space_ship.position)
    print('FUEL: ', space_ship.fuel)

    # print('Direction before: ', space_ship.direction)
    # Rotate(space_ship).execute()
    # print('Direction after: ', space_ship.direction)
