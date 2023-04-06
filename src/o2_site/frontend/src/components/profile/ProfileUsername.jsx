import { createStore } from "solid-js/store";

import { backendHost } from "../../settings";
import ProfileLayout from "./ProfileLayout";
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
    const tokens = JSON.parse(localStorage.getItem('tokens'));
    event.preventDefault();
    fetch(`${backendHost}/api/changeUsername/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${tokens.access_token}`
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
            <label>Новый логин</label>
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
