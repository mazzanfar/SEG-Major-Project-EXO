import axios from "axios";

import { GET_VIDEOS, GET_VIDEO } from "./types";

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

// GET VIDEO
export const getVideo = (id) => (dispatch) => {
    axios.get("/api/videos/" + id + "/").then((res) => {
        dispatch({
            type: GET_VIDEO,
            payload: res.data,
        });
    });
};
