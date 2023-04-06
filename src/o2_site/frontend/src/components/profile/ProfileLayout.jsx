import styles from "../../styles/ProfilePage.module.css";

const ProfileLayout = ({ children }) => {
  if (!JSON.parse(localStorage.getItem('isAuthenticated'))) {
    window.location.href = "/";
    return null;
  };
  return (
    <div id="profile" class={styles.profile}>
      <div id="profile-panel" class={styles.profilePanel}>
        <div id="panel" class={styles.changeButtonsBlock}>
          <div class={styles.innerChangeButtonsBlock}>
            <a href="/profile/">Панель</a>
          </div>
        </div>
        <div id="change-username" class={styles.changeButtonsBlock}>
          <div class={styles.innerChangeButtonsBlock}>
            <a href="/profile/changeUsername">Изменить логин</a>
          </div>
        </div>
        <div id="change-email" class={styles.changeButtonsBlock}>
          <div class={styles.innerChangeButtonsBlock}>
            <a href="/profile/changeEmail">Изменить почту</a>
          </div>
        </div>
        <div id="change-password" class={styles.changeButtonsBlock}>
          <div class={styles.innerChangeButtonsBlock}>
            <a href="/profile/changePassword">Изменить пароль</a>
          </div>
        </div>
      </div>
      { children }
    </div>
  );
};

export default ProfileLayout;
