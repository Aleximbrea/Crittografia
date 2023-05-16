# Image encryption
This is a school project i have made using Python and HTML.
It's a pretty simple project that I made at the beginning of the last year of high school.
>This page is hosted on pythonanywhere https://alex904.pythonanywhere.com/
## Description
The webpage has two forms: one for encoding and one for decoding.
Both pages require an image wich is the key.
The image is converted by a Python script into an array of characters
then this characters are used to make some calculations.
## Example
If i wanted to encrypt the following string "**I like cats**" i would type it into the form on the encryption page then i would need a key, this is the image i have chosen: 
![a cat](https://www.helvetia.com/it/web/it/chi-siamo/blog/Assicurazione/animali/assicurazione-gatto/_jcr_content/storyparsys-01/storystage_copy_1249/image.1674745086536.transform-fp/1920x1080/assicurazione-gatto.jpg)
The image will be resized and every pixel would be replaced with one of this characters ["@","#","S","%","?","*","+",";",":",",","."] depending on the light level of the pixel.

Our encoded string is **49645944287d3c29753e29**.

The decoding is the reverse of the encoding process, we paste the encoded string into the form and use the same image as the key the result is our decoded string **I like cats**.
