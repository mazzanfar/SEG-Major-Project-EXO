import axios from "axios";

import {
    POST_COMMENT,
    DELETE_COMMENT,
    GET_COMMENTS,
    EDIT_COMMENT,
    UPDATE_COMMENT,
} from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

// GET COMMENTS
export const getComments = (id) => (dispatch) => {
    axios.get(`/api/posts/${id}/`).then((res) => {
        dispatch({
            type: GET_COMMENTS,
            payload: id,
        });
    });
};

// DELETE_COMMENT
export const deleteComment = (comment) => (dispatch) => {
    axios.delete(`/api/comments/${comment.id}/`).then((res) => {
        dispatch({
            type: DELETE_COMMENT,
            payload: comment,
        });
    });
};

// POST COMMENT
export const postComment = (comment) => (dispatch) => {
    axios
        .post("/api/comments/", comment)
        .then((res) => {
            dispatch({
                type: POST_COMMENT,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err));
};

export const updateComment = (comment) => (dispatch) => {
    axios
        .put("/api/comments/" + comment.id + "/", comment)
        .then((res) => {
            dispatch({
                type: UPDATE_COMMENT,
                payload: res.data,
            });
        })
        .catch((err) => console.log(err.response));
};
