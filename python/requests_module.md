---
layout: default
parent: PYTHON
---
# *Request module*

requests module is used for REST API call

***Example 1:-***

```python
import requests

r = requests.get('https://api.github.com/events');

print(r.text);
```
