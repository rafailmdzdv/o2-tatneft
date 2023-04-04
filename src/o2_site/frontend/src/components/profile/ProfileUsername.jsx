import { createStore } from "solid-js/store";

import { ProfileLayout } from "./ProfilePage";
import styles from "../../styles/ProfilePage.module.css";

const ProfileUsername = () => {
  const [state, setState] = createStore({
    username: ""
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
      .then(data => {
        let message, statusColor;
        if (data.success) {
          message = "Логин успешно изменён!";
          statusColor = "#00b473";
        } else {
          message = data.error;
          statusColor = "#ee3a43";
        };
        setState({
          message: message,
          statusColor: statusColor
        });
      });
  };
  return (
    <ProfileLayout>
      <div id="change-username-form" class={styles.changeForm}>
        <form onSubmit={handleSubmit}>
          <div id="new-username-field" class={styles.newDataInput}>
            <label>Новое имя пользователя</label>
            <input type="text" id="username" value={state.username} onInput={handleInput}></input>
          </div>
          <div id="submit-button" class={styles.submitButton}>
            <button type="submit">Подтвердить</button>
          </div>
          <div id="status-message" class={styles.statusMessage}>
            <span style={{ color: state.statusColor }}>
              {state.message}
            </span>
          </div>
        </form>
      </div>
    </ProfileLayout>
  );
};

export default ProfileUsername;
