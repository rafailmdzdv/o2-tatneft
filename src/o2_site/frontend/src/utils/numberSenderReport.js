import { backendHost } from "../settings";
import downloadFile from "./fileDownloader";

const onClickNumberSender = (event) => {
  event.preventDefault();
  getNumberSenderReport();
};

const getNumberSenderReport = () => {
  fetch(`${backendHost}/api/getNumberSenderReport/`)
    .then(response => response.blob())
    .then(blob => downloadFile(blob, "firstProgramReport.xlsx"));
};

export default onClickNumberSender;
