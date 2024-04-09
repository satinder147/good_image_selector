# Good Image Selector

## Why I wrote this
Whenever I'm out and about, I'm always snapping away with my camera. I easily rack up between 1000 to 2000 photos a day. These JPEGs are pretty hefty, around 20MB each. So, storing them all on Google Photos would cost a pretty penny. Plus, let's be real, about 95% of them are either duplicates or just not that great. That's where this handy script swoops in. It helps me cherry-pick the gems from the sea of snapshots, ensuring that only the best memories get backed up.

Until recently, my approach involved sifting through images using extra-large previews, which presented a couple of challenges. 
1. despite being labeled as "extra-large," the previews often rendered details too small to discern clearly
2. The risk of accidental clicks or presses loomed large, potentially undoing hours of meticulous selection. Moreover, relying solely on mouse navigation tended to slow down the entire process.

I haven't been able to find a tool that allows me to preview images at a very large size while simultaneously selecting the ones I want to copy.

## Features

I've been searching for a tool that allows me to view images at a large size while simultaneously selecting the ones I want to copy, all without reaching for the mouse.
What I've found frustrating is that most tools either copy images immediately upon selection or only allow copying after I've finished selecting. Neither approach works seamlessly for me. If I copy images right away, I might change my mind later or realize I missed something important. On the other hand, copying images after selecting them all means waiting for the copying process to complete, which can be time-consuming. Plus, any failures during this process mean I have to start over, which is a hassle. To tackle this, I've developed a hybrid approach: I maintain a buffer of images (let's say 10 by default), and whenever the buffer is filled, the least recently selected photo is copied to the destination. This way, I can correct any labeling mistakes I make without losing too much progress.

Additionally, my ideal solution should enable me to accomplish all these tasks using only the keyboard, ensuring maximum efficiency. Here are the controls I envision:

## Controls:
1. Utilize the left and right arrow keys to navigate through the images.
2. Press the "a" key to select an image, and "d" key to deselect it as needed.

