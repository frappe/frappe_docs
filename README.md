# Frappe Docs

> This GitHub repository is archived since we now use a different contribution pipeline.
> 
> You can directly contribute to the documentation through [frappeframework.com](https://frappeframework.com/). For new contribution guidelines, refer to [frappeframework.com/contribute](https://frappeframework.com/contribute).

This is the repository for the Frappe Framework Documentation. Learn more about
Frappe Framework on the [official website](https://frappeframework.com) and the
[GitHub repository](https://github.com/frappe/frappe).

This documentation is hosted on [https://frappeframework.com/docs](https://frappeframework.com/docs).

## Local Setup

To create a local working copy of the documentation (primarily for purposes of
contributing to the documentation):

1. Install `frappe-bench` and setup a bench directory by following the
   [Installation Steps](https://frappeframework.com/docs/user/en/installation).
1. Start the server by running `bench start`.
1. In a separate terminal window, create a new site by running `bench new-site frappeframework.test`.
1. Run `bench get-app frappe_docs`.
1. Run `bench --site frappeframework.test install-app frappe_docs`.
1. Now open the URL [http://frappeframework.test:8000/docs](http://frappeframework.test:8000/docs)
   in your browser, you should see the Frappe Framework Documentation.

## Contributing

1. Go to the `apps/frappe_docs` directory of your installation and execute `git
   pull --unshallow` to ensure that you have the full git repository. Also fork
   the `frappe/frappe_docs` repository on GitHub.
1. Check out a working branch in git (e.g. `git checkout -b my_doc_update`).
1. Make your proposed changes to the documentation sources.
1. Run your local version of the documentation server (e.g. `bench start` in
   your bench installation). Make sure that your changes appear the way you want
   them to.
1. Commit your changes to your branch. Make sure to use a semantic commit
   message.
1. Push your branch to your fork on Github, and issue a pull request.

## License

MIT
