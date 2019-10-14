from structure.command import Command, CommandType
from structure.route import Route
from structure.case import Case
from processor.processor import Processor
import time

start_time = time.time()

cases = []

case2 = Case()

route21 = Route(30, 40, 90)
route21.add_command(Command(CommandType.WALK, 5))

route22 = Route(40, 50, 180)
route22.add_command(Command(CommandType.WALK, 10))
route22.add_command(Command(CommandType.TURN, 90))
route22.add_command(Command(CommandType.WALK, 5))

case2.add_route(route21)
case2.add_route(route22)

cases.append(case2)

case3 = Case()

route31 = Route(87.342, 34.30, 0)
route31.add_command(Command(CommandType.WALK, 10.0))

route32 = Route(2.6762, 75.2811, -45.0)
route32.add_command(Command(CommandType.WALK, 40))
route32.add_command(Command(CommandType.TURN, 40.0))
route32.add_command(Command(CommandType.WALK, 60))

route33 = Route(58.518, 93.508, 270)
route33.add_command(Command(CommandType.WALK, 50))
route33.add_command(Command(CommandType.TURN, 90))
route33.add_command(Command(CommandType.WALK, 40))
route33.add_command(Command(CommandType.TURN, 13))
route33.add_command(Command(CommandType.WALK, 5))

case3.add_route(route31)
case3.add_route(route32)
case3.add_route(route33)

cases.append(case3)


for case in cases:
    Processor.process(case)
    print("average x: %s, average y: %s, average worst: %s" % (round(case.sx, 4), round(case.sy, 4), round(case.aw, 5)))

print("--- %s seconds ---" % (time.time() - start_time))
