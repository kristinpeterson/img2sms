img2sms cli tool
================================

A command line tool which takes an image file path and optional message and 
number, uploads the image to Imgur and texts a link with optional message 
to the given number or the default number setup in `settings.py`. 
If no image is present an SMS with the given message will be sent without an 
image link.

## Setup
Enter your Imgur client_id and secret in 
/img2sms/config.json:

```json
{
    "client_id": "",
    "secret": "",
    "token_store": {}
}
```

[Click here if you don't already have an Imgur API keyset]
(http://goo.gl/7QGfWT)

### Optional Steps

#### Set default recipient mobile number in /img2sms/settings.py:

```python
def init():
    global num
    num = "enter-default-recipient-mobile-number-here"
```

#### Setup Command Line Alias / Macro

##### OSX | Linux
Add the following to your .bash_profile or .aliases file to create a command
 line alias for running img2sms:

```bash
alias sms="python ~/path/to/main.py"
```

##### Windows
Run the following from the command line to create a macro for running img2sms:

```bash
doskey sms=python C:\absolute\path\to\main.py $*
```

## Usage
From img2sms folder run the following command:
```bash
python main.py -p "\\img.file.absolute.path" -m "optional message" -n 
"optional phone number"
```

::argv:: 
* path to an image file
* text string (optional)
* mobile number string (optional) 

::return:: 
* uploads the image to Imgur 
* sends an SMS to either a default mobile number or a number provided on the 
command line.

## Dependencies
* Python 2 or 3
* cURL


Should work on Mac OSX, Linux and Windows (although I primarily use it on 
Mac OSX)

## Thanks to...
* [imgur-python](https://github.com/jacobgreenleaf/imgur-python) - Imgur 
python library
* [textbelt](https://github.com/typpo/textbelt) - Free outgoing SMS API