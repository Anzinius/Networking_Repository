# 3. Urllib_lib

## urllib.parse

This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.), to combine the components back into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL.”

</br>

### urlib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

The return value is a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple), which means that its items can be accessed by index or as named attributes, which are:

| Attribute  | Index | Value                              | Value if not present                                         |
| :--------- | :---- | :--------------------------------- | :----------------------------------------------------------- |
| `scheme`   | 0     | URL scheme specifier               | *scheme* parameter                                           |
| `netloc`   | 1     | Network location part              | empty string                                                 |
| `path`     | 2     | Hierarchical path                  | empty string                                                 |
| `params`   | 3     | Parameters for last path element   | empty string                                                 |
| `query`    | 4     | Query component                    | empty string                                                 |
| `fragment` | 5     | Fragment identifier                | empty string                                                 |
| `username` |       | User name                          | [`None`](https://docs.python.org/3/library/constants.html#None) |
| `password` |       | Password                           | [`None`](https://docs.python.org/3/library/constants.html#None) |
| `hostname` |       | Host name (lower case)             | [`None`](https://docs.python.org/3/library/constants.html#None) |
| `port`     |       | Port number as integer, if present | [`None`](https://docs.python.org/3/library/constants.html#None) |

</br>

### urllib.parse.urlsplit(urlstring, scheme='', allow_fragments=True)

The return value is a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple), its items can be accessed by index or as named attributes:

| Attribute  | Index | Value                              | Value if not present                                         |
| :--------- | :---- | :--------------------------------- | :----------------------------------------------------------- |
| `scheme`   | 0     | URL scheme specifier               | *scheme* parameter                                           |
| `netloc`   | 1     | Network location part              | empty string                                                 |
| `path`     | 2     | Hierarchical path                  | empty string                                                 |
| `query`    | 3     | Query component                    | empty string                                                 |
| `fragment` | 4     | Fragment identifier                | empty string                                                 |
| `username` |       | User name                          | [`None`](https://docs.python.org/3/library/constants.html#None) |
| `password` |       | Password                           | [`None`](https://docs.python.org/3/library/constants.html#None) |
| `hostname` |       | Host name (lower case)             | [`None`](https://docs.python.org/3/library/constants.html#None) |
| `port`     |       | Port number as integer, if present | [`None`](https://docs.python.org/3/library/constants.html#None) |