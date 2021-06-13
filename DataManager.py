import json
from Spot import Spot


def read(file):
    json_content = file.read()
    data = json.loads(json_content)

    width = data['width']
    totalRows = data['total_rows']
    unparsedGrid = data["grid"]
    grid = []
    start = None
    end = None
    for row in range(len(unparsedGrid)):
        grid.append([])
        for column in range(len(unparsedGrid)):
            spotType = unparsedGrid[row][column]
            spot = Spot(row, column, width, totalRows)
            if(spotType == "start"):
                start = spot
                spot.make_start()
            elif(spotType == 'end'):
                end = spot
                spot.make_end()
            elif(spotType == 'barrier'):
                spot.make_barrier()

            grid[row].append(spot)
    return grid, start, end


def save(file, grid, total_rows, came_from):
    data = {
        "width": grid[0][0].get_width(),
        'came_from': came_from,
        "path_cost": len(came_from),
        "total_rows": total_rows,
        "grid": []
    }
    for row in range(len(grid)):
        data['grid'].append([])
        for column in range(len(grid[row])):
            spot = grid[row][column]
            spotType = "none"
            if(spot.is_barrier()):
                spotType = "barrier"
            elif(spot.is_end()):
                spotType = "end"
            elif(spot.is_start()):
                spotType = "start"

            data['grid'][row].append(spotType)

    josnContent = json.dumps(data)
    file.write(josnContent)
