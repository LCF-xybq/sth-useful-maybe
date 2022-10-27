# sth-useful-maybe🖐️

This repository is created for learning teamwork with Git and sharing some scripts.

## 📖 Table of Contents

- 💡  brances : roles of each brance.
- 🛠️ scripts : rules of shared scripts.

## 💡brances : roles of each brance.

1. **main** : 👇
   - stable version for all users, release codes in this brance.
   - do not push.
2. **dev** : 👇
   - for daily development. new scripts will be merged to this brance first.
   - after testing, new scripts will be merged to **main** brance.
   - do not push. Merge **personal brance** to **dev** brance through operation - 'pull request'.
   - keep in sync with this branch.
3. **feature/xxx** : 👇
   - personal brance. used for developing new features.
   - after developing, merging to dev branch through 'pull request'.
   - after merging, this brance will be deleted.
   - can push.
   - keep in sync with **dev**.
4. **bugfix/xxx** : 👇
   - similar to **feature/xxx**

## 🛠️ scripts : rules of shared scripts.

1. do not require packages that is difficult to installing.
2. complete Interfaces documents.
3. essential code annotations.
4. pay attention to Coding Standards.

