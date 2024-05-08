import random
from PIL import Image, ImageDraw


width = int(input("Enter width: "))
height = int(input("Enter height: "))

wallArray = [["wall" for j in range(width + 1)] if i % 2 == 1 else ["wall" for j in range(width)] for i in range((2 * height) + 1)]

mainStack = []
visitedCells = []
currentCell = [random.randint(0, height), random.randint(0, width)]
visitedCells.append(currentCell)
mainStack.append(currentCell)

def getUnvisitedNeighbors(cell):
	neighbors = []
	for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		if cell[0] + dy >= 0 and cell[1] + dx >= 0 and cell[0] + dy < height and cell[1] + dx < width and not ([cell[0] + dy, cell[1] + dx] in visitedCells):
			neighbors.append([cell[0] + dy, cell[1] + dx])
	return neighbors

while len(mainStack) > 0:
	currentCell = mainStack.pop()
	if len(getUnvisitedNeighbors(currentCell)) > 0:
		mainStack.append(currentCell)
		
		chosenCell = random.choice(getUnvisitedNeighbors(currentCell))
		# print(chosenCell)
		if chosenCell[0] == currentCell[0]:
			if currentCell[1] < chosenCell[1]:
				wallArray[chosenCell[0] * 2 + 1][chosenCell[1]] = ""
			else:
				wallArray[currentCell[0] * 2 + 1][currentCell[1]] = ""
		else:
			if currentCell[0] < chosenCell[0]:
				wallArray[chosenCell[0] * 2][chosenCell[1]] = ""
			else:
				wallArray[currentCell[0] * 2][currentCell[1]] = ""
		visitedCells.append(chosenCell)
		mainStack.append(chosenCell)

CELL_SIZE = 5

def generate_maze_image(wallArray):
    # Calculate the dimensions of the maze
    height = len(wallArray) // 2
    width = len(wallArray[0]) if height > 0 else 0

    # Calculate the size of the image
    image_width = width * CELL_SIZE
    image_height = height * CELL_SIZE

    # Create a new image
    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)
    
    # Draw the entrance and exit of the maze
    draw.rectangle((0, 0, CELL_SIZE, CELL_SIZE), fill="green")
    draw.rectangle(((width - 1) * CELL_SIZE, (height - 1) * CELL_SIZE, width * CELL_SIZE, height * CELL_SIZE), fill="red")

    # Draw the walls of the maze
    for y in range(height):
        for x in range(width):
            if wallArray[y * 2][x] == "wall":
                draw.line((x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, y * CELL_SIZE), fill="black", width=1)
            if wallArray[y * 2 + 1][x] == "wall":
                draw.line((x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE, (y + 1) * CELL_SIZE), fill="black", width=1)

    return image

# Example usage:
maze_image = generate_maze_image(wallArray)
maze_image.show()  # displays the image