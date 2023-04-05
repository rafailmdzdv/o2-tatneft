import { createEffect } from "solid-js";

import { backendHost } from "../settings";
import styles from "../styles/Map.module.css";

const Map = () => {
  createEffect(() => {
    fetch(`${backendHost}/api/getMap/`)
      .then(response => response.json())
      .then(data => {
        const mapDivElement = document.getElementById("map-content");
        mapDivElement.innerHTML = data.map;
      });
  });

  return <div id="map-content" class={styles.mapClass} />;
};

export default Map;
