<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
    <h2 align="center">AI Gimp Colorization Plugin</h3>

  <p align="center">
        A Gimp plugin for automated colorzation of layers, using the <a href="https://picwish.com/photo-colorization-api" target="_blank">PicWish Colorization API</a>.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li>
      <a href="#general-installation">General installation</a>
      <ul>
        <li><a href="#windows-specific-installation">Windows specific installation</a></li>
        <li><a href="#linux-specific-installation">Linux specific installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the project

![explanation](https://github.com/ZYR0Z/ai-colorization-gimp/assets/88033542/3d56fca0-a18d-4726-8ebc-6a94eb13a108)

<!-- BUILT WITH -->
### Built with

The Plugin is built using Python 2 (will be updated to Python 3 once GIMP supports it) using the `gimpfu` module provided by GIMP
<br>
<br>

<!-- GENERAL INSTALLATION -->
## General installation

* Download [picwish-colorize.py](https://github.com/ZYR0Z/ai-colorization-gimp/blob/master/picwish-colorize.py) from this repo and place it into your Plugins folder! <br>
* Go to [picwish.com](https://picwish.com/) and login and then go to your account settings and copy it. <br>
* Also download the example [JSON](https://github.com/ZYR0Z/ai-colorization-gimp/blob/master/colorize_api_key.json#L2) file and replace the api_key with your copied API key!
<br>
-> Then you should be good to go! You can find the Plugin under Filters -> Enhance -> Colorizer (PicWish API)

  
<!-- WINDOWS INSTALLATION -->
### Windows specific installation

I created an .bat script for the installation! Just download it here: [/scripts/install_windows.bat](https://github.com/ZYR0Z/ai-colorization-gimp/blob/master/scripts/install_windows.bat) and run it by clicking on it! <br>
You will be promted to enter your API key just follow the instrutctions in the [General Installation](https://github.com/ZYR0Z/ai-colorization-gimp/tree/master#general-installation) <br> <br>

_**To manually install it:** <br>
Place your Python and JSON file into this folder -> `C:\Users\{YOUR USERNAME}\AppData\Roaming\GIMP\2.10\plug-ins` <br>
You can also find your Plugin folder in your gimp preferences in the submenu `Folders` -> `Plug-in Folders` (shown in screenshot below)_

![Screenshot 2023-11-08 212923](https://github.com/ZYR0Z/ai-colorization-gimp/assets/88033542/e608503a-8ff3-4c7d-af25-80a73d00bfce)


<!-- LINUX INSTALLATION -->
### Linux specific installation
_~Currenlty no support, I am waiting for the AUR Repo to be updated to support `gimpfu`~_ <br> <br>
I created an .sh script for the installation! Just download it here: [/scripts/install_linux.sh](https://github.com/ZYR0Z/ai-colorization-gimp/blob/master/scripts/install_linux.sh) and then run the command: `chmod +x install_linux.sh` and then run it like this: `./install_linux.sh`! <br>
You will be promted to enter your API key just follow the instrutctions in the [General Installation](https://github.com/ZYR0Z/ai-colorization-gimp/tree/master#general-installation) <br> <br>
To manually install it just do the same as Windows, just look where your plug-ins folder is located! <br> <br>
_~-> There will be an installation script be added in the future to automate this process!~_


<!-- USAGE EXAMPLES -->
## Usage
Just select the layer you want to colorize and then got to `Filters -> Enhance -> Colorizer (PicWish API)`!


<!-- ROADMAP -->
## Roadmap
- [x] Add Linux Support (primarily Arch based)
- [x] Add installation script for Windows and Linux
- [x] Cleanup code
- [ ] Add MacOS Support (Install Script + modfiy api_key_read())
- [ ] Maybe create a precompiled binary with Cython to C
    - [ ] Create Installer for Windows which places the Binary into the Plugins
    - [ ] Add as an AUR Package to be easily installed for Arch-based systems 
- [ ] Maybe write own colorization algorithm based on this [paper](https://arxiv.org/pdf/1603.08511v3.pdf)




<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact
zyroz (Noah W.) - contact@zyroz.dev


<p align="right">(<a href="#readme-top">back to top</a>)</p>
