import styles from '../styles/App.module.css'

function Layout() {
  const isAuthenticated = JSON.parse(localStorage.getItem('isAuthenticated'));
  const mapLink = <li><a href="/">Карта</a></li>;
  if (isAuthenticated) {
    return (
      <div class={styles.layout}>
        <nav class={styles.auth}>
          <ul>
            {mapLink}
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
            {mapLink}
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
