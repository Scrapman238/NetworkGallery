# NetworkGallery

NetworkGallery is the local file gallery you need, it is a photo and video gallery that runs on the local network and is quite fast

## Notes

- LocalGallery is completely open source and **completely free**! Feel free to download it and give it a try

- LocalGallery is still under development and is not finished so some things may change and become more optimized

- Whenever the terms 'Site' or 'Website' are used, it is referring to the local ip address of the machine that the HTML documents will be hosted on

## Features

Many features are supported, including:

- Uploading media from any device, right on the website with a sleek UI

- Full lossless uploads with [no compression](#optimizations)!

- Loading images from server at a fast speed using [temporary compression](#optimizations)

- A full quality viewing mode when clicked that opens the raw file in full quality

- A blue outline around video content to distinguish it

## Optimizations

One major optimization is using temporary compression, when a file is uploaded:

1. It is saved in the appropriate media folder:
    - Images
    - Videos
2. Video files have a thumbnail automatically generated
    1. Ffmpeg gets the first frame from the video
    2. The frame is saved into the images folder
        - It has the same file name but with an image file extension
3. Everything in the images folder is compressed to 720p in the low_quality folder
    - The compression happens when the file is uploaded or if the compressed version is deleted, it is generated when requested by a user
    - Displaying it this way is a great way to use less data and increase speed when sending it to the user

## Supported OS types:

<table>
  <tr>
    <th>Operating System</th>
    <th>Supported</th>
    <th>Tested</th>
    <th>Test Hardware</th>
  </tr>
  <tr>
    <td>Windows 11</td>
    <td style="color: lime;">Yes</td>
    <td style="color: lime;">Yes</td>
    <td style="color: lime;">Standard Windows Device</td>
  </tr>
    <tr>
    <td>Windows 10</td>
    <td style="color: lime;">Yes</td>
    <td style="color: #FF4040;">No</td>
    <td style="color: #FF4040;">None</td>
  </tr>
  <tr>
    <td>Pi OS (Desktop)</td>
    <td style="color: lime;">Yes</td>
    <td style="color: lime;">Yes</td>
    <td style="color: lime;">Raspberry Pi B 4</td>
  </tr>
  <tr>
    <td>Pi OS (Headless)</td>
    <td style="color: lime;">Yes</td>
    <td style="color: #FF4040;">No</td>
    <td style="color: #FF4040;">None</td>
  </tr>
  <tr>
    <td>Other Linux Distros</td>
    <td style="color: yellow;">Most Likely</td>
    <td style="color: #FF4040;">No</td>
    <td style="color: #FF4040;">None</td>
  </tr>
  <tr>
    <td>Mac</td>
    <td style="color: #FF4040;">N/A</td>
    <td style="color: #FF4040;">No</td>
    <td style="color: #FF4040;">None</td>
  </tr>
</table>

## Setup guides

These are the setup guides for all tested OS types:

- [Linux setup](#linux-setup)

- [Windows setup](#windows-setup)

## Linux setup

### Get the terminal ready

Open a terminal window

```
~ $
```

Get root permission
```bash
sudo -i
```

CD to the user directory (here, the username is "scrap")

```bash
cd /home/scrap
```

### Download python

Ensure python is installed, if it is [you can skip this step](#create-a-virtual-environment)

```bash
python --version
```

If it is not installed, you can install it with this command

```bash
sudo apt update
sudo apt install python3 python3-venv
```

Verify the installation

```bash
python --version
```

### Create a virtual environment

Make the virtual environment to run pip in (you only need to do this once)

```bash
python3 -m venv venv
```

Now activate it (you do need to do this every time it is started)

```bash
source venv/bin/activate
```

### Downloading git on Linux

Check if git is installed, if it is [you can skip this step](#downloading-the-code-on-linux)

```bash
git --version
```

If git is not installed, download it with these commands

```bash
sudo apt-get update
sudo apt-get install git
```

Verify the installation

```bash
git --version
```

### Downloading the code on Linux

Change directory to the place you want to download the code (the code can run on a usb drive, that is what happens here, change directory to any place you have write permission)

```bash
cd /media/scrap/USB/
```

Download the code using git

```bash
git clone --branch main https://github.com/Scrapman238/NetworkGallery.git
```

Unzip the code

```bash
unzip NetWorkGallery.zip
```

Change directory into the new folder

```bash
cd NetworkGallery
```

Install requirements with pip

```bash
pip install requirements.txt
```

### Running the code

Run the python file

```bash
python main.py
```

If all goes well, you should be presented with something similar to this

```bash
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://###.###.###.###:80
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ###-###-###
```

The '###.###.###.###' in 'http://###.###.###.###:80' would be the local ip address of the device. The ':80' at the end is not required in the URL bar when opening the website as 80 is the default port on most browsers.

Any device on the network can now open the link to access the site

## Windows setup

### Get the terminal ready

Open a command prompt window

```
C:\Users\scrap>
```

### Download python

Ensure python is installed, if it is [you can skip this step](#downloading-git-on-windows)

```bash
python --version
```

If it is not installed, you can install it [here](https://www.python.org/downloads/) and run the setup, make sure to add it to path

Verify the installation

```bash
python --version
```

### Downloading git on Windows

Check if git is installed, if it is [you can skip this step](#downloading-the-code-on-windows)

```bash
git --version
```

If git is not installed, download it [here](https://git-scm.com/download/win) and run the setup, make sure to add it to path

Verify the installation

```bash
git --version
```

### Downloading the code on Windows

Change directory to the place you want to download the code (the code can run on a usb drive, that is what happens here, change directory to any place you have write permission)

```bash
F:
```

Download the code using git

```bash
git clone --branch main https://github.com/Scrapman238/NetworkGallery.git
```

Unzip the code

```bash
tar -xf NetWorkGallery.zip
```

Change directory into the new folder

```bash
cd NetworkGallery
```

Install requirements with pip

```bash
pip install requirements.txt
```

### Running the code

Run the python file

```bash
python main.py
```

If all goes well, you should be presented with something similar to this

```bash
F:\NetworkGallery\NetworkGallery>python main.py
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://###.###.###.###:80
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ###-###-###
```

The '###.###.###.###' in 'http://###.###.###.###:80' would be the local ip address of the device. The ':80' at the end is not required in the URL bar when opening the website as 80 is the default port on most browsers.

Any device on the network can now open the link to access the site