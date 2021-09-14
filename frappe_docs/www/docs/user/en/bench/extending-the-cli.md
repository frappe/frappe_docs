---
title: Bench - Extending the CLI
metatags:
 description: >
  The Bench CLI can be extended by adding commands under your Frappe Applications.
---

# Bench - Extending the CLI

Along with the framework commands, Frappe's `bench_manager` module also searches
for any commands in your custom applications. Thereby, bench communicates with
the respective bench's Frappe which in turn will check for available commands in
all of the applications.

To make your custom command available to bench, just create a `commands` module
under your parent module and write the command with a click wrapper and a
variable commands which contains a list of click functions, which are your own
commands.

The directory structure with a Frappe App `flags` may be visualized as:

```bash
frappe-bench
|──apps
    |── frappe
    ├── flags
    │   ├── README.md
    │   ├── flags
    │   │   ├── commands    <------ commands module
    │   ├── license.txt
    │   ├── requirements.txt
    │   └── setup.py
```

The commands module maybe a single file such as `commands.py` or a directory
with an `__init__.py` file. For a custom application of name 'flags', an example
may be given as

```python
# file_path: frappe-bench/apps/flags/flags/commands.py
import click

@click.command('set-flags')
@click.argument('state', type=click.Choice(['on', 'off']))
def set_flags(state):
    from flags.utils import set_flags
    set_flags(state=state)

commands = [
    set_flags
]
```

and with the context of the current bench, this command maybe executed simply as

```zsh
➜ bench set-flags
Flags are set to state: 'on'
```
