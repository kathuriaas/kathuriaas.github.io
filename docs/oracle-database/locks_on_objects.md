---
layout: default
parent: ORACLE
---
# Locks in Oracle

Below SQL can be used to find locks on objects in Oracle:-

```sql

SELECT p.spid unix_spid,s.sid sid,p.addr,s.paddr,
substr(s.username, 1, 10) username,
substr(s.schemaname, 1, 10) schemaname,
s.command command,
substr(s.osuser, 1, 10) osuser,
substr(s.machine, 1, 25) machine
FROM v$session s, v$process p
WHERE s.paddr=p.addr
and s.sid in (SELECT SESSION_ID from v$locked_object)
ORDER BY p.spid;

```
