import { createSignal } from "solid-js";
import { createStore } from "solid-js/store";
import { useSearchParams } from "@solidjs/router";

import { backendHost } from "../../settings";
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
    fetch(`${backendHost}/api/changePassword/`, {
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
          message = "Ссылка для подтверждения отправлена на эл. почту";
          statusColor = "#00b473";
        } else {
          message = data.error.password;
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
      <div id="change-password-form" class={styles.changeForm}>
        <form onSubmit={handleSubmit}>
          <div id="new-password-field" class={styles.newDataInput}>
            <label>Новый пароль</label> <input type="password" id="password" value={state.password} onInput={handleInput}></input>
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

const ProfilePasswordConfirm = () => {
  const [params, _] = useSearchParams();
  const [status, setStatus] = createSignal("");

  const requiredData = { password: params.pass, token: params.token };
  fetch(`${backendHost}/changePasswordConfirm/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    },
    body: JSON.stringify(requiredData)
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        setStatus("Пароль был успешно изменён");
      } else {
        setStatus(data.message);
      };
    });

  return (
    <ProfileLayout>
      <div id="changing-status" class={styles.changingStatus}>
        <h3>{status()}</h3>
      </div>
    </ProfileLayout>
  );
};

export default ProfilePassword;
export { ProfilePasswordConfirm };
