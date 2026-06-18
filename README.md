# Baddroid Payload Generator

A simple Python utility that automatically generates `.dd` payload files compatible with Bruce Firmware for Cardputer devices.

This project was created to simplify the generation of large HID automation payloads, eliminating the need to manually write hundreds of repetitive commands. The generated `.dd` file can be loaded into Bruce and executed directly on a Cardputer.

## Features

* Generate Bruce-compatible `.dd` payloads automatically
* Eliminate repetitive manual payload creation
* Easy to customize
* Lightweight and beginner-friendly
* Useful for HID automation experiments and testing

## How It Works

The script creates a `.dd` file containing a sequence of HID keyboard commands.

Instead of manually writing hundreds of repeated instructions, you simply define:

* The initial setup commands
* The command block to repeat
* The number of repetitions

The script then generates the final payload automatically.

## Requirements

* Python 3.x

No external libraries are required.

## Usage

Clone the repository:

```bash
git clone https://github.com/fabricio-sec/script-BadDroid.git
cd script-BadDroid
```

Run the script:

```bash
python3 generator.py
```

After execution, a `.dd` file will be generated in the same directory as the script.

Example output:

```text
payload_android2.dd
```

## Customization

You can modify:

### Initial Commands

```python
inicio = """
DELAY 500
GUI b
DELAY 3000
...
"""
```

### Repeated Commands

```python
composto = """
CTRL t
DELAY 500
STRING localhost
DELAY 200
ENTER
DELAY 500
"""
```

### Number of Repetitions

```python
quantidade_de_abas = 300
```

Adjust these values according to your testing requirements.

## Project Structure

```text
.
├── generator.py
├── payload_android2.dd
└── README.md
```

## Disclaimer

This project is intended for educational purposes, research, and authorized testing only.

Always ensure you have permission to interact with any target device or environment. The author is not responsible for misuse of this software.

## Contributing

Pull requests, improvements, and suggestions are welcome.

## License

MIT License

Feel free to use, modify, and distribute this project.
