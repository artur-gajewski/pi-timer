Oven timer for Raspberry Pi
============================

Have you ever wanted to go watch TV while you needed to bake something in the oven? Have you ever forgotten about the stuff
in the oven and burned it while watching sports?

Why not putting your Raspberry Pi in use and build a LED timer so that next time your buns are in the oven, you
get notified with red or green LEDs about whether the buns are done or not? Place your Pi next to your TV and you
will see green light before you smell burned food ;-)

### Installation and running

1. Adjust the amount of minutes you wish to bake in the timer.py file as instructed in the code.

2. Run the code with one simple line:

```bash
$ python timer.py
```

If you wish to stop the timer, just click Ctrl+C and the code will clean up the GPIO pins for you.

### In the oven

![The oven is hot!](/images/baking.jpg)

### Buns are ready!

![Time to take them out from the oven!](/images/done.jpg)

### Time to om nom nom!

![Om nom nom nom!](/images/result.jpg)

### Connections

![Connections](/images/timer.png)
