## Introduction

Let us look at how to encrypt text and files using Python.
For this we are going to be using Fernet which is a part of python's cryptography package

## General info

1. Generate a key and save it locally (Only done once)
2. Generate encrypted password and stored it a file locally (Run this when your password changes)
3. Delete clear text password in script
4. To decode the encrypted password (Needs the 2 files stored locally: key + encrypted password)

Steps 1 to 3 is done once.

Step 4 is run whenever we need to run script

Use cases:
Passwords used in your scripts not shown in clear text

## Setup
```
pip install cryptography

```

