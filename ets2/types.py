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
from typing import Dict


@dataclass
class Vector:
    x: float
    y: float
    z: float


def vector_from_dict(value: Dict) -> Vector:
    return Vector(value['x'], value['y'], value['z'])


@dataclass
class Euler:
    heading: float
    pitch: float
    roll: float


def euler_from_dict(value: Dict) -> Euler:
    return Euler(value['heading'], value['pitch'], value['roll'])


@dataclass
class Placement:
    position: Vector
    orientation: Euler


def placement_from_dict(value: Dict) -> Placement:
    return Placement(position=vector_from_dict(value['position']),
                     orientation=euler_from_dict(value['orientation']))