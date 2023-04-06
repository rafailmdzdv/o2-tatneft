import ProfileLayout from "./ProfileLayout";
import onClickAzs from "../../utils/azsList";
import onClickNumberSender from "../../utils/numberSenderReport";
import onClickLimitParser from "../../utils/limitParserReport";
import styles from "../../styles/ProfilePage.module.css";

const ProfilePage = () => {
  return (
    <ProfileLayout>
      <div id="user-panel" class={styles.userPanel}>
        <div id="buttons-block" class={styles.buttonsBlock}>
          <div id="azs-list" class={styles.userButtons}>
            <button type="button" onClick={onClickAzs}>Список АЗС</button>
          </div>
          <div id="first-program-report" class={styles.userButtons}>
            <button type="button" onClick={onClickNumberSender}>Отчёт первой программы</button>
          </div>
          <div id="second-program-report" class={styles.userButtons}>
            <button type="button" onClick={onClickLimitParser}>Отчёт второй программы</button>
          </div>
        </div>
      </div>
    </ProfileLayout>
  );
};

export default ProfilePage;
