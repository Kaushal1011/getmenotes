# getmenotes
```
   ▄██████▄     ▄████████     ███            ▄▄▄▄███▄▄▄▄      ▄████████      ███▄▄▄▄    ▄██████▄      ███        ▄████████    ▄████████ 
  ███    ███   ███    ███ ▀█████████▄      ▄██▀▀▀███▀▀▀██▄   ███    ███      ███▀▀▀██▄ ███    ███ ▀█████████▄   ███    ███   ███    ███ 
  ███    █▀    ███    █▀     ▀███▀▀██      ███   ███   ███   ███    █▀       ███   ███ ███    ███    ▀███▀▀██   ███    █▀    ███    █▀  
 ▄███         ▄███▄▄▄         ███   ▀      ███   ███   ███  ▄███▄▄▄          ███   ███ ███    ███     ███   ▀  ▄███▄▄▄       ███        
▀▀███ ████▄  ▀▀███▀▀▀         ███          ███   ███   ███ ▀▀███▀▀▀          ███   ███ ███    ███     ███     ▀▀███▀▀▀     ▀███████████ 
  ███    ███   ███    █▄      ███          ███   ███   ███   ███    █▄       ███   ███ ███    ███     ███       ███    █▄           ███ 
  ███    ███   ███    ███     ███          ███   ███   ███   ███    ███      ███   ███ ███    ███     ███       ███    ███    ▄█    ███ 
  ████████▀    ██████████    ▄████▀         ▀█   ███   █▀    ██████████       ▀█   █▀   ▀██████▀     ▄████▀     ██████████  ▄████████▀  

 ```

getmenotes is a project that makes markdown notes for you based on comments in the code of your project.
you can use this to make documentation for your project or even make conceptual notes from your project ( in a project based learning approach).I developed this because i have a habit of making markdown notes for my projects and concepts that I learn. With this i can write everything in the code.

According to me this can be very useful for developers that keep learning new stuff and work on projects on a frequent basis. contribute the project and help me develop it. 
__Visit [GNM Project](https://github.com/users/Kaushal1011/projects/5) to learn more about what is to be developed further.__

## Functionality
- currently works for python only (more languages support to be added soon Visit [GNM Project](https://github.com/users/Kaushal1011/projects/5) to learn more) 
- you can give a sub topic and add points to the topic and include some code
- run this to get an idea how this works 
- you add  content <gm></gm> tags and then the app logs content and makes markdown file
- after opening <gm> tag you can add a topic in square braces [topic] optional
- visit [Idea](idea.md) for more info
- visit [Example file in](example.py) to see example of how to add comments that get added to documentation
- visit [GMN Notes](GMN_Notes.md)
- metadata token and raw markdown support to be added soon
   
___code cleaner to be made soon that removes gmn comments from the code to make it cleaner___
___i.e gnm cleaner will make markdown documentation and remove comments from main code___

  
## To Run
"Change name and author in gmn.py as currently metadata support isnt made"

```shell
python3 gmn.py example.py
```
## examples use case

if we have certain part in the code

```python
# <gm> [Linear Regression] this way we can use polynomial features
"code that uses polynomial features linear regression"
# </gm>
```

GMn would make the following markdown output

# Project1

## LinearRegression

- this way we can use polynomial features

```python
"code that uses polynomial features linear regression"
```

## Further Info

- <gm> tag tells gmn to start reading
- [] tell the subtopic name
- anything after ] is to be logged
- if tag isnt closed in the comment, code following comment should be logged until ending tag is received
- error if two consecutive opening fw tags are receive (future feature).
- first gm tag should contain metadata about the code i.e Name of notes file, Author, Date, Language (in the works).
- currently made for python code. 



