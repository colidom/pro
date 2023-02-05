# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    lane_list = []
    with open(input_path, "r") as input_file:
        for line in input_file:
            strip_lane = line.strip()
            lane_list.append([strip_lane])
        if lane_list[line_no - 1] in lane_list and line_no > 0:
            line = "".join(lane_list[line_no - 1])
        else:
            line = None

    return line


if __name__ == "__main__":
    run("data/get_line/nasdaq.txt", 20)
