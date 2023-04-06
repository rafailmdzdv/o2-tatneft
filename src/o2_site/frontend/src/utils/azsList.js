import { backendHost } from "../settings";
import downloadFile from "./fileDownloader";

const onClickAzs = (event) => {
  event.preventDefault();
  getXls();
};

const getXls = () => {
  fetch(`${backendHost}/api/getAzsXls/`)
    .then(response => response.blob())
    .then(blob => downloadFile(blob, "azsList.xlsx"));
};

export default onClickAzs;
