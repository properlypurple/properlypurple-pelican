Title: Getting started with programming in GNU/Linux: the easy way
Date: 2010-05-07 19:21
Author: properlypurple
Category: Blog, Tutorials
Slug: getting-started-with-programming-in-gnulinux-the-easy-way
Status: draft

Are you an engineering student(or anyone for that sake), and are bored with that ugly Turbo C, or are sick of 'javac' to compile java programs. Well, here's an easy way to do all the things nicely, easily, and in complete freedom. With some initial effort, it will be a lot easier and cooler.

The first step is to install a GNU/Linux system. Now mind that, C & C++ were made for UNIX, and that is the correct place to program in them. But since UNIX is out of reach for us, GNU/Linux is the best(and it's free) alternative. Though there are many of them, most of us have heard of Red Hat 5 only, or maybe Ubuntu. But I highly recommend [Trisquel](http://trisquel.info/), which comes with a plenty of software, and media codecs preinstalled. And it's completely free(as in free speech). So our steps are:

Step1-[Download](http://trisquel.info/) and install Trisquel. You can read the tutorial to install it on my blog soon.

Step2-Open Synaptic Package Manager by

> *Main menu->System->Administration->Synaptic*

or by pressing 'Alt+F2' and typing '*gksudo Synaptic*'

search and mark the following packages

-   g++
-   openjdk-6-jdk
-   build-essential
-   gcc
-   geany

click 'Apply'. the packages will be downloaded and installed.

If you want an easy way for all this, just open a terminal by

> *Main menu-> Accesories -> Terminal*

and paste the following

> *sudo apt-get install gcc build-essential openjdk-6-jdk g++ geany  
> *

it will ask for your password. When you type it, you will see nothing, but be patient. Type the password and press enter, the packages will be downloaded and installed automatically.

Step3- Open Geany by

> *Main menu ->Programming -> Geany*

and start typing your first program. Save the program with the appropriate extension.

Step4- Press F8 to compile the program and F5 to run the compiled program.

Step5- Sit back and enjoy a clear air of freedom.

Happy programming:-)!!!
