import { Router, Routes, Route } from "@solidjs/router";

import Layout from "./components/Layout";
import { logout } from "./utils/logout"
import Map from "./components/Map";
import { ProfileUsername, ProfilePage } from "./components/ProfilePage";
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
          <Route path="/profile/changeEmail" />
          <Route path="/profile/changePassword" />
        </Routes>
      </Router>
    </>
  );
};

export default App;
