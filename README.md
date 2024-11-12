# My Project
## RESOURCE
### Video game Library

Attributes
- id (int)
- title (string)
- genre (string)
- rating (int)
- multiplayer (bool)
- price (float)

## Schema
```sql
CREATE TABLE games (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    rating INTEGER,
    multiplayer BOOLEAN,
    price FLOAT
);

```
## REST ENDPOINTS

| Name                                 | Method | Path            |
|--------------------------------------|--------|-----------------|
| Retrieve a list of all games.        | GET    | /games        |
| Get details of a single game by ID.  | GET    | /games/_id_   |
| Add a new game to list.           | PUT    | /games        |
| Update game information.             | POST   | /games/_id_   |
| Delete gamee from list.            | DELETE | /games/_id_   |
