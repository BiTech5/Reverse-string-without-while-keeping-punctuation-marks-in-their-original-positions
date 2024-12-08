# Text Manipulation Tool

A Python utility that reverses the characters in a text while preserving the original positions of punctuation marks.

## Description

This tool takes a string input and reverses all non-punctuation characters while keeping punctuation marks in their original positions. For example:
- Input: "Hello, World!"
- Output: "dlroW, olleH!"

## Features

- Preserves all punctuation marks in their original positions
- Reverses only alphanumeric and space characters
- Includes progress bars for each processing step
- Debug output using icecream for better development experience

## Prerequisites
```bash
   pip install tqdm rich icecream
```

  


## Usage

Run the script and enter your text when prompted:
```bash
  python text_manipulation.py
```
## Example
python
- Input: "Hello, World!"
- Output: "dlroW, olleH!"
- Input: "Hi! How are you?"
- Output: "uoy! era woH? iH"

## Dependencies

- `tqdm`: For progress bars
- `rich`: For enhanced error traceback
- `icecream`: For debug output

## Contributing

Feel free to open issues or submit pull requests to improve the functionality.

