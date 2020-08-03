---
layout: default
parent: ORACLE
---
# Materialized view export import

## MView in oracle can be exported and imported using datapump utility:-

### *export mview:-*

```shell
directory=export_dir
dumpfile=export_mv.dmp
logfile=export_mv.log
schemas=<schema_name>
include=table:"IN('<mv1>','<mv2>')
include=materialized_view:”IN('<mv1>','<mv2>')
flashback_time = “to_timestamp(to_char(sysdate,’YYYY-MM-DD HH24:MI:SS’),’YYYY-MM-DD HH24:MI:SS’)"
```

### *import mview:-*

#### **Step 1: import only table of MV from export dump(by excluding mv from export taken above)**

```shell
directory=export_dir
dumpfile=export_mv.dmp
logfile=import_mv.log
schemas=<schema_name>
exclude=materialized_view:"IN('<mv1>','<mv2>')"
```

#### **Step 2 : import only MV definition from export dump**

```shell
directory=export_dir
dumpfile=export_mv.dmp
logfile=import_mv.log
schemas=<schema_name>
include=materialized_view:”IN(‘<mv1>’,'<mv2>’)
```
