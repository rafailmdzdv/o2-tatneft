import { createStore } from "solid-js/store";

import { backendHost } from "../settings";
import styles from "../styles/SignupPage.module.css";

const SignupPage = () => {

  const [state, setState] = createStore({
    username: "",
    email: "",
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
    fetch(`${backendHost}/signup/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(state)
    })
      .then(response => response.json())
      .then((data) => {
        if (data.status == "success") {
          setState("message", "Регистрация прошла успешно");
          window.location.href = "signin/";
        } else {
          setState("message", Object.values(data.error)[0][0]);
        };
      });
  };

  return (
    <div id="register-form" class={styles.registerForm}>
      <form onSubmit={handleSubmit}>
        <div id="login-input" class={styles.inputFields}>
          <label>Логин</label>
          <input type="text" id="username" value={state.username} onInput={handleInput}></input>
        </div>
        <div id="email-input" class={styles.inputFields}>
          <label>Почта</label>
          <input type="text" id="email" value={state.email} onInput={handleInput}></input>
        </div>
        <div id="password-input" class={styles.inputFields}>
          <label>Пароль</label>
          <input type="password" id="password" value={state.password} onInput={handleInput}></input>
        </div>
        <div id="submit-button" class={styles.submitButton}>
          <button type="submit">Зарегистрироваться</button>
        </div>
        <div class={styles.statusCode}>
          <span>{state.message}</span>
        </div>
      </form>
    </div>
  );
};

export default SignupPage;
