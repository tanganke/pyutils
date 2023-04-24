# pyutils Documentation

This is pyutils project.

## Getting Start

### Installation

install for development

```shell
git clone --recursive https://github.com/tanganke/pyutils
cd pyutils
pip install -r requirements.txt
pip install -e .
```

or install for usage

```shell
pip install git+https://github.com/tanganke/pyutils
```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    pyutils/
        ...
    scripts/      # entrypoints

## Mkdocs Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.
* `mkdocs gh-deploy --force --no-history` - update github pages mannually.

