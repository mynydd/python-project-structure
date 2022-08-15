Demonstrates one way of structuring a Python project.

Unit tests can be run as follows
```
pytest tests
```

`pyproject.toml` declares the module(s) being defined by the project:
```
packages = [
    { include = "package_a", from = "src" },
    ]
```

See:
* https://python-packaging.readthedocs.io/en/latest/minimal.html
* https://blog.ionelmc.ro/2014/05/25/python-packaging/
* https://doc.pytest.org/en/latest/explanation/goodpractices.html
* https://python-poetry.org/docs/pyproject/
