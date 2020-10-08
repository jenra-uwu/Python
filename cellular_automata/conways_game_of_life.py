"""
Conway's Game of Life implemented in Python.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""

from __future__ import annotations

# Define glider example
GLIDER = [
	[0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0],
	[1, 1, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0]
]


def new_generation(cells: list[list[int]]) -> list[list[int]]:
	next_generation = []
	for i in range(len(cells)):
		next_generation_row = []
		for j in range(len(cells[i])):
			# Get the number of live neighbours
			neighbour_count = cells[i - 1][j - 1] \
							+ cells[i - 1][j + 0] \
							+ cells[i - 1][j + 1] \
							+ cells[i + 0][j - 1] \
							+ cells[i + 1][j + 1] \
							+ cells[i + 1][j - 1] \
							+ cells[i + 1][j + 0] \
							+ cells[i + 1][j + 1]

			# Rules of the game of life (excerpt from Wikipedia):
			# 1. Any live cell with two or three live neighbours survives.
			# 2. Any dead cell with three live neighbours becomes a live cell.
			# 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
			alive = cells[i][j] == 1
			if (alive and 2 <= neighbour_count <= 3) or not alive and neighbour_count == 3:
				next_generation_row.append(1)
			else:
				next_generation_row.append(0)

		next_generation.append(next_generation_row)
	return next_generation
