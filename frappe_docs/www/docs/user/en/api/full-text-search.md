## FullTextSearch API Reference

Frappe Wrapper for [Whoosh](https://pypi.org/project/Whoosh/)

### `update_index_by_name(self, doc_name)`

Wraps `update_index` method, gets the document from name and updates the index. This function changes the current user and should only be run as administrator or in a background job.

Args:

- self (object): FullTextSearch Instance
- doc_name (str): name of the document to be updated

### `remove_document_from_index(self, doc_name)`
Remove document from search index

Args:

- self (object): FullTextSearch Instance
- doc_name (str): name of the document to be removed

### `update_index(self, document)`
Update search index for a document

Args:

- self (object): FullTextSearch Instance
- document (_dict): A dictionary with title, path and content


### `build_index(self)`
Build index for all parsed documents

### `search(self, text, scope=None, limit=20)`
Search from the current index

Args:

- text (str): String to search for
- scope (str, optional): Scope to limit the search. Defaults to None.
- limit (int, optional): Limit number of search results. Defaults to 20.

Returns:

- [list(_dict)]: Search results
