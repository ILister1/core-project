#!/bin/bash

git checkout master
git branch -D dev-branch
git push --delete origin dev-branch