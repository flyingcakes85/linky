# Linky

A dead simple static site URL shortener.

For detailed usage, code explanation and hosting, see [x.snehit.dev/linky](https://x.snehit.dev/linky).

## How to use?

Create a `links.json` file with route and redirect specified as follows:

```json
{
  "/": "https://snehit.dev",
  "tw": "https://x.com/flyingcakes85",
  "gh": "https://github.com/flyingcakes85"
}
```

You can add as many routes as you want, as long as there are no duplicates.

Now, invoke the bundled `linky.py`, passing path of the `links.json` file you just created.

```sh
python linky.py links.json
```

You can change the output folder via `-o`/`--output-dir` flag.

```sh
python linky.py links.json --ouptut-dir public
```

Additionally, any files in `static` folder will be copied as it is to the build output folder.

## License

MIT