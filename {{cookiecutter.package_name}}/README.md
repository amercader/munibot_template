# {{cookiecutter.bot_name}}

A friendly Twitter bot built with [Munibot](https://github.com/amercader/munibot).

## Install and setup

Install it with pip:

```
pip install {{cookiecutter.pip_name}}
```

And follow the instructions on [Munibot's documentation](https://github.com/amercader/munibot#usage) regarding configuration and setup.

This particular bot requires:

* The backend SQLite database, which you can download from this repo (`data` folder)


This should be referenced in the `[profile:{{cookiecutter.bot_id}}]` section of your `munibot.ini` file:

```
[profile:{{cookiecutter.bot_id}}]
twitter_key=CHANGE_ME
twitter_secret=CHANGE_ME
db_path=/path/to/data/{{cookiecutter.package_name}}.sqlite
```

## License

[MIT](/amercader/munibot/blob/master/LICENSE.txt)
