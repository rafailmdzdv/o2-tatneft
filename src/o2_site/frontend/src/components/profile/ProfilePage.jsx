import styles from "../../styles/ProfilePage.module.css";

const ProfileLayout = ({ children }) => {
  if (!localStorage.length) {
    window.location.href = "/";
    return null;
  };
  return (
    <div id="profile" class={styles.profile}>
      <div id="profile-panel" class={styles.profilePanel}>
        <a href="/profile/changeUsername">Изменить логин</a>
        <a href="/profile/changeEmail">Изменить почту</a>
        <a href="/profile/changePassword">Изменить пароль</a>
      </div>
      { children }
    </div>
  );
};

const ProfilePage = () => {
  return (
    <ProfileLayout />
  );
};

export default ProfilePage;
export { ProfileLayout };
