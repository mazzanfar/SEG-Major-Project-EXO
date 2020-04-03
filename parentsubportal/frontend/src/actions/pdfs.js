import axios from "axios";

import { GET_PDFS } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// GET POSTS
export const getPDFs = () => (dispatch) => {
    axios
        .get("/api/pdfs/")
        .then((res) => {
            dispatch({
                type: GET_PDFS,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
