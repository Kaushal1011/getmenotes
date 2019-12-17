# Idea for fantastic waddle

## Premise

While working on projects that usually deal with concepts i havent studied yet i would make a seperate markdown file to log  whatever that i was learning. This helps me log my progress and use it for future reference.

## Idea

- User adds notes in comments in the code of project while working
- fanwan makes markdown with notes
- fanwan.clean cleans the code with extra logging notes and cleans the code of too much comments.

## examples use case

if we have certain part in the code

```python
# <gm> [Linear Regression] this way we can use polynomial features
"code that uses polynomial features linear regression"
# </gm>
```

FanWad would make the following markdown output

# Project1

## LinearRegression

- this way we can use polynomial features

```python
"code that uses polynomial features linear regression"
```

## Further Info

- <gm> tag tells fanwad to start reading
- [] tell the subtopic name
- anything after ] is to be logged
- if tag isnt closed in the comment, code following comment should be logged until ending tag is received
- error if two consecutive opening fw tags are receive
- first gm tag should contain metadata about the code i.e Name of notes file, Author, Date, Language
- currently made for python code.  

can use lexer mechanism from DenkInterpreter to implement lexing
decide on a proper datastructure that parser would use
like rather than using a tree we use a hashtable
or maybe a new augmented hashedtree datastructure

Currently use a hashtable develop on it in the future
