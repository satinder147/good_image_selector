# good_image_selector

Why I wrote this script
Whenever I go out, I click a lot of photographs. 1000-2000 photos per day. I use google photos to back up good memories. My camera clicks very large JPEGS(approximately 20MB). Backing up all the photos will be very costly and since 95% of photos are either redundant copies, bad quality photos, this script  comes in very handy to choose the good ones.

Uptill now, I used to do this process by viewing the images as extra large previews and then selecting the images. There were two problems with this
1. Extra large previews are also small, can't see most of the things clearly
2. Any accidental click or click press might ruin all the hardwork I did.
3. Using the mouse makes the process slower

I was not able to find any tool, that helps me preview images(at very large size) and simultaneously select the images I want to copy

Features
1. View images at large size and simultaneously select images. 
2. Images are not copied as soon as you select images, nor they are copied in the end. Reason for not copying images as soon as you select is that you might not want to copy a image, or might decide later after looking at some more images. Copying images later has a problem that it takes a while after you are done labelling to copy the images. Any failures during this operation needs relabelling. I follow a hybrid approach where a buffer of images is kept(default 10 images, user configurable). The least recently selected photo is copied to the destination whenever the buffer is filled. This helps you to correct any labelling mistakes you make.
3. Keyboard only operation

Controls
1. Use left/right arrow keys to move through the images. 
2. Use "a" key to select and "d" key to deselect any image. 

