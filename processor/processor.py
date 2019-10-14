from structure.command import CommandType

class Processor(object):

    @staticmethod
    def process(case):
        for ri, route in enumerate(case.routes):
            for command in route.commands:
                if command.type == CommandType.TURN:
                    route.turn(command.value)
                if command.type == CommandType.WALK:
                    route.change_pos(command.value)

            case.set_sx(route.x)
            case.set_sy(route.y)

        for ri, route in enumerate(case.routes):
            case.set_aw(route.x, route.y)
