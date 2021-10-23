---
add_breadcrumbs: 1
title: Asset Bundling
metatags:
 description: A guide to understanding how static asset bundling works in Frappe Framework.
---

# Asset Bundling

A guide to understanding how static asset bundling works in Frappe Framework.

Frappe ships with a Rich Admin UI accessible at `/app` which is an SPA written
in modern JavaScript syntax and styling which is written in SASS (`.scss`)
files. These files are not directly understandable by the browser and hence need
to be compiled before they are sent to the browser to parse and execute.

Frappe ships with an asset bundler that can compile client side assets like:

- `.js` (Modern syntax with `import` and `export`)
- `.ts` (TypeScript files)
- `.vue` (Vue single file components)
- `.css` (CSS processed using PostCSS)
- `.scss` (SASS files)
- `.sass` (SASS files with indentation syntax)
- `.styl` (Stylus files)
- `.less` (Less files)

These files are compiled to `.js` or `.css` depending on the type and are sent
to the browser.

## Building assets

To compile assets using the asset bundler, you run the following command from
the `frappe-bench` folder:

```sh
$ bench build
```

You can also run it for specific apps by giving it the `--apps` option.

```sh
# build only frappe assets
$ bench build --apps frappe

# build only frappe and erpnext assets
$ bench build --apps frappe,erpnext
```

## Watch mode

When you are working with bundled files you need the build command to run every
time you make a change to your source files. The asset bundler comes with a
watch mode where it will listen to changes in the file system and rebuild
whenever a file changes.

Running the following command will start a long-running process that watches
your files and rebuilds them as they change. It will log a line with the text
"Compiled changes..." every time it does a rebuild.

```sh
$ bench watch
Watching for changes...
1:17:28 PM: Compiled changes...
```

You can also run it for specific apps by giving it the `--apps` option.

```sh
# watch only erpnext assets
$ bench watch --apps erpnext
```

Starting with Version 14, [Desk](/docs/user/en/desk) will be automatically reloaded if assets get rebuilt in watch mode. This behavior can be toggled by setting the `LIVE_RELOAD` environment variable, or changing the value for `live_reload` in [`common_site_config.json`](/docs/user/en/basics/site_config#common-site-config).


## Bundle files

A bundle file is an entry point of an asset that is picked up by the bundler for
compilation. For e.g., if there is a file named `main.bundle.js` in the public
folder of your app it will be automatically picked up by the bundler and
compiled at `/assets/[app]/dist/js/main.bundle.[hash].js`. A unique hash
computed from the contents of the output is also appended to the file name which
is useful for cache-busting in browsers.

Similarly, if there is a file named `style.bundle.scss` in the public folder, it
will be compiled to `/assets/[app]/dist/css/style.bundle.css`. Notice, the
extension changed from `.scss` from `.css` because browsers can understand CSS
files but not SASS files. Bundle files can exist at any nesting level in the
`public` folder, but they will always be compiled in either `dist/js` or
`dist/css` depending upon their type. This means if there is a file at
`public/main.bundle.js` and another file at `public/src/main.bundle.js` the
compiled output of the latter will override. The bundler will also print a
warning for such collisions.

Some more examples of bundle inputs and their outputs:

| Input                                    | Output                                          |
| ---------------------------------------- | ----------------------------------------------- |
| `[app]/public/main.bundle.js`            | `/assets/dist/[app]/js/main.bundle.[hash].js`   |
| `[app]/public/src/main.bundle.js`        | `/assets/dist/[app]/js/main.bundle.[hash].js`   |
| `[app]/public/src/utils/utils.bundle.js` | `/assets/dist/[app]/js/utils.bundle.[hash].js`  |
| `[app]/public/main.bundle.ts`            | `/assets/dist/[app]/js/main.bundle.[hash].js`   |
| `[app]/public/main.bundle.css`           | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/styles/main.bundle.css`    | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.scss`          | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.sass`          | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.styl`          | `/assets/dist/[app]/css/main.bundle.[hash].css` |
| `[app]/public/main.bundle.less`          | `/assets/dist/[app]/css/main.bundle.[hash].css` |

## Importing libraries from npm

If you are familiar with modern web development, you might need to install
3rd-party libraries from npm and use it in your project.

Let's say you want to use the `dayjs` library for working with Date and Time in
your app. You first install it using `yarn` by running the following command
from the root of your apps folder.

```sh
$ cd frappe-bench/apps/myapp
$ yarn add dayjs
```

Now, you can import it in your source files like so:

**myapp/public/main.bundle.js**
```js
import * as dayjs from 'dayjs';

console.log(dayjs())
```

## Including bundled assets in HTML

When a bundle file is compiled, the output file contains a unique hash. So, you
cannot hardcode the path of the file because the next time you make a change to
that file the hash will change. Frappe provides a couple of helpers to do this.

### Including assets in custom HTML files

The Jinja methods `include_script` and `include_style` will output the correct
path of the file including the HTML markup for `.js` and `.css` files respectively.

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My App</title>

    {% raw -%}
    {{ include_style('style.bundle.css') }}
    {%- endraw %}
</head>
<body>
    <div id="myapp"></div>

    {% raw -%}
    {{ include_script('main.bundle.js') }}
    {%- endraw %}
</body>
</html>
```

**index.html (Rendered)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My App</title>

    <link type="text/css" rel="stylesheet" href="/assets/myapp/dist/css/style.bundle.SYKETW5P.css">
</head>
<body>
    <div id="myapp"></div>

    {% raw -%}
    <script type="text/javascript" src="/assets/myapp/dist/js/main.bundle.BYJXV4LB.js"></script>
    {%- endraw %}
</body>
</html>
```

### Including assets in app.html

If you want to include bundled assets from your app in `/app` you can use the
`app_include_js` and `app_include_css` to load them into app.html.

**[app]/hooks.py**
```py
app_include_js = ['main.bundle.js']
app_include_css = ['style.bundle.css']
```

### Get bundled asset path

If for some reason you need only the path of the bundled asset, you can use the
`bundled_asset` Jinja method to generate it.

**Jinja**
```
{% raw -%}{{ bundled_asset('main.bundle.js') }}{%- endraw %}
```

**Rendered**
```html
/assets/myapp/dist/js/main.bundle.BYJXV4LB.js
```

### Python API

These APIs are also available in python. You can import them from jinja_globals.py.

```py
from frappe.utils.jinja_globals import bundled_asset, include_script, include_style

bundled_asset('main.bundle.js')
```

## Including bundled assets lazily in `/app`

If you want to lazy load bundled assets inside the Admin UI (`/app`) you can
use the `frappe.require` method.

```js
frappe.require('main.bundle.js').then(() => {
  // main.bundle.js is now loaded
})
```

This approach is useful when you want to load your code based on some condition.
The first page load won't be impacted and is better for performance.

## Production Mode

When deploying your app to production, you can build your assets in production
mode. In this mode, the bundler will minify the final output of your bundle
which results in smaller file sizes.

To build your assets in production mode, run the following command:
```sh
$ bench build --production
```
