#  Copyright (c) 2020. Anders Arnholm <Anders@Arnholm.se>
#
#   Permission to use, copy, modify, and distribute this software for any
#   purpose with or without fee is hereby granted, provided that the above
#   copyright notice and this permission notice appear in all copies.
#
#   THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#   WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#   MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#   ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#   WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#   ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#   OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
from dataclasses import dataclass
from operator import attrgetter
from typing import List

from ets2.telematic import Telematic
from ets2.types import Vector

@dataclass
class TrackPoint:
    position: Vector
    time: int

class Tracks:
    """Keep tracks of where the truck been"""
    def __init__(self):
        self.points: List[TrackPoint] = []
        self.last_time = 0

    def __str__(self):
        return str(self.points)

    def __repr__(self):
        return str(self.points)

    def add_telematic(self, telematic: Telematic) -> bool:
        if telematic.common.game_time > self.last_time:
            self.last_time = telematic.common.game_time
            self.points.append(TrackPoint(position=telematic.truck.world_placement.position, time=self.last_time))
            return True
        return False

    def bottom_left(self) -> (int, int):
        if self.points:
            x = min(self.points, key=attrgetter('position.x')).position.x
            y = min(self.points, key=attrgetter('position.y')).position.y
            z = min(self.points, key=attrgetter('position.z')).position.z
            return x, y, z
        return -139999, 20000  # ATS Hack

    def top_right(self) -> (int, int):
        if self.points:
            x = max(self.points, key=attrgetter('position.x')).position.x
            y = max(self.points, key=attrgetter('position.y')).position.y
            z = max(self.points, key=attrgetter('position.z')).position.z
            return x, y, z
        return -20000, -85000  # ATS Hack