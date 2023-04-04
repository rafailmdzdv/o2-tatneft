import styles from '../styles/App.module.css'

function Layout() {
  if (localStorage.getItem("refresh_token")) {
    return (
      <div class={styles.layout}>
        <nav class={styles.auth}>
          <ul>
            <li>
              <a href='/profile'>Профиль</a>
            </li>
            <li>
              <a href='/logout'>Выйти</a>
            </li>
          </ul>
        </nav>
      </div>
    );
  } else {
    return (
      <div class={styles.layout}>
        <nav class={styles.auth}>
          <ul>
            <li>
              <a href="/signin">Авторизоваться</a>
            </li>
            <li>
              <a href="/signup">Зарегистрироваться</a>
            </li>
          </ul>
        </nav>
      </div>
    );
  };
};

export default Layout;
