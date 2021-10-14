---
title: Bench
metatags:
 description: Bench is a CLI tool to manage Frappe Deployments.
---

# Bench

Bench is a CLI tool to manage Frappe Deployments. It provides an easy interface
to help you setup and manage multiple sites and apps based on Frappe Framework.

However, the term bench may mean different things depending on the context. We
use the term "bench" to refer to the CLI tool and the directory interchangeably.
This may get confusing a lot of times.

    A: "Did you update the bench?"
    B: "Yes, migrations for the latest version were smoother this time around."
    A: "What?! I told you to update the CLI tool!"
    B: "Let's hope our clients like Version 13"

To avoid these type of situations, we will refer to **"Bench"** as the bench
directory and **"Bench CLI"** to refer to the CLI tool.

> To install the bench CLI and setup a Frappe environment, follow
> [Installation](/docs/user/en/installation).


This may not be known to a lot of people but half the bench commands we're used
to, exist in the Frappe Framework and not in bench directly. Those commands
generally are the `--site` commands. Even commands like `update` provide easy
wrappers around and invoke multiple Frappe commands such as `backup` and
`migrate` along with some other essential bench and system-level operations.

## References

1. [Bench Commands](/docs/user/en/bench/bench-commands)
1. [Frappe Commands](/docs/user/en/bench/frappe-commands)
1. [Command References](/docs/user/en/bench/reference)
1. [Extending the CLI](/docs/user/en/bench/extending-the-cli)

