import threading
import time
import sys


class WallPainter:

    def __init__(self, wallIndex):
        self.wallIndex = wallIndex

    def paint_wall(self):
        time.sleep(1)
        sys.stdout.write('Wall ' + str(self.wallIndex) + ' painted\n')


def work():
    wall_painter_list = [
        WallPainter(1),
        WallPainter(2),
        WallPainter(3),
        WallPainter(4)
    ]
    work_single_threaded(wall_painter_list)
    work_multi_threaded(wall_painter_list)


def work_single_threaded(wall_painter_list):
    sys.stdout.write('\nworking single-threaded\n')
    start_time = time.time()

    for wall_painter in wall_painter_list:
        wall_painter.paint_wall()

    exec_time = str(round(time.time() - start_time, 2))
    sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n')


def work_multi_threaded(wall_painter_list):
    sys.stdout.write('\nworking multi-threaded\n')
    start_time = time.time()

    thread_list = []
    for wall_painter in wall_painter_list:
        thread = threading.Thread(target=wall_painter.paint_wall)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    exec_time = str(round(time.time() - start_time, 2))
    sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n')
