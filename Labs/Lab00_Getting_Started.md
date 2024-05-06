# Lab 0: Getting Started <kbd>[lab00.zip]()</kbd>

*Due by 11:59 pm on Wednesday, January 24.*

## Starter Files

Download [lab00.zip](). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the [Ok]() auto-grader.

**This lab is required for all students and counts toward you lab score,** but try to complete it at home before you come to Lab 1.

## Introduction

This lab explains how to setup your computer to complete assignments and introduces some of the basics of Python. If you need any help at any time through the lab, please feel free to come to [office hours](https://cs61a.org/office-hours), post on Ed, or come to your assigned lab section.

Here's an outline of the lab:

- **Setup**: Setting up the essential software for the course. This will require several components, listed below.
  - **Install a Terminal**: Install a terminal so you can interact with files in this course and run OK commands. If you have a terminal on your computer and feel comfortable using it, you can skip this part.
  - **Install Python 3**: Install the Python programming language to your computer. If you already have Python 3.7 or later (ideally Python 3.9) installed, you can skip this part.
  - **Install a Text Editor**: Install software to edit `.py` files for this course (e.g. VSCode, Atom, etc.). You can skip this part if you already have a text editor you like.
- **Walk-through: Using the Terminal**: This walks you through how to use the terminal and Python interpreter. If you already feel comfortable with both of these you do not need to read this section.
- **Walk-through: Organizing your Files**: This section walks you through how to use your terminal to organize and navigate files for this course. **Everyone should at least skim this section**, as it has important information specific to this class, but if you are already comfortable navigating directory structures with a terminal much of this will feel familiar.
- **Required: Doing the Assignment**: You must complete this section to get points for the assignment. Here you will practice the different types of problems you will be asked to do in lab, homework, and project assignments for this course. The main goal of this assignment is to give you practice using our software.
- **Required: Submitting the Assignment**: You must complete this section to get points for the assignment. This will walk you through how to turn in your work after completing the previous section and how to verify that your work is turned in on Grade-scope.
- **Appendix: Useful Python Command Line Options**: These are commands that are useful in debugging your work, but not required to complete the lab. We include them because we imagine they're likely to be helpful to you throughout the course.

## Setup

> To setup your device, select the guide that corresponds to your operating system.

- [Guide for Windows](https://cs61a.org/articles/setup-windows/)

- **[Guide for Mac & Linux](https://cs61a.org/articles/setup-mac)**

## Your First Assignment

> When working on assignments, ensure that your terminal's working directory is correct (which is likely where you unzipped the assignment).

### 1) What Would Python Do? (WWPD)

One component of lab assignments is to predict how the Python interpreter will behave.

>Enter the following in your terminal to begin this section:
>
>```
>python3 ok -q python-basics -u
>```
>
>You will be prompted to enter the output of various statements/expressions. You must enter them correctly to move on, but there is no penalty for incorrect answers.
>
>The first time you run Ok, you will be prompted for your bCourses email. Please follow [these directions](../Articles/using-ok.md). We use this information to associate your code with you when grading.