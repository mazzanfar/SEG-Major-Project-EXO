import axios from "axios";

import { GET_RESOURCES } from "./types";

// GET DOCUMENTS
export const getResources = () => (dispatch) => {
    axios
        .get("/api/resources/")
        .then((res) => {
            dispatch({
                type: GET_RESOURCES,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
