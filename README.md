# Screenplay Word Count
Count occurrences of words and phrases in TV shows.

```
Usage:
    swc <show> <regexp> [options]

Options:
    -h --help        Show this screen.
    -v --verbose     Output actual lines.
```

### Example

![alt text](https://i.imgur.com/Z4MzeL6.png)



**OR**


### Run with Docker

```
docker run eprykhodko/screenplay:latest swc 'brooklyn nine nine' 'sex tape' -v
```
