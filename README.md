## Frappe Docs

This is the primary repository for the Frappe Framework Documentation. The
Frappe Framework is a full-stack web application builder, used to create
(among other apps) ERPNext, a 100% open-source enterprise resource planning
system.

To see the installed official documentation for the Frappe Framework, please
visit https://frappeframework.com/docs.

### Contibuting to the Frappe Framework Documentation

1. Install a copy of the documentation locally (see "Installation," below.)

2. Go to the apps/frappe_docs directory of your installation and execute `git pull --unshallow` to ensure that you have the full git repository. Also fork the frappe/frappe_docs repository on Github.

3. Check out a working branch in git (e.g. `git checkout -b my_doc_update`).

4. Make your proposed changes to the documentation sources.

5. Run your local version of the documentation server (e.g. `bench start` in your bench installation).

6. Make sure that your changes appear the way you want them to.

7. Commit your changes to your branch. Make sure to use a semantic commit message.

8. Push your branch to your fork on Github, and issue a pull request.

### Installation

To create a local working copy of the documentation (primarily for purposes of contributing to the documentation, see previous section):

1. In your local installation of "bench" (see the README at https://github.com/frappe/bench for further information on how to install bench), create a new site with a fresh subdomain/domain name, e.g. `bench new-site YOURSUB.YOURDOMAIN.TLD` where of course you need to replace the text in all caps.

2. Execute `bench get-app frappe_docs`.

3. Execute `bench --site YOURSUB.YOURDOMAIN.TLD install-app frappe_docs`.

4. Execute `bench start`. The log that will be produced will mention the port that Frappe is listening on, which we will write as PORT. (The port depends on whether you have other sites installed on your machine and other configuration details, but is typically something like 8000 or 8001.) If you direct your browser to http://YOURSUB.YOURDOMAIN.TLD:PORT/docs, you should see the Frappe Framework Documentation displayed.

#### License

MIT