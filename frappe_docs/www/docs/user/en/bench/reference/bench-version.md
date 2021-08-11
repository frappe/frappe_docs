---
title: Bench - bench version
metatags:
  description:
    The Bench CLI has a version command to display the version of your Frappe Apps.
---

# bench version

## Usage

```bash
bench version [OPTIONS]
```

## Description

The `version` command displays compiled info about all the apps installed in the
current bench directory. You can choose your preferred output format: plain
text, JSON or ASCII table. The `--format plain` option displays version
information as plain text, just like `bench version`, but with additional
information.

```bash
$ bench version --format plain
erpnext 14.0.3 version-14 (4e88dcf)
frappe 14.0.1 version-14 (f8ec3d7)
```

The `--format json` option displays version information as a formatted JSON
string. This is particularly useful if you're building tools over the bench CLI.

```json
$ bench version --format json
[
    {
        "app": "erpnext",
        "branch": "version-14",
        "commit": "4e88dcf",
        "version": "14.0.3"
    },
    {
        "app": "frappe",
        "branch": "version-14",
        "commit": "ef0a5e9",
        "version": "14.0.1"
    }
]
```

The `--format table` option displays version information formatted as an ASCII
table.

```bash
$ bench version --format table
+-------------------------+------------+------------------------------+---------+
| App                     | Version    | Branch                       | Commit  |
+-------------------------+------------+------------------------------+---------+
| erpnext                 | 14.0.3     | version-14                   | 4e88dcf |
| frappe                  | 14.0.1     | version-14                   | f8ec3d7 |
+-------------------------+------------+------------------------------+---------+
```

## Options

  - `-f`, `--format` Choose the format for showing versions of the apps
    installed in the current bench. The available options are "plain", "table",
    "json", "legacy". This value defaults to "legacy".


## Examples

1. Get human readable information about the installed apps on current bench,
   with commit messages.

   ```bash
   bench version --format plain
   ```

1. Get bench version information in `JSON` format.

   ```bash
   bench version -f json
   ```
