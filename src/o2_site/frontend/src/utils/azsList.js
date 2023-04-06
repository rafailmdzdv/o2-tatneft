import { backendHost } from "../settings";

const onSubmitAZS = (event) => {
  event.preventDefault();
  getXls();
};

const getXls = () => {
  fetch(`${backendHost}/api/getAzsXls/`)
    .then(response => response.blob())
    .then(blob => {
      const blobObj = new Blob([blob])
      const url = URL.createObjectURL(blobObj);
      const elementLink = document.createElement('a');
      elementLink.href = url;
      elementLink.setAttribute('download', 'azsList.xlsx');
      elementLink.click();
    });
};

export default onSubmitAZS;
