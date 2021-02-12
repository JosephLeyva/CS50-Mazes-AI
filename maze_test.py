
import pytest
import maze


@pytest.mark.parametrize(
    "archivo, meta",
    [
        ( "laberinto/maze1.txt", (0,5) ),
        ( "laberinto/maze2.txt", (8,13)),
        ( "laberinto/maze3.txt", (2,1) ),
        ( "laberinto/maze4.txt", (1,1) ),
        ( "laberinto/maze5.txt", (6,19) )
    ]
)
def test_maze_solution(archivo, meta): 
    m = maze.Maze(archivo)
    m.solve()
    assert m.solution[1][-1] == meta, "prueba de solución fallada"


