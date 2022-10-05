Title: Awesome desktop #1
Date: 2011-03-09 15:31
Author: properlypurple
Category: Awesome desktops, Blog, Computers, Tutorials
Slug: awesome-desktop-1
Status: draft

[![Gaia10_sprout by grvrulz](http://properlypurple.com/wp-content/uploads/2011/03/gaia10_sprout_by_grvrulz-d2zs6b2.jpg "gaia10_sprout_by_grvrulz-d2zs6b2"){.size-full .wp-image-74 width="640" height="359"}](https://gauravblog.mystagingwebsite.com/wp-content/uploads/2011/02/gaia10_sprout_by_grvrulz-d2zs6b2.jpg)

This screenshot has stood second in a desktop contest by OMGUbuntu([link](http://www.omgubuntu.co.uk/2011/02/the-top-5-desktops-from-our-facebook-competition/)) and a lot of people asked me to do a howto for this. So here it is.

Download the theme here [GAIA Sprout by \~lassekongo83](http://browse.deviantart.com/?qh=&section=&global=1&q=gaia+sprout#/d2ywgyr).

Download the wallpaper here [Glacien by \~imrik on deviantART](http://imrik.deviantart.com/art/Glacien-179223097).

Install  p7zip, emerald, gimp & gimp-plugin-registry

> sudo apt-get install p7zip-full emerald gimp gimp-plugin-registry

[**GTK & EMERALD THEMES**]{style="text-decoration:underline;"}

Extract the theme(its a 7zip file). There are 2 emerald themes, 1 panel background image and a folder called "GAIA Sprout" in there. Copy the folder "GAIA Sprout" to \~/.themes/ .

> cp -R 'GAIA Sprout' \~/.themes/

Open Syetem>Preferences>Appearance. Select Gaia Sprout as your theme.

Note: If you dont have equinox engine installed you can install it by adding the ppa

> sudo add-apt-repository [ppa:tiheum/equinox]{.Apple-style-span style="font-size:13px;font-family:Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif;line-height:19px;"}
>
> [sudo apt-get update]{.Apple-style-span style="font-size:13px;font-family:Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif;line-height:19px;"}
>
> [sudo apt-get install gtk2-engines-equinox]{.Apple-style-span style="font-size:13px;font-family:Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif;line-height:19px;"}

Open System>Preferences>Emerald Theme Manager. Click on 'Import', navigate to the folder and import the two emerald themes one-by-one. Then run emerald

> emerald --replace

Note: if you want to permanently use emerald as your window decoration, you might want to put the above command in compizconfig-settings-manager. Just open ccsm-> window decoration-> command. Put *emerald --replace* in the box and press Return.

[![ccsm window decoration setting](http://properlypurple.com/wp-content/uploads/2011/03/2011-03-09-150805_1366x768_scrot-1.png "ccsm window decoration setting"){.aligncenter .size-full .wp-image-79 width="640" height="201"}](https://gauravblog.mystagingwebsite.com/wp-content/uploads/2011/03/2011-03-09-150805_1366x768_scrot.png)

[**ICONS**]{style="text-decoration:underline;"}

Download the iconset from [here](http://alecive.deviantart.com/art/AwOken-1-9-163570862). Follow the instructions on the download page to install the icons using your favourite method. If you want automatic updates, you should use the ppa method.

[**DOCK AT BOTTOM**]{style="text-decoration:underline;"}

The dock at the bottom is AWN(Avant Window Navigator). Install AWN  and plugins with

> sudo apt-get install avant-window-navigator awn-applets-c-core awn-applets-c-extras awn-applets-pyhon-core awn-applets-pyhon-extras

This will install the full package, i.e. including all plugins and features. Start AWN through Applications->Accessories->Avant Window Navigator.

To get the above look, just right click the dock and selec Dock Preferences. Go to themes tab and select any light theme. Then go to Style tab and set style to 3d. You can alter finer details in the 'Themes' tab by clicking on customize. Now go to Applets tab and add the applets you want to get shown on the dock.

[![Avant Window navigator settings](http://properlypurple.com/wp-content/uploads/2011/03/2011-03-09-151150_1366x768_scrot-1.png "Avant Window navigator settings"){.aligncenter .size-full .wp-image-80 width="592" height="561"}](https://gauravblog.mystagingwebsite.com/wp-content/uploads/2011/03/2011-03-09-151150_1366x768_scrot.png)

[ ]{style="text-decoration:underline;"}

[Install conky and conky-colos deps.]{.Apple-style-span style="color:#000000;"}

> [sudo apt-get install aptitude python-statgrab ttf-droid hddtemp curl lm-sensors conky-all]{.Apple-style-span style="color:#000000;"}

Download conky colors from [here](http://gnome-look.org/content/show.php/CONKY-colors?content=92328). Extract it and open terminal in the folder it was extracted in. Enter the following in the terminal.

> make

Then type

> sudo make install

conky-colors will now be installed. now type the following in a terminal to generate ypur conkyrc.

> conky-colors --lang=en --theme=elementary --cpu=2 --clock=bigcairo --hd=default --cairo --network --wireless

Note that you can change the language to suit your own, and the number of cpus to whatever number you have(I have a Core 2 duo so i've written cpu=2).

You'll get something like that in the output

> Your conkyrc was copied to /home/gp/.conkycolors
>
> Generated configuration files are copied to /home/gp/.conkycolors
>
> <div>
>
> To run conky-colors and conky type:
>
> </div>
>
> <div>
>
> [[conky -c /home/gp/.conkycolors/conkyrc]{.Apple-style-span style="font-size:16px;line-height:24px;"}]{.Apple-style-span style="font-size:medium;"}
>
> </div>

<div>

[[Note that this will be different because your username will not be same as mine.:P. Now copy the last line and paste it in the terminal. Conky will now be running. You might want it to automatically start every time you restart. To do that, go to System-> Preferences->Startup Applications. Click Add and put the command in the given box.]{.Apple-style-span style="font-size:16px;line-height:24px;"}]{.Apple-style-span style="font-size:medium;"}

[![Startup Application settings](http://properlypurple.com/wp-content/uploads/2011/03/2011-03-09-174939_1366x768_scrot-1.png "Startup Application settings"){.aligncenter .size-full .wp-image-85 width="455" height="406"}](https://gauravblog.mystagingwebsite.com/wp-content/uploads/2011/03/2011-03-09-174939_1366x768_scrot.png)

</div>

[**TOP PANEL**]{style="text-decoration:underline;"}

Gnome-panel does not support 'real' transparency, even on  a composited desktop. Thats why we embed some graphics in our wallpaper to get the effect as shown in the screenshot.

Open the panel.png image included in the theme folder wih GIMP. Go to Layer->Liquid Rescale. Enter you screen's horizontal resolution in the the width field. Click OK. Save the file.

[![](http://properlypurple.com/wp-content/uploads/2011/03/2011-03-09-152127_1366x768_scrot-1.png "2011-03-09-152127_1366x768_scrot"){.aligncenter .size-full .wp-image-82 width="640" height="413"}](https://gauravblog.mystagingwebsite.com/wp-content/uploads/2011/03/2011-03-09-152127_1366x768_scrot.png)

Now open your wallpaper in GIMP and go to File->Open as layers. Select the resized panel.png and open. Position the panel image at the top edge and save the image as png or jpeg, as you prefer. DO NOT SAVE WITHOUT AN EXTENSION, as it will save it as an .xcf file, the native gimp image format.

Apply the  new image as wallpaper. Right click the panel, select Properties. Set the size to 24 px. Now go to Background tab, select solid color, and move the transparency slider to make the panel fully transparent. You have your awesome desktop ready. Enjoyy.

I'm not very good at writing tutorials, actually this is my first. So please ask any doubts in the comments, and please point out if i've missed some detail. Keep Rockin'. :D

P.S. As a matter o fact, I dont use Ubuntu anymore. I'm  currently using Trisquel GNU/Linux which is a fully free(as in freedom) derivative of Ubuntu. See <http://trisquel.info> for details.
