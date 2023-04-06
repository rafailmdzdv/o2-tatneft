import { createStore } from "solid-js/store";

import { backendHost } from "../settings";
import styles from "../styles/SigninPage.module.css";

const SigninPage = () => {
  const [state, setState] = createStore({
    username: "",
    password: ""
  })

  const handleInput = (event) => {
    let {fieldName, fieldValue} = state;
    fieldName = event.target.id;
    fieldValue = event.target.value;
    setState(fieldName, fieldValue);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch(`${backendHost}/api/auth/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(state)
    })
      .then(response => response.json())
      .then(data => {
        if (!data.success) {
          setState("message", data.error);
        } else {
          setState("message", "Успешно!");
          const tokens = { access_token: "", refresh_token: "" };
          for (const [token, tokenValue] of Object.entries(data).slice(1)) {
            tokens[token] = tokenValue;
          };
          localStorage.setItem('tokens', JSON.stringify(tokens));
          localStorage.setItem("isAuthenticated", true);
          window.location.href = "/";
        };
      });
  };

  return (
    <div id="signin-form" class={styles.signinForm}>
      <form onSubmit={handleSubmit}>
        <div id="login-input" class={styles.inputFields}>
          <label>Логин</label>
          <input type="text" id="username" value={state.username} onInput={handleInput}></input>
        </div>
        <div id="password-input" class={styles.inputFields}>
          <label>Пароль</label>
          <input type="password" id="password" value={state.password} onInput={handleInput}></input>
        </div>
        <div id="submit-button" class={styles.submitButton}>
          <button type="submit">Авторизоваться</button>
        </div>
        <div class={styles.statusCode}>
          <span>{state.message}</span>
        </div>
      </form>
    </div>
  );
};

export default SigninPage;
