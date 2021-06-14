import json
import Spot


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
            spot = Spot.create_spot(row, column, width, totalRows)
            if(spotType == "start"):
                start = spot
                spot = Spot.make_start(spot)
            elif(spotType == 'end'):
                end = spot
                spot = Spot.make_end(spot)
            elif(spotType == 'barrier'):
                spot = Spot.make_barrier(spot)

            grid[row].append(spot)
    return grid, start, end


def save(file, grid, total_rows, came_from):
    data = {
        "width": Spot.get_width(grid[0][0]),
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
            if(Spot.is_barrier(spot)):
                spotType = "barrier"
            elif(Spot.is_end(spot)):
                spotType = "end"
            elif(Spot.is_start(spot)):
                spotType = "start"

            data['grid'][row].append(spotType)

    josnContent = json.dumps(data)
    file.write(josnContent)
