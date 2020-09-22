# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import os
import io
import json
import sys
from glob import glob


def execute():
	validate_sidebar_jsons()


def validate_sidebar_jsons():
	cwd = os.getcwd()
	files = glob(cwd + "/**/_sidebar.json", recursive=True)

	for file_path in files:

		with io.open(file_path) as f:
			content = f.read()
			try:
				json.loads(content)
			except json.decoder.JSONDecodeError:
				print("\n ❌ Invalid sidebar.json at " + file_path)
				sys.exit(1)

	print("👍 All sidebar.json's are valid")
	sys.exit(0)


if __name__ == "__main__":
	execute()
