---
layout: default
parent: GIT
---

# Multiple remote URLs

This document is used to add multiple remotes to a single repo. This will help to backup single repository to multiple remote repositories.

This is useful in cases, when we want to sync our github repo to bitbucket/gitlab/codecommit etc.

Follow below steps to add multiple remote URLs to a repo and register remote as push URLs. This way, when we perform `git push <remote_name>`, changes will be pushed to all remote repositories in one go.

Follow below steps to achieve this. We will assume an existing repo on github has to be cloned loaclly and all changes have to be pushed to other repositories.

## Create new repositories

```text
Login to codecommit and create a new repository, to be used as backup of existing github repo.
```

```text
You may also create one more repo (e.g. on gitlab) for backup.
```

Copy URLs of repositories.