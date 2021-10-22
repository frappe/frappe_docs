import click


@click.command("add-command-reference")
@click.argument("command", required=True)
@click.option("--force", "-f", is_flag=True)
def bench_reference(command, force):
	import os
	from frappe.commands import commands
	from frappe_docs.www.docs.user.en.bench.reference import TEMPLATE

	FILE_PATH = f"../apps/frappe_docs/frappe_docs/www/docs/user/en/bench/reference/{command}.md"

	cmd = [x for x in commands if x.name == command]
	if not cmd:
		import sys

		print("Command not found")
		sys.exit(1)

	import jinja2

	cmd = cmd[0]

	flags = [x for x in cmd.params if x.is_flag]
	options = [x for x in cmd.params if not x.is_flag]
	required_stuff = "".join(x.name for x in options + flags if x.required)
	kwargs = {
		**cmd.__dict__,
		"options": options,
		"flags": flags,
		"command_usage": f"bench {cmd.name} [OPTIONS] {required_stuff}",
	}
	file_content = jinja2.Template(TEMPLATE).render(kwargs)

	if os.path.exists(FILE_PATH) and not force:
		print(file_content)
	else:
		with open(FILE_PATH, "w") as f:
			f.write(file_content)
		print(f"File created at {os.path.realpath(FILE_PATH)}")


commands = [bench_reference]
