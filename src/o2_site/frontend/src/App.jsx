import { Router, Routes, Route } from "@solidjs/router";

import Layout from "./components/Layout";
import { logout } from "./utils/logout"
import Map from "./components/Map";
import ProfileEmail from "./components/profile/ProfileEmail";
import ProfilePage from "./components/profile/ProfilePage";
import ProfilePassword, { ProfilePasswordConfirm } from "./components/profile/ProfilePassword";
import ProfileUsername from "./components/profile/ProfileUsername";
import SigninPage from "./components/SigninPage";
import SignupPage from "./components/SignupPage";

function Home() {
  return (
    <Map />
  );
};

function App() {
  return (
    <>
      <Layout />
      <Router>
        <Routes>
          <Route path="/" component={Home} />
          <Route path="/signin" component={SigninPage} />
          <Route path="/signup" component={SignupPage} />
          <Route path="/logout" element={logout()} />
          <Route path="/profile" component={ProfilePage} />
          <Route path="/profile/changeUsername" component={ProfileUsername} />
          <Route path="/profile/changeEmail" component={ProfileEmail} />
          <Route path="/profile/changePassword" component={ProfilePassword} />
          <Route path="/changePasswordConfirm" component={ProfilePasswordConfirm} />
        </Routes>
      </Router>
    </>
  );
};

export default App;
