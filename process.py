from structure.command import Command, CommandType
from structure.route import Route
from structure.case import Case
from processor.processor import Processor
from random import randrange, choice
import time
import resource

start_time = time.time()


def generator():
    case = Case()
    for cr in range(randrange(0, 19)):
        x = randrange(-1000, 1000)
        y = randrange(-1000, 1000)
        r = randrange(-360, 360)
        route = Route(x, y, r)
        for cc in range(randrange(1, 24)):
            command_type = choice(list(CommandType))

            if command_type == CommandType.TURN:
                command = Command(command_type, randrange(-360, 360))
            else:
                command = Command(command_type, randrange(-1000, 1000))

            route.add_command(command)
        case.add_route(route)
    yield case


for i in reversed(range(99)):
    g = generator()
    g_case = g.next()
    Processor.process(g_case)
    print("average x: %s, average y: %s, average worst: %s" % (round(g_case.sx, 4), round(g_case.sy, 4), round(g_case.aw, )))

print("--- %s seconds ---" % (time.time() - start_time))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)