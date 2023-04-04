import { createStore } from "solid-js/store";

import { ProfileLayout } from "./ProfilePage";
import styles from "../../styles/ProfilePage.module.css";

const ProfilePassword = () => {
  const [state, setState] = createStore({
    password: ""
  });

  const handleInput = (event) => {
    const fieldName = event.target.id;
    const fieldValue = event.target.value;
    setState(fieldName, fieldValue);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("http://127.0.0.1:8001/api/changePassword/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${localStorage.getItem("access_token")}`
      },
      body: JSON.stringify(state)
    })
      .then(response => response.json())
      .then(data => {
      });
  };
  return (
    <ProfileLayout>
      <div id="change-password-form" class={styles.changeForm}>
        <form onSubmit={handleSubmit}>
          <div id="new-password-field" class={styles.newDataInput}>
            <label>Новый пароль</label>
            <input type="password" id="password" value={state.password} onInput={handleInput}></input>
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

export default ProfilePassword;
