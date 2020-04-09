import axios from "axios";

import { GET_CHILDREN } from "./types";

// GET DOCUMENTS
export const getChildren = (parentId) => (dispatch) => {
    axios
        .get("/api/children/", {
            params: { parent: parentId },
        })
        .then((res) => {
            console.log(res.data);
            dispatch({
                type: GET_CHILDREN,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
