import axios from "axios";

import { GET_VIDEOS } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// GET POSTS
export const getVideos = () => (dispatch) => {
    axios
        .get("/api/videos/")
        .then((res) => {
            dispatch({
                type: GET_VIDEOS,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
