# Project 2: CS 61A Autocorrected Typing Software <kbd>[cats.zip](./cats.zip)</kbd>

![cats_typing](./cats_typing.gif)

​																													*Programmers dream of*
​																												*Abstraction, recursion, and*
​																														*Typing really fast.*

## Introduction

> **Important submission note:** For full credit:
>
> - Submit with Phases 1 and 2 complete by **Thursday, February 22**, worth 1 pt.
> - Submit with all phases complete by **Tuesday, February 27**.
>
> Try to attempt the problems in order, as some later problems will depend on earlier problems in their implementation and therefore also when running `ok` tests.
>
> The entire project can be completed with a partner.
>
> You can get 1 bonus point by submitting the entire project by **Monday, February 26**.

In this project, you will write a program that measures typing speed. Additionally, you will implement typing autocorrect, which is a feature that attempts to correct the spelling of a word after a user types it. This project is inspired by [typeracer](https://play.typeracer.com/).

## Final Product

Our staff solution to the project can be interacted with at [cats.cs61a.org](https://cats.cs61a.org/). If you'd like, feel free to try it out now. When you finish the project, you'll have implemented a significant part of this yourself!

## Download Starter Files

You can download all of the project code as a [zip archive](./cats.zip). This project includes several files, but your changes will be made only to `cats.py`. Here are the files included in the archive:

- `cats.py`: The typing test logic.
- `utils.py`: Utility functions for interacting with files and strings.
- `ucb.py`: Utility functions for CS 61A projects.
- `data/sample_paragraphs.txt`: Text samples to be typed. These are [scraped](https://github.com/kavigupta/wikivideos/blob/626de521e04ca643751ed85d549faca6ea528b1d/get_corpus.py) Wikipedia articles about various subjects.
- `data/common_words.txt`: Common [English words in order of frequency](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt).
- `data/words.txt`: Many more [English words in order of frequency](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt).
- `data/final_diff_words.txt`: Even more English words!
- `data/testcases.out`: Test cases for the optional Final Diff extension.
- `cats_gui.py`: A web server for the web-based graphical user interface (GUI).
- `gui_files`: A directory of files needed for the graphical user interface (GUI).
- `multiplayer`: A directory of files needed to support multiplayer mode.
- `favicons`: A directory of icons.
- `images`: A directory of images.
- `ok`, `proj02.ok`, `tests`: Testing files.
- `score.py`: Part of the optional Final Diff extension.

## Logistics

The project is worth 20 points. 19 points are for correctness and 1 point is for submitting Phases 1 & 2 by the checkpoint date.

You will turn in the following files:

- `cats.py`

You do not need to modify or turn in any other files to complete the project. To submit the project, **submit the required files to the appropriate Gradescope assignment.**

For the functions that we ask you to complete, there may be some initial code that we provide. If you would rather not use that code, feel free to delete it and start from scratch. You may also add new function definitions as you see fit.

**However, please do not modify any other functions or edit any files not listed above**. Doing so may result in your code failing our autograder tests. Also, please do not change any function signatures (names, argument order, or number of arguments).

Throughout this project, you should be testing the correctness of your code. It is good practice to test often, so that it is easy to isolate any problems. However, you should not be testing *too* often, to allow yourself time to think through problems.

We have provided an **autograder** called `ok` to help you with testing your code and tracking your progress. The first time you run the autograder, you will be asked to **log in with your Ok account using your web browser**. Please do so. Each time you run `ok`, it will back up your work and progress on our servers.

The primary purpose of `ok` is to test your implementations.

If you want to test your code interactively, you can run

```python
 python3 ok -q [question number] -i 
```

with the appropriate question number (e.g. `01`) inserted. This will run the tests for that question until the first one you failed, then give you a chance to test the functions you wrote interactively.

You can also use the debugging print feature in OK by writing

```python
print("DEBUG:", x) 
```

which will produce an output in your terminal without causing OK tests to fail with extra output.

# Phase 1: Typing

### Problem 1 (1 pt)

Throughout the project, we will be making changes to functions in `cats.py`.

Implement `pick`. This function selects which paragraph the user will type. It takes three parameters:

- a list of paragraphs (strings) called `paragraphs`
- a `select` function, which returns `True` for paragraphs that can be selected
- a non-negative index `k`

The `pick` function returns the `k`th paragraph for which `select` returns `True`. If no such paragraph exists (because `k` is too large), then `pick` returns the empty string.

Before writing any code, unlock the tests to verify your understanding of the question:

```python
python3 ok -q 01 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```python
python3 ok -q 01
```

### Problem 2 (1 pt)

Implement `about`, which takes a list of `subject` words. It returns a function which takes a paragraph and returns a boolean indicating whether that paragraph contains any of the words in `subject`.

Once we've implemented `about`, we'll be able to pass the returned function to `pick` as the `select` argument, which will be useful as we continue to implement our typing test.

To be able to make this comparison accurately, you will need to ignore case (that is, assume that uppercase and lowercase letters don't change what word it is) and punctuation in the paragraph. Additionally, only check for exact matches of the words in subject in the paragraph, not substrings. For example, "dogs" is not a match for the word "dog".

> **Hint**: Use the `split`, `lower`, and `remove_punctuation` functions in `utils.py`.

Before writing any code, unlock the tests to verify your understanding of the question:

```python
python3 ok -q 02 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```python
python3 ok -q 02
```

### Problem 3 (2 pts)

Implement `accuracy`, which takes a `typed` paragraph and a `source` paragraph. It returns the percentage of words in `typed` that exactly match the corresponding words in `source`. Case and punctuation must match as well. "Corresponding" here means that two words must occur at the same indices in `typed` and `source`; the first words of both must match, the second words of both must match, and so on.

A *word* in this context is any sequence of characters separated from other words by whitespace, so treat "dog;" as a single word.

If `typed` is longer than `source`, then the extra words in `typed` that have no corresponding word in `source` are all incorrect.

If both `typed` and `source` are empty, then the accuracy is 100.0. If `typed` is empty but `source` is not empty, then the accuracy is zero. If `typed` is not empty but `source` is empty, then the accuracy is zero.

Before writing any code, unlock the tests to verify your understanding of the question:

```python
python3 ok -q 03 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```python
python3 ok -q 03
```

### Problem 4 (1 pt)

Implement `wpm`, which computes the *words per minute*, a measure of typing speed, given a string `typed` and the amount of `elapsed` time in **seconds.** Despite its name, *words per minute* is not based on the number of words typed, but instead the number of groups of 5 characters, so that a typing test is not biased by the length of words. The formula for *words per minute* is the ratio of the number of characters (including spaces) typed divided by 5 (a typical word length) to the elapsed time in **minutes.**

For example, the string `"I am glad!"` contains ten characters (not including the quotation marks). The words per minute calculation uses 2 as the number of words typed (because 10 / 5 = 2). If someone typed this string in 30 seconds (half a minute), their speed would be 4 words per minute.

Before writing any code, unlock the tests to verify your understanding of the question:

```python
python3 ok -q 04 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```python
python3 ok -q 04
```

**Time to test your typing speed!** You can use the command line to test your typing speed on paragraphs about a particular subject. For example, the command below will load paragraphs about cats or kittens. See the `run_typing_test` function for the implementation if you're curious (but it is defined for you).

```python
python3 cats.py -t cats kittens
```

You can try out the web-based graphical user interface (GUI) using the following command. (You may have to use `Ctrl+C` or `Cmd+C` on your terminal to quit the GUI after you close the tab in your browser).

```python
python3 cats_gui.py
```

# Phase 2: Autocorrect

In the web-based GUI, there is an autocorrect button, but right now it doesn't do anything. Let's implement automatic correction of typos. Whenever the user presses the space bar, if the last word they typed doesn't match a word in the dictionary but is close to one, then that similar word will be substituted for what they typed.

### Problem 5 (2 pts)

Implement `autocorrect`, which takes a `typed_word`, a `word_list`, a `diff_function`, and a `limit`. The goal of `autocorrect` is to return the word in `word_list` that is closest to the provided `typed_word`.

Specifically, `autocorrect` does the following:

- If the `typed_word` is contained inside the `word_list`, `autocorrect` returns that word.
- Otherwise, `autocorrect` returns the word from `word_list` that has the lowest difference from the provided `typed_word` based on the `diff_function`.
- However, if the lowest difference between `typed_word` and any of the words in `word_list` is greater than `limit`, then `typed_word` is returned instead. That is, `limit` puts a "limit" on how bad of a typo can be corrected.

**Note**: Assume that `typed_word` and all elements of `word_list` are lowercase and have no punctuation.

> **Important**: If multiple strings in `word_list` are tied for the lowest difference from `typed_word`, `autocorrect` should return the string that appears closest to the front of `word_list`.

A diff function takes in three arguments. The first is the `typed_word`, the second is the source word (in this case, a word from `word_list`), and the third argument is the `limit`. The output of the diff function, which is a number, represents the amount of difference between the two strings.

Here is an example of a diff function that computes the minimum of `1 + limit` and the difference in length between the two input strings:

```python
>>> def length_diff(w1, w2, limit):
...     return min(limit + 1, abs(len(w2) - len(w1)))
>>> length_diff('mellow', 'cello', 10)
1
>>> length_diff('hippo', 'hippopotamus', 5)
6
```

> **Hint**: Try using `max` or `min` with the optional `key` argument (which takes in a one-argument function). For example, `max([-7, 2, -1], key = abs)` would return `-7` since `abs(-7)` is greater than `abs(2)` and `abs(-1)`.

Before writing any code, unlock the tests to verify your understanding of the question:

```python
python3 ok -q 05 -u
```

Once you are done unlocking, begin implementing your solution. You can check your correctness with:

```python
python3 ok -q 05
```

