import axios from "axios";

import { GET_RESOURCES } from "./types";

// GET DOCUMENTS
export const getResources = (params) => (dispatch) => {
    axios
        .get("/api/resources/", {
            params: params,
        })
        .then((res) => {
            dispatch({
                type: GET_RESOURCES,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
