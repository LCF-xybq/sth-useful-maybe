# sth-useful-maybeποΈ

This repository is created for learning teamwork with Git and sharing some scripts.

## π Table of Contents

- π‘  brances : roles of each brance.
- π οΈ scripts : rules of shared scripts.

## π‘brances : roles of each brance.

1. **main** : π
   - stable version for all users, release codes in this brance.
   - do not push.
2. **dev** : π
   - for daily development. new scripts will be merged to this brance first.
   - after testing, new scripts will be merged to **main** brance.
   - do not push. Merge **personal brance** to **dev** brance through operation - 'pull request'.
   - keep in sync with this branch.
3. **feature/xxx** : π
   - personal brance. used for developing new features.
   - after developing, merging to dev branch through 'pull request'.
   - after merging, this brance will be deleted.
   - can push.
   - keep in sync with **dev**.
4. **bugfix/xxx** : π
   - similar to **feature/xxx**

## π οΈ scripts : rules of shared scripts.

1. do not require packages that is difficult to installing.
2. complete Interfaces documents.
3. essential code annotations.
4. pay attention to Coding Standards.

