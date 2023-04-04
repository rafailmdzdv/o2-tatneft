import { createEffect } from 'solid-js';
import styles from '../styles/Map.module.css'

const Map = () => {
  createEffect(() => {
    fetch('http://127.0.0.1:8001/api/getMap/')
      .then(response => response.json())
      .then(data => {
        const mapDivElement = document.getElementById("map-content");
        mapDivElement.innerHTML = data.map;
      });
  });

  return <div id="map-content" class={styles.mapClass} />;
};

export default Map;
