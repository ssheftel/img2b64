img2b64
=======

store images in json documents using base64 encoding. 

> Thanks Brett for the great idea.


img2b64.py
==========

img2b64.py is a python module for converting images in a directory into a single json file with all images encoded in base64.

To use simply pass a directory containing images as the first argument to the script.py 

		python img2b64.py /Users/sam/SomeDir

img2b64.py will convert all jpg and png in the directory into base64 encoded strings and save them in a single file named `base64imgs.json`. 

Each attribute in the `base64imgs.json` file will be a image file name like _"photo1.jpg"_ and the value of the property will be a object congaing two attributes `"base64"` will contain the images encoded as a base64 string and `"format"` for example.

	{
		"photo1.jpg": {
			"base64": "/9j/4AAQSkZJRgABAQAAAQABA……",
			"format": "jpg"
		},
		"photo2.png": {
			"base64": "iVBORw0KGgoAAAANSUhEUgAAA+……",
			"format": "png"
		}
	}

img2b64.js
==========

img2b64.js once your json data has been loaded into the browser (xhr, copy and past) the base64 encoded images can be used in place of img src urls. that is `<img src="photo1.jpg"/>` can be replaced with `<img src="data:image/jpg;base64,/9j/4AAQSkZJRgABAQAAAQABA……"/>`

**And why would I ever want to do this?** Now rather then loading up each image separately a single request can be made to load the json containing all your images and the src attribute of the `img` can be set to the base64 encoded image. 

the img2b64.js module contains a single utility function `decodeBase64Image(imageName, imageDataObj)` for converting the `img2b64.py` generated json into valid resource identifiers which can be set as the value of the `img` tags `src` attribute. Assuming that the image data is store in the variable `images` then setting a image tag to display `photo1.jpg` would look something like:

	 $('#someImageId').src(img2b64.decodeBase64Image('photo1.jpg', images));
or for old times sake

	document.getElementById('someImageId').src = img2b64.decodeBase64Image('photo1.jpg', images)
	 