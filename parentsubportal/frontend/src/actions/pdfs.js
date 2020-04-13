import axios from "axios";

import { GET_PDFS, GET_PDF } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// GET PDF
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

// GET PDF
export const getPost = (id) => (dispatch) => {
    axios.get("/api/pdf/" + id + "/").then((res) => {
        dispatch({
            type: GET_PDF,
            payload: res.data,
        });
    });
};
