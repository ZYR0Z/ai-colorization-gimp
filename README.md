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

![Unbenannt-2023-11-08-1859](https://github.com/ZYR0Z/ai-colorization-gimp/assets/88033542/62ed6bb8-25d9-4a5c-b034-7a414ce6a07c)

<!-- BUILT WITH -->
### Built with

The Plugin is built using Python 2 (will be updated to Python 3 once GIMP supports it) using the `gimpfu` module provided by GIMP
<br>
<br>

<!-- GENERAL INSTALLATION -->
## General installation

* Download [picwish-colorize.py](https://github.com/ZYR0Z/ai-colorization-gimp/blob/master/picwish-colorize.py) from this repo and place it into your Plugins folder! <br>
* Go to [picwish.com](https://picwish.com/) and login and then go to your account settings and copy your API Key [here](https://github.com/ZYR0Z/ai-colorization-gimp/blob/master/picwish-colorize.py#L34) in the Python file!
<br>
-> Then you should be good to go! You can find the Plugin under Filters -> Enhance -> Colorizer (PicWish API)

  
<!-- WINDOWS INSTALLATION -->
### Windows specific installation

Place in this folder -> `C:\Users\{YOUR USERNAME}\AppData\Roaming\GIMP\2.10\plug-ins` <br>

You can also find your Plugin folder in your gimp preferences in the submenu `Folders` -> `Plug-in Folders` (_shown in screenshot below_)

![Screenshot 2023-11-08 212923](https://github.com/ZYR0Z/ai-colorization-gimp/assets/88033542/e608503a-8ff3-4c7d-af25-80a73d00bfce)


<!-- LINUX INSTALLATION -->
### Linux specific installation
-> Currenlty no support, I am waiting for the AUR Repo to be updated to support `gimpfu`


<!-- USAGE EXAMPLES -->
## Usage
Just select the layer you want to colorize and then got to `Filters -> Enhance -> Colorizer (PicWish API)`!


<!-- ROADMAP -->
## Roadmap
- [x] Add Linux Support (primarily Arch based)
- [x] Add MacOS Support
- [ ] Add installation script for Windows and Linux
- [ ] Maybe create a precompiled binary with Cython to C
    - [ ] Create Installer for Windows which places the Binary into the Plugins
    - [ ] Add as an AUR Package to be easily installed for Arch-based systems 
- [ ] Cleanup code
- [ ] Maybe write own colorization algorithm based on this [paper](https://arxiv.org/pdf/1603.08511v3.pdf)




<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact
zyroz (Noah W.) - contact@zyroz.dev


<p align="right">(<a href="#readme-top">back to top</a>)</p>
