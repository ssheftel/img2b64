(function(root){
    var FORMAT_PROPERTY = 'format',
        BASE64_DATA_PROPERTY = 'base64';
    function decodeBase64Image(imageName, json){
        var imageData = json[imageName];
        return 'data:image/'+imageData[FORMAT_PROPERTY]+';base64,'+ imageData[BASE64_DATA_PROPERTY];  
    }
    root.decodeBase64Image = decodeBase64Image;
}(window));