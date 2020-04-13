import axios from "axios";

import { GET_RESOURCES, DELETE_RESOURCE } from "./types";

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

// TODO: specify type of post to delete
export const deleteResource = (resource) => (dispatch) => {
    axios
        .delete("/api/posts/" + resource.id + "/")
        .then((res) => {
            dispatch({
                type: DELETE_RESOURCE,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
    axios
        .delete("/api/videos/" + resource.id + "/")
        .then((res) => {
            dispatch({
                type: DELETE_RESOURCE,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
    axios
        .delete("/api/pdfs/" + resource.id + "/")
        .then((res) => {
            dispatch({
                type: DELETE_RESOURCE,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};
