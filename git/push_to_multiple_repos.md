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
Login to gitlab and create a new repository, to be used as backup of existing github repo.
```

```text
You may also create one more repo (e.g. on codecommit) for backup.
```

Copy URLs of repositories. These will be used later.

## Clone primary repo

1. Now, clone the repository from github, for which backup is needed.
2. `cd` to repo folder.
3. Verify current remotes using `git remote -v`.
4. Add a new remote for multiple push. You may use existing remote as well (e.g. origin), you can skip this step if using existing remote.

    ```shell
    git remote add push-all <remote url of github>.
    ```

5. Register 1st push url (github URL here) using below command:-

    ```shell
    git remote set-url --add --push push-all <remote url of github>
    ```

6. Now, register 2nd push url (gitlab URL here) using below command:-

    ```shell
    git remote set-url --add --push push-all <remote url of gitlab>
    ```

7. Verify all git remotes using `git remote -v`.
8. Now, run `git push push-all` to push changes to all remotes.
9. Verify changes on github.com and gitlab.com. Branch checked-out on local will be available on github and gitlab.
