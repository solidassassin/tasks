# Task of writing tests for Python command-line application

-----
Intro
-----

This repository holds a simple command-line application called `upper_case_file`. It simply takes a text file as an
input, and converts its contents to upper case. The application is written using 
[click](https://click.palletsprojects.com) module. The application can be launched using the following command:

```commandline
python upper_case_file.py --input-file ~/Documents/my_input.txt --output-file ~/Documents/my_output.txt
```

Which will convert text file `my_input.txt` from this...

```text
Betty Botter bought some butter but, said she, the butter’s bitter.
```

To this in `my_output.txt` ...

```text
BETTY BOTTER BOUGHT SOME BUTTER BUT, SAID SHE, THE BUTTER’S BITTER.
```

----
Task
----

Write a test using `pytest`, which would validate **command-line application** `upper_case_file`. 
You will find test data in `data` folder. It contains input files and reference files. 
For example, `betty.input.txt` file contents, when processed with the application, should match `betty.output.txt`.
Cover **ALL 10 files** with tests

Don't forget to keep your test project and code nice and clean! 
(Sorry, forgot to wrap console application in nice project structure!)

Protip: Use [CliRunner](https://click.palletsprojects.com/en/7.x/api/?highlight=clirunner#click.testing.CliRunner) to
run console applications in python tests
