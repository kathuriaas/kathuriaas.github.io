---
layout: default
parent: ORACLE
---

# Objects Accessed

Objects accessed in an Oracle session

```sql
set linesize 200
set pagesize 300
col object for a31
col program for a30
col type for a20
col username for a15
SELECT
substr(a.object,1,30) object,
a.type,
a.sid,
b.username,
b.osuser,
b.program
FROM
v$access a,
v$session b
WHERE a.sid = b.sid
AND a.owner = upper('&schema_name')
order by object;
```
