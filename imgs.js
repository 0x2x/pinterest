() => {
    function imgs(){
        const images = document.images;
        var img = [];
        for (let index = 0; index < images.length; index++) {
            img.push(images[index].src);
        }
        return {'images': img};
    }
    return imgs();
}