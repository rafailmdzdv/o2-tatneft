import ProfileLayout from "./ProfileLayout";
import onSubmitAZS from "../../utils/azsList";
import styles from "../../styles/ProfilePage.module.css";

const ProfilePage = () => {
  return (
    <ProfileLayout>
      <div id="user-panel" class={styles.userPanel}>
        <div id="buttons-block" class={styles.buttonsBlock}>
          <div id="azs-list" class={styles.userButtons}>
            <button type="button" onClick={onSubmitAZS}>Список АЗС</button>
          </div>
          <div id="first-program-report" class={styles.userButtons}>
            <button type="button">Отчёт первой программы</button>
          </div>
          <div id="second-program-report" class={styles.userButtons}>
            <button type="button">Отчёт второй программы</button>
          </div>
        </div>
      </div>
    </ProfileLayout>
  );
};

export default ProfilePage;
