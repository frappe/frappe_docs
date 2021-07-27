---
add_breadcrumbs: 1
title: Search - API
metatags:
 description: >
  Full Text Search in Frappe
---

# Search

Searching in Frappe is managed by the [Search](https://github.com/frappe/frappe/blob/develop/frappe/search) module. It is a wrapper for [Whoosh](https://pypi.org/project/Whoosh/) a full text search library written in Python.

You can extend the `FullTextSearch` class to create a search class for a specific requirement. For example the [`WebsiteSearch`](https://github.com/frappe/frappe/blob/develop/frappe/search/website_search.py) is a wrapper for indexing public facing web pages and exposing a search.

## The `FullTextSearch` class

Each FullTextSearch (FTS) instance holds a Schema defined by the class itself. That means, a specific FTS implementation will have it's specific schema. You can create a new implementation if you wish to index with a different schema. Along with this the `FTS` class has other controllers to facilitate creating, updating and querying the index.

### Extending the FTS class

When initializing a FTS based class, you need to provide an index name. On instantiation, the following params are initialized
- `index_name`: name of the index provided.
- `index_path`: path of the index in the sites folder
- `schema`: return by the `get_schema` function
- `id`: id used to recognize the document in the index

Once instantiated you can run the `build` function. It gets all the documents from `get_items_to_index`, the documents are a list of `frappe._dict` (frappe dicts) conforming to the defined schema. These documents are then added to the index and written to the file.

You can search the index using the `search` method of the FTS class. These functions are documented in the API reference [here](/docs/user/en/api/full-text-search).

An example implementation for blog will look like the following:

```python
class BlogWrapper(FullTextSearch):
	# Default Schema
	# def get_schema(self):
	# 	return Schema(name=ID(stored=True), content=TEXT(stored=True))

	# def get_id(self):
	# 	return "name"

	def get_items_to_index(self):
		docs = []
		for blog_name in get_all_blogs():
			docs.append(get_document_to_index(blog_name))
		return docs

	def get_document_to_index(self, name):
		blog = frappe.get_doc("Blog Post", name)
		return frappe._dict(name=name, content=blog.content)

	def parse_result(self, result):
		return result["name"]
```

- `get_items_to_index`: Get all routes to be indexed, this includes the static pages in www/ and routes from published documents
- `get_document_to_index`: Render a page and parse it using BeautifulSoup
- `parse_result`: all the search results are parsed using this function
