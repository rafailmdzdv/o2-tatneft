const downloadFile = (blob, fileName) => {
    const blobObj = new Blob([blob]);
    const url = URL.createObjectURL(blobObj);
    const elementLink = document.createElement('a');
    elementLink.href = url;
    elementLink.download = fileName;
    elementLink.click();
};

export default downloadFile;
