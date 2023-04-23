from typing import Any


def players_repr(players: list[dict], verbose: bool) -> None:
    if verbose:
        print(">>>> TEAM:")

    print("Players: ")
    for player in players:
        print(f"{player['name']=}, {player['age']=}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    if players is None:
        raise Exception("players is None")
    if player is None:
        raise Exception("Player is None")
    players.append(player)
    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    res = list(filter(lambda i: i["name"] != name, players))
    print("After deleting: ", res)
    return res


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    res = next((d for d in players if d.get(field) == value),
               [{} for _ in range(1)])
    print(res)


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""
    players_l = [i["name"] for i in players]
    try:
        ind = players_l.index(name)
    except ValueError:
        ind = None

    if ind is not None:
        res = players[ind]
    else:
        res = None

    print("Player information: ", res)
    return res


def main():
    team = [
        {"name": "John", "age": 45, "number": 7},
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
        {"name": "Ihor", "age": 27, "number": 10},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        match input(f"Enter your choice {options}:"):
            case "exit":
                break

            case "repr":
                players_repr(team, True)

            case "add":
                # players_add(...)
                name: str
                print("Adding player\n")
                player_new = dict(
                    input("Enter name and age with space: ").split()
                    for _ in range(2)
                )
                players_add(team, player_new)

            case "del":
                print("Deleting player")
                pl = input("Enter player name: ")
                players_del(team, pl)

            case "find":
                print("Finding player\n")
                player_values = dict(
                    input(
                        "Enter field and value for searching with space: "
                    ).split()
                    for _ in range(1)
                )
                players_find(
                    team, list(player_values.keys())[0],
                    list(player_values.values())[0]
                )

            case "get":
                name = input("Enter name of player: ")
                players_get_by_name(team, name)


if __name__ == "__main__":
    main()
