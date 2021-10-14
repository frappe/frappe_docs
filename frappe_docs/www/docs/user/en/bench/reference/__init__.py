
TEMPLATE = """---
title: Bench - bench {{ name }}
metatags:
 description: >
  {{ help }}
---

# bench {{ name }}

## Usage

```bash
{{ command_usage }}
```

## Description

{{ description_long }}

{% if options %}
## Options

{% for option in options %}
 - `{{ option.name }}` {{ option.help }}
{% endfor %}

{% endif %}

{% if flags %}
## Flags
{% for flag in flags %}
 - `{{ flag.name }}` {{ flag.help }}
{% endfor %}
{% endif %}

### Examples

1. Description of example 1.

    ```bash
    bench {{ name }} content of example 1
    ```

1. Description of example 2.

    ```bash
    bench {{ name }} content of example 2
    ```
"""