class Submarine:
    def __init__(self):
        self.depth = 0
        self.distance = 0
        self.__aim = 0

    def navigate(self, instruction):
        (direction, distance) = instruction.split(" ")

        if direction == "" or distance == "":
            raise Exception("Invalid command")

        numeric_distance = int(distance)

        match direction:
            case "up":
                self.__aim -= numeric_distance
            case "down":
                self.__aim += numeric_distance
            case "forward":
                self.distance += numeric_distance
                self.depth += numeric_distance * self.__aim
            case _:
                raise Exception("Invalid direction")
