import axios from "axios";

import { GET_DISABILITIES } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// GET COMMENTS
export const getDisabilities = () => (dispatch) => {
    axios.get(`/api/disabilities/`).then((res) => {
        dispatch({
            type: GET_DISABILITIES,
            payload: res.data,
        });
    });
};
