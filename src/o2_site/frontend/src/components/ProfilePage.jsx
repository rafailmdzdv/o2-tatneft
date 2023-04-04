import { createStore } from "solid-js/store";

import styles from "../styles/ProfilePage.module.css";

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

const ProfileUsername = () => {
  const [state, setState] = createStore({
    newUsername: ""
  });

  const handleInput = (event) => {
    const fieldName = event.target.id;
    const fieldValue = event.target.value;
    setState(fieldName, fieldValue);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("http://127.0.0.1:8001/api/changeUsername/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("access_token")}`
      },
      body: JSON.stringify(state)
    })
      .then(response => response.json())
      .then(_ => setState("message", "Имя успешно изменено!"));
  };
  return (
    <ProfileLayout>
      <div id="change-username-form" class={styles.changeForm}>
        <form onSubmit={handleSubmit}>
          <div id="new-username-field" class={styles.newUsernameInput}>
            <label>Новое имя пользователя</label>
            <input type="text" id="newUsername" value={state.newUsername} onInput={handleInput}></input>
          </div>
          <div id="submit-button" class={styles.submitButton}>
            <button type="submit">Подтвердить</button>
          </div>
          <div id="status-message" class={styles.statusMessage}>
            <span>{state.message}</span>
          </div>
        </form>
      </div>
    </ProfileLayout>
  );
};

const ProfilePage = () => {
  return (
    <ProfileLayout />
  );
};

export { ProfileUsername, ProfilePage };
