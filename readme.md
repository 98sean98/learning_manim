# Learning Manim

[Manim](https://github.com/ManimCommunity/manim) is a powerful animation engine for explanatory math videos. It is used by [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) to create videos like [this](https://www.youtube.com/watch?v=jsYwFizhncE).
The goal of this repository is to provide a collection of experiments to learn how to use Manim.
The version of Manim used is the community edition, which is a fork of the original project.

## Installation

The installation was done on a macOS machine.
If you are using a different operating system, please refer to the [official documentation](https://docs.manim.community/en/stable/installation.html).

Install packages from homebrew.

```shell
brew install ffmpeg pango
```

Create and source a virtual environment.

```shell
python -m venv .venv
source .venv/bin/activate
```

Install pip packages.

```shell
pip install pycairo scipy manim
```

Install LaTeX.

```shell
brew install --cask mactex-no-gui
```
