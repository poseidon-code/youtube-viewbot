# YouTube Viewbot

> ## ⚠ **DISCLAIMER** ⚠
>
> YouTube Viewbot is just an experiment, and all the risk involved and harm done, on running this program, is solely on the user of this program.\
> The risks may include temporary takedown of the youtube video (by YouTube), temporarily suspending the view counts of the youtube video (by YouTube), and the views gained by this program may get resetted after some time (by YouTube).\
> This program will not take any userdata, but can take high amount of available resources (CPU & RAM) to reach maximum potential of multithreading/concurrency.

---

## Prerequisites

The computer, this program will be running on, must have `Python` installed and `PATH` must be set.

1. Download `Python` from [here](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)

2. Install `Python` by checking all check boxes in the First page of Python Installation. _(**especially** make sure `Add Python to system PATH` option is checked)_

3. The computer must have **Google Chrome** web browser installed.

4. Download Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads). _(this program requires you to download the Chrome WebDriver of **same version** as that of your Google Chrome Browser, and move-replace that to this program's directory)_

4. Download this program from [here](https://github.com/poseidon-code/youtube-viewbot/archive/main.zip)

---

## Using YouTube Viewbot

> **PREFACE**\
> This program is very resource heavy, sometimes you might feel like the computer has hanged/freezed/lagging, but nothing to fear as the program is taking as much resources it could get to complete the process.\
> By theory, the views generated by this program is proportional to the number of proxies in the _proxy-list.txt_, but there are many constraints such as - how many proxies are valid and working, will the views earned by this program be reflected in that YouTube video, maybe those views might get removed as soon as YouTube finds that it is done by a bot and many more.\
> Taking those things into consideration, this program could give a nice amount of boost to view counts, but not by exactly specified numbers.

1. Go to the downloaded folder _(the folder where you downloaded this program)_. `Copy` the **folder path**.

2. Open `cmd` _(in Windows, `terminal` in Linux/MacOS)_, enter the following command, then press <kbd>Enter</kbd>:

    ```bash
    cd paste/the/path/to/that/downloaded/folder
    ```

3. Install required packages by entering the following command :

    ```bash
    pip install -r requirements.txt
    ```

4. Generate `proxy-list.txt` file by entering the following command :

    ```bash
    python proxy.py
    ```

    > Make sure you run this command every time whenever starting this program, as this would get latest proxies everytime.

    > **PRO TIP :** If you have any other source of having proxies (like; PRO/PAID member of free-proxy-list.com or any other proxy provider), then you can get a premium proxy list from them, and make an empty `proxy-list.txt` file in that directory and paste all those premium proxies line-by-line and **skip this step**.

5. Copy the YouTube video `URL` that you want to increase the views of, and execute this command :
    ```bash
    python viewbot.py <paste that URL> <enter watch-time (seconds)>
    ```
    **example :**
    ```bash
    python viewbot.py https://youtu.be/oH3as_QyRsI 30
    ```

### ☕ Now sit back, depending on how many proxies you have in the `proxy-list.txt` file, this program will take some time (more the proxies, more time will be taken, more views can be generated)

---

## Acknowledgement

YouTube Viewbot is made by [poseidon-code](https://github.com/poseidon-code) using [Selenium](https://www.selenium.dev) Web Driver. Free proxies are provided by [FreeProxyList](https://www.freeproxylists.net). This program is an experimental project and one should go through the **Disclaimer** at the start.

## License

MIT License

&copy; poseidon-code 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
