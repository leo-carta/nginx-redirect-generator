# nginx-redirect-generator

Generate nginx redirects from two column excel file

## Requirements
- python3
- pip

## Install python3 and pip
https://docs.python-guide.org/starting/install3/osx/

## Installation
`pip install -r requirements.txt`

## Excel file preparation
You need a two column excel file, in which the first column stands for the url to be redirected to the url in the second column

Example:

| Column 1                         | Column 2                    |
| -------------------------------- | ----------------------------|
| https://example.com/404errorsite | /nicesitewithouterror/cool/ |
| https://example.com/old/url/down | /new/url/up/                |
