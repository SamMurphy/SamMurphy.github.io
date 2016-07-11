---
title: "Pi vs Printer"
layout: single
author_profile: true
read_time: true
comments: true
share: true
related: true
categories:
  - Technology
  - Hardware
  - Tutorial
tags:
  - technology
  - hardware
  - linux
  - "raspberry  pi"
---

Recently I decided to try and get the Raspberry Pi working as a print server with my aging HP printer, and wow what a challenge it was I had no idea how impossible it is to find drivers for old printers that work with Linux, ARM architecture and CUPS, speaking of CUPS that too took a considerable amount of time to get working.

The first thing I did was try to install cups, software that should handle all of the print jobs and sharing the printers across multiple OS’. This was a mistake I should have done a bit of research first so when I got a bunch of errors that’s exactly what I did. After my research I realised that the first thing I needed to do was find and install some drivers this proved more difficult than it sounds as for order for the drivers to work properly they would have to be compatible with Linux, the ARM architecture that the pi uses and CUPS. My first stop was HP’s website, no luck there like most manufacturers HP don’t provide any kind of driver for Linux, so after a while of searching I stumbled across the open source HP Linux imaging & printing (hplip) suite which provides driver support for more than 2000 HP printers. I went about installing hplib, however you can’t complete the installation though SSH, my normal way of interacting with my pi, to my surprise you have to do it through the GUI which meant installing vnc server and doing it that way as I certainly wasn’t going to the trouble of hooking up a monitor, keyboard and mouse. Once that was working I printed off a test page and miraculously it worked, printing out a nice Linux penguin.

![Pi Printer]({{ site.url }}/images/PivsPrinter-Printing.jpg){: .align-center}

Then I tried getting cups working again and this time it picked up my printer without a hitch and I was able to print a test page off though the rather useful cups web interface. The next step was to get it working across my network on the variety of OS’ though out my house, it worked pretty quickly on Linux so that didn’t take long to set up on my Linux PC and my sisters Laptop. As for Windows that took a bit of tinkering, requiring me to install samba on to the pi, but that installed with relative ease and from there on adding the printer in Windows was a breeze.

![Pi Printer]({{ site.url }}/images/PivPrinter-CUPSinterface.png){: .align-center}

The one thing I regret about this process though is that I didn’t document it for this blog, however I won’t be making the same mistake when I install AirPrint, to let iOS uses print, later in the week.

![Pi Printer]({{ site.url }}/images/PivsPrinter-Pi.jpg){: .align-center}