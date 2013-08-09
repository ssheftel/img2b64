(function(root){
	var FORMAT_PROPERTY = 'format',
		BASE64_DATA_PROPERTY = 'base64';
	root.img2b64 = {
		decodeBase64Image: function(imageName, imageData){
			var imageData = json[imageName];
			return 'data:image/'+imageData[FORMAT_PROPERTY]+';base64,'+ imageData[BASE64_DATA_PROPERTY];
		}
	};
}(window));