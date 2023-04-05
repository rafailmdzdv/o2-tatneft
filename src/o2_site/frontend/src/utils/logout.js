import { backendHost } from "../settings";

const logout = () => {
  fetch(`${backendHost}/api/logout/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${localStorage.getItem("access_token")}`
    },
    body: JSON.stringify({"refresh_token": localStorage.getItem("refresh_token")})
  });
  localStorage.clear();
  window.location.href = "/";
};

export { logout };
