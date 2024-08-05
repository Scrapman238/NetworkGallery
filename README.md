# NetworkGallery

NetworkGallery is the local file gallery you need, it is a photo and video gallery that runs on the local network and is quite fast

## Notes

- LocalGallery is completely open source and **completely free**! Feel free to download it and give it a try

- LocalGallery is still under development and is not finished so some things may change and become more optimized

- Whenever the terms 'Site' or 'Website' are used, it is referring to the local IP of the machine that the HTML documents will be hosted on

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

These are the setup guides for all tested OS types

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
python3 --version
```

If it is not installed, you can install it with this command

```bash
sudo apt update
sudo apt install python3 python3-venv
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

### Downloading git

Check if git is installed, if it is [you can skip this step](#downloading-the-code)

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

### Downloading the code

Change directory to the place you want to download the code (the code can run on a usb drive, that is what happens here, just change directory to any place you have write permission)

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

### Running the code

Change directory into the new folder

```bash
cd NetworkGallery
```