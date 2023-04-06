import { backendHost } from "../settings";

const logout = () => {
  const tokens = JSON.parse(localStorage.getItem("tokens"));
  fetch(`${backendHost}/api/logout/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${tokens.access_token}`
    },
    body: JSON.stringify({"refresh_token": tokens.refresh_token})
  });
  localStorage.setItem("isAuthenticated", false);
  localStorage.removeItem("tokens");
  window.location.href = "/";
};

export { logout };
