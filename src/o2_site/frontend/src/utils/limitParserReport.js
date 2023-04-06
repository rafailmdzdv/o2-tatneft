import { backendHost } from "../settings";
import downloadFile from "./fileDownloader";

const onClickLimitParser = (event) => {
  event.preventDefault();
  getLimitParserReport();
};

const getLimitParserReport = () => {
  fetch(`${backendHost}/api/getLimitParserReport/`)
    .then(request => request.blob())
    .then(blob => downloadFile(blob, "secondProgramReport.xlsx"));
};

export default onClickLimitParser;
