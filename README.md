# NoiseGenerator

Utilizes quantum RNG to generate noise images


Example:
```python
generator = Generator()
generator.GenerateImage(imgHeigth, imgWidth, type, path)
```

Parameters:

(int)imgHeight =  height of generated image file

(int)imgWidth = width of generated image file

(string)type = "RGB" or "BW"

(string)path = path to save image relative to source file dir. default is source dir
