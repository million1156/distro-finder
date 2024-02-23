# Distro finder

This is a very quick project that I whipped up in like an hour. 

# What is this?
This is a **Discord bot** that checks [GS1](https://www.gs1.org/services/verified-by-gs1/) in order to retrive the company that has registered the specified UPC.

UPC's are commonly used in the shipping & marketing industry (for example, those little barcodes? those are UPC's!), but they're also used in the [digital music industry](https://www.musicgateway.com/blog/music-industry/what-is-upc) in order to identify digital albums (this includes singles, although individual tracks are identified via an [ISRC](https://isrc.ifpi.org/en/)).


## How was this started?
To be honest, I was extremely bored. I wanted to see which distributor (in the digital music space) used a certain UPC, this is useful in cases where an Artist may be like "yeah, I like the distro i'm using right now!", but they don't specify what distributor.

This can also be used in the industrial/shipping space, where manufactures are able to tell the authenticity of a specific product that they've recieved.

## How do I get the bot started up?
First, replace the bot token at the bottom of the `main.py` file!

Then, replace the ReCaptcha token
> [!INFO]
> Unfortunately, I cannot find an efficient way to automatically make a ReCaptcha token, so you have to manually go to [GS1's website](https://www.gs1.org/services/verified-by-gs1/) and complete the captcha, then press `Ctrl+Shift+I` (or `Option + Command + I` on macOS), go to "Network", then click on the `results` on the left side. Scroll down until you see "captcha_token", then replace the "captcha_token" in the `main.py` script to the one you just got.


## How can I contribute?

Honestly, I have no idea. It might be helpful to have a way to automatically generate ReCaptcha tokens?
