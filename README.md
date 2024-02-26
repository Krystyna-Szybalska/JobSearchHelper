# JobSearchHelper

A project to help automate job search *and* present skills to potential
future employers. The package name is currently `job_search_helper`, while the
module import name is `job_search`.

## Setup

Easiest way is to create a Conda or Mamba environment, using `mamba env create`.

Alternatively, create a virtual environment manually (e.g. using `pyenv`) and
install the package via `pip install -e .[dev]` (it will be an editable install).

Within your environment, you should be able to run:

```sh
python -c "from job_search import __version__ as v; print(v)"
```

and get a version output.
